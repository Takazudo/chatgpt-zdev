#!/usr/bin/env python3
"""Validate the source/package contract using only the Python standard library."""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILLS = {'zdev', 'zplan', 'zproto', 'zgh', 'zstatus', 'zwatch', 'zkicadactions'}


def validate_execution_prompt(prompt):
    """Reject planner dependencies in execution prose, allowing factual paths/commands."""
    if re.search(r'(?i)\b(?:app|plugin)://', prompt):
        raise ValueError('Nonportable app/plugin link in execution prompt')
    # Repository URLs and source paths can legitimately contain a skill's name.
    prose = re.sub(r'https?://[^\s`<>]+', '', prompt)
    prose = re.sub(r'(?<!\w)(?:\.{0,2}/)?(?:[\w.-]+/)+[\w.-]+', '', prose)
    skills = r'zdev[123]?|zplan|zproto|zgh|zstatus|zwatch|zkicadactions|z-dev-flow|zudo-dev-flow|big-plan|x-wt-teams|prc'
    if re.search(r'(?i)\b(?:' + skills + r')\b', prose):
        raise ValueError('Nonportable skill reference in execution prompt')
    if re.search(r'(?i)\b(?:planning\s+(?:chat(?:gpt)?|session)|(?:source|originating)\s+chat|chatgpt\s+planning)\b', prose):
        raise ValueError('Planning-session reference in execution prompt')
    if re.search(r"(?i)\b(?:do not|never|don't)\s+(?:create|open)\s+(?:(?:any|new|planning|tracking|github)\s+)*(?:issues?|epics?|trackers?)\b", prose):
        raise ValueError('Blanket issue-creation ban in execution prompt')
    # Shell -m/--merge/etc. are not planner flags. Exempt command snippets, not
    # snippets consisting only of flags; private invocations were checked above.
    commands = r'(?:python[\d.]*|git|gh|pytest|pnpm|npm|npx|node|bash|sh|cargo|docker|make|curl|rg|ls|\./[\w./-]+)\b'
    flag_prose = re.sub(r'https?://[^\s`<>]+', '', prompt)
    flag_prose = re.sub(r'```(?:bash|sh|shell|console)\n.*?```', '', flag_prose, flags=re.S)
    flag_prose = re.sub(r'`([^`\n]+)`', lambda m: '' if re.match(commands + r'\s', m[1]) else m[0], flag_prose)
    flag_prose = re.sub(r'(?im)^\s*(?:run\s+)?' + commands + r'\s+[^\n]*$', '', flag_prose)
    flags = r'--(?:merge|prototype|issuesweep|issue-sweep(?:-ask)?|refresh-epic|plan-only|filter|exclude)|-(?:[ \t]*cccp|coc|cowsl|comac|ccwsl|ccmac|grmac|grwsl|grc|isask|is|pr|po|re|ex|m|f|a)'
    if re.search(r'(?<![\w-])(?:' + flags + r')(?![\w-])', flag_prose):
        raise ValueError('Raw planning flag in execution prompt')


# Retain the original helper name for callers outside this repository.
validate_codex_prompt = validate_execution_prompt


def handoff_variants(template):
    """Select each documented merge branch without passing planner flags onward."""
    branches = {}
    lines = template.splitlines()
    pattern = re.compile(r'<If merge is (not )?authorized: (.*)>')
    for line in lines:
        match = pattern.fullmatch(line)
        if match:
            key = not bool(match[1])
            if key in branches:
                raise ValueError('Duplicate merge-permission branch')
            branches[key] = match[2]
    if set(branches) != {False, True}:
        raise ValueError('Missing merge-permission branch')
    variants = {}
    for authorized in (False, True):
        selected = []
        for line in lines:
            match = pattern.fullmatch(line)
            if not match:
                selected.append(line)
            elif (not bool(match[1])) == authorized:
                selected.append(match[2])
        variants[authorized] = '\n'.join(selected)
    return variants


def execution_additions(root=ROOT):
    """Read documented copyable blocks; this is not a flag parser or planner."""
    def blocks(name):
        text = (root / f'skills/zdev/references/{name}.md').read_text()
        result = re.findall(r'```text\n(.*?)```', text, re.S)
        if not result:
            raise ValueError(f'Missing execution addition for {name}')
        return result

    environments = blocks('execution-environments')
    if len(environments) != 4:
        raise ValueError('Expected environment, local worker and two Grok capability additions')
    return {
        'environment': environments[0],
        'local': environments[1],
        'grok_local': environments[2],
        'grok_cloud': environments[3],
        'project': '\n\n'.join(blocks('claude-code-cloud-project')),
        'continuous': '\n\n'.join(blocks('continuous-development')),
    }


def handoff_profiles(template, additions):
    """Compose template checks for resolved targets, merge and continuous modes."""
    for authorized, base in handoff_variants(template).items():
        for target in ('portable', 'cccp', 'coc', 'cowsl', 'comac', 'ccwsl', 'ccmac', 'grmac', 'grwsl', 'grc'):
            for continuous in (False, True):
                parts = [base, additions['environment']]
                if target == 'cccp':
                    parts.append(additions['project'])
                elif target in ('cowsl', 'comac', 'ccwsl', 'ccmac'):
                    parts.append(additions['local'])
                elif target in ('grmac', 'grwsl'):
                    parts.extend((additions['local'], additions['grok_local']))
                elif target == 'grc':
                    parts.append(additions['grok_cloud'])
                if continuous:
                    parts.append(additions['continuous'])
                yield target, authorized, continuous, '\n\n'.join(parts)



def validate(root=ROOT):
    errors = []
    def check(condition, message):
        if not condition:
            errors.append(message)
    manifest = json.loads((root / 'plugin.json').read_text())
    legacy = json.loads((root / '.codex-plugin/plugin.json').read_text())
    check(manifest['name'] == 'z-dev-flow', 'Package identity changed')
    check(bool(re.fullmatch(r'\d+\.\d+\.\d+', manifest['version'])), 'Version is not strict semver')
    check(not {'skills', 'mcpServers', 'apps', 'interface'} & manifest.keys(), 'Nonportable root fields')
    interface = manifest['extensions']['com.openai']['interface']
    check(len(interface['shortDescription']) <= 30, 'Listing subtitle exceeds 30 characters')
    check(interface['displayName'] == 'zudo-dev-flow', 'Display identity changed')
    check(interface['defaultPrompt'] == 'Use zdev to help me plan and implement a development task.', 'Stale or unexpected default prompt')
    for key in ('name', 'version', 'description', 'author'):
        check(manifest[key] == legacy[key], f'Overlay {key} drift')
    for key, value in interface.items():
        check(legacy['interface'].get(key) == value, f'Overlay interface.{key} drift')
    check(legacy.get('skills') == './skills', 'Overlay skill discovery changed')
    for key in ('logo', 'composerIcon'):
        asset = root / interface[key]
        check(asset.is_file() and asset.resolve().is_relative_to(root.resolve()), f'Invalid {key}')
    actual = {p.name for p in (root / 'skills').iterdir() if p.is_dir()}
    check(actual == SKILLS, f'Expected seven skills; got {sorted(actual)}')
    for name in sorted(actual):
        path = root / 'skills' / name / 'SKILL.md'
        check(path.is_file(), f'{name}: missing SKILL.md')
        if not path.is_file():
            continue
        text = path.read_text()
        front = re.match(r'\A---\n(.*?)\n---\n', text, re.S)
        check(front is not None, f'{name}: no frontmatter')
        if front:
            check(f'name: {name}\n' in front[1] + '\n', f'{name}: name mismatch')
            desc = re.search(r'^description: (.+)$', front[1], re.M)
            check(desc is not None and bool(json.loads(desc[1])), f'{name}: no description')
        check(f'# {name}\n' in text, f'{name}: heading mismatch')
        agent_path = path.parent / 'agents/openai.yaml'
        check(agent_path.is_file(), f'{name}: missing agent metadata')
        if not agent_path.is_file():
            continue
        agent = agent_path.read_text()
        check(f'display_name: "{name}"' in agent, f'{name}: agent display mismatch')
        check(f'Use ${name} for this development task.' in agent, f'{name}: stale agent prompt')
    for path in root.rglob('*'):
        if '.git' in path.parts or '__pycache__' in path.parts:
            continue
        check(not path.is_symlink(), f'Symlink: {path.relative_to(root)}')
        if not path.is_file() or path.suffix != '.md':
            continue
        text = path.read_text()
        check(not re.search(r'ELLIPSIZATION|\[rest omitted\]', text), f'Truncated source: {path}')
        for target in re.findall(r'\[[^\]]*\]\(([^)]+)\)', text):
            if re.match(r'[a-z]+:', target) or target.startswith('#'):
                continue
            target = target.split('#', 1)[0]
            dest = (path.parent / target).resolve()
            check(dest.is_relative_to(root.resolve()) and dest.exists(), f'Broken/escaping link in {path.relative_to(root)}: {target}')
    # Protect planning, direct handoff and independent observation contracts.
    anchors = {
        'skills/zstatus/SKILL.md': ['host-supported connected-computer delegation route', 'every window and every pane', 'do not send `go on`'],
        'skills/zstatus/references/observation.md': ['source data, not authorization', 'physical server/pane', 'Restarted work', 'Test/build failures', 'unknown/inaccessible'],
        'skills/zwatch/SKILL.md': ['rescan all sessions, windows and panes', 'newly created active sessions', 'Do not restart idle/completed agents', 'explicit user authorization', 'two per run', 'three total per watch', 'do not resend', 'An echoed input alone', 'at most three read-only reconnect checks', 'monitoring has ended', 'stop watching', 'do not invent a default deadline', 'keep unchanged cycles quiet', 'retain the unresolved watch as blocked', 'Preserve the ledger, event deduplication and recovery budgets'],
        'skills/zdev/SKILL.md': ['During the current ChatGPT planning session', 'GitHub and repository history are read-only', 'This includes delegated helpers', 'Do not initiate GitHub-write approval requests here', 'sole planning entry point', '-isask', '-m', '-cccp', '-coc', '-cowsl', '-comac', '-ccwsl', '-ccmac', '-grmac', '-grwsl', '-grc', '-a', 'Codex, Claude Code, or Grok', 'before implementation'],
        'skills/zdev/references/execution-environments.md': ['deduplicated allowed set, not an ordered preference list', 'This prompt can run in any supported environment.', 'hard scope constraint', 'select only from that set', 'Do not start or assign an inseparable task whose required implementation or acceptance needs an environment outside the allowed set', 'CI may satisfy legitimate repository gates but does not expand the allowed environments', 'only when Claude Code Cloud Project is selected', 'Reuse the same subagent for follow-ups and corrections within its topic', 'one coherent substantive topic', 'preserve chosen models and effort unless the user explicitly changes them', 'Grok CLI has no computer-use interaction', 'Grok bot cloud likewise uses only actual cloud facilities'],
        'skills/zdev/references/workflow-contract.md': ['Combinations compose', 'merge or hold decision for each PR', 'Task-specific user constraints', 'Without merge authorization', 'leave it open', 'every helper it delegates perform read-only GitHub research', 'initiate GitHub-write approval requests here', 'before changing implementation code', 'children before parents'],
        'skills/zdev/references/issue-sweep.md': ['--issuesweep', '--issue-sweep-ask', 'no-auto', 'Untouched', 'local task keys', '## Implementation order', 'Do not treat silence as assent'],
        'skills/zkicadactions/SKILL.md': ['Never dispatch a workflow', 'UNKNOWN is not PASS', 'not defaults for other repositories', 'Never bypass a denied access'],
        'skills/zkicadactions/references/contract.md': ['Artifact-only', 'persist-credentials: false', 'fail closed', 'UNIMPLEMENTED', 'never rerun an unchanged failure', 'Adoption is always an owner decision'],
        'skills/zdev/references/handoff.md': ['Copyable prompt template', 'PR plan:', 'delegated helpers perform read-only GitHub research', 'initiate GitHub-write approval requests here', 'Codex, Claude Code, or Grok', 'Keep normalized flags in producer-side notes only'],
        'skills/zdev/references/implementation-tracking.md': ['before changing implementation code', 'Search before creating missing records', 'Use one tracker for a focused task', 'Use one parent epic plus sub-issues', 'Use issue comments as a concise chronological development record', 'close completed children after integration', 'entire accepted scope is complete', 'Actual tool permissions, repository policies and explicit user restrictions still apply'],
        'skills/zdev/references/claude-code-cloud-project.md': ['This environment flag alone does not request a sweep, a continuous loop, a merge, a release or a deployment', 'Preserve any user-selected model', 'If unavailable, report the limitation and continue independent manager-owned work', 'If the repository reserves pushes for the manager, children commit locally', 'Do not start duplicate workers'],
        'skills/zdev/references/continuous-development.md': ['An explicit `-isask` interview takes precedence', 'Preserve `no-auto`', 'Without it, leave PRs and delivery issues open', 'Do not stop merely because the first plan, child session or PR is complete', 'Before reporting completion, perform a fresh issue/PR and verification sweep', 'A blocked or interrupted sweep is not full delivery', 'separate decision register and blocker register', 'On resume, read this checkpoint', 'Before choosing each task and every new wave', 'stop its execution chain and checkpoint partial work', 'allowed environments, selected host or portable status, environment-excluded tasks'],
        'skills/zplan/SKILL.md': ['GitHub and repository history are read-only', 'all helpers delegated from this session', 'Do not initiate GitHub-write approval requests here', 'creation/reuse of tracking issues before implementation'],
        'skills/zgh/SKILL.md': ['GitHub and repository history are read-only', 'all helpers delegated from this session', 'Do not initiate GitHub-write approval requests here', 'explicit standalone user request', 'Do not reinterpret delegated planning as standalone authorization'],
    }
    for filename, required in anchors.items():
        text = (root / filename).read_text()
        for anchor in required:
            check(anchor in text, f'Missing contract anchor {anchor!r} in {filename}')
    environment_text = (root / 'skills/zdev/references/execution-environments.md').read_text()
    definitions = dict(re.findall(r'^\| `(-[a-z]+)` \| ([^|]+?) \|', environment_text, re.M))
    expected_definitions = {
        '-cccp': 'Claude Code Cloud using the Project feature',
        '-coc': 'Codex Cloud',
        '-cowsl': 'Codex local CLI on WSL',
        '-comac': 'Codex local CLI on Mac',
        '-ccwsl': 'Claude Code local CLI on WSL',
        '-ccmac': 'Claude Code local CLI on Mac',
        '-grmac': 'Grok local CLI on Mac',
        '-grwsl': 'Grok local CLI on WSL',
        '-grc': 'Grok bot cloud',
    }
    check(definitions == expected_definitions, 'Execution environment flag mapping drift')
    planning_paths = [root / 'skills' / name / 'SKILL.md' for name in ('zdev', 'zplan', 'zgh', 'zproto')]
    planning_paths += list((root / 'skills/zdev/references').glob('*.md'))
    forbidden_planning = (
        'A focused task can use one spec issue', 'A decomposed plan uses one epic',
        'create ordinary seed issues', 'Two or more epics require',
        'push the shared base ref', 'Maintain one date-titled',
        'zdev authorizes its requested planning issues',
        'during planning; comment with verified replacement links',
        'Create a planning issue', 'Create a planning PR',
        'Never ask a downstream implementer to create planning issues',
        'Never defer planning issue creation to the implementer',
        'Do not create replacement planning issues in that session',
    )
    for path in planning_paths:
        text = path.read_text().casefold()
        for phrase in forbidden_planning:
            check(phrase.casefold() not in text,
                  f'Obsolete planning write instruction in {path.relative_to(root)}: {phrase}')
        for phrase in (
                'Merge authorization never grants deployment',
                'Merge authorization does not authorize deployment or a release',
                'Neither stage implicitly authorizes deployment',
                'No deployment or release authority'):
            check(phrase.casefold() not in text,
                  f'Obsolete blanket merge/deployment boundary in {path.relative_to(root)}: {phrase}')
    watch = (root / 'skills/zwatch/SKILL.md').read_text()
    for obsolete_watch in ('Default supervised window is 30 minutes', 'Give a quiet heartbeat about every five minutes', 'end as disconnected with the last successful observation time'):
        check(obsolete_watch not in watch, f'Obsolete watch lifetime/reporting rule: {obsolete_watch}')
    for path in (root / 'skills').rglob('*.md'):
        text = path.read_text()
        for phrase in ('First verify that the required files <names> are readable', 'Open every required artifact in this destination session'):
            check(phrase not in text, f'Obsolete ZIP startup gate in {path.relative_to(root)}')
    handoff = (root / 'skills/zdev/references/handoff.md').read_text()
    prompts = re.findall(r'```text\n(.*?)```', handoff, re.S)
    check(bool(prompts), 'Missing execution prompt template')
    common = ['Before implementing, establish durable GitHub tracking',
              'search for other matching open records before creating missing ones',
              'For one focused task, use one tracker',
              'create or reuse a parent epic plus linked sub-issues',
              'respect actual access controls',
              'Use those issues as the development notebook throughout the work',
              'At meaningful milestones and before pausing or handing off',
              'test commands and observed results with relevant revisions',
              'PR/commit links, blockers and the next action',
              'after an uncertain response, inspect for an existing result before retrying',
              'do not close a source issue merely because another record references it',
              'Do not report a check as passed unless observed',
              'Separate deployment commands, release creation, manual plugin publication and deployment/security setting changes require their own authorization',
              'Preserve higher-priority safety requirements, actual permissions, access controls, required approvals and explicit task restrictions',
              'If a concrete conflict or materially different side effect requires a decision or approval, report that exact blocker']
    lifecycle = {
        False: ['Leave implementation PRs open', 'Keep delivery issues open pending integration; do not merge'],
        True: ['You are instructed to complete the merge after development, not merely prepare a merge-ready PR',
               'merge only after its accepted work, review, required approvals and current-head required checks pass under repository policy',
               "This includes updates to published websites or services automatically triggered by the repository's existing merge workflow",
               'disclose its known production effects before merging',
               'do not skip the merge or ask for another generic merge/deployment approval solely because of those automatic updates',
               'report available automatic deployment results separately without assuming deployment succeeded',
               'Leave held or incomplete PRs open', 'Confirm integration into the intended target',
               'add completion notes with PR and verification evidence',
               'close only issues whose own criteria are fully satisfied',
               'Close completed children first',
               'close their parent only when every accepted requirement and required child is complete',
               'If any gate remains, hold that PR and record the exact blocker'],
    }
    # Check every copyable block, then only valid selected-host compositions.
    # This validates documented templates, not the planner's semantic decisions.
    additions = None
    try:
        additions = execution_additions(root)
        for name, block in additions.items():
            try:
                validate_execution_prompt(block)
            except ValueError as exc:
                errors.append(f'{name}: {exc}')
    except ValueError as exc:
        errors.append(str(exc))
    for template in prompts:
        try:
            for authorized, prompt in handoff_variants(template).items():
                validate_execution_prompt(prompt)
                check(prompt.find('Before implementing, establish durable GitHub tracking') < prompt.find('Implement the accepted scope in dependency order'), 'Tracking must precede implementation')
                for phrase in common + lifecycle[authorized]:
                    check(phrase in prompt, f'Missing implementation contract {phrase!r} (merge={authorized})')
            if additions is not None:
                for target, authorized, continuous, composed in handoff_profiles(template, additions):
                    validate_execution_prompt(composed)
        except ValueError as exc:
            errors.append(str(exc))
    kicad = (root / 'skills/zkicadactions/references/templates.md').read_text()
    kicad_prompt = kicad.split('## Codex Cloud handoff', 1)[-1]
    check('```text' in kicad_prompt, 'Missing KiCad Codex prompt template')
    prompts += re.findall(r'```text\n(.*?)```', kicad_prompt, re.S)
    for prompt in prompts:
        try:
            validate_execution_prompt(prompt)
        except ValueError as exc:
            errors.append(str(exc))
    for filename in ('skills/zdev/SKILL.md', 'skills/zdev/references/workflow-contract.md', 'skills/zdev/references/handoff.md'):
        text = (root / filename).read_text()
        check('mandatory Chat → Work → Codex' not in text, f'Obsolete staging in {filename}')
    if errors:
        raise ValueError('\n'.join(errors))
    return manifest


if __name__ == '__main__':
    manifest = validate()
    print(f"PASS: {manifest['name']} {manifest['version']}; seven skills, manifests, assets, references, and contract anchors")
