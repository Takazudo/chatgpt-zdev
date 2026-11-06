---
name: zdev
description: "Plan Takazudo development work in Chat, optionally prototype UI or sweep issues, and deliver a standalone implementation prompt for Codex or Claude Code, locally or in the cloud."
---

# zdev

Read [the workflow contract](references/workflow-contract.md), [the handoff rules](references/handoff.md), [implementation tracking](references/implementation-tracking.md), [the artifact storage rules](references/artifact-storage.md), and the relevant `zplan`, `zproto`, or `zgh` skill.

- During the current ChatGPT planning session, GitHub and repository history are read-only: do not create or update issues, epics, labels, comments, branches or PRs; do not commit, push, close or merge. This includes delegated helpers. Do not initiate GitHub-write approval requests here.
- Return a complete standalone prompt plus necessary artifacts. Require the separate implementing agent to establish or reuse a tracker or epic with sub-issues before implementation, keep development notes in those issues, and close them on verified completion under the authorized integration lifecycle. Prepare concrete issue content here without posting it.
- `zdev` is the sole planning entry point. Route rough development requests here in the current Chat.
- Route `-pr`/`--prototype` through the accepted UI feedback loop before freezing the handoff. Route explicit `-is`/`--issuesweep`/`--issue-sweep` and `-isask`/`--issue-sweep-ask` through the sweep procedure. If both sweep flags appear, `-isask` wins.
- `-m`/`--merge` carries conditional merge authorization into the execution prompt only. It does not merge during planning, authorize deployment or publication, or waive repository policy and verification.
- Forward normalized flags to `zplan` internally, then express their effective meaning as ordinary actions in the final prompt. Never infer a flag from context. Explain unknown flags instead of silently dropping them.
- Write for the user's chosen Codex or Claude Code session, local or cloud. Include the entire workflow in plain language; do not include plugin names, app links, private skill calls, raw planner flags or instructions to use this flow in the execution prompt.
- Save session-created deliverable files to Dropbox as specified in the artifact storage rules, including during prototype rounds.
- Finish with the complete accepted brief, an artifact ZIP when real implementer inputs exist, and one complete copyable execution prompt. It must work without this plugin or Chat history.
- `zstatus` and `zwatch` remain independent connected-computer observation routes. They do not start development. Retired planning aliases have no execution route.
