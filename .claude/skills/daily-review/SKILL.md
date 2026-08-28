---
name: daily-review
description: Extract durable value from a vault daily note — project updates, actions, decisions, knowledge, links. Use when asked to review a daily note or promote today's/a date's captures.
---

# Daily Review

**Purpose:** the system, not the owner, does the reorganising. Daily notes
are capture surfaces; this skill harvests them.

**Required context first:** the daily note in `vault/05 Daily/` (default:
most recent), plus the READMEs of any projects it mentions.

## Workflow

1. Read the daily note. Identify: project state changes · actionable items ·
   decisions · durable knowledge · unresolved questions · useful links.
2. Promote only genuinely valuable items:
   - project changes/actions → that project README (UPDATE level)
   - significant decisions → `/capture-decision`
   - durable knowledge → existing knowledge note, or propose a new one
3. Add `[[links]]` in the daily note to where things were promoted.
4. Leave the daily note's original text intact — it is the record of the day.

## Contract

- Level: ORGANISE + targeted UPDATE of mentioned project READMEs.
- Prohibited: rewriting the daily note, promoting trivia, creating notes for
  passing thoughts, treating an empty section as a problem.
- Ambiguous item (is this a decision? whose action?) → flag, don't guess.

## Output

What was promoted where; what was flagged; what was deliberately left alone.
