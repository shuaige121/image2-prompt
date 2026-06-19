# optflow — does the whole optimization process beat naive prompting? (gpt-image-2)

**Question:** exp4 showed which *components* help. This tests the *integrated process* end-to-end: does a prompt composed by our rules beat what a naive user actually writes?

**Design.** 4 subjects (2 story-capable: night noodle stall, elderly potter; 2 hard objects: skeleton wristwatch, honey jar) × 3 arms × 2 reps = **24 images**, one clean Codex token, paced. Blind: per subject, the 6 images (2 of each arm) shuffled A–F; 3 raters/subject (12 sheets) scored realism/depth/light/emotion/technical/overall (1–10). Arms compared within subject+rater.

- **N1 bare** — `A photo of {X}.`
- **N2 render-spam** — `{X}, 8k, hyperrealistic, masterpiece, studio lighting, vibrant, cinematic, award-winning…` (the common naive "more quality words")
- **OPT** — composed by the process: subject specifics first, mode-appropriate intent, light-via-scene, one lens anchor, no render-spam.

## Result

Mean overall: **OPT 7.74 > N1 bare 6.52 > N2 render-spam 5.77.**

| comparison | overall | realism | depth | light | emotion | technical |
|---|---|---|---|---|---|---|
| OPT − N1 (bare) | +1.21 | +0.89 | +1.00 | +1.29 | +1.82 | +0.76 |
| OPT − N2 (render-spam) | +1.97 | +2.07 | +1.27 | +1.67 | +1.95 | +1.55 |

Per-subject OPT vs best baseline: noodle **+1.32**, potter **+2.25**, honey **+1.83**, **watch −0.88**. OPT won outright in **9/12** rater cells (all 3 losses on the watch).

## Takeaways
1. **The process works**, and **render-spam is actively worse than writing nothing** (N2 < N1 overall, −0.75; render-spam tanks realism −1.2).
2. **Render-spam harm is subject-class-dependent — a people problem.** It craters human-skin realism, but on the isolated hard product (watch) it scored *highest* ("sharp/studio/vivid" = catalog aesthetic; product defaults are already commercial-grade).
3. **Mode discipline has a price tag.** OPT only lost on the watch (−0.88), because that OPT prompt leaked Evocative elements (mood line, window light, shallow DoF) into a Precise subject — confirming "Evocative-on-a-lone-product = expensive emptiness." Pure products need a hard switch to studio clarity / deep focus / dead-sharp / exact spec / no mood.

*Caveats:* n=12 sheets, 4 subjects. OPT prompts were authored by an LLM applying the process, so this measures the process *as applied* — the watch loss is partly a mode-discipline slip (a strict Precise-mode watch prompt was NOT tested as a 4th arm and might beat the baselines). "Hard-product" render-spam tolerance rests mainly on the single watch subject. Complements exp4 (component ROI) and the n=3 ratio study. See `recipes/MODES.md` Calibration III.
