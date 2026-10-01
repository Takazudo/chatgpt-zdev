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

## Required unfinished-work ending

Deliver the actual PR link(s) and a fenced text prompt. Fill all fields with observed values. The PR URL must be **inside** the prompt as well as visible in the response. Include issue URLs and enough accepted scope that Codex does not need ChatGPT history.

```text
Continue <goal> in <repository URL>.
PR: <actual URL>. Issues: <actual URLs>.
Base: <branch>; head: <branch>; inspected head SHA: <SHA>.
Accepted decisions and acceptance criteria: <concise complete summary; linked durable spec>.
Completed: <implemented behavior>.
Resources: <pinned commit/path/manifest and base PR, or none required>.
Checks: <commands and actual passed/failed/blocked/not-run results>. CI: <jobs, revision, failure messages or pending/unknown status>.
Remaining: <ordered implementation, platform verification, review, CI repair and merge steps; commands where known>.
First inspect the current PR and branch state, then resume only outstanding work. Preserve accepted scope and repair change-related failures without weakening checks.
<If baked: adopt the existing base PR, use its resources, and delete the temporary resource directory after migrating lasting files and before merge.>
Merge authorization: <not granted OR already granted by -m, conditional on complete acceptance, review, required approvals, and current-head checks>. Deployment is not included.
Keep issues with unfinished requirements open. Report final evidence and actual PR/merge status.
```

If PR creation itself is blocked, do not fabricate a link. Supply the pushed branch/SHA or complete patch artifact, exact blocker, and a prompt whose first pending action is to create the PR. State the PR deliverable remains blocked. Complete all independent checks and implementation first.
