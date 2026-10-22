"""Regression checks for the direct planning-to-Codex contract."""
import json
import shutil
import tempfile
import unittest
from pathlib import Path
from validate import ROOT, validate, validate_codex_prompt


class ValidationTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name) / 'plugin'
        shutil.copytree(ROOT, self.root, ignore=shutil.ignore_patterns('.git', '__pycache__', 'dist'))

    def test_valid_source_and_inventory(self):
        self.assertEqual(validate(self.root)['version'], '0.6.1')
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

    def test_zdev_is_sole_planning_entry_point(self):
        self.assertFalse((self.root / 'skills/zdev1').exists())
        self.assertFalse((self.root / 'skills/zdev2').exists())
        facade = (self.root / 'skills/zdev/SKILL.md').read_text()
        self.assertIn('sole planning entry point', facade)
        for flag in ('-m', '-pr', '-is', '-isask'):
            self.assertIn(flag, facade)

    def test_flag_combinations_and_issue_lifecycle(self):
        contract = (self.root / 'skills/zdev/references/workflow-contract.md').read_text()
        for phrase in ('`-isask` wins', '`-isask -m -pr`', 'merge or hold decision for each PR', 'Intentionally held and incomplete PRs remain open', 'Task-specific user constraints override generic flag defaults', 'comment on each original in-scope issue', 'keep delivery issues open pending integration', 'never authorizes deployment'):
            with self.subTest(phrase=phrase):
                self.assertIn(phrase, contract)

    def test_handoff_instructions_cover_both_merge_modes_and_partial_multi_pr(self):
        handoff = (self.root / 'skills/zdev/references/handoff.md').read_text()
        for phrase in ('PR plan:', 'each actual or planned PR, target, merge/hold decision', 'Without -m:', 'With -m:', 'intentionally held or incomplete PRs open', 'Do not deploy', 'Do not report a check as passed unless observed', 'do not create a duplicate'):
            with self.subTest(phrase=phrase):
                self.assertIn(phrase, handoff)

    def test_planning_boundaries_and_standalone_management(self):
        for filename in ('skills/zdev/SKILL.md', 'skills/zplan/SKILL.md',
                         'skills/zgh/SKILL.md', 'skills/zdev/references/workflow-contract.md',
                         'skills/zdev/references/handoff.md'):
            with self.subTest(filename=filename):
                text = (self.root / filename).read_text()
                self.assertIn('Planning is read-only for GitHub and repository history', text)
                self.assertIn('do not commit, push, close, or merge', text)
                self.assertIn('This applies to delegated helpers too', text)
                self.assertIn('Never ask a downstream implementer to create planning issues', text)
        github = (self.root / 'skills/zgh/SKILL.md').read_text()
        self.assertIn('explicit standalone user request', github)
        self.assertIn('Do not reinterpret delegated planning as standalone authorization', github)

    def test_reintroduced_planning_writes_are_rejected(self):
        cases = {
            'skills/zplan/SKILL.md': 'A focused task can use one spec issue.',
            'skills/zdev/references/issue-sweep.md': 'Two or more epics require one super-epic.',
            'skills/zgh/SKILL.md': 'Create a planning PR after triage approval.',
            'skills/zdev/references/handoff.md': 'Ask the implementer to create planning issues.',
        }
        for filename, instruction in cases.items():
            with self.subTest(filename=filename):
                path = self.root / filename
                original = path.read_text()
                path.write_text(original + '\n' + instruction + '\n')
                with self.assertRaisesRegex(ValueError, 'Obsolete planning write instruction'):
                    validate(self.root)
                path.write_text(original)

    def test_sweep_is_decisions_only_even_after_approval(self):
        sweep = (self.root / 'skills/zdev/references/issue-sweep.md').read_text()
        for phrase in ('Approval accepts planning scope only', 'Do not treat silence as assent',
                       'local task keys', 'without creating seed issues',
                       'Do not bootstrap refs', 'Do not close the issue',
                       'Do not create replacement planning issues', 'Artifacts: none required'):
            self.assertIn(phrase, sweep)

    def test_no_automatic_planning_writes_regressions(self):
        paths = list((self.root / 'skills').rglob('*.md'))
        paths += [self.root / 'README.md', self.root / 'docs/acceptance-cases.md']
        obsolete = ('creates or updates durable issues when authorized',
                    'A focused task can use one spec issue',
                    'A decomposed plan uses one epic',
                    'after issue creation', 'Read back published issue bodies',
                    'create ordinary seed issues', 'Only after this checkpoint apply',
                    'Two or more epics require', 'push the shared base ref',
                    'Maintain one date-titled', 'zdev authorizes its requested planning issues',
                    'during planning; comment with verified replacement links')
        for path in paths:
            for phrase in obsolete:
                with self.subTest(path=path.relative_to(self.root), phrase=phrase):
                    self.assertNotIn(phrase, path.read_text())

    def test_handoff_embeds_plan_without_publication_prerequisite(self):
        handoff = (self.root / 'skills/zdev/references/handoff.md').read_text()
        for phrase in ('separate user-started Codex Cloud implementation session',
                       'Do not create planning issues or epics',
                       'Accepted scope:', 'Acceptance criteria:', 'Non-goals:',
                       'Dependency order:', 'Verification already observed:',
                       'Artifacts: none required'):
            self.assertIn(phrase, handoff)
        self.assertNotIn('planning issue URLs', handoff)

    def test_codex_prompt_rejects_private_skills(self):
        for invocation in ('Use zdev2', 'Use zgh', 'Run x-wt-teams', 'Run /prc', 'Install plugin://example'):
            with self.subTest(invocation=invocation):
                with self.assertRaisesRegex(ValueError, 'Nonportable skill'):
                    validate_codex_prompt(invocation + ' to finish the PR.')

    def test_watch_safety_contract_survives(self):
        path = self.root / 'skills/zwatch/SKILL.md'
        path.write_text(path.read_text().replace('rescan all sessions, windows and panes', 'REMOVED'))
        with self.assertRaisesRegex(ValueError, 'Missing contract anchor'):
            validate(self.root)


if __name__ == '__main__':
    unittest.main()
