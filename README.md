# zudo-dev-flow

A personal ChatGPT plugin for planning in Chat, implementing bounded work in a new Work chat, and handing oversized or unfinished work to Codex cloud or local.

## Start here

```text
Use zdev1 for <repository URL>. I want <rough outcome>.
Use zdev1 -pr for <repository URL>. Let's prototype and polish <UI>.
Use zdev1 -is for <repository URL>.
Use zdev1 -isask for <repository URL>.
```

`zdev1` finishes with durable GitHub issues, a copyable continuation prompt, and an artifact ZIP when there are generated files the implementer needs. There is no mandatory production-code “first dev” stage.

Keep the planning Chat in a ChatGPT Project. Open a **new Work chat in the same Project** and paste the generated prompt. It explicitly names the source Chat and artifacts. Work checks it can actually read the files; if it cannot, download the ZIP from the planning Chat and attach it in Work. A source-session `/mnt/data` path is not a transferable file.

[OpenAI's Projects documentation](https://learn.chatgpt.com/docs/projects) describes shared project context and Chat/Work chats in one Project. It does not establish guaranteed access to every prior generated attachment; the receiver check is part of this workflow.

| Planned work | Generated inputs to transfer | Next step |
|---|---|---|
| Bounded | Either | `zdev2`: implement, verify, open PR |
| Oversized | Yes | `zdev2` resource-only: bake files on a draft base PR, then Codex |
| Oversized | No | Skip Work and give Codex the issue hierarchy |

Super-epics are conservatively oversized. This is a workflow judgment, not a documented Work product limit. Resources already durably baked can be passed directly to Codex.

## Skills

| Skill | Purpose |
|---|---|
| `zdev` | Route the request |
| `zdev1` | Chat planning, prototyping, issue sweep, final handoff |
| `zdev2` | Work implementation or resource-only persistence |
| `zplan` | Repository-grounded plans and issue decomposition |
| `zproto` | Prototype feedback loop until explicit acceptance |
| `zgh` | GitHub operations and evidence |

There is no `zdev3`, `z-local`, or `z-skill`. Maintain this plugin in this repository. The package identity remains `z-dev-flow` and display name is **zudo-dev-flow**; skill names have no hyphens.

## Flags

- `zdev1 -pr` / `--prototype`: prototype and polish in Chat before final planning.
- `zdev1 -is` / `--issuesweep` / `--issue-sweep`: bulk issue sweep with one triage checkpoint.
- `zdev1 -isask` / `--issue-sweep-ask`: revisit postponed issues with an interview; wins over `-is`.
- Sweep helpers: `-f` / `--filter`, `-ex` / `--exclude`, `-re` / `--refresh-epic`. Include labels use AND; exclusions use ANY.
- `zdev2 -m` / `--merge`: merge only when full implementation, acceptance, review, required approvals, and current-head checks are complete. Resource-only PRs remain draft and unmerged.
- No `zdev2 -a` is needed. Routine implementation proceeds without repeated questions. `-a` never grants merge permission.

Sweeps preserve epic/sub-issue decomposition, super-epics for multiple independent epics, dependency markers and ordering, postponed-work dashboards, and seed closure **after verified replacement**, clearly marked superseded. Planning never silently launches implementation.

Work finishes with a PR. If anything remains, including a merge that was not authorized, it also gives a copyable Codex prompt containing the PR URL and exact outstanding work. Fully merged and verified work needs no invented follow-up stage.

## Build and check

Python 3.9+ standard library only:

```sh
python3 scripts/validate.py
python3 -m unittest discover -s scripts -p 'test_*.py'
python3 scripts/package.py --output /absolute/output/directory/zudo-dev-flow-0.3.1.zip
```

The ZIP contains one `z-dev-flow/` directory with the skills, manifests, assets, and linked documentation. Repository scripts, tests, and caches are excluded. Generated archives remain local and ignored; Git LFS is never used.

See [behavior acceptance cases](docs/acceptance-cases.md), [source provenance](docs/provenance.md), and [release/migration notes](docs/releasing.md). Static validation checks packaging and contract consistency; an actual Chat/Work run is still needed to validate host behavior.
