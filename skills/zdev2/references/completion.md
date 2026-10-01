# Work completion, merge, and Codex continuation

## Normal completion

Finish accepted scope, review the resulting diff against the issue, run the appropriate checks, and inspect CI for the current head. Keep draft status while implementation or essential verification remains; otherwise mark ready. Without merge authorization, leave the PR open even when green and provide the user a continuation prompt for review/merge.

No indefinite CI watch is promised. Fix concrete change-related failures while the tools and session can make progress. When work remains because of access, platform, unresolved failures, or practical session limits, preserve it as a precise Codex task. Do not present limitations as success or abandon independent implementation.

## `-m` / `--merge` gate

This is the only merge flag; `-a` is unnecessary and is not merge authorization. Apply the user's “perfectly done” standard as observable requirements:

- All accepted implementation and acceptance criteria are satisfied, including required platform/UI checks; no deferred required verification or unresolved change-related failures.
- The final diff has been reviewed, actionable findings fixed, and required repository approvals satisfied. Do not invent a human approval or treat self-review as a required external approval.
- Relevant local checks passed, and all required CI checks for the **current head SHA** have succeeded. Pending, failed, unknown, cancelled, or unexpectedly missing required CI blocks merging. If no CI applies, verify and record why rather than treating an empty check list as proof.
- Correct repository, head, target, issue scope, and mergeability are freshly confirmed. New commits invalidate old head-specific evidence. Preserve branch protections; no admin bypass, no force push, no inherited prc `--no-wait` shortcut.
- Any baked temporary resources have been migrated and removed from the merge diff; no unfinished sibling work is being falsely closed. Resource-only mode never qualifies.

If any gate is unmet, do not merge. Leave the PR open with exact evidence and a continuation prompt carrying the original merge intent conditionally. Do not ask again for authorization already granted. If all gates pass, merge with the repository-supported method and head-SHA guard when available; confirm the merged state. Close only fully satisfied linked issues. Clean up only task-owned obsolete branches where safe; never delete a host-owned session branch.

After merge, inspect target-branch checks when available. If post-merge CI fails or remains unknown/pending, report that separately and provide a Codex continuation; do not call the overall workflow fully verified. Do not promise a background watcher unless a real supported monitor was created at the user's request.

## Portable Codex handoff: mandatory for every exit with work remaining

Codex is a different environment. Assume it has **none of this plugin's skills** and no ChatGPT chat history. This rule applies to partial implementation, resource-only passthrough, dependency-blocked/no-change attempts, unavailable write access, post-merge repair, and direct-to-Codex routing from planning.

Do not copy the incoming Work prompt unchanged. Rewrite it as executable plain-language instructions. The outgoing Codex prompt must not invoke `zdev`, `zdev1`, `zdev2`, `zplan`, `zproto`, `zgh`, a plugin namespace, a plugin installation, or another private workflow skill such as `x-wt-teams` or `prc`. Expand the needed behavior into actual steps. Translate flags such as `-m` into their explicit authorization and conditions. Do not merely say “follow the workflow” or “finish cleanup.”

### Inventory and ordered actions

Before writing the prompt, inventory every relevant issue, dependency PR, feature/base/resource PR, branch and resource directory. For each include the full URL or repository-relative path, role, last observed state/SHA, requested action, prerequisite, and final disposition. Re-read current state when possible; label observations that could not be refreshed. Use `none created` for missing feature PRs, not fabricated URLs.

Spell out this order with actual task-specific identifiers:

1. Read repository instructions, full issue bodies and relevant comments; refresh all listed PRs, issues and target branches. Preserve current user work. Reassess stale observations before acting.
2. Resolve dependency gates first. State which prerequisite must land in which branch. If authorized to finish that prerequisite, name the precise PR to update, review, verify and merge; then refresh the target branch. If not authorized, preserve its branch/PR and report the concrete blocker; do not close it merely to unblock the feature. Work that is independent of the gate can continue. A feature handoff does not silently grant authority over an unrelated migration.
3. State whether to **reuse and update an existing PR** or create a new feature branch/PR from the refreshed target once the gate is satisfied. A resource/base PR is normally adopted and updated into the implementation PR, not closed or merged as a resource-only delivery. Include its branch, base, pinned resources and exact cleanup paths.
4. Describe full accepted implementation, non-goals, tests/commands, review and CI repair. Include what is already done and what was not run. Move lasting files into production locations and remove specified temporary resource directories before merge.
5. For each PR, explicitly choose update/keep open/merge/close-as-superseded. Merge only with carried user authorization, completed acceptance, review, required approvals, and current-head checks. Closing an unmerged PR discards its delivery; do that only for a verified superseded/abandoned PR within authorized scope, with a replacement link. Never use “close PR” as an ambiguous synonym for merge.
6. After confirmed delivery and required verification, close only fully satisfied issues and include evidence/PR links. Verify auto-closures rather than assuming them. Close completed sub-issues before their epic, and completed epics before a super-epic; keep any parent with unfinished descendants open. Keep dependency issues outside scope unchanged. Do not close an implementation issue merely because a resource PR exists or a handoff was produced.
7. If merge is not authorized, leave the verified PR ready and the delivery-tracking issues open; state that final merge and then eligible issue closure remain. Report actual final state, blockers, and kept resources. Delete only task-owned obsolete branches after confirmed merge when safe; preserve platform-owned or still-needed bases.

### Final prompt template

Deliver actual PR links and a fenced text prompt with all relevant URLs **inside** it. Replace all placeholders, remove inapplicable lines, and ensure each relevant issue/PR has a concrete action and condition. No plugin access should be needed to understand or execute it.

```text
Implement/finish <goal> in <repository URL> in a writable repository session.
Read <full issue URLs and comment URLs> and repository instructions.
Accepted scope: <behavior, decisions, acceptance criteria and non-goals>.
Last observed state: <each relevant issue/PR URL, role, open/draft/merged state, head/base and SHA>. Feature PR: <actual URL or none created>.
Completed: <actual work, or no implementation/branch/commit created>.
Resources: <pinned commit, paths, provenance, or none required>.
Verification so far: <commands/results, current CI revision/jobs, blocked or not-run checks>.

Execute in this order:
1. Refresh the listed issues, PRs and <target branch>; verify the current state before changing anything.
2. Prerequisite: <exact dependency PR URL must land in branch; authorized steps to finish it OR leave it unchanged and report the gate if still unmet>. Do not modify protected/out-of-scope branches <names>.
3. Once that gate is satisfied, <adopt and update PR URL on branch OR create a feature branch from refreshed target and open a PR to target>. Do not create a duplicate PR.
4. Implement <remaining concrete steps>. Run <commands and required platform checks>; review, fix change-related failures, and inspect CI for the current head.
5. Remove <exact temporary resource paths after migrating lasting files, or no resource cleanup needed>. Update <PR URL/body> with final scope and evidence. Keep <other PR URLs> open; close <superseded PR URLs> only after <verified replacement condition and authorization>, or state none to close.
6. Merge permission: <explicitly authorized for these PRs, with complete acceptance/review/approvals/current-head checks OR not authorized: leave the PR ready and open>. No deployment or package publication is included unless expressly authorized.
7. After confirmed merge/delivery and required verification, close <specific fully satisfied issue URLs in child-to-parent order> with evidence; keep <unfinished/dependency issues> open. If merge is not authorized or a gate remains unmet, leave those delivery issues open and report what remains.
8. Report final PR/issue states, verification, unresolved work, and retained resources.
```

If no feature PR exists, state why and give its conditional creation step. A dependency gate may need to be resolved before that step; do not make creating a PR the first action unconditionally. No-change passthrough still needs this full action sequence. Do not invent work or silently elevate merge/closure permissions.

Before sending, review the actual outgoing prompt: remove skill calls and plugin names, expand workflow shorthand, resolve every PR/issue reference into a full URL, distinguish merge from close, check order and conditions, and verify that a fresh Codex session can proceed using only this prompt and the repository/GitHub context.
