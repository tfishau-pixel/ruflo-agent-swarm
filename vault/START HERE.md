# Start Here

How this vault works, in five minutes. The design goal: you rarely think
about the vault itself — capture naturally, work normally, retrieve reliably.

## The one habit that matters

**Capture everything into `00 Inbox/` (or today's daily note) without
classifying it.** Organisation happens later — ask Claude to `/process-inbox`.
Capture must always be easier than organisation.

## Where things live

| Question | Answer |
|---|---|
| "Where do I put this?" | `00 Inbox/` — always a safe answer |
| "What's the state of project X?" | `01 Projects/X/README.md` — the single source of truth |
| "Ongoing responsibilities?" | `02 Areas/` (created only when real content needs them) |
| "Things I've learned and trust" | `03 Knowledge/` |
| "Original sources, references" | `04 Resources/` — never overwritten by summaries |
| "What did the AI produce that I haven't checked?" | `06 AI Workspace/` — the trust boundary |
| "Finished projects" | `99 Archive/` — moved, never deleted |

## Working with Claude

Claude reads `vault/CLAUDE.md` automatically and retrieves minimal context
(search → narrow → read), never the whole vault. Useful workflows (skills):

- `/process-inbox` — triage captured material
- `/project-brief` — build working context for a project
- `/project-update` — update a project README after real work
- `/vault-search` — answer a question from the vault, read-only, with provenance
- `/research` — research lands in `06 AI Workspace/Research` until you review it
- `/daily-review` · `/weekly-review` — extract durable value, surface stalls
- `/capture-decision` — record what was decided and why
- `/process-apple-note` — integrate one imported Apple Note
- `/vault-maintenance` — report-only health audit
- `/archive-project` — conservative project conclusion

Claude never deletes, bulk-renames, or restructures without explicit approval.
Unreviewed AI conclusions stay in `06 AI Workspace/` until you promote them.

## Decisions

Significant decisions get a note from `07 Templates/Decision.md` (what +
why + options rejected), linked from the project README. This stops future
sessions — yours or the AI's — from reopening settled questions.

## Obsidian settings to verify once (UI)

Minimal config is pre-seeded in `.obsidian/`, but confirm in the UI:

1. **Settings → Files & links**: "Default location for new attachments" =
   `08 Attachments`; "Automatically update internal links" = on.
2. **Settings → Core plugins**: enable **Daily notes**, **Templates**,
   **Backlinks**, **Page preview**, **File recovery**, **Bases**.
3. **Daily notes**: folder `05 Daily`, template `07 Templates/Daily Note`.
4. **Templates**: folder `07 Templates`.
5. **File recovery**: snapshot interval 5 min, history length ≥ 30 days.

No community plugins are required. Add one only when a real friction demands
it.

## Backup and recovery (important)

**Sync is not backup.** Sync propagates deletions and mistakes; backup lets
you go back in time. This vault uses layers:

1. **Git (already in place)** — the vault lives in this repository. Commit
   and push regularly (ask Claude to commit vault changes with a clear
   message). Pushing to GitHub = versioned, off-device backup. `.gitignore`
   excludes volatile workspace state but versions your notes and settings.
2. **Obsidian File Recovery (core plugin)** — local snapshots; recovers a
   single note after a bad edit even between commits.
3. **Device backup** — keep your machine's own backup (Time Machine or
   equivalent) covering the vault folder.
4. *(Optional)* **Obsidian Sync or iCloud** for multi-device access — that is
   sync/convenience, not backup; layers 1–3 remain the safety net.

**To recover:** single note → File Recovery snapshots; anything bigger →
`git log -- "vault/<path>"` and `git checkout <commit> -- "vault/<path>"`,
or ask Claude to restore a file from git history.

## What was deliberately left out (add only when justified)

Community plugins · MOCs · elaborate dashboards · tag taxonomy · hooks ·
MCP integrations · semantic search · automation. Each waits for a
demonstrated need — see the complexity budget in [[CLAUDE|vault/CLAUDE.md]].
