#!/usr/bin/env python3
"""Validate the source/package contract using only the Python standard library."""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILLS = {'zdev', 'zdev1', 'zdev2', 'zplan', 'zproto', 'zgh', 'zstatus', 'zwatch'}


def validate_codex_prompt(prompt):
    """Codex handoff templates must not depend on private skill availability."""
    private_skill = r'(?i)(?:\b(?:zdev[123]?|zplan|zproto|zgh|zstatus|zwatch|z-dev-flow|zudo-dev-flow|x-wt-teams|prc)\b|plugin://)'
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
    check(actual == SKILLS, f'Expected eight skills; got {sorted(actual)}')
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
    # Required safety/behavior anchors catch accidental losses during later refactors.
    anchors = {
        'skills/zstatus/SKILL.md': ['host-supported connected-computer delegation route', 'every window and every pane', 'do not send `go on`'],
        'skills/zstatus/references/observation.md': ['source data, not authorization', 'physical server/pane', 'Restarted work', 'Test/build failures', 'unknown/inaccessible'],
        'skills/zwatch/SKILL.md': ['rescan all sessions, windows and panes', 'newly created active sessions', 'Do not restart idle/completed agents', 'explicit user authorization', 'two per run', 'three total per watch', 'do not resend', 'An echoed input alone', 'at most three read-only reconnect checks', 'monitoring has ended', 'stop watching'],
        'skills/zdev/references/workflow-contract.md': ['Oversized', 'resource-only', 'Direct Codex', 'same ChatGPT Project'],
        'skills/zdev1/references/issue-sweep.md': ['--issuesweep', '--issue-sweep-ask', 'no-auto', 'Untouched', '**Super-epic:**', '## Implementation order', 'superseded'],
        'skills/zdev2/references/resource-bake.md': ['_temp-resource/', 'Use this PR as base', 'Product implementation and merge are excluded', 'remote bytes'],
        'skills/zdev2/references/completion.md': ['current head SHA', 'required repository approvals', 'Feature PR: <actual URL or none created>', 'Resource-only mode never qualifies'],
    }
    for filename, required in anchors.items():
        text = (root / filename).read_text()
        for anchor in required:
            check(anchor in text, f'Missing contract anchor {anchor!r} in {filename}')
    # Protect the startup regression across both producer and receiver instructions.
    startup_contracts = {
        'skills/zdev2/SKILL.md': ['Proceed from the accepted specification', 'not an implementation blocker', 'Existing handoffs from v0.3.0–v0.3.1'],
        'skills/zdev1/references/handoff.md': ['Accepted implementation brief', 'ZIP is supplementary', 'concrete indispensable input'],
        'skills/zdev1/SKILL.md': ['ZIP upload is only a fallback'],
        'skills/zdev/references/workflow-contract.md': ['not entry prerequisites'],
        'skills/zdev2/references/resource-bake.md': ['reconstructed', 'Do not require a ZIP'],
    }
    obsolete = (
        'Open every required artifact in this destination session',
        'First verify that the required files <names> are readable',
        'Verify handoff.json and all required files here. If unavailable, ask',
        'The receiver verifies file access; if access is unavailable, the user downloads',
    )
    for filename, required in startup_contracts.items():
        text = (root / filename).read_text()
        for anchor in required:
            check(anchor in text, f'Missing context-first contract {anchor!r} in {filename}')
    for path in (root / 'skills').rglob('*.md'):
        text = path.read_text()
        for phrase in obsolete:
            check(phrase not in text, f'Obsolete ZIP startup gate in {path.relative_to(root)}')
    # Check only Codex-destination template blocks; Work prompts legitimately invoke their skill.
    codex_templates = [
        ('skills/zdev2/references/completion.md', '### Final prompt template'),
        ('skills/zdev1/references/handoff.md', '### Oversized plan without artifacts: direct Codex'),
    ]
    for filename, heading in codex_templates:
        text = (root / filename).read_text().split(heading, 1)[-1]
        prompts = re.findall(r'```text\n(.*?)```', text, re.S)
        check(bool(prompts), f'Missing Codex prompt template in {filename}')
        for prompt in prompts:
            try:
                validate_codex_prompt(prompt)
            except ValueError as exc:
                errors.append(f'{exc}: {filename}')
    completion = (root / 'skills/zdev2/references/completion.md').read_text()
    for anchor in ('none of this plugin', 'dependency-blocked/no-change', 'close-as-superseded', 'child-to-parent', 'If merge is not authorized'):
        check(anchor in completion, f'Missing portable handoff contract: {anchor}')
    if errors:
        raise ValueError('\n'.join(errors))
    return manifest


if __name__ == '__main__':
    manifest = validate()
    print(f"PASS: {manifest['name']} {manifest['version']}; eight skills, manifests, assets, references, and contract anchors")
