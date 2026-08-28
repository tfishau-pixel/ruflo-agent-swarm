---
name: archive-project
description: Conservatively conclude a vault project — preserve outcome, decisions, and reusable knowledge, then move (never delete) to 99 Archive. Use when the owner says a project is finished or should be archived.
---

# Archive Project

**Purpose:** conclude without losing anything future-you will want.

**Precondition:** the owner explicitly asked to archive this project.

## Workflow

1. Read the project README and skim its supporting notes.
2. Before moving anything:
   - Update README: final **Outcome** achieved, `status: archived`, closing
     Status summary.
   - Ensure significant decisions are recorded (Decision notes or README).
   - Promote reusable knowledge to `03 Knowledge/` (via review in
     `06 AI Workspace/` if it involves new AI conclusions).
   - Remaining Next Actions: mark resolved, moved (say where), or explicitly
     "dropped — owner confirmed".
3. Move the whole project folder to `vault/99 Archive/<Project Name>/`.
4. Fix links that the move broke; leave a `[[99 Archive/<Name>/README]]`
   pointer anywhere the project is still referenced prominently.

## Contract

- Level: UPDATE + the approved move. Nothing is deleted — ever.
- Prohibited: archiving on inference ("seems done"), pruning notes during
  the move, editing archived content afterwards.
- Unresolved actions the owner hasn't ruled on → stop and ask before moving.

## Output

Confirmation of the move, knowledge/decisions preserved, links fixed,
anything the owner still needs to rule on.
