# Source and design provenance

Reviewed 2026-10-11 for the direct Codex handoff rewrite.

- User-supplied `plugin.zip`, v0.2.3: starting manifest identity, compatibility overlay, logo, focused GitHub/prototype guidance, and cross-session file verification safeguards.
- [codex-settings at a2ebd6a](https://github.com/Takazudo/codex-settings/tree/a2ebd6a61b8a48dbcca30808c4f1d85e9ac0ee17): `skills/big-plan/SKILL.md`, issue-sweep and resource-bake references, and x-wt-teams contracts.
- [claude-settings at 939a657](https://github.com/Takazudo/claude-settings/tree/939a657f40c5d797e72ec0f912ee42c6c0e93249): big-plan sweep/prototype flags, x-wt-teams merge semantics, and `skills/prc/SKILL.md` completion/approval checks.
- Relevant project conversations were read for context: the prior conversion/handoff repair and skill usage discussion. Their private transcripts are not copied into this repository.

Reviewed again 2026-11-07 for the planning/implementation boundary correction. The user's clarification requires the planning Chat to avoid GitHub writes and their approval requests, while the separate implementation agent creates or reuses tracking issues and records development history. The user's [current big-plan reference](https://github.com/Takazudo/claude-settings/tree/main/skills/big-plan) informed the epic/sub-issue structure, self-contained issue specifications and completion lifecycle. That skill is a design reference, not a dependency of generated prompts.

## Deliberate adaptations

- Default handoff is a standalone prompt for Codex or Claude Code, locally or in the cloud, grounded in current source and existing issue evidence. Planning performs no GitHub writes; real artifacts are supplied when available.
- zdev is the sole planning facade; it does not start implementation.
- Implementation targets the repository default branch unless the accepted task specifies a different target.
- The separate implementation agent establishes tracking before code changes: one tracker for focused work, or an epic with linked sub-issues for multiple tasks. Matching open records are reused to preserve history and prevent duplicates.
- Issues are the durable development notebook, with accepted requirements, decisions, progress, verification evidence, blockers, next actions and PR links. Close delivery issues only after their own criteria and required integration are verified; close a parent only after its whole scope is complete.
- Handoffs inline the required procedure and translate planning flags into plain actions. They do not require plugin names, app links, private skills, a particular orchestration tool or the original Chat history.
- `-m` cannot bypass incomplete acceptance, missing verification, review, approvals, or CI. It is per-PR and permits intentional holds and partial integration.
- Existing global/personal skills and the installed plugin cache are not edited by this source release.
