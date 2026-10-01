# Release and migration

## v0.3.0 → v0.3.1

The source of truth is https://github.com/Takazudo/chatgpt-zdev. The archive includes six skills and preserves the `z-dev-flow` package identity, **zudo-dev-flow** display name, author, and logo. Both manifests use the same version and presentation.

| Prior entry | Replacement |
|---|---|
| z-dev | zdev |
| z-first-dev | zdev1 (planning/handoff; mandatory seed implementation removed) |
| z-work-dev | zdev2 |
| z-plan | zplan |
| z-proto | zproto |
| z-gh | zgh |
| z-local | Removed; ordinary Codex continuation prompt |
| z-skill | Removed; maintain this repository |

The plugin default prompt changes only the invoked skill name from `z-dev` to `zdev`, as part of the requested rename.

## Build and release

1. Edit source here. Keep both manifests synchronized and bump their strict semantic version.
2. Run `python3 scripts/validate.py`, review the behavioral cases, and build an archive with `scripts/package.py`. Keep generated archives outside tracked source.
3. Push validated source to the repository. A GitHub push alone does not update an installed personal plugin.
4. Use a supported full-package replacement or repository-backed installation that discovers only the six new skill directories. Validate the resulting skill inventory in a fresh chat before claiming the installed copy is updated.

During the initial v0.3.0 migration, the available account updater only overlaid files and could not delete retired skill directories. The source release therefore supplied a clean package instead of applying that overlay. The account was subsequently updated successfully; the verified current state is recorded below. Future skill deletion still requires a supported full replacement rather than assuming omitted files are removed.

If a host provides full replacement, preserve the existing plugin's identity, ownership and visibility and verify read-back. If only new installation is possible, explain that it creates a separate plugin and obtain the user's choice before creating one. Reload or start a fresh chat after installation; a saved release and the skills loaded into an already-open chat can differ.

## Account state confirmed for v0.3.1

The account plugin was successfully replaced with v0.3.0 outside the initial source-release step. A fresh source read confirmed exactly the six intended skill directories and no retired ones. v0.3.1 changes only the display name and related documentation; it preserves the internal `z-dev-flow` identifier and existing account plugin ID. This update requires no file deletion and can use the guarded overlay updater.
