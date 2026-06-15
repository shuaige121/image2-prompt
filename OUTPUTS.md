# Organizing finished images

A convention so generated images stay findable and a calling agent always knows where to put things. Mirrors the genre taxonomy.

## Directory layout

```
outputs/
  <genre>/                 # one of the 12 genres (food_beverage, portrait_people, ...)
    <project>/             # a shoot/subject/client, e.g. "poxiaoman-menu"
      <name>.png           # the rendered shot (with background)
      cutouts/
        <name>.png         # transparent-background subject (from cutout.swift)
      manifest.jsonl       # one line per image — provenance + tags
```

Keep `<genre>` identical to the recipe filename stem so outputs map 1:1 onto `recipes/<genre>.md`.

## Naming

`<subject>_<variant>_<YYYYMMDD>.png` — lowercase, hyphen/underscore, no spaces.
e.g. `balanced-set_v2_20260616.png`, `ceo-headshot_window-left_20260616.png`.

## Manifest (one JSON object per line)

Write a `manifest.jsonl` line every time you save an image — this is what makes a folder searchable and re-runnable:

```json
{"file":"balanced-set_v2_20260616.png","genre":"food_beverage","subcategory":"menu-catalog","subject":"Balanced Set combo","prompt":"<full prompt used>","refs":["01.png","05.png"],"model":"gpt-image-2","quality":"high","size":"1024x1024","cutout":"cutouts/balanced-set_v2_20260616.png","date":"2026-06-16"}
```

Minimum fields: `file, genre, prompt, date`. Add `refs, cutout, subcategory, subject` when present. A folder full of these lines is greppable ("find every food menu shot that used 01.png") and lets you regenerate any image from its own record.

## Generate → cutout → organize (the automation loop)

```bash
G=food_beverage; P=poxiaoman-menu; NAME=balanced-set_v2_20260616
DIR="outputs/$G/$P"; mkdir -p "$DIR/cutouts"

# 1. generate (fill a snippet from recipes/$G.md)
python3 scripts/image2.py "<snippet>" --ref 01.png --out-dir "$DIR" --quality high
mv "$DIR"/<generated>.png "$DIR/$NAME.png"

# 2. cut the subject onto transparent background (macOS 14+, Apple Vision)
swift scripts/cutout.swift "$DIR/$NAME.png" "$DIR/cutouts/$NAME.png"

# 3. record provenance
printf '%s\n' "$(jq -nc --arg f "$NAME.png" --arg g "$G" --arg p "<prompt>" --arg d 2026-06-16 \
  '{file:$f,genre:$g,prompt:$p,cutout:("cutouts/"+$f),date:$d}')" >> "$DIR/manifest.jsonl"
```

> Cutout is macOS-only (Vision framework). On Linux/CI, swap step 2 for [`rembg`](https://github.com/danielgatis/rembg) (see `RESOURCES.md`).

## Why transparent cutouts

A subject on transparent background composites into any scene, drops onto product/menu cards, and feeds img2img "place this exact subject into a new background" (with the anti-pasted-on clause from the genre's img2img notes). Generating *and* cutting out in one pass is what raises the automation rate — you get both the hero photo and a reusable asset.
