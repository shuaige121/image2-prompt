# Automotive (cars & vehicles)

> **When to use:** Pick this when the subject is a car, motorcycle, or vehicle — hero studio shots, rolling/motion shots, detail close-ups, or lifestyle-on-location.

## Base recipe

Shot brief, fill the bracketed slots, delete what you don't need:

"[full color/make/model + body style], [3/4 front hero | profile | low front-corner] angle, shot on [Canon EOS R5 / Sony A1] with a [35mm | 50mm | 85mm | 24-70mm at 35mm] lens at [f/8 for whole-car sharpness | f/2.8 to isolate], [eye-level | knee-height low angle], parked on [wet asphalt / concrete studio floor / mountain switchback]. Lighting: [large overhead softbox + a long gradient highlight rolling down the door panels | low raking late-afternoon sun grazing the bodylines]. Clean controlled reflections on the paint, no blown highlights on the chrome, visible flake in the metallic clearcoat, sharp panel gaps and tire sidewall lettering. [overcast soft daylight | warm golden-hour color]. Natural color, realistic contrast."

Rules that make it read as a real photo, not a render:
- Always name a real focal length + aperture and a real camera body. f/8–f/11 for the whole car in focus; f/2.8–f/4 only for detail isolation.
- Name the reflection behavior explicitly ("soft gradient reflection rolling across the hood," "no studio gear reflected in the paint") — uncontrolled reflections are the #1 tell of a fake car shot.
- Anchor real textures: "metallic flake in the clearcoat," "brushed aluminum trim," "rubber tire sidewall lettering," "stitched leather," "carbon-fiber weave," "tiny dust and brake dust on the wheels."
- Put the car at a known angle (3/4 front is the default hero) and a known camera height (low, at the headlight line, makes cars look planted and aggressive).
- Specify the ground and the sky/ceiling — both reflect into the bodywork and sell realism.

## Sub-categories

### Studio hero (cyc wall / seamless)
- **When:** Catalog hero, configurator, launch key visual — clean isolated car, full control of light.
- **Camera:** 50mm at f/9, eye/headlight height, 3/4 front
- **Lighting:** large overhead softbox + side fill, subtractive black flags, gradient panel highlight, reflective floor

```text
silver [make/model] on a seamless white cyclorama sweep, 3/4 front hero angle at headlight height, 50mm lens at f/9, lit by one huge overhead softbox plus side fill, a long smooth gradient highlight rolling from roof down the door panels, black flags subtracting glare so reflections stay soft and clean, faint mirror reflection of the car on the polished studio floor, sharp panel gaps, metallic flake visible in the paint, even soft shadow under the car
```


### Rolling / motion shot
- **When:** Action hero showing the car driving — blurred ground, spinning wheels, tack-sharp body.
- **Camera:** 17-24mm wide at f/8, ~1/40s for motion blur, low front 3/4 from a tracking/rig position
- **Lighting:** available daylight, side or back light to rake bodylines

```text
red [make/model] driving on a coastal road, rolling shot from a tracking camera car at matched speed, 24mm lens at f/8, shutter around 1/40s so the asphalt and background streak with motion blur and the wheels spin into a disc while the car body stays sharp, low front 3/4 angle, late-afternoon side light raking the bodylines, slight road grime on the lower panels
```


### Detail / macro close-up
- **When:** Badge, headlight, wheel/caliper, stitching, carbon weave, exhaust tip — texture storytelling.
- **Camera:** 90-105mm macro at f/2.8-f/4, shallow DOF, frame-filling
- **Lighting:** single soft raking light + polarizer to cut glare, dark clean background

```text
extreme close-up of the [brake caliper behind spoke wheel | quilted leather seat stitching | carbon-fiber weave on the diffuser], 100mm macro lens at f/3.5, shallow depth of field with the logo/stitch in razor focus and the rest melting to soft bokeh, raking soft light revealing surface texture, polarizer killing glare on the gloss, no studio gear reflected, tiny realistic brake dust and fine scratches
```


### Lifestyle on-location
- **When:** Editorial/ad story — car in a real place, mood and environment, optional person.
- **Camera:** 35mm or 85mm prime at f/2.8-f/4, eye-level, environmental framing
- **Lighting:** golden-hour sun or blue-hour city ambient, reflections and flare as mood

```text
[make/model] parked on a wet city street at golden hour, 35mm lens at f/4, eye-level, neon shop signs and bokeh streetlights reflecting in the wet road and the car's flank, warm low sun flaring softly off the windshield, [a person leaning on the door in casual clothes,] lived-in environment with puddles and texture, cinematic but natural color
```


### Off-road / dirty action
- **When:** SUV/truck/rally hero in dirt, water, snow — grit and dynamics.
- **Camera:** 24-35mm at f/8, very low ground angle, action-frozen
- **Lighting:** diffuse overcast or backlit dust, gritty realistic contrast

```text
[SUV/truck] climbing a muddy trail, 35mm lens at f/8, low angle from the ground, mud spray off the tires frozen mid-air, dust kicked up behind catching the backlight, dirt and water beading realistically on the fenders and skid plates, overcast diffused light, deep tire tread packed with mud
```


### Night / city lights
- **When:** Moody hero with light trails, neon, garage, or showroom-after-dark vibe.
- **Camera:** 35mm at f/4-f/5.6, long exposure, low or eye level
- **Lighting:** mixed practical/ambient night light, controlled reflective streaks, deep shadow

```text
[make/model] parked in an empty underground garage at night, 35mm lens at f/4, long exposure, overhead fluorescent tubes and a single warm practical light reflecting in long streaks down the wet bodywork, deep shadows, color cast from mixed lighting, faint light trails of a passing car in the background, no blown highlights
```


## Banned words (trigger the AI/uncanny look)

`8k` `4k` `hyper-detailed` `ultra-detailed` `masterpiece` `best quality` `studio lighting` `cinematic lighting` `octane render` `unreal engine` `3D render` `CGI` `vibrant` `hyperrealistic` `photorealistic` `award-winning` `professional photography` `highly detailed` `sharp focus` `glossy showroom shine` `perfect reflections`

## img2img / reference-image

Reference images help most here because car proportions and badges are hard to hallucinate correctly. Patterns: (1) Feed a real photo of the exact make/model at the angle you want and prompt "keep the car's exact body shape, proportions, badges and wheel design; restyle only the LIGHTING and BACKGROUND to [studio cyc / golden-hour street]" — this preserves the silhouette that text alone gets wrong. (2) For color/paint swaps, supply the car image and say "change paint to [color] metallic, keep all reflections, geometry, and trim identical." (3) For a clean studio plate, pass a reference of the desired cyc-wall reflection/floor and let the car be the variable. (4) Reflections and wheel spokes are the parts gpt-image-2 most often warps — if generating from scratch, expect to regenerate wheels/badges; an img2img reference of the real wheel fixes spoke count and caliper placement. Keep prompts as a shot brief even in img2img; describe the camera and light you want layered onto the reference.
