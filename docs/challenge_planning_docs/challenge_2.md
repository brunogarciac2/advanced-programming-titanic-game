## Overview

Challenge 2 (“Echoes of Deck C”) now uses **seven echoes (A–G)**, combines data validation with sequencing, and ends with a 4‑letter code derived from a survival-by-birth-year chart.

## Story Context

Time-scrambled echoes from passengers on Deck C include both real and fabricated fragments. Players must filter out fakes, reconstruct the voyage/night sequence, then use a survival-rate chart to pull letters from the real passengers’ names and stabilize the rift.

## Challenge Description

1. **Echo set:** Seven echoes labelled A–G. Each includes label, short narrative, embarkation port, ticket wording, class, and an event timing clue.
2. **Goal:** Produce a 4-letter code using only the real echoes, ordered chronologically, and mapped through the survival-by-birth-year chart.
3. **Chart:** “Survival Rate by Birth-Year Band” bar chart is already sorted left→right from lowest to highest survival. Leftmost band = 1st letter of the displayed name, next = 2nd, next = 3rd, rightmost = 4th.

## How to Solve (Player-Facing Logic)

**Stage 1 – Separate Truth from Fiction**
- Valid embarkation ports are only S, C, or Q. Ports like B (Belfast) or N (New York) indicate a fake.
- Ticket wording must match class: first-class should sound expensive, second-class moderate, third-class cheap. Any mismatch = likely fake.

**Stage 2 – Reconstruct the Night (Real Echoes Only)**
- Route order is S → C → Q. Early calm boarding language precedes impact; tilted/helping/chaos comes after; lifeboat/escape is latest.
- Use the provided event phrasing plus embarkation order to sort the real echoes chronologically.

**Stage 3 – Decode the Echo Word (Real Echoes, Timeline Order)**
- Compute birth year as 1912 – age for each real echo; place into the birth-year bands on the chart (already sorted low→high survival).
- Use band → letter index: leftmost band picks the 1st letter of the displayed name, next band picks 2nd, next 3rd, rightmost 4th.
- Pull those letters in the real-echo timeline order to get the final 4-letter code.

## GM Notes

- Real/fake assignments, voyage order, chart image, letter positions, and the final code are all generated and stored in `game_challenge.json` and surfaced in `gm_guide.md/html`.
- Hints: Level 1 (fake detection), Level 2 (timeline ordering), Level 3 (birth-year bands and letter mapping).
