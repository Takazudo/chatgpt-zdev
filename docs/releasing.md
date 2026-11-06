# Release and migration

## v0.6.4 implementation tracking and standalone prompts

The ChatGPT planning session and all delegated helpers remain read-only for GitHub and never initiate GitHub-write approval requests. The separate implementation prompt requires tracking before code changes: reuse or create a tracker for a focused task, or an epic and linked sub-issues for a larger plan. Issues hold the accepted specification and development notes throughout the work. Close completed children after required integration, then their parent when the full accepted scope is complete.

Prompts support Codex or Claude Code, locally or in the cloud. Convert every accepted planning flag into plain actions and explicit lifecycle conditions. Do not pass plugin names, app links, private skill invocations or the planning Chat's permissions to the implementing agent. Preserve actual repository access controls and all existing merge gates.

Review the shared workflow, handoff, tracking, sweep and repository-research guidance together. Check representative focused and multi-task prompts, existing tracker reuse, issue-write failures, resume-after-compaction behavior, and both merge-permission cases. Keep the seven-skill inventory, plugin identity, audience, default prompts and unrelated behavior unchanged. Update the existing account plugin in place, then read back the version and affected files; a locally built archive does not establish installation or live host behavior.

## v0.6.3 planning-session issue boundary

Keep GitHub writes and their approval requests out of the ChatGPT planning session and its delegated helpers. Prepare issue content in the handoff when useful and let the separate user-started implementation session reuse, create or update in-scope issues and useful epics under its actual permissions and repository policy. Preserve explicit user restrictions, duplicate prevention, merge gates, plugin identity and sharing. Verify the shared contract, handoff template and issue-sweep guidance agree on this boundary.

## v0.6.2 Dropbox artifacts

Save zdev deliverables and prototype rounds in a unique Dropbox session folder, subject to connector requirements. Preserve existing plugin identity and sharing.

## v0.6.1 prompt and artifacts only

Planning and its delegated helpers perform read-only GitHub research. No planning issues, epics, PRs, labels, comments, branches, commits, pushes or merges. Sweep decisions stay in the handoff; standalone GitHub management and separately authorized implementation remain available. Update the existing private plugin in place, preserving identity and sharing; this source/package build does not publish or install it.

## v0.6.0 KiCad Actions skill

Adds `skills/zkicadactions/` (SKILL.md, agent metadata, references, offline scripts and config templates). Nothing is retired; an overlay update only adds files. Read back v0.6.0 and the seven-skill inventory in a fresh chat.

## v0.5.1 sole planning facade

`zdev` is the sole planning entry point. The `zdev1` alias is removed; its handoff and sweep references now live under `skills/zdev/references/`. `zdev2` remains retired. The package retains its `z-dev-flow` identity, `zudo-dev-flow` display name, author, logo, default prompt and observation skills.

An installed-plugin update is separate from this source release. Because the updater overlays files, inspect the installed inventory and explicitly delete these retired `zdev1` paths if present:

- `skills/zdev1/SKILL.md`
- `skills/zdev1/agents/openai.yaml`
- `skills/zdev1/references/handoff.md`
- `skills/zdev1/references/issue-sweep.md`

Delete any remaining `zdev2` paths from the actual installed inventory as well. Preserve plugin identity and sharing. Read back v0.5.1 and the six-skill inventory in a fresh chat.

## Build

```bash
python3 scripts/validate.py
python3 -m unittest discover -s scripts -p 'test_*.py'
python3 scripts/package.py --output /tmp/zudo-dev-flow-0.6.4.zip
```

Source PR merge and account-plugin update are separate operations.
