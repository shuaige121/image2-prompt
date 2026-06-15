# Food & Beverage Photography

> **When to use:** Pick this when the subject is something edible or drinkable — a plated dish, menu/delivery shot, cocktail, dessert, or street-food scene — and the goal is appetizing realism, not a render.

## Base recipe

Write the prompt as a shot brief in five labeled lines, in this order:

Scene: [surface + setting + time/window light, e.g. "on a worn walnut table by a north-facing window, late-morning"]
Subject: [the dish/drink, named concretely with its real textures, e.g. "a soft-boiled ramen egg, yolk just oozing, halved"]
Camera: [named lens + aperture feel + angle, e.g. "shot on a 100mm macro at f/4 feel, 45-degree angle, shallow depth of field with the back of the plate falling soft"]
Light: [direction + quality + one shaping note, e.g. "soft directional window light from camera-left, gentle falloff into shadow on the right, a single white bounce card lifting the shadows"]
Finish: [film/color-science + real-texture anchors + use case, e.g. "natural color, warm neutral white balance, faint specular highlights on the oil, real-photograph look, editorial food shot"]

Rules that make it read real, not rendered:
- Always name a lens AND an aperture feel ("f/2.8 feel"), plus the camera angle (top-down / 45-degree / eye-level). These steer realism far more than "8k".
- Always state ONE light direction and quality (e.g. "soft side-backlight at 10 o'clock"). One key light reads photographic; "studio lighting" reads CGI.
- Anchor at least two real, edible textures or imperfections: steam, condensation, a sauce smear, crumbs, oil sheen, a torn herb leaf, a fingerprint of flour. Believable imperfection is what sells it.
- Say "real photograph" or "iPhone photo" / "editorial food photo" so the model targets a photo, not an illustration.
- Keep the palette to 3-4 colors and one hero; clutter and rainbow plates read as stock-art AI.

## Sub-categories

### Menu / delivery-app catalog shot
- **When:** Uber Eats / DoorDash / digital menu — one dish, clean, has to look exactly like what arrives. Top-down for flat items (pizza, bowls, salads), 45-degree for tall items (burgers, layered drinks).
- **Camera:** 50mm feel for top-down flat-lay; 100mm macro at f/4 feel, 45-degree angle for tall items; whole dish in focus front-to-back
- **Lighting:** soft diffused daylight from one side, no harsh shadows, neutral white balance, no yellow cast

```text
Scene: a single plated [dish] centered on a clean light-grey ceramic plate, neutral pale background, generous breathing room. Subject: [dish named with real textures, e.g. a double cheeseburger, glossy brioche bun, melted cheese pulling at the edge]. Camera: shot on a 100mm macro at f/4 feel, 45-degree angle, the whole dish sharp front to back. Light: soft diffused daylight from camera-right, a white bounce card on the left, gentle even shadows, warm-neutral white balance. Finish: natural realistic color and true portion size, faint steam, real-photograph look, clean delivery-app menu shot. 5:4 crop.
```


### Editorial / magazine dark-and-moody
- **When:** Cookbook spreads, restaurant features, story-driven food. Dramatic, restrained, intimate.
- **Camera:** 100mm macro or 85mm short-tele at f/2.8 feel, 30-45 degree angle, shallow depth of field with creamy falloff
- **Lighting:** single soft window light from camera-left through a sheer curtain, deep graduated shadows on a dark background

```text
Scene: [dish] on a dark slate surface against a near-black background, textured charcoal linen, vintage tarnished cutlery, deep burgundy-and-green palette. Subject: [dish named with real textures, e.g. a rare-roasted lamb rack, glistening fat cap, a smear of pea puree, scattered torn mint]. Camera: shot on an 85mm at f/2.8 feel, 35-degree angle, shallow depth of field, the far rim of the plate falling soft. Light: soft directional window light from camera-left through a sheer curtain, deep graduated shadows pooling on the right, no fill on the shadow side. Finish: muted natural color, gentle film grain, low-key contrast, real-photograph editorial look, restrained 3-color frame.
```


### Fine-dining hero
- **When:** Flagship dish, restaurant homepage, the one shot that has to look impeccable and chef-styled.
- **Camera:** 100mm macro at f/2.8-f/4 feel, low 20-30 degree hero angle to give the plate height, tight crop
- **Lighting:** soft key from back-left with a precise highlight, flagged to keep the background dark and clean

```text
Scene: a single composed plate on dark polished stone, minimal negative space, one fresh herb sprig as accent. Subject: [signature dish styled with tweezers-level precision, e.g. seared scallop, golden crust, a comma of citrus gel, micro-greens, a dusting of bottarga]. Camera: shot on a 100mm macro at f/2.8 feel, low 25-degree hero angle so the plating reads tall, tight crop with shallow depth of field. Light: soft key light from back-left raking across the surface to catch the sear, background flagged into clean shadow, a small mirror bounce picking out one specular highlight on the sauce. Finish: precise natural color, crisp focus on the hero element softening behind, real-photograph fine-dining look.
```


### Flat-lay / overhead spread
- **When:** Multiple dishes, table-scape, brunch board, ingredients-and-process layouts where you want the whole story in one frame.
- **Camera:** 50mm feel, true top-down 90-degree, everything in focus, shot square to the table
- **Lighting:** large soft side light across the table, consistent shadows all falling the same direction

```text
Scene: a wooden table shot straight down, [3-4 dishes] arranged with intentional gaps, scattered napkins, a few loose ingredients (herbs, halved citrus, crumbs) bridging the elements. Subject: [the spread named, e.g. a mezze board — hummus with a swirl and pooled olive oil, charred pita, olives, marinated feta]. Camera: 50mm feel, true top-down 90-degree, full depth of field with everything crisp edge to edge. Light: one large soft light from the top-left of the table, all shadows falling the same direction, soft and graduated. Finish: warm natural color, real-photograph flat-lay look, restrained palette, deliberate composition not cluttered.
```


### Beverage / cocktail
- **When:** Cocktails, iced drinks, juices, beer, anything in a glass where liquid glow and condensation are the selling point.
- **Camera:** 100mm macro at f/2.8-f/4 feel, eye-level or slightly above, drink isolated against a darker background
- **Lighting:** backlight or side-backlight at 10-11 o'clock to make the liquid glow, plus rim light to separate the glass

```text
Scene: a [cocktail] in a [glass type] on a dark bar surface, moody background, a twist of citrus peel and one ice cube catching light. Subject: [drink named with liquid detail, e.g. a negroni, deep red, oil slick of orange peel, a single large clear ice cube, fresh glycerin-style condensation beading on the glass]. Camera: shot on a 100mm macro at f/2.8 feel, eye-level, the drink isolated with shallow depth of field. Light: soft side-backlight at 10 o'clock making the liquid glow from within, a thin rim light separating the glass from the dark background, fill card camera-front to hold the front of the glass. Finish: rich saturated liquid color, real condensation droplets that hold their shape, faint bubbles, real-photograph beverage look.
```


### Dessert
- **When:** Cakes, pastries, plated sweets, ice cream — where drips, dustings, and indulgent texture do the work.
- **Camera:** 100mm macro at f/2.8 feel, 30-45 degree or eye-level for layered/tall desserts, tight on the texture
- **Lighting:** soft side light to rake across texture (crumb, glaze, sugar crystals), warm and gentle

```text
Scene: [dessert] on a small dessert plate, neutral soft background, a few echoing garnishes (berries, cocoa beans) scattered close. Subject: [dessert named with indulgent detail, e.g. a molten chocolate cake, a thin meandering caramel drizzle catching the light, a dusting of cocoa just sieved on, a scoop of vanilla starting to soften]. Camera: shot on a 100mm macro at f/2.8 feel, 35-degree angle, tight crop, shallow depth of field. Light: soft side light from camera-left raking across the surface to bring out crumb and glossy glaze, gentle warm tone, a bounce card lifting the shadows. Finish: warm natural color, glossy specular highlights on the drizzle, fresh-dusted powder, real-photograph dessert look, no thick puddles.
```


### Street food / documentary
- **When:** Night markets, food trucks, hawker stalls, hands-and-action shots — energy and place matter as much as the food.
- **Camera:** 35mm or 50mm documentary feel, f/2.0 feel, eye-level or slightly low, shallow depth blurring the busy background
- **Lighting:** available light — golden-hour warmth or mixed night-market neon/tungsten, motion and atmosphere kept

```text
Scene: a busy [night market / street stall] at [golden hour / after dark], the chaotic background of stalls and string lights blurred into soft bokeh. Subject: [street dish in action, e.g. skewers of charring satay over open coals, smoke rising, a hand turning them, glistening marinade]. Camera: 35mm documentary feel, f/2.0 feel, eye-level and slightly low, shallow depth of field isolating the food against the impressionistic background. Light: available light only — warm golden-hour glow / mixed neon and tungsten of the market, real flame highlights, drifting smoke. Finish: warm natural color, faint handheld energy, real-photograph documentary look, mild grain, true-to-life mixed white balance, candid not staged.
```


## Banned words (trigger the AI/uncanny look)

`8k` `4k` `masterpiece` `hyper-detailed` `ultra-detailed` `studio lighting` `professional lighting` `award-winning` `stunning` `gorgeous` `mouth-watering` `delicious` `vibrant` `vivid colors` `highly detailed` `cinematic` `HDR` `trending on artstudio` `perfect` `flawless` `glossy CGI render` `oversaturated` `insane detail` `epic` `beautiful`
