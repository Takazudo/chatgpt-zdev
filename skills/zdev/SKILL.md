---
name: zdev
description: "Plan Takazudo development work in Chat, optionally prototype UI or sweep issues, and deliver a self-contained Codex Cloud implementation prompt with available artifacts."
---

# zdev

Read [the workflow contract](references/workflow-contract.md), [the handoff rules](../zdev1/references/handoff.md), and the relevant `zplan`, `zproto`, or `zgh` skill.

- `zdev` is the planning facade. Route rough development requests and explicit `zdev1` calls here in the current Chat. `zdev1` is a compatibility alias with identical flags and output; it does not start a different stage.
- Route `-pr`/`--prototype` through the accepted UI feedback loop before freezing issues. Route explicit `-is`/`--issuesweep`/`--issue-sweep` and `-isask`/`--issue-sweep-ask` through the sweep procedure. If both sweep flags appear, `-isask` wins.
- `-m`/`--merge` carries conditional merge authorization into the final Codex prompt and planning issues. It does not merge during planning, authorize deployment or publication, or waive repository policy and verification.
- Forward the normalized flag set and its meaning to `zplan`, issue text, and the final handoff. Never infer `-m` or a sweep from context. Explain unknown flags instead of silently dropping them.
- Finish with repository-grounded issues when available, the accepted brief, an artifact ZIP when real implementer inputs exist, and one complete copyable Codex Cloud prompt. The prompt is executable without this plugin or Chat history.
- `zstatus` and `zwatch` remain independent connected-computer observation routes. They do not start development. Legacy names in prose map to current skill names; `zdev2` is retired and has no execution route.
