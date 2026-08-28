---
description: Project management rules for the Obsidian vault
paths:
  - "vault/01 Projects/**"
---

# Rules — vault/01 Projects/

- Each project's `README.md` is the **single source of truth** for its
  status, next actions, and open questions. Update it there and nowhere else;
  other notes link to it, never mirror it.
- Keep the README answering: *"If I returned in six months, what would I need
  to resume quickly?"* It is a current-state document, not a chronological log.
- After meaningful work on a project, update Status / Next Actions / Decisions /
  Open Questions if they changed. Do not append noise when nothing changed.
- New projects: create `01 Projects/<Name>/README.md` from
  `vault/07 Templates/Project README.md`; supporting notes live beside it.
- Significant decisions get a Decision note (template in `07 Templates/`)
  linked from the README; small decisions may be recorded inline in the README.
- Never mark a project done or archive it on your own initiative — propose it.
- Conflicting status information anywhere in the vault: surface the conflict;
  do not silently pick a version.
