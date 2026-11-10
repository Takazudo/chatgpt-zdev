## 0.9.0 — 2026-11-11

- Add three zdev allowed-environment flags: `-grmac` for Grok CLI on Mac, `-grwsl` for Grok CLI on WSL, and `-grc` for Grok bot cloud (Codex Cloud-like).
- Explicitly constrain Grok CLI to no computer-use interactions and favor smaller, routine, well-specified and verifiable work suited to its less capable model. Use optional subagents only if actually available; never claim unavailable GUI/visual verification.
- Apply cloud tool/capability discovery to Grok bot, without inheriting Project or local CLI worker APIs. Extend the existing unordered environment set, acceptance filter, standalone prompt, docs and regression coverage to nine targets, preserving independent continuous/merge flags.
- Update the two synchronized plugin manifests; source updates do not automatically update an installed account plugin.

## 0.8.1 — 2026-11-09

- Treat `-m`/`--merge` as the author's explicit request to complete the merge after development and required gates, not merely prepare a merge-ready PR.
- Include existing automatic updates to published websites and services triggered by that merge; disclose the effects and report merge/deployment outcomes separately instead of adding a generic deployment hold.
- Keep no-flag behavior non-merging unless the user gives an equally explicit prose instruction. Preserve review, current-head checks, task restrictions, actual permissions and higher-priority safety requirements; separate deployment, release and publication actions retain their own authorization.
- Align the facade, shared contract, standalone handoff and helper references; add regression coverage and behavioral acceptance cases. Preserve plugin identity, seven skills and unrelated workflows.

## 0.8.0 — 2026-11-08

- Define six execution environments: `-cccp` for Claude Code Cloud Project, `-coc` for Codex Cloud, `-cowsl` and `-comac` for Codex local CLI on WSL and Mac, and `-ccwsl` and `-ccmac` for Claude Code local CLI on WSL and Mac.
- Resolve no environment by task requirements, including mandatory Mac confirmation; explicitly keep unconstrained portable work runnable in any supported environment. Treat one environment as a hard scope constraint and multiple environments as a deduplicated, unordered allowed set.
- Exclude tasks whose implementation or mandatory acceptance cannot finish within the allowed set. Preserve original issues and unmet requirements; permit independently useful portable slices only with complete acceptance criteria of their own. Keep environment exclusions distinct from decisions and actual capability or verification blockers.
- Apply `-a` continuous sweeps and development on every environment, refiltering scope before each new wave and discovered task. Keep merge authority independent and retain all review, approval and current-head check gates.
- Apply Project manager/child instructions only when Project is selected. For local CLI execution, children are subagents owning substantive topics across investigation, planning, implementation and focused verification, with follow-ups and corrections kept with the same worker.
- Keep the parent responsible for coordination, difficult cross-topic decisions, integration and independent acceptance review. Preserve repository ownership rules, use real host capabilities, and retain sequential fallback when workers are unavailable.
- Treat examples such as Opus medium and Astra low as capability guidance, not universal model identifiers or authority to change configured models or effort. Carry environment choices, exclusions and topic ownership into durable continuation checkpoints.
- Preserve the seven-skill inventory, plugin identity, sharing, default prompts, planning read-only boundary, implementation tracking and unrelated observation/artifact behavior.

## 0.7.0 — 2026-11-07

- Add `-cccp` for Claude Code Cloud Project manager/child-session execution; normalize the spaced spelling `- cccp` and preserve actual host capabilities, model choices and repository ownership rules.
- Add `-a` for an autonomous issue/PR sweep plus repeated planning, implementation, review, verification and resweeping until no actionable in-scope work remains.
- Ground the first wave in current issues, comments, source, PRs and recent merges; retain later batches as an evidence-driven queue rather than stopping after the first PR.
- Separate unresolved product decisions from access, native/live/human verification and CI/review blockers; preserve no-auto restrictions, explicit interviews, UI acceptance and conditional merge gates.
- Keep the environment, continuous-loop and merge flags independent. Retain planning read-only and translate the full workflow into one standalone prompt with durable issue/worker checkpoints.
- Preserve the seven-skill inventory, plugin identity, sharing, default prompts, artifact-storage behavior and independent observation routes.

## 0.6.4

- Keep GitHub writes and their approval requests out of the ChatGPT planning session and its delegated helpers only.
- Start the separate implementation session by creating or reusing one tracker, or an epic with linked sub-issues, before implementation.
- Use issues for durable requirements, decisions, progress, verification, blockers and PR links; close completed children after required integration, then the fully completed parent.
- Generate standalone prompts for Codex or Claude Code, locally or in the cloud. Expand planning flags into plain instructions and omit plugin names, app links and private skill dependencies.
- Preserve existing tracking history, duplicate prevention, merge gates, plugin identity, sharing and default prompts.

## 0.6.3 — 2026-11-07

- Scope the GitHub write restriction to the ChatGPT planning session and its delegated helpers, avoiding unattended write-approval requests there.
- Prepare issue content in the handoff and allow the separate implementation session to reuse, create or update in-scope issues and useful epics under its permissions and repository policy.
- Remove downstream issue bans from the shared contract, handoff template, planning helpers and issue sweep; preserve merge gates, explicit user restrictions and duplicate prevention.

## 0.6.2

- Save zdev session deliverables and prototype rounds to a session-specific Dropbox folder, with explicit upload status and fallback.

# v0.6.1

- Planning returns a self-contained prompt and necessary artifacts, with no GitHub or repository-history writes, including delegated helpers.
- Preserve sweep checkpoints and downstream conditional merge intent; standalone GitHub management remains explicit.

## 0.6.0

- Add zkicadactions: plan, review and hand off KiCad native verification on pinned GitHub Actions (artifact-only, owned containers, separate authorities, UNKNOWN is not PASS).
- Bundle offline receipt and workflow checkers with tests; extend validation to seven skills and the KiCad Codex prompt template.

## 0.5.1

- Remove zdev1, leaving zdev as the sole planning facade.
- Move handoff and sweep references under zdev; keep the same flags and direct Codex Cloud workflow.

## 0.5.0

- Make zdev the Chat planning facade and retain zdev1 as a thin alias.
- Replace mandatory Work execution with a direct, self-contained Codex Cloud handoff; remove zdev2.
- Carry -m, -is, -isask and -pr through issues and prompt with explicit PR and issue lifecycle rules.
- Preserve UI prototype artifacts and independent zstatus/zwatch behavior.

# Changelog

## 0.4.1

- Honor ongoing watch lifetime and user-defined stopping conditions; remove the invented 30-minute deadline.
- Keep unchanged cycles quiet by default and adapt cadence to host costs and task needs.
- Retain disconnected or host-blocked watches as unresolved with resumable state and unchanged recovery budgets.


## 0.4.0

- Add zstatus and zwatch using host-supported connected-computer delegation.
- Rescan sessions/windows/panes every cycle and track newly active/restarted work.
- Report completion and detailed decisions; bound authorized API recovery and handle cancellation, duplicates, stale output and connection loss.
- Add a read-only snapshot helper and regression coverage; preserve plugin identity, default prompt and development routes.

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
