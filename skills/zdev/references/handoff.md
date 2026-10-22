# Codex Cloud handoff

## Producer checklist

Complete the accepted implementation brief in readable Chat and prompt text: goal, accepted UI and corrections, behavior/states, constraints and non-goals, acceptance criteria, components, dependency order, verification and actual permissions. Do not publish the plan to GitHub. Planning is read-only for GitHub and repository history: do not create or update issues, epics, labels, comments, branches or PRs; do not commit, push, close, or merge. This applies to delegated helpers too. Return only a self-contained prompt plus necessary artifacts. Never ask a downstream implementer to create planning issues as a workaround. A ZIP is supplementary and contains real implementer-needed prototype source/assets/fixtures when they exist; inspect and validate the archive. If none exist, say `Artifacts: none required`. Never claim that a source Chat's sandbox path or attachment bytes automatically transfer to Codex Cloud. If exact input bytes are indispensable, identify them and their destination-readable locator, or name the concrete blocker and continue independent planning.

Read current GitHub state before writing the prompt. Record actual issue and PR URLs, target branch and SHA, existing bases/resources, checks already observed, and what is merely planned. Describe whether the later implementation session should reuse/update a matching task PR or create a branch and draft PR; do not perform those actions during planning. For multiple topics, give dependency order, integration checkpoints, and explicit per-PR merge/hold decisions. Choose the simplest fitting implementation workflow; explain any consequential deviation from the plan. The prompt must be self-contained and use no plugin or private skill names.

Carry normalized flags into the prompt: `-pr` means the accepted UI direction; `-is` means only the accepted bulk sweep scope; `-isask` means only the accepted interview scope; `-m` means conditional merge after verified delivery. If both sweep flags were supplied, record `-isask` as effective. Do not convert a planning permission into release/deployment authority.

## Copyable prompt template

Replace every placeholder with actual information and omit inapplicable lines. Include the prompt in one fenced text block in the final Chat response; link any artifact ZIP separately. This is a template, not a claim that the listed work already happened.

```text
Implement <accepted goal> in <repository URL> in this separate user-started Codex Cloud implementation session.
The complete plan is below. Do not create planning issues or epics; no planning publication is required.
Read repository instructions, <existing relevant issue URLs, if any>, relevant comments, and current source. Base: <branch>, last inspected at <SHA>. Refresh all state before changes.
Accepted scope: <requirements and accepted prototype decisions>. Non-goals: <explicit exclusions>. Acceptance criteria: <observable results>.
Planning flags and scope: <normalized -is or -isask scope, -pr direction if applicable; -m authorization or no merge authorization>. Follow only the accepted scope; preserve unrelated issues.
Dependency order: <prerequisites and integration checkpoints>. Suggested execution/model policy: <simple direct implementation or justified delegated topics with difficulty hints; manager stays on the session model and user overrides prevail>. PR plan: <each actual or planned PR, target, merge/hold decision, gate, and issue effect>. Existing PRs/branches: <actual URLs, roles, states and SHAs, or none created>. Reuse/update <matching PR URL or none>; do not create a duplicate. Artifacts: <repository paths/attached files and whether exact bytes are required, or none required>.
Verification already observed: <commands and results, CI revision, unknown/not-run checks>. Do not report a check as passed unless observed.
Implement the full accepted scope in dependency order, review the diff, run relevant checks and UI verification, fix change-related failures, push a branch, and open or update a draft PR targeting <branch>. Inspect required CI for the current head and obey repository approvals and merge policy. Leave the PR draft while essential work or verification remains.
<Without -m: Leave the implementation PR open. Comment on each original in-scope issue with the PR URL and actual completion/verification status; keep it open pending integration. Do not merge or close delivery issues.>
<With -m: For each PR marked eligible to merge, merge only after its accepted work, review, required approvals and current-head required checks pass under repository policy. Leave intentionally held or incomplete PRs open. Confirm each integration, then close only issues whose own criteria are genuinely met, with PR and verification evidence; leave incomplete parents and unrelated issues open. If a gate remains, hold that PR and report it.>
For each existing dependency/resource PR, state whether to update, preserve, merge when authorized, or close as superseded only after verifying its replacement. Move lasting resources into production paths and remove temporary resource paths before merge. Never treat closing an unmerged PR as delivery.
Do not deploy, publish a release, or close unrelated issues based on merge authorization. Report actual final PR/issue states, verification, unresolved work and retained resources.
```
