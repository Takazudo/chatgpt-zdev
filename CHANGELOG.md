# Changelog

## 0.3.3 — 2026-10-02

- Make all Codex-bound handoffs independent of plugin/private skill availability, including resource-only and blocked/no-change passthrough.
- Require concrete ordered PR/issue actions, dependency gates, explicit permissions, resource cleanup and conditional child-to-parent issue closure.
- Distinguish updating, merging and closing a superseded PR; preserve unrelated prerequisite work and unfinished issues.

## 0.3.2 — 2026-10-02

- Fix the mandatory ZIP/manifest/hash/verifier gate that blocked same-Project zdev2 startup despite a readable accepted spec.
- Require zdev1 to expose accepted requirements and prototype decisions in readable chat/issue text.
- Make zdev2 implement from sufficient context, including old generated handoffs; request only indispensable exact inputs and continue unaffected work.
- Let resource-only Work persist accessible or explicitly reconstructed source with provenance, without claiming missing original bytes were verified.
- Separate real environment permission restrictions from artifact access; preserve all merge and acceptance gates.

## 0.3.1 — 2026-10-02

- Rename the displayed plugin to `zudo-dev-flow`, preserving the existing package identity and six skills.
- Confirm the account plugin successfully contains the clean v0.3.0 six-skill release before applying this metadata update.

## 0.3.0 — 2026-10-02

- Replace eight hyphenated skill entries with zdev, zdev1, zdev2, zplan, zproto, and zgh.
- Make Chat planning/prototype/sweep end with issues, an explicit same-Project continuation prompt, and available artifact ZIP; preserve receiver verification and manual-upload fallback.
- Port bulk/interview issue-sweep semantics, hierarchy, ordering, human-check dashboard, and verified seed supersession.
- Route oversized plans directly to Codex or through resource-only Work with reusable draft base PRs and cleanup requirements.
- Make Work implementation autonomous by default with conditional -m/--merge and complete Codex continuation prompts containing PR links.
- Remove mandatory first-dev implementation, z-local/zdev3, and z-skill.
- Add source provenance, migration guidance, packaging, static validation, and behavioral acceptance cases.
- Preserve package identity and logo. Installed account replacement is separate because the available updater cannot delete retired skill files.

# v0.2.3

- Require durable cross-session source transfer and self-contained continuation prompts.
- Add artifact manifest, integrity checks, and destination input preflight.
- Detect truncated seed source and request exact missing transfers before dependent work.
- Apply the same contract to local finalization; preserve zdev1/zdev2/zdev3 titles.

# v0.2.2

- Set the three phase skill UI titles and document headings to exactly zdev1, zdev2, and zdev3.
- Preserve internal identifiers and workflow references for compatibility.

# v0.2.1

- Convert to Agent Plugins 1.0 with root plugin.json.
- Preserve all eight workflow skills and their reference contracts.
- Synchronize the legacy Codex manifest and add listing metadata and a default icon.
- Update z-skill packaging guidance for the portable format.

# Changelog

## 0.2.0

- Reworked workflow around explicit Chat → Work → local phases.
- Added `first dev` as a required Chat-side seed implementation stage.
- Added Work-specific completion semantics: PR progress is primary; unavailable modules/device checks and unreproducible CI red may hand off locally.
- Added detailed GitHub operations/handoff skill.
- Added ChatGPT Sites preference when the active surface exposes Sites, with standalone prototype fallback in ordinary Chat.
- Renamed all personal skills to short `z-` aliases.
- Made the user, not the workflow, trigger the Work transition.
