# Source and design provenance

Reviewed 2026-10-02 for this requested rewrite.

- User-supplied `plugin.zip`, v0.2.3: starting manifest identity, compatibility overlay, logo, focused GitHub/prototype guidance, and cross-session file verification safeguards.
- [codex-settings at a2ebd6a](https://github.com/Takazudo/codex-settings/tree/a2ebd6a61b8a48dbcca30808c4f1d85e9ac0ee17): `skills/big-plan/SKILL.md`, issue-sweep and resource-bake references, and x-wt-teams contracts.
- [claude-settings at 939a657](https://github.com/Takazudo/claude-settings/tree/939a657f40c5d797e72ec0f912ee42c6c0e93249): big-plan sweep/prototype flags, x-wt-teams merge semantics, and `skills/prc/SKILL.md` completion/approval checks.
- Relevant project conversations were read for context: the prior conversion/handoff repair and skill usage discussion. Their private transcripts are not copied into this repository.
- [Official Projects documentation](https://learn.chatgpt.com/docs/projects): supports organizing Chat and Work chats with shared project context. Required artifact access is still verified in the receiving session.

## Deliberate adaptations

- Default handoff uses the same ChatGPT Project, with exact Chat/artifact references and ZIP fallback.
- zdev1 always stops at the prompt/artifact handoff; it does not inherit big-plan's auto-implementation chain or require a production seed.
- zdev2 targets the repository default branch unless the accepted task specifies a different target.
- Work capacity is assessed as a planning heuristic, not a claimed platform cap. Super-epics go to Codex, using Work only to persist needed resources.
- Work does not require multi-agent execution. Issue execution-mode markers are retained for the downstream Codex workflow.
- `-m` cannot bypass incomplete acceptance, missing verification, review, approvals, or CI. prc's no-wait bypass is deliberately not ported.
- Existing global/personal skills and the installed plugin cache are not edited by this source release.
