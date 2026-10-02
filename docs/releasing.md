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
4. Use a supported full-package replacement or repository-backed installation that discovers the intended release skill directories. Validate the resulting skill inventory in a fresh chat before claiming the installed copy is updated.

During the initial v0.3.0 migration, the available account updater only overlaid files and could not delete retired skill directories. The source release therefore supplied a clean package instead of applying that overlay. The account was subsequently updated successfully; the verified current state is recorded below. Future skill deletion still requires a supported full replacement rather than assuming omitted files are removed.

If a host provides full replacement, preserve the existing plugin's identity, ownership and visibility and verify read-back. If only new installation is possible, explain that it creates a separate plugin and obtain the user's choice before creating one. Reload or start a fresh chat after installation; a saved release and the skills loaded into an already-open chat can differ.

## Account state confirmed for v0.3.1

The account plugin was successfully replaced with v0.3.0 outside the initial source-release step. A fresh source read confirmed exactly the six intended skill directories and no retired ones. v0.3.1 changes only the display name and related documentation; it preserves the internal `z-dev-flow` identifier and existing account plugin ID. This update requires no file deletion and can use the guarded overlay updater.

## v0.3.2 handoff correction

The previous generated prompts made ZIP integrity verification an unconditional startup gate. v0.3.2 supersedes that generated transport checklist: a sufficient accepted sibling-chat/issue specification is the implementation input. Explicit user demands for exact files remain authoritative. Existing chats may retain an older skill snapshot; to resume one, tell it to use v0.3.2 and proceed from the accepted readable specification, requesting only indispensable unavailable inputs. Do not claim inaccessible ZIP bytes were verified.

## v0.4.0 observation skills

This additive release has eight skills and retains the same identity, assets, visibility and default prompt. Both manifests are synchronized. Update the existing account plugin using its verified ID and current-release guard; do not install a second identity. Apply both changed and new source files, preserve unchanged files, and verify the release version and eight-skill inventory. Start a fresh chat to load the new skill snapshot. Repository push and ZIP validation do not prove account publication or live host monitoring.

## v0.4.1 ongoing-watch correction

The existing account plugin `plugins_6abd41174f9081919dbf23cd406e1750` received v0.4.0 as release `pluginrel_6abf6116753c8191942c2531ecbd558b` (confirmed by the coordinating parent session). The source PR remains unmerged. Apply v0.4.1 as a guarded update of that same identity, preserving permissions and unchanged assets; source push alone does not apply this patch to the account.

This patch removes the invented 30-minute watch deadline and routine five-minute heartbeats. Ongoing watches honor user stopping conditions and available host execution; blocked connection/authorization/execution retains an unresolved resumable task. This does not add a permanent daemon or bypass host limits.
