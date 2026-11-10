# Release and migration

## v0.9.0 Grok execution environments

Add `-grmac` (Grok local CLI on Mac), `-grwsl` (Grok local CLI on WSL) and `-grc` (Grok bot cloud, Codex Cloud-like). All nine flags remain unordered allowed candidates with the same implementation/acceptance filter and independent `-a` / `-m` lifecycle. Grok CLI targets have no computer-use capability and use a less capable model suited to bounded, concrete daily tasks with explicit verification; do not invent subagent, GUI or visual acceptance facilities. Grok bot cloud uses only confirmed cloud capabilities, not Project or desktop APIs.

Review all nine selected hosts and the portable profile under merge/non-merge and continuous/non-continuous execution; reject raw Grok planner flags in handoffs and preserve legitimate shell commands. Confirm the new copyable capability blocks apply only to the selected Grok host. Run source validation, regression tests, and packaging. Update both manifests consistently. A main-branch source update does not itself update the installed ChatGPT plugin; that remains a separate action.

## v0.8.1 requested merges and automatic publication

Clarifies that `-m`/`--merge` requests completion of the merge after development and its gates, including existing automated updates to published websites or services. The handoff discloses known production effects and requires separate merge/deployment status reporting; an expected automatic update alone is not a reason to hold or reconfirm the merge. No merge intent is inferred without the flag or an equally explicit prose instruction. Separate deployment commands, releases, manual plugin publication and settings changes remain separately authorized; concrete safety, permission, approval and task-specific restrictions remain effective.

Review the behavior with and without merge intent, with automatic website/service updates, failed or unknown deployment results, separate manual publication, and real approval/access conflicts. Validate all resolved environment and continuous-mode handoff profiles. Static template checks do not prove live host behavior. Synchronize both manifests and build the source package. Source merge and account-plugin update remain separate, authorized operations; neither a local package nor a source PR proves the installed plugin changed. Preserve plugin identity, inventory, sharing, default prompts and unrelated behavior.

## v0.8.0 execution environments and topic ownership

Defines `-cccp` (Claude Code Cloud Project), `-coc` (Codex Cloud), `-cowsl` and `-comac` (Codex local CLI on WSL and Mac), and `-ccwsl` and `-ccmac` (Claude Code local CLI on WSL and Mac). With no environment constraint, select from implementation and acceptance requirements, or explicitly keep the prompt portable when no host-specific requirement exists. One environment is a hard scope constraint; multiple environments form a deduplicated, unordered allowed set. Explicit prose constraints have the same effect. Never infer extra destinations from the current host.

Review complete acceptance when filtering executable scope. A WSL-only plan excludes inseparable Mac-required tasks instead of implementing them with mandatory Mac acceptance deferred. Independent portable slices need their own complete criteria and leave their larger issues open. An empty compatible scope must be reported honestly. Existing CI gates do not expand the allowed set or replace real native, physical or human evidence; actual missing capabilities are separate blockers.

Continuous development applies on every environment and repeats this filter for each new wave and discovered task. Project child-session instructions apply only when Project is selected. Local CLI children are subagents: prefer one coherent substantive topic per worker, reuse it for follow-ups and corrections, and split only for independent outcomes, ownership/capability boundaries or an unmanageable topic. The parent owns coordination, cross-topic decisions, integration, independent review and acceptance. Preserve repository commit/push rules and configured models/effort; Opus medium and Astra low are illustrative capability examples, not fixed identifiers or settings overrides. Use only actual host worker facilities, with sequential fallback when unavailable.

Review the behavioral cases for no/one/multiple environments, duplicate flags, explicit prose constraints, Project as an unselected candidate, incompatible and independently portable tasks, physical verification blockers, local topic ownership and resume after a changed requirement. Check standalone prompts for all selected environments and portable output, both merge states and continuous/non-continuous operation. Confirm all six planner flags are translated into plain instructions rather than leaked. Static validation and package tests do not establish actual worker or native-verification behavior in another host.

This release adds `skills/zdev/references/execution-environments.md` and retires no files. Preserve plugin identity, the seven-skill inventory, audience, default prompts and unrelated behavior. Synchronize both manifests, validate and package the source, merge the reviewed source update, then update the existing account plugin in place and read back its version and affected files. A source commit or package build alone does not update the installed plugin; backend readback also does not prove that an already-open chat has hot-reloaded its mounted skills.

## v0.7.0 Project teams and continuous development

Adds two independent planning options: `-cccp` selects Claude Code Cloud Project manager/child execution, and `-a` requests a continuous issue-sweep/development loop. The spaced spelling `- cccp` normalizes to `-cccp`. Neither option grants merge authority; `-m` retains its conditional review, approval and current-head CI gates. Explicit interviews, UI acceptance, no-auto restrictions and external verification holds remain effective. The continuous mode removes a redundant bulk approval for already-requested routine fixes, not those boundaries.

Review the first-wave plan, continuing queue, new-defect scope, decision/blocker separation, manager/child ownership, fresh-sweep end condition and checkpoint/resume behavior. Test flag leakage, both merge branches, ordinary no-flag behavior, flag combinations and stale/landed-issue handling. Static package validation does not establish actual child-session behavior in another host.

This release adds two reference files and retires none. Preserve plugin identity, the seven-skill inventory, audience, default prompts and unrelated behavior. Synchronize both manifests, validate and package the source, then update the existing account plugin in place and read back the new release and affected source. A source commit or package build alone does not update the installed plugin.

## v0.6.4 implementation tracking and standalone prompts

The ChatGPT planning session and all delegated helpers remain read-only for GitHub and never initiate GitHub-write approval requests. The separate implementation prompt requires tracking before code changes: reuse or create a tracker for a focused task, or an epic and linked sub-issues for a larger plan. Issues hold the accepted specification and development notes throughout the work. Close completed children after required integration, then their parent when the full accepted scope is complete.

Prompts support Codex or Claude Code, locally or in the cloud. Convert every accepted planning flag into plain actions and explicit lifecycle conditions. Do not pass plugin names, app links, private skill invocations or the planning Chat's permissions to the implementing agent. Preserve actual repository access controls and all existing merge gates.

Review the shared workflow, handoff, tracking, sweep and repository-research guidance together. Check representative focused and multi-task prompts, existing tracker reuse, issue-write failures, resume-after-compaction behavior, and both merge-permission cases. Keep the seven-skill inventory, plugin identity, audience, default prompts and unrelated behavior unchanged. Update the existing account plugin in place, then read back the version and affected files; a locally built archive does not establish installation or live host behavior.

## v0.6.3 planning-session issue boundary

Keep GitHub writes and their approval requests out of the ChatGPT planning session and its delegated helpers. Prepare issue content in the handoff when useful and let the separate user-started implementation session reuse, create or update in-scope issues and useful epics under its actual permissions and repository policy. Preserve explicit user restrictions, duplicate prevention, merge gates, plugin identity and sharing. Verify the shared contract, handoff template and issue-sweep guidance agree on this boundary.

## v0.6.2 Dropbox artifacts

Save zdev deliverables and prototype rounds in a unique Dropbox session folder, subject to connector requirements. Preserve existing plugin identity and sharing.

## v0.6.1 prompt and artifacts only

Planning and its delegated helpers perform read-only GitHub research. No planning issues, epics, PRs, labels, comments, branches, commits, pushes or merges. Sweep decisions stay in the handoff; standalone GitHub management and separately authorized implementation remain available. Update the existing private plugin in place, preserving identity and sharing; this source/package build does not publish or install it.

## v0.6.0 KiCad Actions skill

Adds `skills/zkicadactions/` (SKILL.md, agent metadata, references, offline scripts and config templates). Nothing is retired; an overlay update only adds files. Read back v0.6.0 and the seven-skill inventory in a fresh chat.

## v0.5.1 sole planning facade

`zdev` is the sole planning entry point. The `zdev1` alias is removed; its handoff and sweep references now live under `skills/zdev/references/`. `zdev2` remains retired. The package retains its `z-dev-flow` identity, `zudo-dev-flow` display name, author, logo, default prompt and observation skills.

An installed-plugin update is separate from this source release. Because the updater overlays files, inspect the installed inventory and explicitly delete these retired `zdev1` paths if present:

- `skills/zdev1/SKILL.md`
- `skills/zdev1/agents/openai.yaml`
- `skills/zdev1/references/handoff.md`
- `skills/zdev1/references/issue-sweep.md`

Delete any remaining `zdev2` paths from the actual installed inventory as well. Preserve plugin identity and sharing. Read back v0.5.1 and the six-skill inventory in a fresh chat.

## Build

```bash
python3 scripts/validate.py
python3 -m unittest discover -s scripts -p 'test_*.py'
python3 scripts/package.py --output /tmp/zudo-dev-flow-0.9.0.zip
```

Source PR merge and account-plugin update are separate operations.
