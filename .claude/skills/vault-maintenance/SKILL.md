---
name: vault-maintenance
description: Report-only vault health audit — broken links, duplicates, stale projects, inconsistent properties, orphaned material, AI review backlog. Use when asked to check vault health or run maintenance.
---

# Vault Maintenance

**Purpose:** surface decay before it compounds. **Default is report-only** —
no file is modified unless the owner explicitly authorises specific fixes.

For a large vault, delegate the sweep to the `vault-auditor` subagent and
synthesise its findings.

## Audit checklist

- Broken `[[wiki links]]` (target file missing)
- Duplicate / near-duplicate notes (similar titles or content)
- `00 Inbox/` items older than ~2 weeks
- Stale projects: `status: active` but long-untouched, or README
  contradicting other notes
- Property drift: synonyms or values outside the canonical schema in
  `vault/CLAUDE.md`
- Orphaned useful notes (no links in or out) worth connecting
- Dead external references in `04 Resources/`
- Oversized notes that would genuinely benefit from splitting
- `06 AI Workspace/` backlog, especially `Pending Review/`

## Contract

- Level: READ. Bulk modification is DESTRUCTIVE and requires explicit,
  itemised approval. After approval, fix in small reviewable batches.

## Output

Grouped report: issue → affected paths → recommended fix → risk level.
Lead with the few items that matter most; do not pad the report.
