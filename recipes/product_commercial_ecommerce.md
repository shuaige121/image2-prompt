# Product / Commercial / E-Commerce

> **When to use:** Pick this when the subject IS a physical product to sell or advertise — pack-shots, catalog/Amazon white-background, lifestyle in-scene hero, macro texture/detail, flat-lay, jewelry/reflective, or cosmetics/skincare.

## Base recipe

Photorealistic commercial product photograph of [PRODUCT — exact material, finish, color, label text if any], shot on a 100mm macro lens at f/8 for edge-to-edge sharpness, [BACKGROUND — e.g. seamless pure-white sweep / white acrylic with soft mirror reflection / warm oak counter]. Two large softboxes at 45 degrees either side as key and fill, plus a separate background light blowing the backdrop to clean white; a thin gradient floor shadow anchors the product. Even diffused studio light, true-to-life color, neutral white balance. Real material texture: [anchor — brushed-aluminum micro-grain / condensation beads on cold glass / matte cardboard fiber / fingerprint-free polished chrome with soft graded reflections]. Product centered, generous negative space, label legible and undistorted, 1:1 framing. Clean professional packshot, no props unless specified.

## Sub-categories

### White-background pack-shot (Amazon / catalog)
- **When:** E-commerce listing, marketplace hero, catalog grid — the default that platforms like Amazon require.
- **Camera:** 100mm at f/8–f/11, straight-on or slight 3/4 hero angle, eye-level to product
- **Lighting:** two-softbox 45-degree key+fill, separate background light to blow white pure, soft floor contact shadow

```text
photorealistic packshot of [PRODUCT] on a seamless pure-white sweep, 100mm lens at f/9, two 45-degree softboxes plus a dedicated background light burning the backdrop to clean #ffffff, a soft thin contact shadow under the base, neutral white balance, true product color, label sharp and readable, product filling ~85% of frame, centered, generous white margin
```


### Lifestyle in-scene hero
- **When:** Brand/ad hero, social, website banner — show the product being used in a real environment.
- **Camera:** 35–50mm at f/2–f/2.8, eye-level or slight high angle, product off-center on a thirds line
- **Lighting:** single soft window key from one side, subtle bounce fill, warm daylight white balance

```text
photorealistic lifestyle product photo of [PRODUCT] on a [sunlit kitchen counter / wooden cafe table / bathroom shelf], 50mm lens at f/2.8, shallow depth of field so the product is tack-sharp and the background falls into soft blur, soft window light from the left with a gentle reflector fill on the right, warm natural color, real surrounding context [steam, a hand reaching in, fresh ingredients], lived-in not staged, eye-level human perspective
```


### Macro detail / texture
- **When:** Conversion shot proving texture, finish, mechanism, or material quality — caps, stitching, gemstone facets, cream texture.
- **Camera:** 100mm macro 1:1, f/4–f/8 for a thin focal slice, very close working distance
- **Lighting:** hard raking side light to reveal texture relief, single small reflector to lift shadows

```text
extreme macro photograph of [DETAIL — the threaded pump, the woven strap edge, the cream swatch], 100mm macro lens at 1:1 magnification, f/5.6, razor-thin focal plane on the key detail with the rest melting to bokeh, raking side light to carve out micro-texture, visible real surface detail [fibers, brush marks, condensation, powder grain], true color, no smoothing
```


### Flat-lay (overhead)
- **When:** Lifestyle/social grid, kits, collections, bundles styled from above.
- **Camera:** 50mm at f/8 for full sharpness, perfectly perpendicular overhead
- **Lighting:** one diffused source from a single side, unidirectional soft shadows, no competing fill

```text
top-down flat-lay of [PRODUCT plus 2–4 complementary props], true 90-degree overhead angle with zero perspective tilt, 50mm lens at f/8, single soft diffused light from one side casting consistent gentle shadows in one direction, clean [linen / concrete / pastel paper] backdrop, items arranged in an odd-numbered balanced composition with breathing room, props angled toward the center, cohesive 2–3 color palette
```


### Jewelry / reflective metal & glass
- **When:** Rings, watches, chrome, glass, gold — anything mirror-like that fights glare.
- **Camera:** 100mm macro, f/11–f/16 for deep facet sharpness, slight top-down 3/4 angle
- **Lighting:** light-tent wraparound diffusion, black gobos for edge definition, pinpoint highlight for sparkle

```text
photorealistic macro of [JEWELRY — 18k gold ring with a brilliant-cut diamond], 100mm macro at f/11 for facet-to-facet sharpness, lit inside a light tent for wraparound soft diffusion, small black gobo cards placed to draw clean dark edge reflections that define the form, controlled specular highlights and gemstone sparkle, no blown glare, on a [dark gradient / white acrylic] surface with a faint mirror reflection
```


### Cosmetics / skincare
- **When:** Beauty hero, foundation/serum/cream, swatches, splash and texture energy shots.
- **Camera:** 85–100mm at f/8, straight-on or slight hero tilt, product upright and centered
- **Lighting:** directional soft key with grid for edge definition, white-acrylic mirror reflection, optional rim light for glass

```text
photorealistic beauty product photo of [BOTTLE/JAR — frosted glass serum dropper], 85mm lens at f/8, on a white acrylic surface with a clean mirror reflection, soft directional key from the left with a small grid for a crisp edge highlight, [optional: a glossy cream swatch / water droplets / a frozen liquid splash arc], true color, dewy luxury feel, label sharp, subtle specular on the cap
```


### Floating / levitation product
- **When:** Dynamic ad hero, supplements, drinks, gadgets — energetic suspended composition.
- **Camera:** 85mm at f/8, slight low angle to add lift, product dead-center or rule-of-thirds
- **Lighting:** soft frontal key+fill, rim light for edge separation, soft cast shadow on the floor for grounding

```text
photorealistic product shot of [PRODUCT] floating mid-air against a [soft gradient teal / clean white] backdrop, 85mm lens at f/8, [optional: ingredients, droplets, or powder suspended around it], a soft elliptical drop-shadow below selling the levitation, even studio softbox lighting with a crisp rim light to separate edges from the background, true color, sharp label
```


## Banned words (trigger the AI/uncanny look)

`8k` `4k` `ultra-HD` `hyper-detailed` `hyperrealistic` `masterpiece` `best quality` `award-winning` `professional photography` `studio lighting` `vibrant` `vivid colors` `highly detailed` `photoreal render` `octane render` `unreal engine` `cinematic` `trending on artstation` `sharp focus` `bokeh background` `CGI` `3D render` `glossy plastic look` `oversaturated` `perfect` `flawless` `stunning` `beautiful lighting` `ultra-realistic` `insanely detailed`

## img2img / reference-image

img2img is the single biggest realism win for this genre — feed the actual product so label text, logo, color, and proportions stay correct instead of being hallucinated. Patterns: (1) Pack-shot cleanup — pass a phone snap of the real product, prompt 'keep the product, its label text and exact colors identical; replace the background with a seamless pure-white sweep and add a soft contact shadow' to get a catalog-ready cut-out without retyping the label. (2) Re-light / re-scene — pass a clean packshot, prompt 'place this exact product on a sunlit oak counter, relight with soft window light from the left, match shadow direction and color temperature to the new scene so it does not look pasted in.' (3) Color/material swap — pass the product, prompt 'same bottle and label, change the cap from silver to matte black, keep all text and proportions unchanged.' Always instruct it to PRESERVE label/logo/text and match lighting + shadow direction + white balance to the target scene; the cookbook stresses matching light, shadows, and color temperature so a composited product integrates rather than looks pasted. For jewelry/reflective and tiny-text labels, reference images are near-mandatory — text-only prompts garble small type and faceting.
