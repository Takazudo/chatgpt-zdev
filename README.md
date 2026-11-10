# zudo-dev-flow

A personal ChatGPT plugin for repository-grounded development planning in Chat, optional UI prototyping and issue sweeps, and a standalone implementation prompt for Codex, Claude Code, or Grok, locally or in the cloud. `zdev` is the sole planning facade.

## Use

- `zdev for https://github.com/owner/repo: <goal>` plans the work and returns a copyable implementation prompt.
- `zdev -pr ...` iterates UI prototypes in Chat until the user accepts a direction, then plans and packages real artifacts when available.
- `zdev -is ...` sweeps the requested backlog with one bulk triage checkpoint. `-isask` interviews candidates, including postponed issues. If both appear, `-isask` wins.
- `zdev -m -is for https://github.com/zudolab/zudo-text` sweeps issues, and tells the later implementation session to merge only after complete implementation and verification under repository policy.
- `zdev -cccp ...` targets Claude Code Cloud's Project feature. Choose another environment or an allowed set using the flags below. The spaced spelling `- cccp` is normalized to `-cccp`.
- `zdev -a ...` requests an issue/PR sweep and repeated planning/development in any supported environment until a fresh sweep finds no actionable in-scope work. Routine bug fixes need no extra bulk approval; user decisions and other blockers stay recorded.
- `zdev -cccp -a -m for https://github.com/zudolab/zudo-text` combines a Project team, continuous development and conditional merge authorization. These three choices are independent: neither `-cccp` nor `-a` implies merge permission, and `-cccp` alone does not start a continuous sweep.
- `zdev -cowsl -a -m ...` continuously handles work that can be implemented and fully accepted in Codex local CLI on WSL. It excludes inseparable Mac-required tasks and conditionally merges only eligible work.
- `zdev -cccp -comac -a ...` allows Project or Codex local CLI on Mac. If mandatory Mac acceptance is required, select the Mac environment and its local subagents; the mere presence of Project in the candidate set does not add Project child-session instructions.
- `zdev -grmac ...` or `zdev -grwsl ...` targets Grok local CLI on Mac or WSL. It is intended for smaller daily development tasks, has no computer-use capability, and must verify acceptance through actually available tools.
- `zdev -grc ...` targets a Grok bot cloud environment comparable to Codex Cloud, with actual cloud tools and workers checked before use; it does not inherit Project or desktop features.

The ChatGPT planning session and every delegated helper use GitHub read-only. They prepare the prompt, proposed tracking structure and necessary artifacts without creating or changing issues, epics, labels, comments, branches, commits or PRs, closing or merging anything, or initiating GitHub-write approval requests. Explicit standalone GitHub management requests are separate from this planning facade.

## Execution environments

| Flag | Execution environment |
| --- | --- |
| `-cccp` | Claude Code Cloud using the Project feature |
| `-coc` | Codex Cloud |
| `-cowsl` | Codex local CLI on WSL |
| `-comac` | Codex local CLI on Mac |
| `-ccwsl` | Claude Code local CLI on WSL |
| `-ccmac` | Claude Code local CLI on Mac |
| `-grmac` | Grok local CLI on Mac (no computer use) |
| `-grwsl` | Grok local CLI on WSL (no computer use) |
| `-grc` | Grok bot cloud (Codex Cloud-like) |

With no environment flag or explicit prose constraint, choose from the task's implementation and acceptance requirements. If real Mac confirmation is mandatory, choose an appropriate Mac environment. If there is no host-specific requirement, keep the prompt portable and explicitly tell the user: **This prompt can run in any supported environment.** Expand the actual environment names in the standalone prompt; do not assume that another session knows this flag table or that the planning host is the requested destination.

One environment is a hard scope constraint. Include only work whose implementation and all required acceptance can finish there. A WSL-only plan excludes inseparable Mac-required work; do not start it and defer mandatory Mac acceptance. Record the original issue, unmet requirement and suitable environment, and continue compatible tasks. A useful portable slice can proceed only with its own complete acceptance criteria, while the larger original issue remains open.

Multiple flags form a deduplicated, unordered allowed set. Choose only within it and prefer one sufficient environment; the flags neither select the first or last entry nor require all candidates to run. Use different allowed hosts for independent tasks only when necessary, with explicit boundaries. If no task fits, report the empty compatible executable scope. Honor equivalent constraints in prose and never widen the set because another host happens to be available.

CI may satisfy legitimate repository gates, but it does not add an allowed execution environment or replace required native, physical or human evidence. An environment name is not proof that credentials, native tools or physical inputs are available. Record actual capability blockers separately from environment-excluded scope and unresolved decisions. See the shared [environment contract](skills/zdev/references/execution-environments.md).

## Continuous development and worker ownership

With `-a`, the brief supplies a repository-grounded first wave and a complete continuation procedure on all nine environments, including a local CLI working sequentially. The implementation session refreshes issues, PRs, recent merges and checks; plans the next ready batch; develops, reviews and verifies it; integrates only when authorized; then sweeps again. Newly found in-scope defects join the queue after the same environment and acceptance filter is reapplied. A merged PR is a checkpoint, not the end of the requested session. Existing issue bodies are checked against comments and current source so already-landed fixes are not reimplemented.

Keep genuine product/design decisions separate from access, platform, human-verification and CI/review blockers. Preserve `no-auto`, accepted UI and protected coordination. Continue independent work while a topic is held. An explicit `-isask` interview still wins, and `-pr` still requires UI acceptance; `-a` replaces only the ordinary bulk approval for already-requested routine fixes. Without `-m`, the loop leaves PRs and delivery issues open pending integration. Stop at a fresh sweep with no ready work, or a real external/session limit, and report the exact remaining state without claiming incomplete acceptance is delivered.

When Claude Code Cloud Project is the selected environment, its manager owns the queue, difficult decisions, review and integration, and children are Project child sessions. Apply that procedure only after selection, not because Project is one allowed candidate. Codex Cloud uses only the worker facilities actually exposed there. Grok bot cloud also uses only its actual available cloud facilities, with no assumed desktop, Project sessions, or computer-use tools.

For a selected local CLI environment, child work means subagents. Prefer one coherent substantive topic per subagent, with a clear outcome, owned paths, dependencies and acceptance criteria. Let it investigate, plan, implement, self-review and run focused tests across the topic's related files or issues. Reuse the same subagent for follow-ups and corrections. Split only for independently completable outcomes, ownership or capability boundaries, or an unmanageably broad topic. The parent keeps the queue, cross-topic decisions, ownership coordination, integration, independent review and final acceptance. Serialize overlapping edits and follow the repository's worktree, commit and push rules. Without subagent support, the parent proceeds sequentially and the continuous loop still applies. For Grok local CLI, subagents are optional only if verified available; size work into smaller, unambiguous daily tasks with explicit checks. Grok CLI cannot operate the desktop through computer-use features, so tasks requiring inseparable GUI interaction/acceptance must be excluded or assigned to a separately allowed capable environment.

Use capable workers at the user's selected or configured model and effort. Opus at medium effort and Astra at low effort are examples of the intended worker capability, where available; they are not fixed model identifiers or permission to override configured settings. Discover supported capabilities, preserve chosen model and effort, respect cost and concurrency limits, and avoid artificial fan-out. Durable issue checkpoints retain the allowed environments, selected host, excluded tasks, SHAs, topic/worker/branch/PR mappings, results and next actions so the parent can resume without duplicate work.

## Tracking during implementation

The generated prompt directs the separate implementation agent to establish tracking after inspecting the repository and before changing implementation code. A focused task uses one tracker; a larger plan uses an epic and linked sub-issues. Reuse matching open records and PRs, and create only what is missing. Put accepted requirements, decisions, dependencies, acceptance criteria and verification plans in the issues so another session can resume from them.

Use the issues as the development notebook: record meaningful findings, decisions, progress, checks with observed results and relevant revisions, PR links, blockers and next actions. The prompt authorizes the requested in-scope issue operations without an additional generic confirmation step; actual access controls and repository policy still apply. If an issue write is unavailable, preserve the proposed content, report the precise blocker and continue independent authorized work.

All flag combinations become ordinary instructions in the final prompt. `-m`/`--merge` means the author wants the merge completed after development, not just a merge-ready PR. Merge after required review, approvals and current-head checks pass, even when the repository's existing automation updates published websites or services on merge. Inspect and disclose those effects; do not skip or reconfirm the merge solely for them. Report integration and automatic deployment results separately. Without `-m` or an equally explicit merge instruction, do not infer merge intent: leave the implementation PR and delivery issues open pending integration, with honest status notes. Close completed children after verified integration and the parent only when its whole accepted scope is complete. Preserve incomplete original issues, unrelated work, actual permissions and higher-priority safety requirements. Separate deployment commands, releases, manual plugin publication and deployment/security setting changes need their own authorization.

## Standalone handoff

The handoff contains actual repository/issue/PR URLs, the complete accepted scope, dependency order, artifact references, verification evidence and lifecycle instructions. It uses no plugin names, app links, private skill invocations, raw planning flags or planning-Chat permission instructions. The implementing agent needs only the prompt, accessible repository and identified inputs; it does not need this plugin or the source Chat.

Session-created deliverable files and the ZIP are saved under a session folder in Dropbox `codex-artifacts/` when the connector permits; failures and pending confirmations are reported. A ZIP supplements the complete readable prompt when real prototype source/assets/fixtures exist. Missing ZIP bytes are requested only when an exact input is indispensable.

`zstatus` and `zwatch` remain independent connected-computer observation skills.

`zkicadactions` plans and reviews KiCad native verification on pinned GitHub Actions: artifact-only workflow rules, owned-container cleanup, separate authorities, and receipt review where UNKNOWN is never PASS. Its bundled offline checkers (`check_receipt.py`, `lint_workflow.py`) never dispatch or start KiCad, and its Codex Cloud prompt template carries the same limits. It never dispatches, publishes, merges, adopts outputs, edits CAD or starts manufacturing.

## Source validation and packaging

```bash
python3 scripts/validate.py
python3 -m unittest discover -s scripts -p 'test_*.py'
python3 scripts/package.py --output /tmp/zudo-dev-flow-0.9.0.zip
```

See [acceptance cases](docs/acceptance-cases.md), [provenance](docs/provenance.md), and [release steps](docs/releasing.md). A source PR does not update the installed account plugin.
