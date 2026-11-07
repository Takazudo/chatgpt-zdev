"""Regression checks for planning boundaries and standalone execution prompts."""
import json
import re
import shutil
import tempfile
import unittest
from pathlib import Path
from validate import (ROOT, execution_additions, handoff_profiles, handoff_variants,
                      validate, validate_codex_prompt, validate_execution_prompt)


class ValidationTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name) / 'plugin'
        shutil.copytree(ROOT, self.root, ignore=shutil.ignore_patterns('.git', '__pycache__', 'dist'))

    def mutate_and_reject(self, filename, old, new, error):
        path = self.root / filename
        original = path.read_text()
        self.assertIn(old, original)
        path.write_text(original.replace(old, new, 1))
        try:
            with self.assertRaisesRegex(ValueError, error):
                validate(self.root)
        finally:
            path.write_text(original)

    def prompt_template(self):
        text = (self.root / 'skills/zdev/references/handoff.md').read_text()
        return re.findall(r'```text\n(.*?)```', text, re.S)[0]

    def test_valid_source_and_inventory(self):
        expected_version = json.loads((ROOT / 'plugin.json').read_text())['version']
        self.assertEqual(validate(self.root)['version'], expected_version)
        self.assertFalse((self.root / 'skills/zdev2').exists())
        self.assertFalse((self.root / 'skills/zdev1').exists())

    def test_retired_skill_is_rejected(self):
        for retired in ('zdev1', 'zdev2'):
            with self.subTest(retired=retired):
                path = self.root / 'skills' / retired
                path.mkdir()
                with self.assertRaisesRegex(ValueError, 'Expected seven skills'):
                    validate(self.root)
                path.rmdir()

    def test_stale_overlay_is_rejected(self):
        path = self.root / '.codex-plugin/plugin.json'
        data = json.loads(path.read_text())
        data['version'] = '0.4.1'
        path.write_text(json.dumps(data))
        with self.assertRaisesRegex(ValueError, 'Overlay version drift'):
            validate(self.root)

    def test_bad_links_are_rejected(self):
        path = self.root / 'skills/zdev/SKILL.md'
        path.write_text(path.read_text() + '\n[bad](references/missing.md)\n')
        with self.assertRaisesRegex(ValueError, 'Broken/escaping link'):
            validate(self.root)

    def test_planner_flags_stay_in_producer_instructions(self):
        facade = (self.root / 'skills/zdev/SKILL.md').read_text()
        self.assertIn('sole planning entry point', facade)
        for flag in ('-m', '-pr', '-is', '-isask', '-cccp', '-coc', '-cowsl',
                     '-comac', '-ccwsl', '-ccmac', '-a'):
            self.assertIn(flag, facade)
        contract = (self.root / 'skills/zdev/references/workflow-contract.md').read_text()
        for phrase in ('`-isask` wins', '`-isask -m -pr`', 'merge or hold decision for each PR',
                       'Intentionally held and incomplete PRs remain open',
                       'Task-specific user constraints override generic flag defaults',
                       'replace all flags with their plain-language scope and actions'):
            self.assertIn(phrase, contract)

    def test_planning_read_only_and_helper_boundaries_are_required(self):
        for name in ('zdev', 'zplan', 'zgh'):
            with self.subTest(skill=name):
                self.mutate_and_reject(f'skills/{name}/SKILL.md',
                                       'GitHub and repository history are read-only',
                                       'GitHub writes are permitted', 'Missing contract anchor')
        for filename, phrase in (
                ('skills/zdev/SKILL.md', 'This includes delegated helpers'),
                ('skills/zdev/references/workflow-contract.md', 'every helper it delegates perform read-only GitHub research'),
                ('skills/zdev/references/handoff.md', 'delegated helpers perform read-only GitHub research')):
            with self.subTest(filename=filename):
                self.mutate_and_reject(filename, phrase, 'REMOVED', 'Missing contract anchor')
        github = (self.root / 'skills/zgh/SKILL.md').read_text()
        self.assertIn('explicit standalone user request', github)
        self.assertIn('Do not reinterpret delegated planning as standalone authorization', github)

    def test_planning_must_not_initiate_write_approval_requests(self):
        self.mutate_and_reject('skills/zdev/SKILL.md',
                              'Do not initiate GitHub-write approval requests here',
                              'Ask for GitHub write approval', 'Missing contract anchor')

    def test_reintroduced_planning_writes_and_cross_stage_bans_are_rejected(self):
        cases = {
            'skills/zplan/SKILL.md': 'A focused task can use one spec issue.',
            'skills/zdev/references/issue-sweep.md': 'Two or more epics require one super-epic.',
            'skills/zgh/SKILL.md': 'Create a planning PR after triage approval.',
            'skills/zdev/references/handoff.md': 'Never ask a downstream implementer to create planning issues.',
        }
        for filename, instruction in cases.items():
            with self.subTest(filename=filename):
                path = self.root / filename
                original = path.read_text()
                path.write_text(original + '\n' + instruction + '\n')
                try:
                    with self.assertRaisesRegex(ValueError, 'Obsolete planning write instruction'):
                        validate(self.root)
                finally:
                    path.write_text(original)

    def test_sweep_scope_approval_does_not_authorize_planning_writes(self):
        sweep = (self.root / 'skills/zdev/references/issue-sweep.md').read_text()
        for phrase in ('Approval accepts planning scope only', 'Do not treat silence as assent',
                       'local task keys', 'without creating seed issues', 'Do not bootstrap refs',
                       'Do not close the issue', 'create only missing records', 'Artifacts: none required'):
            self.assertIn(phrase, sweep)

    def test_prompt_contains_plan_and_tracking_without_plugin_dependencies(self):
        template = self.prompt_template()
        for phrase in ('Accepted scope:', 'Acceptance criteria:', 'Non-goals:',
                       'Tasks and dependency order:', 'Verification already observed:',
                       'Artifacts:', 'This task authorizes creating, updating and closing'):
            self.assertIn(phrase, template)
        validate_execution_prompt(template)

    def test_both_merge_branches_are_standalone(self):
        variants = handoff_variants(self.prompt_template())
        self.assertEqual(set(variants), {False, True})
        for authorized, prompt in variants.items():
            with self.subTest(merge=authorized):
                validate_execution_prompt(prompt)
                self.assertNotIn('<If merge', prompt)
                self.assertIn('Before implementing, establish durable GitHub tracking', prompt)
                self.assertIn('Use those issues as the development notebook', prompt)
        self.assertIn('Keep delivery issues open pending integration; do not merge', variants[False])
        self.assertNotIn('Close completed children first', variants[False])
        self.assertIn('Close completed children first', variants[True])
        self.assertNotIn('Leave implementation PRs open.', variants[True])

    def test_missing_merge_branch_is_rejected(self):
        self.mutate_and_reject('skills/zdev/references/handoff.md',
                              '<If merge is not authorized:', '<When ready:',
                              'Missing merge-permission branch')

    def test_tracker_first_and_duplicate_prevention_regressions_are_rejected(self):
        for old, new in (
                ('Before implementing, establish durable GitHub tracking', 'After implementing, consider tracking'),
                ('search for other matching open records before creating missing ones', 'always create new records'),
                ('For one focused task, use one tracker', 'For one focused task, omit tracking'),
                ('create or reuse a parent epic plus linked sub-issues', 'use an unlinked local checklist')):
            with self.subTest(removed=old):
                self.mutate_and_reject('skills/zdev/references/handoff.md', old, new,
                                       'Missing implementation contract')

    def test_notebook_and_verified_evidence_regressions_are_rejected(self):
        for phrase in ('Use those issues as the development notebook throughout the work',
                       'At meaningful milestones and before pausing or handing off',
                       'test commands and observed results with relevant revisions',
                       'PR/commit links, blockers and the next action',
                       'after an uncertain response, inspect for an existing result before retrying'):
            with self.subTest(removed=phrase):
                self.mutate_and_reject('skills/zdev/references/handoff.md', phrase, 'REMOVED',
                                       'Missing implementation contract')

    def test_completion_and_merge_gates_are_required(self):
        for phrase in ('Keep delivery issues open pending integration; do not merge',
                       'merge only after its accepted work, review, required approvals and current-head required checks pass under repository policy',
                       'Confirm integration into the intended target',
                       'close only issues whose own criteria are fully satisfied',
                       'Close completed children first',
                       'close their parent only when every accepted requirement and required child is complete'):
            with self.subTest(removed=phrase):
                self.mutate_and_reject('skills/zdev/references/handoff.md', phrase, 'REMOVED',
                                       'Missing implementation contract')

    def test_execution_prompt_rejects_private_skills_and_app_links(self):
        for invocation in ('Use zdev2', 'Use `zgh`', 'Run x-wt-teams', 'Run /prc',
                           'Follow the big-plan skill', 'Install plugin://example',
                           'Use [$zudo-dev-flow](app://plugins_example)'):
            with self.subTest(invocation=invocation):
                with self.assertRaisesRegex(ValueError, 'Nonportable'):
                    validate_execution_prompt(invocation + ' to finish the PR.')
        self.assertIs(validate_codex_prompt, validate_execution_prompt)

    def test_execution_prompt_rejects_flags_stage_leakage_and_blanket_issue_bans(self):
        for text, error in (
                ('Planning flags: `-m -is`.', 'Raw planning flag'),
                ('Use --merge when ready.', 'Raw planning flag'),
                ('Target flags: `-cccp -a`.', 'Raw planning flag'),
                ('Execution target: -coc.', 'Raw planning flag'),
                ('Allowed targets: `-cowsl -comac`.', 'Raw planning flag'),
                ('Execution target: -comac.', 'Raw planning flag'),
                ('Run with -ccwsl.', 'Raw planning flag'),
                ('Target: `-ccmac`.', 'Raw planning flag'),
                ('Use - cccp for the manager.', 'Raw planning flag'),
                ('Continue with -a after the first PR.', 'Raw planning flag'),
                ('The planning Chat made no GitHub writes.', 'Planning-session reference'),
                ('In the ChatGPT planning session, issues were read-only.', 'Planning-session reference'),
                ('Do not create planning issues or epics.', 'Blanket issue-creation ban'),
                ('Never create new GitHub issues.', 'Blanket issue-creation ban')):
            with self.subTest(text=text):
                with self.assertRaisesRegex(ValueError, error):
                    validate_execution_prompt(text)

    def test_factual_paths_shell_flags_and_duplicate_limits_remain_valid(self):
        for text in (
                'Implement https://github.com/Takazudo/chatgpt-zdev and edit skills/big-plan/SKILL.md.',
                'Inspect `skills/zdev/SKILL.md` and run `python3 -m unittest discover -s scripts`.',
                'Run `git commit -m "Record change"` and `gh pr merge --merge` after authorized checks.',
                'Run python3 -m unittest discover -s scripts',
                'Run ./scripts/check -m',
                'Run checks:\n```sh\ncustom-check --filter changed\n```',
                'Run `ls -a` to inspect the checkout.',
                'Run `rg -a pattern fixture` to inspect test data.',
                'Run `./scripts/check -cccp` when the repository defines that command.',
                'Run `./scripts/check -coc -cowsl -comac -ccwsl -ccmac` as documented in this repository.',
                'Inspect https://github.com/example/project/tree/feature-coc for existing work.',
                'Do not create duplicate issues or close unrelated issues.'):
            with self.subTest(text=text):
                validate_execution_prompt(text)

    def test_resolved_environment_profiles_compose_with_both_lifecycles(self):
        additions = execution_additions(self.root)
        profiles = list(handoff_profiles(self.prompt_template(), additions))
        self.assertEqual(len(profiles), 28)
        self.assertEqual({target for target, *_ in profiles},
                         {'portable', 'cccp', 'coc', 'cowsl', 'comac', 'ccwsl', 'ccmac'})
        for target, merge, continuous, composed in profiles:
            with self.subTest(target=target, merge=merge, continuous=continuous):
                validate_execution_prompt(composed)
                self.assertIn('Do not start or assign an inseparable task', composed)
                self.assertEqual('Run this work in Claude Code Cloud using the Project feature.' in composed, target == 'cccp')
                self.assertEqual('Use local subagents when this CLI supports them.' in composed,
                                 target in {'cowsl', 'comac', 'ccwsl', 'ccmac'})
                self.assertEqual('Do not stop after the first batch or PR.' in composed, continuous)
                if not merge:
                    self.assertIn('Keep delivery issues open pending integration; do not merge', composed)
                else:
                    self.assertIn('current-head required checks pass under repository policy', composed)

    def test_environment_mapping_cannot_drift(self):
        self.mutate_and_reject('skills/zdev/references/execution-environments.md',
                              '| `-comac` | Codex local CLI on Mac |',
                              '| `-comac` | Codex Cloud |',
                              'Execution environment flag mapping drift')

    def test_environment_scope_and_topic_worker_guards_are_required(self):
        for guard in (
                'Do not start or assign an inseparable task whose required implementation or acceptance needs an environment outside the allowed set',
                'CI may satisfy legitimate repository gates but does not expand the allowed environments',
                'only when Claude Code Cloud Project is selected',
                'preserve chosen models and effort unless the user explicitly changes them'):
            with self.subTest(guard=guard):
                self.mutate_and_reject('skills/zdev/references/execution-environments.md',
                                       guard, 'REMOVED', 'Missing contract anchor')
        additions = execution_additions(self.root)
        local = additions['local']
        for guard in ('one coherent substantive topic', 'follow-ups and corrections',
                      'never per file or tiny step', 'independent review of the integrated result',
                      "obey the repository's push policy", 'proceed sequentially in the parent'):
            self.assertIn(guard, local)

    def test_mode_specific_prompt_flags_cannot_leak_through_additions(self):
        for name, flag in (('claude-code-cloud-project', '-cccp'),
                           ('claude-code-cloud-project', '- cccp'),
                           ('continuous-development', '-a'),
                           *[('execution-environments', flag) for flag in
                             ('-cccp', '-coc', '-cowsl', '-comac', '-ccwsl', '-ccmac')]):
            with self.subTest(mode=name, flag=flag):
                self.mutate_and_reject(f'skills/zdev/references/{name}.md',
                                      '```text\n', f'```text\nUse {flag} to start.\n',
                                      'Raw planning flag')

    def test_mode_permissions_and_continuity_guards_are_required(self):
        cases = (
            ('claude-code-cloud-project', 'This environment flag alone does not request a sweep, a continuous loop, a merge, a release or a deployment'),
            ('claude-code-cloud-project', 'If the repository reserves pushes for the manager, children commit locally'),
            ('continuous-development', 'An explicit `-isask` interview takes precedence'),
            ('continuous-development', 'Preserve `no-auto`'),
            ('continuous-development', 'Without it, leave PRs and delivery issues open'),
            ('continuous-development', 'Before reporting completion, perform a fresh issue/PR and verification sweep'),
            ('continuous-development', 'A blocked or interrupted sweep is not full delivery'),
            ('continuous-development', 'On resume, read this checkpoint'),
            ('continuous-development', 'Before choosing each task and every new wave'),
            ('continuous-development', 'stop its execution chain and checkpoint partial work'),
        )
        for name, guard in cases:
            with self.subTest(mode=name, guard=guard):
                self.mutate_and_reject(f'skills/zdev/references/{name}.md', guard, 'REMOVED',
                                       'Missing contract anchor')

    def test_watch_safety_contract_survives(self):
        self.mutate_and_reject('skills/zwatch/SKILL.md',
                              'rescan all sessions, windows and panes', 'REMOVED',
                              'Missing contract anchor')


if __name__ == '__main__':
    unittest.main()
