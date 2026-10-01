---
name: zdev2
description: "Execute an accepted plan in a separately opened ChatGPT Work session, create a PR, and give a Codex continuation prompt when unfinished. Accept -m/--merge only for fully verified work. Oversized plans with artifacts use resource-only mode without product implementation."
---

# zdev2

Read [the workflow contract](../zdev/references/workflow-contract.md), [handoff verification](../zdev1/references/handoff.md), and [completion and merge rules](references/completion.md). Use zgh for GitHub operations.

## Entry: read context, then implement

1. Read the named sibling Chat in this Project, including the accepted prototype delivery, the user's acceptance and subsequent corrections. Retrieve older turns when needed; a chat listing or short summary is not the plan. Read the linked issue's complete specification and inspect current repository instructions/source. Resolve accepted scope and version from this evidence.
2. **Proceed from the accepted specification.** If the sibling chat and issue provide sufficient requirements, start repository implementation immediately. A missing ZIP, `handoff.json`, hash, empty Project Sources list, or unavailable `verify_handoff.py` is not an implementation blocker. ZIPs are supplementary delivery, not the default entry ticket.
3. Read accessible prototype text, code, screenshots, and decisions. Implement the accepted behavior in the production architecture; do not require the original throwaway prototype bytes merely to implement the same behavior. If regenerating a reference from complete text, label it reconstructed, never the original verified artifact. Do not invent missing design decisions or claim an unseen screenshot was inspected.
4. Before asking for a file, identify the exact requirement that cannot be satisfied from the chat, issue, repository, or accessible resources. Only an indispensable missing input (for example a specific binary asset, dataset, or explicitly required exact source) blocks its dependent work. Ask for that input once, explain its concrete role, and continue all unaffected implementation. Do not repeatedly demand the whole ZIP because a previous agent marked every bundled file required.
5. Inspect actual execution capabilities separately from artifact access. Use authorized available repository tools and write access; do not infer read-only status from missing artifacts. If permissions really forbid changes, report the actual restriction and how to enable an execution-capable session. Never bypass it or describe ZIP upload as the remedy for a permission problem.
6. Honor the explicit mode. `resource-only` uses [resource bake](references/resource-bake.md) and never implements product features, even with `-m`. Unexpectedly oversized plans follow the routing contract without dropping topics.

### Existing handoffs from v0.3.0–v0.3.1

Those releases generated an overbroad “verify every ZIP/hash before implementation” prerequisite. Treat that generated transport checklist as superseded by this context-first contract. Do not present it as the user's independent requirement merely because they pasted the generated prompt. Preserve genuine user requirements for exact artifacts or integrity verification, and never claim a missing archive was verified. The correction permits implementation from an adequate accepted spec; it does not authorize ignoring explicit user constraints.

## Implementation mode

1. Use one branch and a PR explicitly targeting the repository's default branch unless another target was specified. Reuse a verified existing task branch/PR when resuming.
2. Implement the full accepted scope in dependency order. Use seed artifacts only if supplied and verified; zdev1 is not required to produce production code. Honor accepted UI behavior while using production components/tokens.
3. Make routine reversible decisions and continue without repeated approvals. There is no `-a`/`--auto` option: normal implementation already proceeds autonomously. If supplied, explain once that it is unnecessary and continue; it grants no merge permission.
4. Run appropriate focused tests, type/lint/build checks, and available UI verification. Follow repository heavy-test guards. Repair change-related failures and retest. Do not weaken tests or silently redefine acceptance to fit the environment.
5. Commit and push the actual work; open a draft PR when a meaningful diff exists. Keep the issue and PR current. Finish unaffected implementation if a platform or external service blocks some verification.
6. Inspect and address actionable CI failures while productive. Work is not an indefinite CI repair service: when blocked or unable to finish, preserve concrete evidence and the remaining work for Codex. Finish all unaffected scope rather than treating the first failure as a reason to stop.
7. Without `-m`/`--merge`, leave the PR open. With it, apply every gate in completion.md. Merge only when all requested work and verification are actually complete; otherwise leave it open and carry the user's merge authorization into the continuation prompt without weakening the gate.
8. End with the PR URL and a **copyable fenced text prompt for Codex whenever any work, checks, CI repair, or merge remains**. The PR URL must appear inside that prompt. Include issues, base/head/SHA, artifacts, remaining commands, evidence, and authorized actions. Use the portable Codex handoff contract in completion.md for every exit with work remaining, including passthrough, dependency-blocked and no-change cases. Never put this plugin’s skill names or invocations in that outgoing prompt. Spell out implementation, PR reuse/update/merge-or-close decisions, and conditional issue closure in dependency order. A fully merged and verified task can end with the merged PR and verification result; do not invent a zdev3 step.
