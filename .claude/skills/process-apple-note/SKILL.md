---
name: process-apple-note
description: Integrate one imported Apple Note into the vault per the migration policy — preserve content and dates, clean formatting noise, link, detect duplicates. Use when asked to process/migrate an Apple Note.
---

# Process Apple Note

**Purpose:** incremental, loss-free migration of Apple Notes — one note at a
time, never a big-bang reorganisation.

## Workflow (one note)

1. Preserve the original content verbatim; keep meaningful created/modified
   dates (as `created:` property or noted in the text).
2. Clean only obvious formatting noise (import artifacts, broken characters);
   never rewrite the owner's words.
3. Give it a descriptive title if the original is unusable.
4. Search the vault for related notes, the owning project/area, and probable
   duplicates.
5. Place it: project folder / `03 Knowledge/` / `04 Resources/` /
   `00 Inbox/` if genuinely unclassifiable. Link what is obviously related.
6. Extract reusable knowledge into an existing knowledge note only when
   clearly useful — and keep the original intact regardless.
7. Duplicates: link the candidates and flag; do not merge or delete.

## Contract

- Level: ORGANISE. The original is preserved until the owner approves
  deletion — always.
- Prohibited: manufacturing metadata to look organised; guessing at ambiguous
  meaning (flag instead); batch-processing many notes without being asked.

## Output

Where the note went, what was cleaned, links added, duplicates/ambiguities
flagged for the owner.
