# Handoff artifacts and continuation prompts

## Producer: make the plan readable without downloading the ZIP

Use the same-Project route by default. Name the exact source Chat and known URL/ID, and tell the user to open a new Work chat in that Project. Put a complete **Accepted implementation brief** directly in the final Chat message and the repository issue: goal, accepted variant, user corrections, behavior, UI states/interactions, content, constraints, non-goals, acceptance criteria, affected components, execution mode, and actual permissions. Do not hide essential decisions only inside an archive. For a long plan, put the complete spec in the issue and an accurate summary plus its URL in the final Chat.

For prototype work, explicitly describe the accepted layout and behavior, attach or embed useful visible evidence when supported, and retain complete source in the artifact ZIP. Where exact source or assets are indispensable, persist them through an authorized destination-readable source or expose necessary text/code in the chat/issue. Never claim that a sandbox download link transferred bytes to another chat.

Deliver the prompt plus a downloadable ZIP when artifacts exist, as requested. The ZIP is an additional reusable deliverable and manual-transfer fallback, not a prerequisite to ordinary implementation from the accepted spec. If there are no artifacts, say so. Inspect files for completeness and validate an archive you actually produce. Do not generate a `verify_handoff.py` ceremony or require the receiver to execute a generated verifier before starting work.

An optional `handoff.json` may record task, source chat, mode, repository/base/SHA, issues, accepted decisions and resource inventory. For each resource classify it as **reference/reconstructible** or **exact input required**, with the concrete reason for the latter. A legacy `required: true` label alone does not prove that implementation needs the exact bytes. Hashes, if computed, describe actual files and can check a transfer; absent hashes/manifests never gate a specification-driven implementation. No manifest is mandatory.

## Receiver: use the available specification

1. Read the named sibling Chat's relevant messages and actual user acceptance, not only its title or a summary. Read the full issue and current repository. Use further chat turns and documented resource locators to resolve missing context. An empty attachment inventory is not an empty specification.
2. Assess requirements coverage. If accepted behavior and acceptance criteria are clear, proceed with implementation. Use accessible source, screenshots, and prototype references; implement from the accepted design when original prototype files are unavailable. Do not claim original files were read or hashes matched when they were not.
3. Inspect exact files when the work actually consumes their bytes. Verify supplied integrity metadata when receiving/applying those files; a mismatch means that particular input is untrusted until reconciled. It does not erase an independently sufficient specification or block unrelated work.
4. Ask for an attachment only when a concrete indispensable input remains unavailable after consulting accessible context. Name that input and the dependent requirement. Continue all unaffected implementation; do not stop at research when product work is already specified. Preserve explicit user exact-file/integrity requirements.
5. For old generated handoffs, replace the blanket ZIP/manifest/verifier prerequisite with this sufficiency assessment. A pasted agent-authored checklist is not evidence that the user separately demanded byte-for-byte reproduction. If the user did explicitly demand that, honor it.

Resource-only work can materialize complete text/code from readable chat or issue content and persist it, recording provenance and that it is reconstructed. It must not invent missing binary assets or claim a reconstructed prototype is the accepted original. Ask only for irreplaceable missing resources. Codex handoffs must put all needed context in GitHub or attached files rather than requiring sibling-chat access.

## Prompt templates

Replace every angle-bracket field with actual values before delivery, omit inapplicable lines, and never fabricate identifiers. Include a short accepted-spec summary even when linking issues. Each final prompt is one fenced text block, not only a prose offer to continue. Carry `-m` only when explicitly authorized.

### Bounded implementation in a new Work chat

```text
Use zdev2 for <goal> in <repository URL>.
In this ChatGPT Project, refer to the sibling Chat “<exact source title>” <known URL/ID> and its accepted artifact <ZIP filename/version, entry paths>.
Read <issue/epic URLs>. Accepted decisions: <summary>. Acceptance criteria: <criteria>. Out of scope: <non-goals>.
Base: <branch>, inspected at <SHA>. Mode: implementation.
Read the accepted brief, prototype decisions and my acceptance in that sibling Chat, plus the full issue. Begin implementation from that specification. The ZIP is supplementary: do not stop because its bytes, handoff.json, hashes or a generated verifier are unavailable. Request a file only for a concrete indispensable input missing from all available context, and continue unaffected work. Exact inputs, if any: <names and reasons, otherwise none>.
<For no-artifact work: Artifacts: none required; the linked issues contain the complete specification.>
Implement the full accepted scope, run the relevant checks, push a branch, and open/update a PR explicitly targeting <base>.
Merge authorization: <not authorized OR -m, only after all completion gates pass>.
If anything remains, end with the PR link and a copyable Codex continuation prompt that includes that link, exact remaining steps, evidence, and permissions.
```

### Oversized plan with resources: Work only bakes

```text
Use zdev2 in resource-only mode for <repository URL> and <issue/epic/super-epic URLs>.
This plan is oversized because <reasons>. Do not implement product changes in this Work session and do not merge the resource PR.
In this Project, read sibling Chat “<exact title>” <known URL/ID>, its accepted brief and accessible resources <names/locators>. Persist accessible originals or materialize complete text/code from that context with explicit provenance. The ZIP <filename> is supplementary; request only indispensable missing exact resources, without inventing or claiming to verify their bytes.
Base: <branch and inspected SHA>. Accepted decisions: <summary>.
Persist the smallest complete accepted resource set at <_temp-resource/issue-slug/> on <planned reusable base branch>, with only necessary scanner exclusions. Push and open a draft base PR targeting <base>, read back the remote files, and update the issues with Use this PR as base and the pinned paths/SHA.
For a super-epic preserve its shared base and each child epic's base markers; prepare per-epic resources as specified in the hierarchy.
Leave all implementation issues open. End with the base PR link(s) and a self-contained Codex prompt containing them, implementation order, resource locators, cleanup-before-merge requirement, and <actual merge authorization for the eventual implementation>.
```

### Oversized plan without artifacts: direct Codex

```text
Implement <goal> in <repository URL> from <issue/epic/super-epic URLs>.
Skip ChatGPT Work; this plan is oversized because <reasons> and needs no Chat-generated file artifacts.
Read the full issue hierarchy and implementation order. Accepted decisions: <summary>. Acceptance criteria: <criteria>. Base: <branch and inspected SHA>.
<If the receiving Codex has the user's x-wt-teams skill: use x-wt-teams with the real epic entry and authorized flags. Otherwise execute the same dependency graph using the self-contained issues.>
For a super-epic, verify or create the documented shared base from the intended parent, preserve child markers, complete each epic in order, and open the final PR to <parent>. Explicitly honor the stated authorization for intermediate merges into the staging base; absent that permission, prepare the PR topology and request it before merging.
Run applicable checks, review the result, and keep unfinished issues open. Merge authorization: <actual permission>; deployment is not included.
The specification must be executable from GitHub without access to ChatGPT history.
```
