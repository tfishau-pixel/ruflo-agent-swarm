---
name: vault-search
description: Answer a question from the vault's own contents, read-only, separating found facts from synthesis, inference, and gaps. Use for "what do I know about / did I decide / have I tried" questions.
---

# Vault Search

**Purpose:** vault-grounded answers with honest epistemic labelling.

## Workflow

1. Search titles, then content (Grep/Glob across `vault/`), for the question's
   terms and obvious synonyms.
2. Read the strongest hits; follow meaningful links one hop where needed.
3. Treat `06 AI Workspace/` content as unreviewed — usable only when labelled
   as such. Treat `04 Resources/` as evidence with provenance.

## Contract

- Level: READ. Default mode is strictly read-only — no writes, moves, or
  "quick fixes" while answering.

## Output — always four labelled parts

1. **Found** — information explicitly present, with the path/link to each
   supporting note (strongest first).
2. **Synthesis** — reasonable combination of found material.
3. **Inference** — conclusions going beyond the notes, clearly flagged.
4. **Missing** — what the vault does not contain that the question needs.

Never let synthesis or inference read as if it were found material.
