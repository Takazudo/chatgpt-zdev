---
name: zdev
description: "Plan Takazudo development work in Chat, optionally prototype UI or sweep issues, and deliver a self-contained Codex Cloud implementation prompt with available artifacts."
---

# zdev

Read [the workflow contract](references/workflow-contract.md), [the handoff rules](references/handoff.md), and the relevant `zplan`, `zproto`, or `zgh` skill.

- Planning is read-only for GitHub and repository history: do not create or update issues, epics, labels, comments, branches or PRs; do not commit, push, close, or merge. This applies to delegated helpers too. Return only a self-contained prompt plus necessary artifacts. Never ask a downstream implementer to create planning issues as a workaround.
- `zdev` is the planning facade. Route rough development requests here in the current Chat. `zdev` is the sole planning entry point.
- Route `-pr`/`--prototype` through the accepted UI feedback loop before freezing the handoff. Route explicit `-is`/`--issuesweep`/`--issue-sweep` and `-isask`/`--issue-sweep-ask` through the sweep procedure. If both sweep flags appear, `-isask` wins.
- `-m`/`--merge` carries conditional merge authorization into the final Codex prompt only. It does not merge during planning, authorize deployment or publication, or waive repository policy and verification.
- Forward the normalized flag set and its meaning to `zplan` and the final handoff. Never infer `-m` or a sweep from context. Explain unknown flags instead of silently dropping them.
- Finish with the complete accepted brief, an artifact ZIP when real implementer inputs exist, and one complete copyable Codex Cloud prompt. The prompt is executable without this plugin or Chat history.
- `zstatus` and `zwatch` remain independent connected-computer observation routes. They do not start development. Retired planning aliases have no execution route.
