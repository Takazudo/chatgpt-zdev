# zudo-dev-flow

A personal ChatGPT plugin for repository-grounded development planning in Chat, optional UI prototyping and issue sweeps, and a standalone implementation prompt for Codex or Claude Code, locally or in the cloud. `zdev` is the sole planning facade.

## Use

- `zdev for https://github.com/owner/repo: <goal>` plans the work and returns a copyable implementation prompt.
- `zdev -pr ...` iterates UI prototypes in Chat until the user accepts a direction, then plans and packages real artifacts when available.
- `zdev -is ...` sweeps the requested backlog with one bulk triage checkpoint. `-isask` interviews candidates, including postponed issues. If both appear, `-isask` wins.
- `zdev -m -is for https://github.com/zudolab/zudo-text` sweeps issues, and tells the later implementation session to merge only after complete implementation and verification under repository policy.
- `zdev -cccp ...` targets Claude Code Cloud's Project feature, with a capable manager session and bounded child-session work. The spaced spelling `- cccp` is normalized to `-cccp`.
- `zdev -a ...` requests an issue/PR sweep and repeated planning/development until a fresh sweep finds no actionable in-scope work. Routine bug fixes need no extra bulk approval; user decisions and other blockers stay recorded.
- `zdev -cccp -a -m for https://github.com/zudolab/zudo-text` combines a Project team, continuous development and conditional merge authorization. These three choices are independent: neither `-cccp` nor `-a` implies merge permission, and `-cccp` alone does not start a continuous sweep.

The ChatGPT planning session and every delegated helper use GitHub read-only. They prepare the prompt, proposed tracking structure and necessary artifacts without creating or changing issues, epics, labels, comments, branches, commits or PRs, closing or merging anything, or initiating GitHub-write approval requests. Explicit standalone GitHub management requests are separate from this planning facade.

## Continuous development and Project teams

With `-a`, the brief supplies a repository-grounded first wave and a complete continuation procedure. The implementation session refreshes issues, PRs, recent merges and checks; plans the next ready batch; develops, reviews and verifies it; integrates only when authorized; then sweeps again. Newly found in-scope defects join the queue. A merged PR is a checkpoint, not the end of the requested session. Existing issue bodies are checked against comments and current source so already-landed fixes are not reimplemented.

Keep genuine product/design decisions separate from access, platform, human-verification and CI/review blockers. Preserve `no-auto`, accepted UI and protected coordination. Continue independent work while a topic is held. An explicit `-isask` interview still wins, and `-pr` still requires UI acceptance; `-a` replaces only the ordinary bulk approval for already-requested routine fixes. Without `-m`, the loop leaves PRs and delivery issues open pending integration. Stop at a fresh sweep with no ready work, or a real external/session limit, and report the exact remaining state without claiming incomplete acceptance is delivered.

With `-cccp`, the Project manager owns the queue, difficult decisions, review and integration. Children receive bounded tasks, ownership, dependencies and verification; follow the repository's worktree and push rules. Use the host's actual capabilities and preserve model choices. Durable issue checkpoints retain SHAs, task/worker/branch/PR mappings, results and next actions so the manager can resume without duplicate work.

## Tracking during implementation

The generated prompt directs the separate implementation agent to establish tracking after inspecting the repository and before changing implementation code. A focused task uses one tracker; a larger plan uses an epic and linked sub-issues. Reuse matching open records and PRs, and create only what is missing. Put accepted requirements, decisions, dependencies, acceptance criteria and verification plans in the issues so another session can resume from them.

Use the issues as the development notebook: record meaningful findings, decisions, progress, checks with observed results and relevant revisions, PR links, blockers and next actions. The prompt authorizes the requested in-scope issue operations without an additional generic confirmation step; actual access controls and repository policy still apply. If an issue write is unavailable, preserve the proposed content, report the precise blocker and continue independent authorized work.

All flag combinations become ordinary instructions in the final prompt. Without `-m`, leave the implementation PR and delivery issues open pending integration, with PR links and honest status notes. With `-m`, merge only after required review, approvals and current-head checks pass, then close completed children after verified integration. Close the parent only when its whole accepted scope is complete. Preserve incomplete original issues and unrelated work. `-m` never authorizes deployment or publication.

## Standalone handoff

The handoff contains actual repository/issue/PR URLs, the complete accepted scope, dependency order, artifact references, verification evidence and lifecycle instructions. It uses no plugin names, app links, private skill invocations, raw planning flags or planning-Chat permission instructions. The implementing agent needs only the prompt, accessible repository and identified inputs; it does not need this plugin or the source Chat.

Session-created deliverable files and the ZIP are saved under a session folder in Dropbox `codex-artifacts/` when the connector permits; failures and pending confirmations are reported. A ZIP supplements the complete readable prompt when real prototype source/assets/fixtures exist. Missing ZIP bytes are requested only when an exact input is indispensable.

`zstatus` and `zwatch` remain independent connected-computer observation skills.

`zkicadactions` plans and reviews KiCad native verification on pinned GitHub Actions: artifact-only workflow rules, owned-container cleanup, separate authorities, and receipt review where UNKNOWN is never PASS. Its bundled offline checkers (`check_receipt.py`, `lint_workflow.py`) never dispatch or start KiCad, and its Codex Cloud prompt template carries the same limits. It never dispatches, publishes, merges, adopts outputs, edits CAD or starts manufacturing.

## Source validation and packaging

```bash
python3 scripts/validate.py
python3 -m unittest discover -s scripts -p 'test_*.py'
python3 scripts/package.py --output /tmp/zudo-dev-flow-0.7.0.zip
```

See [acceptance cases](docs/acceptance-cases.md), [provenance](docs/provenance.md), and [release steps](docs/releasing.md). A source PR does not update the installed account plugin.
