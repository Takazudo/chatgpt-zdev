# Templates — UNKNOWN is not PASS

## Plan

```text
Purpose / allowed operations / excluded operations:
Acceptance questions answered by this lane / dimensions not judged:
Source repository + immutable SHA / exact input file hashes:
Tooling/workflow SHA / image digest / CLI+pcbnew versions:
Public inputs versus unpublished transfer (owner, destination, authorized files):
Isolated output path / original read-only protection / expected change allowlist:
CPU, memory, PIDs, worker count, controller/step/job deadlines, cleanup/upload reserves:
Owned process/container identity and refusal rules:
Positive controls / missing identity, mismatched hash, timeout, cleanup-failure negative controls:
Independent reviewer and exact reviewed diff:
Publication / merge / dispatch / adoption authority (separate):
```

## Run receipt review

```text
RunID/attempt/URL, mode, exact source/tooling SHA:
Status (pending/success/failure/uncertain) and first-failure location:
Versions, command argv, exits, measured time, output hashes:
Before/after originals, owned-container normal exit and removal evidence:
Artifact IDs/digests/bytes/expiry, actually inspected files:
Missing/unread evidence and exact denied operation, if any:
Identity / connectivity / DRC / electrical / assembly result (separate):
Changed-input follow-up rationale; no unchanged rerun:
Adoption decision + reviewer + owner authority (not implied by PASS):
```

## Codex Cloud handoff

Replace placeholders with actual facts and omit inapplicable lines. Keep authorities exactly as the user granted them.

```text
Work in <repository URL>. Read repository instructions and <issue/PR URLs>. Base: <branch> at <SHA>; refresh state first.
Goal: <accepted goal>. Acceptance questions: <what this lane answers>. Not judged: connectivity, DRC, electrical, assembly, manufacturing unless a reviewed mode implements them.
Pins: source <SHA>, tooling <SHA or "the reviewed PR head">, image <name@sha256:digest>, KiCad <exact version>, inputs <path: sha256 list>.
Workflow rules: workflow_dispatch only; permissions contents: read; checkout persist-credentials: false; no secrets, cache, pickle or push; actions pinned by commit SHA; one hosted job and worker; every step has timeout-minutes within the job limit; allowlisted small artifacts only, with a failure receipt written first.
Containers: create with recorded random name, label and CID plus CPU/memory/PID limits; remove only owned objects after verifying identity; uncertain create or cleanup fails closed; a client timeout is not termination.
Tests: add negative controls for <list>; run unit tests in normal and -O modes; never invoke native entrypoints on a shared local host.
Authority: <publish yes/no>, <merge yes/no>, <dispatch yes/no, at most once, record run ID>, candidate upload no, adoption no, physical actions no.
If a dispatch response is uncertain, inspect existing runs before any new dispatch. Never rerun an unchanged failure; keep the first failing receipt.
If artifact retrieval is denied, record the denial and stop; do not use another tool, host or URL.
Report: exact SHAs, run ID, artifacts actually read, each dimension separately, unread evidence, and anything still UNKNOWN.
```
