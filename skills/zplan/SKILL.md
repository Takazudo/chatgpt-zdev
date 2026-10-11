---
name: zplan
description: "Turn a rough development request or issue into a repository-grounded plan with acceptance criteria and durable GitHub issues. Supports zdev and its zdev1 alias; UI direction goes through zproto."
---

# zplan

Read [the workflow contract](../zdev/references/workflow-contract.md). Use `zgh` for repository research and writes.

1. Read repository instructions, current source/config, related issues/PRs, and relevant accessible sibling-chat decisions. Validate claimed root causes against current source; retain the issue's intent when its proposed fix is stale.
2. Resolve the default branch from GitHub unless the user or accepted handoff specifies another. Record base name and inspected commit. A random current feature branch is not an implicit target.
3. Capture problem, outcome, scope, non-goals, accepted decisions, affected components, dependencies, risks, and measurable acceptance criteria. Resolve ordinary choices with a stated recommendation. Ask only when competing interpretations materially change the work.
4. For `-pr` or genuinely unsettled UI direction, run zproto before freezing the plan. Accepted feedback supersedes rejected ideas; record Added/Removed/Superseded requirements explicitly.
5. A focused task can use one spec issue. A decomposed plan uses one epic and self-contained sub-issues. A sweep follows zdev1's full sweep procedure: tiny topics can share a batch epic; independent substantial topics become separate epics, with a super-epic when there are two or more.
6. When an epic and child issue graph is useful, each child carries `**Wave:**`, `**Depends on:**`, `**Execution mode:** subagents|teams - reason`, and `**Difficulty:** high|mid|standard - reason`. These describe downstream Codex execution; they do not require Work to spawn agents. Dependencies gate execution; waves are descriptive only. For genuine delegated topics, use difficulty as a worker hint: high → gpt-6-astra/high, mid → gpt-6.1-sol/medium, standard → gpt-6-luna/max, subject to available models and user overrides. The manager remains on its session model; do not claim to switch it or require delegation for a simple task. Use `none` or real sibling issue refs (`#123, #124`), never invented numbers or free text in the dependency value. Specify resource ordering as dependencies where parallel work would collide.
7. Define focused checks, integration checkpoints, and platform-specific verification. When feasible, establish the baseline; otherwise label it unverified. Record existing failures separately and require no regressions rather than silently assigning unrelated repairs.
8. Review the whole plan, including edge cases and contrary evidence; use an independent reviewer only when available and authorized, otherwise do a distinct inline review. Verify complete requirement coverage, valid references, and an acyclic dependency graph after issue creation. Check that resource ordering actually prevents simultaneous conflicting tasks.
9. Use a single durable issue spec or maintain `brief.md`, `decisions.md`, and `plan.md` when files improve the handoff. Put all accepted requirements and prototype decisions in readable chat/issue text. Never require a ZIP or manifest just to recover the plan, or another session to discover an undocumented local scratch log.
10. Return to zdev for a direct Codex Cloud prompt and available artifacts. Record normalized -m/-is/-isask/-pr intent in every relevant issue and the handoff. Planning does not automatically become implementation.
