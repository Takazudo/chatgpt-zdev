# Handoff artifacts and continuation prompts

## Producer

Use the same-Project route by default. State which Chat to keep in the Project and that the user opens a new Work chat there. Name the source Chat exactly when available; do not invent a chat URL or promise automatic file transfer.

If implementation needs generated files, create a ZIP containing complete accepted source and its dependencies, plus `handoff.json`. Include concise `brief.md`, `decisions.md`, `plan.md`, and `github.md` if useful. Keep rejected prototype variants out unless they are needed to explain an accepted decision. Validate the archive and examine source for accidental truncation or omitted sections. Generated code, drafts, and pseudocode must be distinguished. Provide a real download link in the final response; a code block naming a nonexistent archive is not delivery.

The manifest records:

- `task`: goal, accepted decisions, constraints, non-goals, acceptance criteria, authorized actions;
- `mode`: `implementation`, `resource-only`, or `direct-codex`;
- `size_assessment`: bounded/oversized and the reasons;
- `source_chat`: exact title and known URL/ID, plus Project name if known;
- `repository`: URL, base branch, inspected base SHA, issue URLs, implementation order, and any existing seed/base branch, commit and PR;
- `transfer_status`: `producer-verified`, `attachment required`, or `destination-verified` (only the receiver sets the last);
- `artifacts`: logical name, purpose, required boolean, filename, archive-relative entry path, byte size, SHA-256, locator/transport and access requirements; compute hashes from actual file bytes, or explicitly mark unavailable;
- `verification`: actual checks/results, draft/provisional files, and limitations.

List payload files only; do not put the manifest's own hash inside itself. Use safe relative archive paths without traversal. A Project source reference and ZIP attachment can both be recorded; neither is marked destination-verified by the producer. If there are no file inputs, a complete issue spec plus explicit `Artifacts: none required` is sufficient and a manifest is optional.

## Receiver

Open the named sibling Chat/context and actual required files using available tools. Extract the ZIP safely, check integrity, and compare manifest sizes and hashes when supplied. Read requirements and accepted decisions, not just file names. Report exactly what was readable. Reconcile the planned revision with current code before applying any patch.

If a required file is unavailable, try the documented alternative locator, then ask for that exact attachment/access. Do not search another session's filesystem or substitute a smaller implementation. Independent repository research can continue. Optional images do not block work whose full specification is available.

For Codex, all needed context must be in issues, committed resources, or explicitly attached files. Do not make sibling-chat access a Codex prerequisite.

## Prompt templates

Replace every angle-bracket field with actual values before delivery, omit inapplicable lines, and never fabricate identifiers. Include a short accepted-spec summary even when linking issues. Each final prompt is one fenced text block, not only a prose offer to continue. Carry `-m` only when explicitly authorized.

### Bounded implementation in a new Work chat

```text
Use zdev2 for <goal> in <repository URL>.
In this ChatGPT Project, refer to the sibling Chat “<exact source title>” <known URL/ID> and its accepted artifact <ZIP filename/version, entry paths>.
Read <issue/epic URLs>. Accepted decisions: <summary>. Acceptance criteria: <criteria>. Out of scope: <non-goals>.
Base: <branch>, inspected at <SHA>. Mode: implementation.
First verify that the required files <names> are readable and complete in THIS session; read handoff.json and validate its payload. If the Project context cannot provide them, ask me to attach <exact ZIP filename>. A source-session path is not a transferred file.
<For no-artifact work: Artifacts: none required; the linked issues contain the complete specification.>
Implement the full accepted scope, run the relevant checks, push a branch, and open/update a PR explicitly targeting <base>.
Merge authorization: <not authorized OR -m, only after all completion gates pass>.
If anything remains, end with the PR link and a copyable Codex continuation prompt that includes that link, exact remaining steps, evidence, and permissions.
```

### Oversized plan with resources: Work only bakes

```text
Use zdev2 in resource-only mode for <repository URL> and <issue/epic/super-epic URLs>.
This plan is oversized because <reasons>. Do not implement product changes in this Work session and do not merge the resource PR.
In this Project, refer to sibling Chat “<exact title>” <known URL/ID> and accepted artifact <ZIP filename/version, entry paths>. Verify handoff.json and all required files here. If unavailable, ask me to attach <exact ZIP>.
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
