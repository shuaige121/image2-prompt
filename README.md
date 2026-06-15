# image2-prompt

Paste-ready, **anti-uncanny prompts for gpt-image-2** (OpenAI "Image 2" / the Codex `image_gen` tool) across **12 photography genres** — Food, Portrait, Product, Landscape, Architecture, Street, Still Life, Fashion, Wildlife, Event/Wedding, Automotive, Macro.

It's also a **Claude skill**: load [`SKILL.md`](SKILL.md) and any agent immediately sees the genre "interfaces" (top-level category → sub-categories → when-to-use), then drills into [`recipes/<genre>.md`](recipes/) for the full shot-brief. See [`TAXONOMY.md`](TAXONOMY.md) for the one-screen map.

The whole thing exists because of one hard-won lesson with gpt-image-2: **subjects look fake when you prompt them like a render and real when you prompt them like a camera.** Words like `studio product photo`, `pure white background`, `8k`, `vibrant`, `high detail` produce flat, oversaturated, depth-less, uncanny-valley images. Camera language — named lens + aperture, shallow depth of field, film stock, one soft light direction — produces something that looks *shot*, not generated. Food is the worked example below; every other genre follows the same rule in `recipes/`.

## What's inside

| File | What it is |
|------|-----------|
| `prompts.md` | The prompt library (zh/en, snippet-first): people anti-uncanny, **food recipe**, **img2img / reference-image patterns**, reference sourcing, and a 2026 research-upgrade section (§6). |
| `scripts/image2.py` | Parallel gpt-image-2 generator driven headlessly via `codex exec`. Text2img + img2img (`--ref`), per-image isolated threads, usage reporting. No `OPENAI_API_KEY` — uses the Codex subscription auth. |
| `scripts/findref.py` | Headless reference-image fetcher (DuckDuckGo → Bing tiers, magic-byte validation, stock-watermark blocklist) for the img2img workflow. |
| `examples/` | Finished outputs. |

> Config note: `image2.py` reads `GEMINI`/counter settings from files **outside** the repo (`~/.codex/...`). No tokens are committed.

## The food recipe (the part that matters)

Build the prompt like a shot brief, not a wish list:

```
Photorealistic professional food photograph of <dish> in <vessel>,
shot on a 50mm lens at f2.0, shallow depth of field with background falloff,
soft natural window light from camera-left with gentle shadow fall-off, daylight white balance,
shot on Kodak Portra 400, muted film-like color science, subtle film grain,
<2-3 named textures>, <1-2 realism anchors: faint flour dusting / a thin wisp of backlit steam>,
realistic portion size, clear foreground-to-background separation.
The image should feel honest and unposed, with real texture and everyday detail.
No glamorization, no heavy retouching, no plastic glaze, no AI-perfect symmetry, no neon colors, no studio lighting.
```

**Banned words** (they trigger the plastic/uncanny look): `8k` `masterpiece` `studio lighting` `vibrant` `smooth` `perfect lighting` `hyper-detailed` `Ektar`.

## img2img / reference images

`image2.py --ref a.jpg --ref b.jpg` rides reference images along (up to 16). For composition control, label each image's role and pin the anti-pasted-on clause:

```
Image 1: dish to preserve.  Image 2: lighting/color-grade reference.  Image 3: background.
Preserve the dish shape, color, garnish, proportions exactly.
Match lighting, scale, shadow, and perspective. Do not restyle it.
```

Mechanics (gpt-image-2): no `input_fidelity` param (inputs are always high-fidelity); a mask hits the **first** image only; max 16 input images.

## Example

`examples/c1-balanced-set.png` — four steamed buns in one bamboo steamer, each cut open to reveal a different real filling (minced pork / curry chicken / braised eggplant / bok-choy & shiitake), generated img2img from the real product photos with the recipe above. Note the depth of field and the muted, filmic color — no oversaturation, no uncanny sheen.

## Quick start

```bash
# one image
python3 scripts/image2.py "Photorealistic professional food photograph of ..." --quality high

# img2img from a real product photo
python3 scripts/findref.py "char kway teow delivery app photo" --n 2 --out ./refs
python3 scripts/image2.py "...our dish..." --ref ./refs/ref1.jpg --quality high
```

Requires a working Codex CLI with image_gen access.

## Credits / built on

The food recipe and img2img patterns are distilled from the **[OpenAI Cookbook image-generation prompting guide](https://developers.openai.com/cookbook/examples/multimodal/image-gen-models-prompting-guide)** plus a survey of existing community tooling — see **[`RESOURCES.md`](RESOURCES.md)** for the full curated list (36 repos). Reuse the wheels; don't reinvent them. Highlights:

- Prompt corpora: [EvoLinkAI/awesome-gpt-image-2-API-and-Prompts](https://github.com/EvoLinkAI/awesome-gpt-image-2-API-and-Prompts) (CC0), [YouMind-OpenLab/awesome-gpt-image-2](https://github.com/YouMind-OpenLab/awesome-gpt-image-2), [ZeroLu/awesome-gpt-image](https://github.com/ZeroLu/awesome-gpt-image)
- Same-shape Codex generators worth studying: [aldegad/image-gen](https://github.com/aldegad/image-gen), [buluslan/gpt-image2-ecommerce](https://github.com/buluslan/gpt-image2-ecommerce) (25 "product-in-scene" templates), [wuyoscar/GPT-Image2-Skill](https://github.com/wuyoscar/GPT-Image2-Skill)
- Compositing / cutout pipeline (for img2img prep): [danielgatis/rembg](https://github.com/danielgatis/rembg), [lllyasviel/IC-Light](https://github.com/lllyasviel/IC-Light) (relight to match a scene), [Sanster/IOPaint](https://github.com/Sanster/IOPaint)
- Reference sourcing: [deedy5/ddgs](https://github.com/deedy5/ddgs), [mikf/gallery-dl](https://github.com/mikf/gallery-dl)

## License

MIT — see `LICENSE`.
