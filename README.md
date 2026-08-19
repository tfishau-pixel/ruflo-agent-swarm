# ruflo-agent-swarm

Ruflo v3 scaffold for Claude Code — configures the `claude-flow` MCP server
for swarm/agent coordination, memory, and hooks. No application source yet.

## What's here

- `.mcp.json` — declares the `claude-flow` MCP server (`ruflo` CLI)
- `CLAUDE.md` — project instructions and Ruflo/Claude Code configuration
- `.claude/` — Claude Code settings, hooks, and local config
- `.claude-flow/` — Ruflo runtime state and policy
- `.swarm/`, `.agents/` — Ruflo swarm/agent runtime data and skills

## Setup

```bash
claude mcp add claude-flow -- npx -y ruflo@latest mcp start
npx ruflo@latest doctor --fix
```

See `CLAUDE.md` for the full agent/swarm workflow and CLI reference.
