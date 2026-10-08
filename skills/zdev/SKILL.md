---
name: zdev
description: "Route Takazudo development requests through Chat planning (zdev1) and a separately opened ChatGPT Work session (zdev2). Use for zdev, rough development requests, planning, prototyping, continuing this workflow, or connected-computer status and observation."
---

# zdev

Read [the workflow contract](references/workflow-contract.md).

- `zstatus` or a one-shot terminal-work inventory uses [zstatus](../zstatus/SKILL.md). `zwatch` or ongoing observation of Codex/Claude Code uses [zwatch](../zwatch/SKILL.md). These routes use the selected connected computer through host-supported delegation; they do not start planning or implementation.
- A rough request, question about a proposed change, plan, prototype, or explicit issue sweep starts `zdev1` in the current Chat session.
- An explicit `zdev2` or Work implementation request uses `zdev2` in a Work session. In ordinary Chat, prepare its prompt and artifacts and tell the user to open Work.
- “Chain to zdev2” means finalize the handoff: a copyable prompt plus available artifacts. Do not claim to switch this chat to Work or silently create another session.
- Default handoff: the user keeps this Chat in a ChatGPT Project and opens a new Work chat in that same Project. Name the source chat and artifact explicitly. ZIP upload is the fallback.
- Oversized work follows the routing table in the contract: artifacts → resource-only zdev2; no artifacts → direct Codex.
- Forward `-pr`/`--prototype`, `-is`/`--issuesweep`/`--issue-sweep`, and `-isask`/`--issue-sweep-ask` to zdev1. Forward `-m`/`--merge` to zdev2 only when the user actually supplied merge authorization. Do not invent flags.
- Old names such as z-dev, z-first-dev, z-work-dev, z-plan, z-proto, and z-gh are migration aliases in prose only. Map them to zdev, zdev1, zdev2, zplan, zproto, and zgh. “First dev” now means planning and handoff, without mandatory seed implementation.
- There is no zdev3 or local-finalization skill. Codex continuation is an ordinary self-contained prompt. Plugin maintenance belongs in https://github.com/Takazudo/chatgpt-zdev, not a z-skill skill.
