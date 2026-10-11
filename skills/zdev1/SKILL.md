---
name: zdev1
description: "Compatibility alias for zdev planning in Chat. Accepts the same -m, -pr, -is and -isask flags and produces the same Codex Cloud handoff."
---

# zdev1

This is a thin compatibility alias. Read and follow [zdev](../zdev/SKILL.md) with the user's full request and flags unchanged. Do not route through a Work session or invoke the retired zdev2 workflow. Example: `zdev1 -m -is for https://github.com/zudolab/zudo-text` means a bulk issue sweep in Chat, then a self-contained Codex Cloud prompt with conditional merge authorization. Preserve all accepted scope, sweep/prototype checkpoints, artifacts and lifecycle instructions from zdev.
