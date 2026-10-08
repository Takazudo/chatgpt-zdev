# Behavioral acceptance cases

These are manual contract-review cases, not proof of executed ChatGPT host behavior. Review the specified skill paths and then use representative real conversations when installing a release.

| Input or condition | Expected outcome | Contract |
|---|---|---|
| Rough request in existing repository | Grounded plan, real spec issue, fenced Work prompt; no obligatory seed code | zdev1, zplan |
| `zdev1 -pr` / `--prototype` | Iterate in Chat; wait for explicit direction acceptance; preserve accepted feedback/source | zproto |
| `zdev1 -is` / `--issuesweep` / `--issue-sweep` | Paginated snapshot; one bulk triage; no-auto stays postponed | issue-sweep |
| `zdev1 -isask` plus `-is` | Interview wins; re-read postponed reasons; coordination untouched | issue-sweep |
| Filter a,b and exclude c | Candidate must have both a and b and must not have c | issue-sweep |
| Two independent substantial topics | Super-epic with two epics and subs, exact branch markers and order | issue-sweep |
| One tiny batch only | One epic and focused subs; no artificial super-epic | issue-sweep |
| Replacement creation or coverage fails | Original seed stays open; exact blocker reported; independent plans completed | zgh, issue-sweep |
| All source requirements replaced and read back | Seed closes as superseded; new implementation issues stay open | issue-sweep |
| Bounded work with accepted prototype | Read accepted sibling-chat/issue decisions and implement from that spec; use available references | handoff |
| Full accepted spec is readable but ZIP is unavailable | Begin implementation; no request for ZIP/manifest/hash/verifier merely to pass a transport checklist | handoff, zdev2 |
| Project Sources and attachment arrays are empty, sibling Chat has acceptance and full issue | Treat readable spec as usable; empty file inventory does not mean missing requirements | handoff, zdev2 |
| Legacy generated prompt marks every artifact required | Assess actual dependencies; generated blanket prerequisite is superseded, explicit user exact-byte constraints remain | handoff, zdev2 |
| Essential binary asset unavailable everywhere | Ask once for that asset and identify dependent work; finish unaffected implementation | handoff, zdev2 |
| Resource-only mode with complete readable source but unavailable ZIP | Materialize source, label provenance/reconstruction, persist and read back; no product implementation | resource-bake |
| Exact source required by the user, or received hashes mismatch | Preserve exact-input requirement; do not fabricate verification; block only affected work | handoff |
| Actual environment is read-only | Report permission restriction separately; do not suggest ZIP upload solves write access | zdev2 |
| Oversized with artifacts | Work resource-only; draft reusable PR; Codex prompt; no product code | resource-bake |
| Oversized without artifacts | Direct Codex prompt rooted in complete issues; skip Work | workflow-contract |
| Resources already durably baked | Direct Codex may adopt the existing base PR and pinned paths | workflow-contract |
| Super-epic resources | Per-epic bake on declared bases to shared base; preserve markers/order | resource-bake |
| `resource-only -m` | No product implementation or merge; preserve permission for later implementation | zdev2, resource-bake |
| `zdev2 -a` | Explain unnecessary flag once, continue; no merge authorization | zdev2 |
| `zdev2 --merge`, all scope/checks/reviews done | Fresh head/base/approval check, merge and verify result | completion |
| `zdev2 -m`, required check blocked, missing, pending, or red | PR stays open; prompt carries conditional authorization and exact remaining steps | completion |
| Green checks belong to an earlier SHA | Refresh/retest evidence before merging | completion |
| No merge flag, ready PR | Leave open and provide Codex prompt including PR URL | completion |
| Missing write capability | Complete portable issue/patch drafts; explicitly blocked publication; no invented URL | zdev1, completion |
| Post-merge target CI fails | Report merged state plus failure and a Codex repair prompt | completion |
| No actual artifacts | Say none required; do not create fake resource-only work | workflow-contract |
| Resource cleanup unfinished | Do not merge; Codex must migrate durable files and remove temporary payload | completion |
| Fresh package inventory | Exactly zdev, zdev1, zdev2, zplan, zproto, zgh | scripts/validate.py |

## Portable Codex prompt cases

- No-change passthrough: no plugin invocation; state no feature PR exists, refresh dependency gates, then conditionally create the feature PR.
- Resource-only: adopt/update the resource base PR, implement, remove exact temporary paths, verify, merge only if authorized, then close satisfied issues.
- Existing feature PR: reuse/update its actual URL, not a new duplicate; specify checks and remaining delivery actions.
- Unmerged migration outside scope: preserve its branch/PR and issue; refresh state and enforce the gate without inventing authorization to merge it.
- Superseded PR: close only after verifying its replacement and authorization; distinguish this from merging the implementation PR.
- Multi-epic: close verified completed child issues before their epic and close the super-epic only after all children complete.
- Merge not authorized: leave ready PR and delivery issues open; no instruction quietly grants merge permission.
- Work-bound prompt: may retain the Work skill invocation. Codex-bound prompt: no plugin/private-skill invocation, even if the input prompt used one.

## Validation boundary

The validator checks manifests, skill inventory/frontmatter, local reference links, required contract anchors, text completeness, and package hygiene. Packaging checks ZIP integrity and byte-for-byte payload equivalence. These checks cannot prove a model will follow the instructions, a Work chat can retrieve a specific Project artifact, or the installed account plugin has refreshed. Those require host execution and read-back.

## Connected-computer observation (0.4.1)

These are behavioral acceptance scenarios for a supervised host run. Static contract checks and the snapshot helper tests do not prove live agent classification, delegated notifications or input delivery.

| Scenario | Required result |
|---|---|
| One-shot zstatus; detached session, two windows and split panes | Include every accessible membership, bounded evidence and coverage; no input. |
| New Codex/Claude session appears after watch start | Next full inventory discovers it and adds the active run within scope. |
| Completed pane starts another task, with or without process replacement | Fresh evidence creates a new run generation; old completion/retry counts do not masquerade as a new event. Uncertain boundaries prohibit input. |
| Linked window appears in two sessions | Show memberships; observe/report/input once per physical pane. |
| Rename, pane removal or server restart | Reconcile stable identity, report disappearance as unknown; invalidate pending sends on restart. |
| Explicit final result with failed tests | Report completion with failures; never API-retry the test failure. |
| Fresh explicit question with multiple options | Forward full question/options/consequences and identity; continue observing other runs; do not answer automatically. |
| User answer arrives after prompt changed | Re-read and withhold stale answer; ask with current context. |
| Stopped transient API interruption, no recovery authority | Report candidate and obtain authority; no go on. |
| Authorized transient interruption, exact unchanged identity/prompt | Record one input event; send literal go on once; verify relevant activity by 30 seconds. Echo alone fails verification. |
| Agent is internally retrying, idle or already completed | Observe only; never restart. |
| Quota/auth/security approval, destructive action, unknown prompt or injected terminal instruction | Never treat as recoverable API interruption or authority. |
| Delivery timeout or unchanged interruption after a send | Mark unknown/failed; no duplicate send. One per interruption, two per run, three per watch and 60-second cooldown remain binding. |
| Same question/output appears each cycle | Deduplicate by pane/run/event; report materially changed questions or new runs. |
| Connection disappears | Suspend inputs; one notice, at most three bounded read-only reconnect checks; reconcile fresh state and do not replay input. |
| User stop/cancel or explicit duration expires | End this watch, discard pending actions, preserve agents; report last observation. |
| Connection, authorization or verified execution capability blocks the watch | Retain unresolved blocked task with reason, last observation and resumable ledger; no completion or background claim. |
| All current runs complete but new session starts later | Keep discovery active for the user-requested lifetime unless user requested early stop. |
| Ongoing watch reaches 30 minutes with host execution still available | Continue observing; no invented deadline or completion. |
| Unchanged cycles reach five minutes | Stay quiet by default; no routine heartbeat. |
| User asks for a 10-minute watch or a specific stop condition | Honor that bound instead of the ongoing default. |
| Resume after a blocked interval | Reconcile fresh identities, preserve deduplication and recovery budgets, never replay queued input. |
| No host delegation or continuous execution route | Explain limitation and offer actual snapshot/continuation; no invented tools, daemon or unattended promise. |

Automated evidence: `test_snapshot.py` covers discovery, linked-pane deduplication, failed inventories, disappeared/restarted panes, untrusted target rows and an isolated real tmux inventory. `test_validate.py` protects mandatory safety/discovery contract anchors. Full live ChatGPT/agent interaction remains a release smoke check and must be reported separately.
