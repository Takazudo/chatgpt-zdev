---
name: zkicadactions
description: "Plan, review and hand off KiCad native verification on pinned GitHub Actions (artifact-only, digest-pinned KiCad image). Use for zkicadactions, KiCad CI, kicad-cli/pcbnew in Actions, board smoke/identity runs, receipt review, KiCad検証. Not for CAD edits, routing, DRC acceptance, ordering or manufacturing."
---

# zkicadactions

Read [the verification contract](references/contract.md) and [the templates](references/templates.md). Answer in the user's language; Japanese is fine.

## What this skill does in Chat

- Fill the Plan template with the user: purpose, allowed and excluded operations, acceptance questions, immutable source SHA and separate tooling SHA, image digest and exact CLI/pcbnew version, input allowlist with hashes, explicit limits, positive and negative controls, reviewer, and each authority separately. Write `UNKNOWN` for anything not established.
- Review a workflow file or receipt the user provides. When a Python sandbox is available, run [lint_workflow.py](scripts/lint_workflow.py) and [check_receipt.py](scripts/check_receipt.py) on the supplied bytes with a config copied from [project-config.example.json](templates/project-config.example.json). They are offline: no dispatch, download, Docker or KiCad. Without a sandbox, apply the same checks by reading.
- Produce one self-contained Codex Cloud prompt for implementation or a reviewed run, using the handoff template. It must work without this plugin or the Chat history.

## Never from this skill

- Never dispatch a workflow, publish, merge, upload a candidate, adopt outputs, edit CAD, or start ordering or manufacturing. Planning text and handoff bundles create no new authority.
- Never call an unread artifact validated, an identity PASS a connectivity/DRC/electrical/assembly/manufacturing PASS, or a PASS an adoption decision. UNKNOWN is not PASS.
- Never bypass a denied access through another tool, host or URL; record the denial and report the evidence limit.
- Never present unimplemented modes (nonpublic candidate ingestion; CAD change, routing, refill, DRC acceptance) as usable. Their design and acceptance criteria are in the contract.

The OSC project values in [osc-hole-field.config.json](templates/osc-hole-field.config.json) are one reviewed example, not defaults for other repositories.
