---
name: research
description: Perform research for the vault owner and file unreviewed findings in vault/06 AI Workspace/Research with sources preserved. Use when asked to research a topic for the knowledge vault.
---

# Research

**Purpose:** research that lands inside the trust boundary, not in trusted
knowledge.

**Required context first:** `.claude/rules/ai-workspace.md`; search the vault
for what is already known about the topic (avoid re-researching settled
questions — check Decisions too).

## Workflow

1. Check existing vault material; state what is already established.
2. Research (web/tools as available). Keep source URLs, titles, dates.
3. Write findings to `vault/06 AI Workspace/Research/<Descriptive Title>.md`
   with `status: pending-review`, structured as:
   - **Question** · **Sourced findings** (each with its source) ·
   - **Synthesis** · **Inference/opinion** (clearly separated) ·
   - **Sources** list · **Suggested destination** if promoted.
4. Link the related project/area; note it under the project README's Open
   Questions or Key Notes **only if explicitly asked**.

## Contract

- Level: UPDATE, confined to `06 AI Workspace/`. No writes to trusted folders.
- Prohibited: presenting inference as sourced fact; dropping source URLs;
  promoting findings yourself.

## Output

Summary of findings + the file path created + what needs the owner's review.
