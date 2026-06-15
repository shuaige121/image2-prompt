# Portrait & People

> **When to use:** Pick this when the subject is one or more humans and likeness, skin, expression, or pose is the point — headshots, candid lifestyle, environmental, group, or beauty/closeup.

## Base recipe

[CANDID photograph / environmental portrait — pick one, avoid the word "headshot" unless you truly want studio polish] of [WHO: age range, build, hair, one specific wardrobe detail], [WHAT THEY'RE DOING + where they're looking — e.g. mid-laugh glancing off-camera, not staring down the lens].
Shot on a [50mm / 85mm / 35mm] lens at [f/2 for one face, f/2.8 individual, f/5.6–f/8 for groups], [eye-level / slightly above], medium close-up, shallow depth of field with the background falling soft.
Lighting: [soft window light from camera-left / overcast open shade / late golden-hour backlight], directional so one cheek falls into gentle shadow.
Skin reads real: visible pores and fine peach-fuzz, faint under-eye texture, a few freckles or a small blemish, natural redness around the nose and ears, slight oil sheen on the forehead — not airbrushed, not even-toned.
Color science of [Kodak Portra 400 / Fujifilm Pro 400H], faint film grain, true-to-life muted color, a touch of warmth.
Honest and unposed; no glamorization, no heavy retouching.

## Sub-categories

### Candid lifestyle
- **When:** User wants a natural, in-the-moment feel — laughing, walking, coffee, kids, couples; the default for warm authentic people shots.
- **Camera:** 35mm or 50mm prime, f/1.8–f/2.8, eye-level, slight handheld feel
- **Lighting:** golden hour backlight or soft window light; warm, directional, not flat

```text
candid photograph, 35mm lens at f/2, eye-level, subject mid-motion looking off-camera, late golden-hour backlight rim-lighting the hair with warm bokeh balls behind, Kodak Portra 400 color, faint grain, motion caught not posed, honest and unposed
```


### Studio headshot
- **When:** Corporate, actor, or LinkedIn-style clean headshot on a controlled background.
- **Camera:** 85mm or 105mm, f/4–f/8, eye-level, tight head-and-shoulders
- **Lighting:** loop or Rembrandt: key 45 degrees + above with softbox, soft fill or reflector, 1:2 ratio

```text
professional headshot, 85mm lens at f/4, eye-level, head-and-shoulders crop, single softbox key at 45 degrees and slightly above for loop lighting (small soft shadow off one side of the nose), gentle fill, seamless mid-grey backdrop, real skin with visible pores and slight forehead sheen, catchlights in both eyes, subtle film grain
```


### Environmental portrait
- **When:** Subject shown in their workplace or meaningful space — craftsperson, chef, farmer; context tells the story.
- **Camera:** 35mm or 24–70mm at 35–50mm, f/4–f/5.6 for deeper field, eye-level or slightly low
- **Lighting:** available daylight, window or open shade, reflector fill to shape

```text
environmental portrait, 35mm lens at f/4 so the workspace stays readable, subject framed within their setting (workshop / kitchen / field) engaging with their tools, soft directional daylight from a window, weathered skin with visible wrinkles pores and sun texture, lived-in props, Fujifilm color, no glamorization
```


### Group portrait
- **When:** Two or more people — family, team, friends; everyone must be sharp.
- **Camera:** 35–50mm, f/5.6 for one row / f/8–f/11 for multiple rows, focus on middle plane
- **Lighting:** soft even open shade or overcast so no one is shadowed out

```text
group photograph of [N] people arranged close together in two staggered rows, 50mm lens at f/8 with focus on the middle row so front and back faces stay sharp, soft even overcast light, natural relaxed spacing leaning toward each other, real varied skin tones and textures, candid half-smiles not stiff posing, faint film grain
```


### Beauty / macro closeup
- **When:** Makeup, skincare, jewelry-on-skin, glossy editorial beauty where skin and eyes are the subject.
- **Camera:** 100mm macro, f/5.6–f/8 for sharp detail, dead-on or slight angle
- **Lighting:** clamshell (key above + fill/reflector below), soft and even, twin catchlights

```text
beauty closeup, 100mm macro lens at f/5.6, tight crop on face and eyes, clamshell lighting (softbox above, reflector below) for soft sculpted cheekbones and bright catchlights, dewy real skin with fine pores and peach-fuzz visible, individual eyelashes and lip texture sharp, gentle natural retouch not plastic, clean color
```


### Anti-uncanny skin booster
- **When:** Append to ANY of the above when the face comes back waxy, plastic, or too symmetrical.
- **Camera:** (modifier — keep the parent shot's lens/aperture)
- **Lighting:** (modifier — keep the parent shot's lighting)

```text
real human skin: visible pores across the nose and cheeks, fine peach-fuzz on the jaw, faint under-eye lines and texture, a few freckles and one small blemish, natural redness at the nostrils and ear tips, slight asymmetry in the eyes and smile, light forehead oil sheen, no airbrushing, no even-toned smoothing, no porcelain finish
```


## Banned words (trigger the AI/uncanny look)

`8k` `4k` `hyper-detailed` `ultra-detailed` `masterpiece` `studio lighting` `vibrant` `flawless skin` `porcelain skin` `perfect skin` `smooth skin` `airbrushed` `glamorous` `stunning` `beautiful` `gorgeous` `photorealistic` `hyperrealistic` `render` `octane` `CGI` `symmetrical face` `professional retouching` `glowing skin` `cinematic` `dramatic lighting` `magazine cover`

## img2img / reference-image

For likeness, pass a clear front-lit reference face and instruct "keep this person's identity, face shape, and features the same — change only the [lighting / setting / wardrobe]"; on multi-step edits re-specify critical features each turn since identity drifts. For pose/composition reference, supply a second image and say "use this framing and pose." When a generated face is too plastic, run img2img on the output with the anti-uncanny skin snippet and a low-to-moderate edit strength so geometry holds but pore texture is rebuilt. For groups, a reference photo of the row arrangement controls spacing far better than text. Reference a real film stock (Portra 400, Pro 400H) by name to pull color and grain toward photographic, away from the default over-clean digital look.
