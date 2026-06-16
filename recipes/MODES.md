# Step 0 — pick a mode (you, the calling LLM, choose)

Before composing any prompt, decide **what you are optimizing**. This is the single most important choice and it routes the whole prompt. There is no default — pick per task.

These two modes are the field's two fundamental axes — **alignment (adherence)** vs **human preference (resonance)**. They pull in different directions; don't try to max both.

## 🎯 Precise Control (精确控制) — optimize *adherence*
The image must **obey** the prompt: exact subject, count, position, label, identity, composition.
**Use for:** product / packshot, brand consistency, person likeness, precise multi-object scenes, anything matching a **reference image** (`--ref`), catalog/spec work.

## 🌫️ Evocative (意境圆满) — optimize *resonance*
The image must **make people feel something**: mood, story, atmosphere.
**Use for:** editorial / hero / mood shots, brand emotion, art, anything whose job is to land emotionally.

## How to choose — the subject's *story-capacity*
- Subject **can carry a feeling** (people, scenes, evocative food) **and you want resonance** → **Evocative**.
- Subject **can't tell a story** (isolated product, icon, diagram) **or you need exactness** → **Precise Control**.
- Empirically, Evocative on a lone product yields "expensive emptiness"; Precise Control on a human face yields a clean but soulless headshot. Match the mode to the job.

## Word budget per mode
*(provisional ratios — being calibrated by an ongoing intent×genre experiment; the shape is the point, not the exact %.)*

| component | 🎯 Precise Control | 🌫️ Evocative |
|---|---|---|
| **Intent** — mood / message / narrative | ~15% | **~50%** |
| **Subject** + real specifics | ~30% | ~25% |
| **Control** — lens / light / angle | **~35%** | ~15% (1–2 anchors only) |
| **Constraints** — banned-word avoidance | ~20% | ~10% |

Keep **one subject under ~110 words** in either mode (length sweet-spot; past ~150 it dilutes to *generic*, not ugly — the model just drops the excess).

## Iron rules
- **Precise Control:** pin counts/positions explicitly; pass a reference image and use the **anti-pasted-on clause** (see each genre's img2img notes: *"preserve shape/color/proportion exactly; match lighting, scale, shadow, perspective; do not restyle"*).
- **Evocative:** lead with the feeling; keep the **implied scene simple and renderable** — intent that forces a complex scene (boat rigging, crowds, hands, many objects) invites AI artifacts. Trust the model's defaults; under-specify on purpose (a clean 12-word evocative prompt often beats a 100-word one).
- **Either mode:** never use render-spam — `8k, 4k, masterpiece, hyper-detailed, studio lighting, cinematic, vibrant, stunning, flawless, octane, unreal engine, award-winning`.

Then go to `recipes/<genre>.md`, and compose at the **ratio your mode dictates** — the genre files give the control-layer snippets; in Evocative mode you lead with intent and borrow only one or two control anchors from them.
