# Release and migration

## v0.5.0 direct Codex handoff

The source of truth is https://github.com/Takazudo/chatgpt-zdev. This release keeps package identity `z-dev-flow`, display name `zudo-dev-flow`, author, logo, visibility and unrelated observation skills. It changes the workflow to Chat planning and optional prototype iteration followed by a direct, self-contained Codex Cloud prompt. `zdev1` remains as a thin alias for `zdev`. The `zdev2` Work execution skill and its obsolete resource-only route are removed.

Existing prompts that name `zdev2` should be rewritten as plain Codex Cloud instructions using the accepted issue specification, actual PR/resource URLs, verification state and merge authority. An old account install may still expose `zdev2` until separately updated. Removing that installed skill requires a full-package replacement that deletes retired files; an overlay-only updater is insufficient. Do not install a second plugin identity or alter sharing to work around this.

## Build and install separately

1. Edit source and synchronize both manifests with a strict semantic version bump.
2. Run `python3 scripts/validate.py`, `python3 -m unittest discover -s scripts -p 'test_*.py'`, and `python3 scripts/package.py --output /tmp/zudo-dev-flow-0.5.0.zip`. Review the acceptance cases and package inventory.
3. Push source to a reviewable PR targeting `main`; verify pushed SHA and checks. Merging that PR and publishing to the account are separate actions.
4. After source acceptance, use a supported full-package replacement for the existing account plugin, preserving its ID, identity and sharing. Read back version and seven-skill inventory, ensuring `zdev2` is absent. Start a fresh chat to load the updated snapshot.

This source update alone does not reinstall or publish the account plugin. Host behavior and installed inventory require a separate smoke check after an authorized install.
