# Source and design provenance

Reviewed 2026-10-11 for the direct Codex handoff rewrite.

- User-supplied `plugin.zip`, v0.2.3: starting manifest identity, compatibility overlay, logo, focused GitHub/prototype guidance, and cross-session file verification safeguards.
- [codex-settings at a2ebd6a](https://github.com/Takazudo/codex-settings/tree/a2ebd6a61b8a48dbcca30808c4f1d85e9ac0ee17): `skills/big-plan/SKILL.md`, issue-sweep and resource-bake references, and x-wt-teams contracts.
- [claude-settings at 939a657](https://github.com/Takazudo/claude-settings/tree/939a657f40c5d797e72ec0f912ee42c6c0e93249): big-plan sweep/prototype flags, x-wt-teams merge semantics, and `skills/prc/SKILL.md` completion/approval checks.
- Relevant project conversations were read for context: the prior conversion/handoff repair and skill usage discussion. Their private transcripts are not copied into this repository.

## Deliberate adaptations

- Default handoff is a self-contained Codex Cloud prompt grounded in durable issues; real artifacts are supplied when available.
- zdev is the sole planning facade; it does not start implementation.
- Codex implementation targets the repository default branch unless the accepted task specifies a different target.
- Super-epics go directly to Codex with their issue hierarchy and available artifacts.
- Issue execution-mode markers inform the downstream Codex workflow without requiring a particular orchestration tool.
- `-m` cannot bypass incomplete acceptance, missing verification, review, approvals, or CI. It is per-PR and permits intentional holds and partial integration.
- Existing global/personal skills and the installed plugin cache are not edited by this source release.
