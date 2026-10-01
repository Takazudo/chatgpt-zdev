---
name: zproto
description: "Iterate on UI and interaction prototypes in ordinary Chat for zdev1, especially -pr/--prototype. Preserve feedback rounds and require an accepted direction before implementation planning is finalized."
---

# zproto

Read [the workflow contract](../zdev/references/workflow-contract.md).

1. Do a light source review for stack, tokens, components, content, and constraints. Write a shared brief with target interactions, responsive states, realistic worst-case content, and accessibility needs.
2. Prefer a private ChatGPT Sites preview when available. Otherwise deliver a standalone HTML/CSS/JS prototype that the user can open. Do not require a Work session merely to host a prototype. Public publication needs the user's intent.
3. For exploration, show meaningfully different options; for polish, make focused changes. Preserve round directories and identify variants so feedback can refer to earlier rounds.
4. Exercise available interactions and breakpoints, capture screenshots when possible, and inspect actual output. Label unexecuted checks and visual limitations. A screenshot alone does not supply editable source.
5. Present the result and wait for feedback each round. Iterate until the user explicitly accepts a direction. Never infer acceptance from silence or an iteration count. If no direction is accepted, offer continued iteration or a clearly deferred plan; do not finalize a pretend winner.
6. Record accepted behavior, content, hierarchy, states, and Added/Removed/Superseded feedback in `decisions.md`. Written accepted requirements outrank incidental prototype CSS. Production must use the repository's existing architecture, tokens, and reusable components.
7. Pass the accepted direction to zplan. Bundle complete accepted source, required assets, useful screenshots, and a short rationale in zdev1's artifact ZIP. Preserve rejected rounds locally but exclude them from implementer-required resources unless comparison is necessary.
8. State concrete visual acceptance requirements (breakpoints, interactions, content extremes, and screenshots to compare) in the issue and handoff. A private preview URL supplements the transferable source; it never replaces it.
