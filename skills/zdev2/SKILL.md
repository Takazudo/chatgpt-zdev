---
name: zdev2
description: "Execute an accepted plan in a separately opened ChatGPT Work session, create a PR, and give a Codex continuation prompt when unfinished. Accept -m/--merge only for fully verified work. Oversized plans with artifacts use resource-only mode without product implementation."
---

# zdev2

Read [the workflow contract](../zdev/references/workflow-contract.md), [handoff verification](../zdev1/references/handoff.md), and [completion and merge rules](references/completion.md). Use zgh for GitHub operations.

## Entry

1. Read the continuation prompt, named sibling Chat in this Project when accessible, durable issue spec, and `handoff.json` when files exist. Open every required artifact in this destination session, validate ZIP integrity and supplied sizes/hashes, and identify accepted versions. Same-project context is the preferred discovery route, not proof that file bytes transferred.
2. If a required artifact is missing, try the recorded alternate locator. Then request the exact ZIP or missing file and explain that the old session path is not accessible here. Do not invent source or start dependent work. Continue useful independent research. A prose-only issue may explicitly need no artifact.
3. Inspect current repository state, instructions, base branch and SHA, existing task PRs, and drift from planning. Reconcile changes without reopening settled product choices unnecessarily.
4. Honor the explicit execution mode. `resource-only` goes directly to [resource bake](references/resource-bake.md) and never implements product features, even with `-m`. A super-epic or unexpectedly oversized plan must be rerouted using the contract; do not silently drop topics or pretend one small slice fulfills the batch.

## Implementation mode

1. Use one branch and a PR explicitly targeting the repository's default branch unless another target was specified. Reuse a verified existing task branch/PR when resuming.
2. Implement the full accepted scope in dependency order. Use seed artifacts only if supplied and verified; zdev1 is not required to produce production code. Honor accepted UI behavior while using production components/tokens.
3. Make routine reversible decisions and continue without repeated approvals. There is no `-a`/`--auto` option: normal implementation already proceeds autonomously. If supplied, explain once that it is unnecessary and continue; it grants no merge permission.
4. Run appropriate focused tests, type/lint/build checks, and available UI verification. Follow repository heavy-test guards. Repair change-related failures and retest. Do not weaken tests or silently redefine acceptance to fit the environment.
5. Commit and push the actual work; open a draft PR when a meaningful diff exists. Keep the issue and PR current. Finish unaffected implementation if a platform or external service blocks some verification.
6. Inspect and address actionable CI failures while productive. Work is not an indefinite CI repair service: when blocked or unable to finish, preserve concrete evidence and the remaining work for Codex. Finish all unaffected scope rather than treating the first failure as a reason to stop.
7. Without `-m`/`--merge`, leave the PR open. With it, apply every gate in completion.md. Merge only when all requested work and verification are actually complete; otherwise leave it open and carry the user's merge authorization into the continuation prompt without weakening the gate.
8. End with the PR URL and a **copyable fenced text prompt for Codex whenever any work, checks, CI repair, or merge remains**. The PR URL must appear inside that prompt. Include issues, base/head/SHA, artifacts, remaining commands, evidence, and authorized actions. A fully merged and verified task can end with the merged PR and verification result; do not invent a zdev3 step.
