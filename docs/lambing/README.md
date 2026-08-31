# Lambing Resource Set — Valais Blacknose, NZ Edition

Two complementary resources for a first lambing season with three pregnant Valais Blacknose ewes, designed as one system: same section order, urgency language (GREEN observe / AMBER monitor–prepare / RED ring the vet), terminology and diagrams across every format.

## Files

| File | What it is | How to use it |
|---|---|---|
| `handbook.md` | **First Lambing Season** — source Markdown | Read/edit; canonical content |
| `handbook.html` | Designed handbook (A4 print layout, screen-readable) | Open in a browser; print to PDF |
| `emergency-guide.md` | **Lambing Emergency Guide** — source Markdown | Read/edit; canonical content |
| `emergency-guide.html` | **Interactive emergency guide** — mobile-first, fully offline | **Save to your phone before lambing** (Files app → open in Safari, or AirDrop). Symptom menu, one problem per card, offline search, persistent CALL VET + SYMPTOMS buttons, editable contacts and ewe records (stored on-device only), dark mode for night checks |
| `cheatsheet.html` | One-page emergency field card | Print + laminate; lives with the lambing kit |
| `far-from-help.md` / `far-from-help.html` | **Far From Help** — trained-hands procedures for a property ~1.5 h from veterinary help (assisted delivery/malpresentation correction, stomach-tubing, IP glucose injection, bearing replacement), with sourced step-by-steps, stop conditions, extended kit, and the load-and-drive Plan B | Read before lambing; print + laminate §§2–4; also compact in the emergency guide (card 15) |
| `pdf/far-from-help-A4.pdf` | The supplement, printable | Print; laminate the procedure pages |
| `pdf/first-lambing-season-handbook-A4.pdf` | Printable handbook | Print at A4 |
| `pdf/first-lambing-season-handbook-mobile.pdf` | Narrow-page handbook | Comfortable phone/tablet reading |
| `pdf/lambing-emergency-cheatsheet-A4.pdf` | The field card, single page | Print, laminate |

## Before lambing — the 15-minute setup

1. Open `emergency-guide.html` on your phone, tap **CALL VET**, and enter your vet's numbers (the button then dials directly). Add each ewe's scan results to the record cards.
2. Print and laminate the cheat sheet; put it in the lambing kit bin.
3. Fill in the emergency contacts page of a printed handbook and leave it in the shed.
4. Ask your vet clinic: after-hours number, expected travel time, and whether they run pre-lambing training (get shown stomach-tubing there).

## Regenerating the PDFs

Any Chromium/Chrome build:

```sh
chromium --headless=new --no-sandbox --print-to-pdf=pdf/first-lambing-season-handbook-A4.pdf --no-pdf-header-footer handbook.html
chromium --headless=new --no-sandbox --print-to-pdf=pdf/lambing-emergency-cheatsheet-A4.pdf --no-pdf-header-footer cheatsheet.html
# mobile variant: swap the two "@variant-" CSS markers in handbook.html
sed -e 's|size:A4; /\* @variant-page \*/|size:120mm 212mm;|' -e 's|--base:10.5pt; /\* @variant-base \*/|--base:11pt;|' handbook.html > /tmp/handbook-mobile.html
chromium --headless=new --no-sandbox --print-to-pdf=pdf/first-lambing-season-handbook-mobile.pdf --no-pdf-header-footer /tmp/handbook-mobile.html
```

## Scope and evidence

Recognition and safe first aid for beginners; early veterinary contact over DIY heroics, throughout. Clinical thresholds (stage timings, the 30-minute rule, colostrum 50 ml/kg by 2–6 h / ~200 ml/kg per 24 h, hypothermia bands and the 5-hour glucose-before-warming rule, retained placenta at 12–18 h) are sourced in the handbook's bibliography (Beef + Lamb NZ, NZ vet clinics, NADIS, AHDB, FAS Scotland/SRUC, Merck/MSD Veterinary Manual). Valais Blacknose lambing claims are labelled breeder-reported where no veterinary evidence exists. Illustrations are original labelled schematics; links to clinical photo references are included where real photographs matter (prolapses). Compiled August 2026. Not a substitute for veterinary care.
