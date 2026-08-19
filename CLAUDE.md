# Ruflo — Claude Code Configuration

## Project State

This repo is a `ruflo init` scaffold — config, hooks, memory, no application
source. There is no `package.json` and no `src/`, so there is nothing to build,
test, or lint today. Once real code lands: run its tests after changes and
verify the build before committing, and replace this section with the actual
commands.

## Setup

```bash
claude mcp add claude-flow -- npx -y ruflo@latest mcp start
npx ruflo@latest doctor --fix
```

**The package is `ruflo`; `claude-flow` is only the MCP server name.** Commands
written as `npx @claude-flow/cli@latest ...` install a different package — see
`.mcp.json`, which is the source of truth for how the server actually starts
(`autoStart` is `false`, so it starts on demand).

> The background `daemon` is optional and **burns tokens continuously** — it runs
> interval workers that each spawn a headless `claude` session. Start it only if
> you want those sweeps: `npx ruflo@latest daemon start` (self-stops after 12h;
> `--ttl 0` disables that, `daemon status --all` audits running daemons).

## Rules

- ALWAYS read a file before editing it.
- NEVER commit secrets, credentials, or `.env` files.
- Keep working files out of the repo root — use `/src`, `/tests`, `/docs`,
  `/config`, `/scripts`.
- **NEVER add a `Co-Authored-By` trailer to user commits** unless this project's
  `.claude/settings.json` sets `attribution.commit` (#2078). The Bash tool
  suggests one in its default commit template — ignore it. `Co-Authored-By` is
  semantic authorship attribution under git/GitHub convention; the tool is the
  facilitator, not a co-author.

## Concurrency and authority

- **Never allow two writers in one worktree.** Give each writing agent an
  isolated worktree and explicit file ownership.
- Read-only research agents may run concurrently and report to the owner.
- Only the integration owner edits shared manifests and lockfiles, or reconciles
  overlapping changes.
- A child agent may drop capabilities but cannot add tools, network, secrets,
  spend, concurrency, or delegation depth.
- A lease or claim coordinates ownership; it does not authorize a side effect.
- Bind tests, benchmarks, and release evidence to an exact commit.

## Agent comms

Named agents coordinate via `SendMessage`, not polling. Spawn the whole team in
one message, each knowing who to message next:

```javascript
Agent({ prompt: "Research the codebase. SendMessage findings to 'architect'.",
  subagent_type: "researcher", name: "researcher", run_in_background: true })
Agent({ prompt: "Wait for 'researcher'. Design the solution. SendMessage to 'coder'.",
  subagent_type: "system-architect", name: "architect", run_in_background: true })
Agent({ prompt: "Wait for 'architect'. Implement it. SendMessage to 'tester'.",
  subagent_type: "coder", name: "coder", run_in_background: true })

SendMessage({ to: "researcher", summary: "Start", message: "[task context]" })
```

- ALWAYS `name:` an agent — that is what makes it addressable.
- ALWAYS say who to message and what to send, in the prompt.
- Don't poll; agents message back or complete on their own.

**When to swarm** — yes: 3+ files, new features, cross-module refactors, API
changes, security, performance. No: single-file edits, 1–2 line fixes, docs,
config, questions.

## Ruflo tools

Discover with `ToolSearch("keyword")`; the registry is authoritative over any
list written here.

| Category | Key tools |
|---|---|
| Memory | `memory_store`, `memory_search`, `memory_search_unified` |
| Swarm | `swarm_init`, `swarm_status`, `swarm_health` |
| Agents | `agent_spawn`, `agent_list`, `agent_status` |
| Hooks | `hooks_route`, `hooks_post-task` |
| Security | `aidefence_scan`, `aidefence_is_safe`, `aidefence_has_pii` |

```bash
npx ruflo@latest memory search --query "[keywords]" --namespace patterns
npx ruflo@latest memory store --namespace patterns --key "[name]" --value "[what worked]"
npx ruflo@latest hooks route --task "[description]"
npx ruflo@latest doctor --fix
```

Agent tool executes (files, code, git); MCP tools coordinate (swarm, memory,
hooks); the CLI is the same surface via Bash.
