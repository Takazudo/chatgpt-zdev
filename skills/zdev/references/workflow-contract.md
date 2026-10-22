# zdev workflow contract

## Chat plan to Codex Cloud

Planning is read-only for GitHub and repository history: do not create or update issues, epics, labels, comments, branches or PRs; do not commit, push, close, or merge. This applies to delegated helpers too. Return only a self-contained prompt plus necessary artifacts. Never ask a downstream implementer to create planning issues as a workaround.

Plan in the current Chat with `zdev`; Inspect current repository instructions, source, issues, PRs and base SHA. Resolve ordinary choices and record assumptions, dependencies, acceptance criteria, review and verification in a self-contained handoff prompt. Decompose larger tasks using local task keys, not newly created issues or epics. Choose a fitting workflow; big-plan and x-wt-teams are inspiration, not mandatory orchestration. Simple cases need no artificial multi-PR topology. Explain consequential deviations briefly. Task-specific user constraints override generic flag defaults. The user opens a Codex Cloud implementation session with the final prompt. Chat does not claim to start or transform that session.

Use `-pr` for a UI prototype and feedback loop. Show working variants when appropriate, preserve rounds, and wait for explicit acceptance before finalizing a direction. Put accepted behavior in readable Chat and prompt text. Supply a validated ZIP with complete accepted source/assets when these files exist. A ZIP supplements the specification; it is not an entry prerequisite unless the user requires exact bytes. Identify any truly indispensable missing input and continue independent work.

Use `-is` only for an explicit issue sweep; use `-isask` for the per-candidate interview, including previously postponed issues. When both appear, `-isask` wins. Follow [the sweep procedure](issue-sweep.md). Neither `-m` nor routine autonomy skips the sweep checkpoint or prototype acceptance.

## Flag and lifecycle contract

| Flag | Planning effect | Codex handoff effect |
|---|---|---|
| no flag | Plan and record scope, dependencies, verification and permissions. | Implement and verify; leave PR open. Comment on the original issue with PR link and actual completion/verification status; keep it open pending integration. |
| `-m` / `--merge` | Record explicit conditional merge intent in the handoff only. Planning never creates PRs or merges. | Complete implementation and verification, then merge only under repository policy with current-head checks and required approvals. Close only genuinely completed in-scope issues after confirmed integration. No deployment or release authority. |
| `-is` / `--issuesweep` / `--issue-sweep` | Triage the requested backlog with a bulk checkpoint and named task groups in the handoff. | Implement the accepted sweep scope in dependency order; preserve unrelated issues. |
| `-isask` / `--issue-sweep-ask` | Revisit postponed candidates with the interview checkpoint; wins over `-is`. | Same implementation lifecycle for accepted scope only. |
| `-pr` / `--prototype` | Iterate in Chat until the user accepts a UI direction; record decisions and artifacts. | Implement accepted direction using repository architecture and verify UI states. |

Combinations compose: `zdev -m -is for https://github.com/zudolab/zudo-text` performs a bulk sweep and conditional merge instruction; `-isask -m -pr` interviews first, prototypes selected UI topics, then hands the accepted scope to Codex with merge conditions. Flags are recorded as normalized intent, not as private commands for Codex. Do not pass `-po`, `-a`, or other unsupported big-plan flags through as if they work here.

The final prompt must include actual repository URL and existing issue URLs when relevant, target branch and inspected SHA, accepted scope and non-goals, dependency order, relevant existing PRs and whether to reuse them, artifact locations and exact-input needs, checks and current evidence, and the authorized lifecycle. Codex receives plain-language actions, never plugin skill invocations. GitHub writes are not a planning prerequisite. Do not present their absence as blocked publication; never invent issue IDs or URLs.

In the separate user-started implementation session only:

Without `-m`, open or update a reviewable PR, leave it open, comment on each original in-scope issue with that PR URL and its actual implementation and verification status, and keep delivery issues open pending integration. With `-m`, state a merge or hold decision for each PR. Merge only eligible authorized in-scope PRs after their own accepted work, review, required approvals, required CI on the current head, and repository policy are satisfied. Intentionally held and incomplete PRs remain open; partial integration can be correct when the plan says so. If any gate is blocked, leave the PR and issues open and report the exact remaining gate. Close only fully satisfied in-scope sub-issues after confirmed integration, then eligible parents. Never close unrelated issues or treat a planning issue, prototype, resource PR or partial implementation as delivery. `-m` never authorizes deployment, release or plugin publication.

If a resource base PR already exists, inspect it and tell Codex whether to adopt and update it; do not create duplicate PRs. Lasting files must move into production locations and temporary resource paths must be removed before merge. Existing durable resources can be linked directly. Keep oversized generated files local/ignored; never use Git LFS. Do not infer permission to message people outside the requested GitHub workflow.

## Observation routes

`zstatus` is one read-only inventory; `zwatch` observes active Codex/Claude Code runs for the user-requested lifetime through available supervised execution. Follow [the observation contract](../../zstatus/references/observation.md) and [watch lifecycle](../../zwatch/SKILL.md). These are independent of planning and grant no authority to answer agent questions or resume agents.
