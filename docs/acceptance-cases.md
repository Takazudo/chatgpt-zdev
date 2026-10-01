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
| Bounded work with accepted prototype | Same-Project zdev2 implementation; verify artifact first | handoff |
| Work cannot read a required Project artifact | Ask for exact ZIP; no invented source or dependent implementation | handoff, zdev2 |
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

## Validation boundary

The validator checks manifests, skill inventory/frontmatter, local reference links, required contract anchors, text completeness, and package hygiene. Packaging checks ZIP integrity and byte-for-byte payload equivalence. These checks cannot prove a model will follow the instructions, a Work chat can retrieve a specific Project artifact, or the installed account plugin has refreshed. Those require host execution and read-back.
