# Vault Instructions (Obsidian Knowledge System)

This folder is the owner's Obsidian vault: their external memory, project
system, decision history, and archive. Plain local Markdown is the permanent
source of truth. Everything else (Bases, plugins, skills, this file) is an
enhancement.

Optimise for: Capture → Retrieval → Context → Understanding → Action → Preservation.
Reduce the owner's cognitive load. Never add structure for its own sake.

## Map

| Folder | Purpose |
|---|---|
| `00 Inbox/` | Frictionless capture; unclassified material awaiting processing |
| `01 Projects/` | Active projects; each has a `README.md` = authoritative current state |
| `02 Areas/` | Ongoing responsibilities with no end date |
| `03 Knowledge/` | Reusable long-term knowledge (accepted, trusted) |
| `04 Resources/` | Source material and references; provenance preserved |
| `05 Daily/` | Daily notes; rapid capture surface |
| `06 AI Workspace/` | **Trust boundary** — unreviewed AI output lives here until promoted |
| `07 Templates/` | Note templates |
| `08 Attachments/` | Non-Markdown files |
| `99 Archive/` | Concluded projects and inactive material (moved, never deleted) |

Do not create new top-level folders without explicit approval.

## Progressive context

Never treat the whole vault as context. Retrieve the minimum sufficient
context: this file → HOME or the relevant project README → linked notes →
source material. **Search first (Grep/Glob titles and content), then narrow,
then read, then reason.** Do not bulk-read folders because they exist.

## Before substantial work

1. Determine which project, area, or topic is involved.
2. Locate its README, MOC, or index.
3. Search for relevant existing material (titles, aliases, content).
4. Read only the context required; follow meaningful links when necessary.
5. Prefer existing sources of truth over creating parallel ones.
6. Read the matching rule file in `../.claude/rules/` (see Rules below).

## While working

- Preserve source material and the owner's original words where wording matters.
- Prefer reversible changes; never silently delete useful information.
- Never silently convert uncertainty into fact; surface conflicts rather than
  silently choosing one version.
- Distinguish user statements, source material, AI synthesis, and AI inference.
- Do not duplicate information; link to the single source of truth instead.
- Use standard Markdown and `[[wiki links]]` for meaningful relationships.
- Keep filenames descriptive and human-readable.
- Never expose secrets, credentials, or API keys.
- No large-scale restructuring unless explicitly requested.

## After substantial work

If the work produced a decision, changed project state, a next action, durable
knowledge, an unresolved question, or a useful relationship — update the
appropriate source of truth (usually the project README). Do not create
administrative noise merely because work occurred.

## Single source of truth

- Project status → that project's `README.md` (only there)
- Permanent source material → `04 Resources/`
- Accepted reusable knowledge → `03 Knowledge/`
- Unreviewed AI material → `06 AI Workspace/`
- Significant decisions → a Decision note linked from the project README

## Read/write contract

Every task falls into one level; when uncertain, choose the less destructive:

- **READ** — search and inspect; no modifications.
- **ORGANISE** — low-risk structural work (linking, formatting) preserving meaning.
- **UPDATE** — update known sources of truth when specifically authorised.
- **DESTRUCTIVE** — deletion, bulk rename, major restructuring, loss of
  history. Requires explicit approval. Prefer archive over overwrite,
  move over delete, report over bulk-fix.

## Provenance

Every important claim should be traceable to one of:

- **user** — the owner directly wrote, observed, or stated it
- **source** — from identifiable external material (keep title/URL/date)
- **ai-synthesis** — AI restructuring/summarising existing evidence
- **ai-inference** — AI conclusion beyond stated evidence
- **unknown** — not established

New AI conclusions go to `06 AI Workspace/` until reviewed. A summary is a
layer on top of a source, never a replacement for it. Do not let repeated
summaries turn inference into apparent fact.

## Properties (canonical schema)

Use properties only when they aid retrieval. Reuse these names exactly; do
not invent synonyms (no `projects`, `related-project`, etc.):

- `type:` project | area | knowledge | source | decision | daily | moc
- `status:` active | waiting | done | archived (projects); pending-review (AI notes)
- `project:` link to the owning project README
- `area:` link to the owning area
- `source:` origin of the information (URL, book, person, "user", "ai-synthesis")
- `created:` YYYY-MM-DD

Most notes need no properties at all.

## Safety — never automatically

Delete substantial user-authored content · overwrite sources with summaries ·
mass-rename · restructure the vault · expose or commit secrets · install
automation · change external services.

## Rules, skills, agents

Path-scoped rules live in `../.claude/rules/` — read the relevant one before
working in its folder: `projects.md` (01 Projects), `knowledge.md`
(03 Knowledge), `sources.md` (04 Resources), `ai-workspace.md`
(06 AI Workspace), `archive.md` (99 Archive).

Vault workflows are skills in `../.claude/skills/` (process-inbox,
project-update, project-brief, vault-search, research, process-apple-note,
daily-review, capture-decision, vault-maintenance, archive-project,
weekly-review). Use `research-librarian` and `vault-auditor` subagents for
broad multi-file reading so this conversation stays uncluttered.
