#!/usr/bin/env python3
"""Validate the source/package contract using only the Python standard library."""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILLS = {'zdev', 'zplan', 'zproto', 'zgh', 'zstatus', 'zwatch', 'zkicadactions'}


def validate_codex_prompt(prompt):
    """Codex handoff templates must not depend on private skill availability."""
    private_skill = r'(?i)(?:\b(?:zdev[123]?|zplan|zproto|zgh|zstatus|zwatch|zkicadactions|z-dev-flow|zudo-dev-flow|x-wt-teams|prc)\b|plugin://)'
    if re.search(private_skill, prompt):
        raise ValueError('Nonportable skill reference in Codex prompt')


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
        'skills/zdev/SKILL.md': ['planning facade', 'sole planning entry point', '-isask', '-m', 'Codex Cloud'],
        'skills/zdev/references/workflow-contract.md': ['Combinations compose', 'merge or hold decision for each PR', 'Task-specific user constraints', 'Without `-m`', 'leave it open', 'comment on each original'],
        'skills/zdev/references/issue-sweep.md': ['--issuesweep', '--issue-sweep-ask', 'no-auto', 'Untouched', '**Super-epic:**', '## Implementation order', 'superseded'],
        'skills/zkicadactions/SKILL.md': ['Never dispatch a workflow', 'UNKNOWN is not PASS', 'not defaults for other repositories', 'Never bypass a denied access'],
        'skills/zkicadactions/references/contract.md': ['Artifact-only', 'persist-credentials: false', 'fail closed', 'UNIMPLEMENTED', 'never rerun an unchanged failure', 'Adoption is always an owner decision'],
        'skills/zdev/references/handoff.md': ['Copyable prompt template', 'PR plan:', 'intentionally held or incomplete PRs open', 'Do not deploy', 'pending integration'],
    }
    for filename, required in anchors.items():
        text = (root / filename).read_text()
        for anchor in required:
            check(anchor in text, f'Missing contract anchor {anchor!r} in {filename}')
    watch = (root / 'skills/zwatch/SKILL.md').read_text()
    for obsolete_watch in ('Default supervised window is 30 minutes', 'Give a quiet heartbeat about every five minutes', 'end as disconnected with the last successful observation time'):
        check(obsolete_watch not in watch, f'Obsolete watch lifetime/reporting rule: {obsolete_watch}')
    for path in (root / 'skills').rglob('*.md'):
        text = path.read_text()
        for phrase in ('First verify that the required files <names> are readable', 'Open every required artifact in this destination session'):
            check(phrase not in text, f'Obsolete ZIP startup gate in {path.relative_to(root)}')
    handoff = (root / 'skills/zdev/references/handoff.md').read_text()
    prompts = re.findall(r'```text\n(.*?)```', handoff, re.S)
    check(bool(prompts), 'Missing Codex prompt template')
    kicad = (root / 'skills/zkicadactions/references/templates.md').read_text()
    kicad_prompt = kicad.split('## Codex Cloud handoff', 1)[-1]
    check('```text' in kicad_prompt, 'Missing KiCad Codex prompt template')
    prompts += re.findall(r'```text\n(.*?)```', kicad_prompt, re.S)
    for prompt in prompts:
        try:
            validate_codex_prompt(prompt)
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
