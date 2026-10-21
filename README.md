# zudo-dev-flow

A personal ChatGPT plugin for repository-grounded development planning in Chat, optional UI prototyping and issue sweeps, and a self-contained Codex Cloud handoff. `zdev` is the sole planning facade.

## Use

- `zdev for https://github.com/owner/repo: <goal>` plans the work, creates or updates durable issues when authorized, and returns a copyable Codex Cloud implementation prompt.
- `zdev -pr ...` iterates UI prototypes in Chat until the user accepts a direction, then plans and packages real artifacts when available.
- `zdev -is ...` sweeps the requested backlog with one bulk triage checkpoint. `-isask` interviews candidates, including postponed issues. If both appear, `-isask` wins.
- `zdev -m -is for https://github.com/zudolab/zudo-text` sweeps issues, and tells the later Codex session to merge only after complete implementation and verification under repository policy.

All flag combinations carry their effective meaning into planning issues and the final prompt. Without `-m`, the implementation PR stays open, original issues get a PR link and honest status comment, and delivery issues stay open pending integration. With `-m`, Codex may merge after required review, approvals and current-head checks pass, then close only fully satisfied in-scope issues. `-m` never authorizes deployment or publication.

The handoff contains actual repository/issue/PR URLs, accepted scope, dependency order, artifacts, verification evidence and lifecycle instructions. The implementation session need not install this plugin or read the source Chat. A ZIP supplements readable issues when real prototype source/assets/fixtures exist. Missing ZIP bytes are requested only when an exact input is indispensable.

`zstatus` and `zwatch` remain independent connected-computer observation skills.

`zkicadactions` plans and reviews KiCad native verification on pinned GitHub Actions: artifact-only workflow rules, owned-container cleanup, separate authorities, and receipt review where UNKNOWN is never PASS. Its bundled offline checkers (`check_receipt.py`, `lint_workflow.py`) never dispatch or start KiCad, and its Codex Cloud prompt template carries the same limits. It never dispatches, publishes, merges, adopts outputs, edits CAD or starts manufacturing.

## Source validation and packaging

```bash
python3 scripts/validate.py
python3 -m unittest discover -s scripts -p 'test_*.py'
python3 scripts/package.py --output /tmp/zudo-dev-flow-0.6.0.zip
```

See [acceptance cases](docs/acceptance-cases.md), [provenance](docs/provenance.md), and [release steps](docs/releasing.md). A source PR does not update the installed account plugin.
