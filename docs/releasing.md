# Release and migration

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
python3 scripts/package.py --output /tmp/zudo-dev-flow-0.6.0.zip
```

Source PR merge and account-plugin update are separate operations.
