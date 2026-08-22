---
name: capture-decision
description: Record an important decision and its reasoning in the vault's correct source of truth so it is never re-litigated. Use when the owner makes or reports a significant decision.
---

# Capture Decision

**Purpose:** preserve *what was decided and why* so future sessions (human or
AI) do not reopen resolved questions.

## Workflow

1. Establish from the conversation/notes: the decision, context, options
   considered (including rejected ones), reasoning, consequences, follow-ups.
   Missing pieces → ask or mark "not recorded", never invent reasoning.
2. Significance test: does it constrain future work or would re-deciding be
   costly? If yes → create a Decision note from
   `vault/07 Templates/Decision.md`, filed in the owning project's folder
   (or `03 Knowledge/` for project-independent decisions).
   If minor → a dated line under the project README's Decisions section.
3. Link both ways: README ↔ Decision note; link affected notes.
4. Set `project:` and `created:` properties.

## Contract

- Level: UPDATE (Decision note + the owning README's Decisions section only).
- Prohibited: recording the owner's tentative musings as decisions —
  when unsure whether it was actually decided, ask.

## Output

Path of the record created and the links added.
