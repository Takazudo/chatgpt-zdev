# Behavioral acceptance cases

Expected results distinguish the ChatGPT planning session from the separate implementation session. Review actual generated prompts against these cases; static checks alone do not prove live host behavior or account installation.

| Input or situation | Expected result |
|---|---|
| `zdev` rough request | Complete grounded standalone prompt plus necessary artifacts; the planning Chat and its helpers perform only read-only GitHub research and initiate no GitHub-write approval requests. |
| Focused implementation task | Prompt directs the implementing agent to inspect state, reuse or create one tracker, and then implement. It includes accepted requirements, acceptance criteria and verification. |
| Multiple independently completable tasks | Prompt directs creation or reuse of a parent epic and linked sub-issues before implementation, with dependencies, concrete criteria, parent/child links and progress tracking. |
| Matching tracker, epic or children already exist | Read their scope and state, reuse appropriate records and create only missing ones. Preserve existing history and original issues. |
| Resume after compaction or uncertain issue-creation response | Recover canonical URLs and inspect existing records before retrying; do not create duplicate trackers or children. |
| Issue operations already requested by the execution prompt | No generic additional confirmation step for those in-scope writes; actual tool access controls and repository policy still apply. |
| User expressly forbids new issues across implementation | Carry that restriction forward, reuse permitted existing tracking, and adapt the default template so it grants no conflicting creation authority. |
| GitHub issue write unavailable | Preserve the proposed issue content and task mapping, report the exact failed operation or missing access, and continue independent authorized work without claiming the issue exists. |
| Meaningful implementation milestone or change of approach | Record findings, decisions, progress, verification commands/results with relevant revisions, PR links, blockers and next actions in the issues; keep parent and children consistent. |
| Pausing or handing off unfinished work | Update the issues with enough durable context for another session to resume without the originating Chat or private skill. |
| Generated prompt for Codex or Claude Code, local or cloud | Inline the complete execution procedure and preserve the specified environment. Include no plugin invocation, app link, raw planning flag or instruction about the planning Chat's permissions. |
| `zdev -m -is for https://github.com/zudolab/zudo-text` | Bulk sweep checkpoint; prompt translates accepted task groups and conditional merge intent into plain actions. No deployment or release authority. |
| `zdev -isask -is -pr -m` | Interview wins, accepted UI topics prototype after triage, and effective scope and lifecycle become plain instructions in the prompt. |
| `zdev -pr` | Explicit UI acceptance before plan; readable decisions and validated artifact ZIP when real files exist. |
| Standalone explicit GitHub management request | zgh may perform the requested operation; planning delegation never supplies that authority. |
| `-re` or newly reported sweep problem | Refresh only the handoff summary or add a local task during planning; tracking for accepted work is established later by the implementation agent. |
| Planning helper asked to publish resources | Return actual required files in the artifact ZIP; no resource PR, branch push or commit during planning. |
| No artifacts | State none required; give the complete standalone implementation prompt. |
| Indispensable exact asset unavailable | Name the dependent requirement and blocker; finish independent planning. |
| No `-m` | Implementation agent still creates/reuses tracking and records progress, but leaves the PR and delivery issues open pending integration with PR links and honest status. |
| `-m` with required check pending or red | Hold the affected PR and delivery issues open; record the exact gate and make no delivery claim. |
| `-m` with full acceptance, review, approvals, current-head checks | Merge per repository policy, confirm integration, add completion evidence, close fully satisfied children, then close the parent only when its entire accepted scope is complete. |
| Genuine non-code task | Close only after its explicit accepted deliverable and verification are complete; do not invent a code-merge requirement. |
| Partial implementation or merely replaced source issue | Keep remaining requirements visible and the issue open; creating a replacement or linking a PR does not establish completion. |
| Multi-PR `-m` with one eligible PR and one intentionally held PR | Merge only the eligible PR after its gates; retain the held PR, its incomplete issues and incomplete parent. State dependency order and each disposition in the prompt. |
| Task-specific user constraint | Honor it over generic defaults; choose a fitting workflow without needless orchestration. |
| Existing feature/resource PR | Inspect read-only and instruct the implementation session to reuse/update it when appropriate; distinguish merge from close-as-superseded. |
| Session creates deliverable files | Save each under one unique Dropbox `codex-artifacts/` session folder as produced, including prototype rounds and final ZIP; report actual upload status. |
| Dropbox unavailable or upload requires confirmation | Report the blocker or pending confirmation and provide available download fallback; never claim an upload succeeded. |
| zstatus/zwatch | Existing one-shot/ongoing observation behavior remains independent of planning. |
| `zkicadactions` plan request | Plan template filled with UNKNOWN where unestablished; separate authorities; no dispatch. |
| `zkicadactions` green identity receipt | Identity PASS only; connectivity, DRC, electrical, assembly and manufacturing reported NOT_EVALUATED; adoption left to the owner. |
| `zkicadactions` artifact download denied | Reported as unread evidence (UNKNOWN); no alternate tool, host or URL. |
| `zkicadactions` asked to upload a nonpublic candidate or auto-adopt routing | Held as unimplemented with its acceptance criteria; no upload or push. |
