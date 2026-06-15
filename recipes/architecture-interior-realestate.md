# Architecture / Interior / Real-Estate

> **When to use:** Pick this when the subject is a building, a room, or a property listing — exteriors, interior spaces, real-estate hero shots, architectural details, or twilight/dusk facade shots.

## Base recipe

Photorealistic [interior/exterior] photograph of [SUBJECT: e.g. a mid-century living room / a brick townhouse facade], shot on a full-frame camera with a [17mm tilt-shift / 24mm wide / 50mm prime] lens kept perfectly level so vertical lines stay straight and parallel (no keystoning), [eye-level / chest-height tripod] framing. Aperture f/8 for edge-to-edge sharpness, deep focus from foreground to back wall. Lighting: [natural window light from camera-left / soft overcast daylight / warm low golden-hour sidelight], white-balanced so daylight reads neutral and tungsten lamps glow warm tungsten. Real-texture anchors: visible wood grain, slightly uneven plaster, fabric weave on upholstery, faint floor reflections, dust motes in a light shaft, real grout lines. Natural color, balanced exposure that holds detail in both window highlights and shadow corners, mild contrast. Composition: clean leading lines, one clear focal point, tidy but lived-in staging. Looks like a real magazine real-estate photo, not a 3D render.

## Sub-categories

### Interior room (real-estate / editorial)
- **When:** Listing photo or magazine-style shot of a furnished room — living room, kitchen, bedroom.
- **Camera:** 17mm tilt-shift, f/8, level eye-level tripod, deep focus
- **Lighting:** flambient (window daylight + soft even fill), neutral daylight WB, warm lamps

```text
Photorealistic interior real-estate photograph of a [living room], shot on a 17mm tilt-shift lens held perfectly level so wall verticals stay dead straight and parallel, eye-level tripod framing into a back corner to show depth. f/8, deep focus, whole room sharp. Flash-and-ambient lighting blend: soft natural daylight pouring from the windows plus an even fill so shadows stay open and colors read true; daylight neutral, table lamps a warm tungsten glow. Real texture: wood-grain flooring with faint reflections, fabric weave on the sofa, slightly creased throw pillows, a few real lived-in details. Balanced exposure that holds the view through the window without blowing it out, natural color, mild contrast.
```


### Building exterior (facade, golden hour)
- **When:** Hero shot of a house or building front with warm directional light and texture.
- **Camera:** 24mm shift lens, f/8, three-quarter angle, level
- **Lighting:** golden-hour raking sidelight from one side, long soft shadows

```text
Photorealistic exterior architectural photograph of a [brick townhouse / glass office facade], shot on a 24mm shift lens kept level so the building's vertical edges run straight and parallel, three-quarter angle showing two faces for depth. f/8, sharp front to back. Low golden-hour sun raking across the facade from camera-right, long soft shadows revealing the texture of brick, stone, and window reveals, warm side light, deep blue sky opposite. Real texture: mortar lines, weathering on the stone, glint on window glass, a real street and a little foreground greenery. Natural color, balanced exposure, mild contrast, clean leading lines toward the entrance.
```


### Twilight / dusk exterior (blue hour)
- **When:** Premium listing or architecture shot with glowing windows against a deep blue sky.
- **Camera:** 24mm shift lens, f/8, tripod, level, three-quarter
- **Lighting:** blue-hour cool sky gradient + warm interior/exterior glow

```text
Photorealistic twilight real-estate photograph of a [modern home] at blue hour, ~25 minutes after sunset, shot on a 24mm shift lens kept level so verticals stay straight, three-quarter framing. f/8, tripod, deep focus. Deep saturated blue sky that darkens from horizon up to zenith, every interior room lit with warm tungsten glow spilling through the windows, warm exterior path and soffit lights, balanced so the warm window glow and the cool sky sit in harmony. Real texture: faint warm reflections on the driveway, soft pool of light on the lawn, real landscape lighting. Natural color, exposure balanced between glowing windows and the dusk sky, no harsh black shadows.
```


### Architectural detail / texture
- **When:** Close isolation of a material, joint, or design element — a railing, brick bond, a corner, a stairwell.
- **Camera:** 50mm prime, f/8, tight isolating frame, slight off-axis
- **Lighting:** soft overcast / even diffused daylight, near-shadowless

```text
Photorealistic architectural detail photograph of [a steel-and-oak staircase joint / a herringbone brick wall], shot on a 50mm prime, tighter framing that isolates the element and fills the frame, slight off-axis angle to show form. f/8 for crisp material detail, focus on the texture. Soft overcast daylight acting like a giant softbox — even, near-shadowless light that keeps color accurate and shows every surface. Real texture: tool marks, grain, oxidation, mortar joints, subtle wear at the edges, fingerprint-level surface detail. Natural color, neutral white balance, mild contrast, honest material rendering.
```


### Wide-angle small space (bathroom / kitchen / hallway)
- **When:** Cramped real-estate spaces that need to read as open and bright.
- **Camera:** 16mm wide-angle, f/8, level and centered, doorway framing
- **Lighting:** bright flambient, open shadows, daylight-neutral WB

```text
Photorealistic interior real-estate photograph of a [compact bathroom / galley kitchen], shot on a 16mm wide-angle held perfectly level and centered so tile grout lines and cabinet edges stay straight (no bowing, no leaning walls), framed from the doorway to show the whole space. f/8, deep focus, everything sharp. Bright flash-and-ambient blend: clean even light, open shadows, daylight-neutral white balance so white tile reads white and wood reads warm. Real texture: grout lines, faint water spots on glass, brushed-metal fixtures, fabric on a towel. Balanced bright exposure that still holds window detail, natural color, mild contrast, feels open and airy.
```


### Open-plan / wide interior establishing shot
- **When:** A large great-room or loft where the goal is to show flow and scale.
- **Camera:** 20mm shift lens, f/8, corner framing, level, deep focus
- **Lighting:** window daylight + even fill, neutral WB, warm pendants

```text
Photorealistic interior architectural photograph of an [open-plan great room with kitchen and dining], shot on a 20mm shift lens kept level so all verticals stay straight, framed from a corner to lead the eye through the space. f/8, deep focus across the whole depth. Soft natural daylight from a wall of windows plus gentle even fill, daylight-neutral white balance, warm pendant lights glowing tungsten. Real texture: engineered-wood floor with faint reflections, stone countertop veining, fabric on seating, a few real lived-in props. Balanced exposure that holds the bright window view, natural color, mild contrast, strong sense of depth and flow.
```


## Banned words (trigger the AI/uncanny look)

`8k` `4k` `masterpiece` `hyper-detailed` `ultra-detailed` `photoreal render` `octane render` `unreal engine` `3D render` `CGI` `architectural visualization` `archviz` `studio lighting` `cinematic` `dramatic lighting` `vibrant` `stunning` `breathtaking` `luxury (as adjective)` `HDR look` `oversaturated` `perfectly clean` `flawless` `award-winning` `epic` `trending on artstation`

## img2img / reference-image

img2img is the single biggest realism lever for this genre, because gpt-image-2 left to itself drifts toward archviz/CGI. Pass a real listing or magazine photo as the reference (image2 --ref or codex -i) and the model copies real-camera cues — straight verticals, true flat lighting, real material grain. Patterns: (1) Restyle a real room — keep the geometry/lens feel of a reference photo, change only the furniture/style/era in the prompt, so perspective and light stay photographic. (2) Day-to-dusk — feed a daytime exterior and prompt only the blue-hour sky + warm window glow change; far more believable than generating twilight from scratch. (3) Material/finish swap — reference a detail shot, swap the material (oak to walnut, brick to stone) while keeping real texture and lighting. (4) Empty-to-staged — reference an empty room, prompt furniture in, keeping the real window light and floor. Always tell it to preserve straight verticals and the existing light direction so it does not 'correct' the photo into a render. Reference photos with mild lens imperfection (a touch of vignetting, real reflections, slight clutter) beat pristine ones — they anchor the output away from the too-clean CGI look.
