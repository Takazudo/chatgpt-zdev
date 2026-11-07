---
name: zdev
description: "Plan Takazudo development work in Chat, optionally prototype UI or sweep issues, and deliver a standalone prompt for Codex or Claude Code. Supports six cloud/local execution environments and continuous issue-sweep/development with -a."
---

# zdev

Read [the workflow contract](references/workflow-contract.md), [the handoff rules](references/handoff.md), [implementation tracking](references/implementation-tracking.md), [the artifact storage rules](references/artifact-storage.md), and the relevant `zplan`, `zproto`, or `zgh` skill.

Read [execution environments](references/execution-environments.md) for the allowed-set selection and scope filter. Read [Claude Code Cloud Project execution](references/claude-code-cloud-project.md) only when that environment is selected. For `-a`, read [continuous development](references/continuous-development.md) and [the sweep procedure](references/issue-sweep.md).

- During the current ChatGPT planning session, GitHub and repository history are read-only: do not create or update issues, epics, labels, comments, branches or PRs; do not commit, push, close or merge. This includes delegated helpers. Do not initiate GitHub-write approval requests here.
- Return a complete standalone prompt plus necessary artifacts. Require the separate implementing agent to establish or reuse a tracker or epic with sub-issues before implementation, keep development notes in those issues, and close them on verified completion under the authorized integration lifecycle. Prepare concrete issue content here without posting it.
- `zdev` is the sole planning entry point. Route rough development requests here in the current Chat.
- Route `-pr`/`--prototype` through the accepted UI feedback loop before freezing the handoff. Route explicit `-is`/`--issuesweep`/`--issue-sweep`, `-isask`/`--issue-sweep-ask`, and `-a` through the sweep procedure. An explicit `-isask` interview wins over the other sweep modes.
- `-cccp`, `-coc`, `-cowsl`, `-comac`, `-ccwsl` and `-ccmac` form a deduplicated allowed environment set. Normalize `- cccp` to `-cccp`. Choose by requirements when unconstrained, enforce one environment as a hard scope constraint, and select only from multiple allowed candidates. Exclude tasks whose required implementation or acceptance cannot finish there; refilter every continuous wave. For portable unconstrained work, explicitly say the prompt can run in any supported environment. Apply Project child sessions only when Project is selected; local CLI children are subagents owning coherent substantive topics. Environment flags do not imply continuous development or merge authorization.
- `-a` requests an autonomous issue sweep and a repeated inspect → plan → implement → review → verify → integrate when authorized → resweep loop on every supported environment, including a local parent running sequentially. Ground the first wave here and include the entire continuation procedure in the prompt. The explicit mode accepts routine in-scope defect work without another bulk approval; preserve decision, no-auto, human/platform/access holds, an explicit interview, and UI acceptance. It does not imply merge authorization.
- `-m`/`--merge` carries conditional merge authorization into the execution prompt only. It does not merge during planning, authorize deployment or publication, or waive repository policy and verification.
- Forward normalized flags to `zplan` internally, then express their effective meaning as ordinary actions in the final prompt. Honor explicit prose constraints without inferring extra flags or permissions from the current runtime. Explain unknown flags instead of silently dropping them.
- Write for the user's chosen Codex or Claude Code session, local or cloud. Include the entire workflow in plain language; do not include plugin names, app links, private skill calls, raw planner flags or instructions to use this flow in the execution prompt.
- Save session-created deliverable files to Dropbox as specified in the artifact storage rules, including during prototype rounds.
- Finish with the complete accepted brief, an artifact ZIP when real implementer inputs exist, and one complete copyable execution prompt. It must work without this plugin or Chat history.
- `zstatus` and `zwatch` remain independent connected-computer observation routes. They do not start development. Retired planning aliases have no execution route.
