---
name: zdev1
description: "Plan in ordinary Chat and finish with issues, a continuation prompt, and available artifact ZIP. Use zdev1 for rough requests, -pr/--prototype UI polish, -is/--issuesweep/--issue-sweep backlog sweeps, or -isask interviews of postponed issues."
---

# zdev1

Read [the workflow contract](../zdev/references/workflow-contract.md) and [handoff rules and prompts](references/handoff.md). Use `zplan`, `zproto`, and `zgh` as needed.

## Modes

A. **Rough request → plan:** inspect the repository and relevant sibling chats, clarify the intended result, and use zplan to create an implementation-ready plan. For an existing repository, create or update a GitHub spec issue; reuse an adequate existing issue instead of duplicating it.

B. **Prototype → plan:** `-pr` / `--prototype` explicitly requests the zproto feedback loop in this Chat. Complete the loop and preserve accepted decisions before finalizing issues. Combining it with a sweep prototypes only the selected UI topics.

C. **Issue sweep:** `-is`, `--issuesweep`, or `--issue-sweep` selects a bulk sweep; `-isask` or `--issue-sweep-ask` selects the interview variant and takes precedence if both are supplied. Read [the full sweep procedure](references/issue-sweep.md). Never infer a sweep merely from a large backlog. Natural-language explicit sweep requests are equivalent.

## Finish every planned handoff

1. Check the plan against the original request, accepted feedback, actual repository, and issue bodies. Review dependencies, risks, and verification. Fix omissions before handing off.
2. Assess whether a single Work implementation session is appropriate. Record the reasons, using the workflow contract's routing table. A super-epic is conservatively oversized; there is no invented numerical Work capacity limit.
3. For an existing repository, finish and read back its spec issue or epic/sub-issue hierarchy. If GitHub writing is unavailable, deliver complete issue drafts and label publication blocked; never invent issue URLs.
4. Write the complete Accepted implementation brief in readable Chat/issue text, including accepted prototype behavior and feedback. Package generated prototypes or other implementer-needed files as one complete ZIP; a manifest is optional and the ZIP supplements the readable specification. If there are no file artifacts beyond the durable issue spec, say `Artifacts: none required`; do not manufacture a ZIP just to route through Work.
5. End with the destination and reason, actual issue links, a **complete copyable continuation prompt in a fenced text code block**, and a download link to the ZIP when present. The prompt names the exact sibling Chat in this Project, accepted artifact/version/entry paths, repository, issues, base branch, execution mode, verification, and authorized actions. If the host cannot expose the source chat identifier, provide its visible title and task description without inventing a URL.
6. Default instructions tell the user to open a new Work chat in this same Project and paste the prompt. If the source Chat is not in a Project yet, tell the user to move it into one and open Work there. The receiver reads the sibling Chat and issue and implements from sufficient accepted context. ZIP upload is only a fallback for indispensable missing inputs, not the default prerequisite. For direct Codex routing, provide a GitHub-complete prompt instead, since Codex must not depend on Chat project history.

No automatic Work launch, no product implementation as a condition of finishing zdev1, and no inherited big-plan auto-implementation/merge chain. A prototype acceptance or sweep interview still needs the user's actual answer; routine planning decisions do not create extra approval gates. Explicit user instructions override workflow defaults.
