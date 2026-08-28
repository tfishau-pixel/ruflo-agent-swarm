---
name: project-update
description: Update a vault project's README (status, next actions, decisions, open questions) after meaningful work. Use when asked to update project state or after completing work on a vault project.
---

# Project Update

**Purpose:** keep each project README a trustworthy current-state document.

**Required context first:** the project's `README.md` in `vault/01 Projects/`,
plus `.claude/rules/projects.md`. Read notes changed by the recent work if
needed to state the new status accurately.

## Workflow

1. Re-read the README's Status, Next Actions, Decisions, Open Questions.
2. Determine what actually changed: state, completed/new actions, decisions
   made, questions opened or resolved, new key notes worth linking.
3. Edit only the affected sections. Status stays a few sentences of *current*
   state — move superseded detail to History only if it is a real milestone.
4. Record significant decisions via a Decision note (`/capture-decision`);
   small ones inline under Decisions.

## Contract

- Level: UPDATE — authorised for the named project's README only.
- Prohibited: rewriting unrelated sections, touching other projects,
  changing status to done/archived without instruction, turning the README
  into a log.
- Conflict between README and other notes → surface it, don't pick silently.

## Output

Show the sections changed (before → after in brief) and anything flagged.
