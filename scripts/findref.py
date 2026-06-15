#!/usr/bin/env python3
"""findref — headless reference-image fetcher for img2img workflows. stdlib only.

Searches the web for photos matching a query (e.g. a competitor's dish) and
downloads the top N as local files to pass to image2.py --ref.

Tiers (live-verified 2026-06-12):
  1. DuckDuckGo i.js JSON endpoint (vqd handshake) — keyless, CJK-capable,
     returns full-res URLs with dimensions.
  2. Bing images murl scrape — fallback when DDG yields too few; keep the URL
     minimal (extra params make Bing serve cached unrelated junk to bots).
Skipped on purpose: delivery platforms (dianping/UberEats/Meituan) are
login/location-walled AND ToS-prohibited; the same photos surface via DDG/Bing.

Hygiene built in: magic-byte validation (dead links return HTML), watermarked
stock-domain blocklist (poisons style AND highest legal risk), min-width filter.

Legal note: refs are private style references, never republished. The real
copyright risk is OUTPUT similarity — so generate with a "borrow style, do not
copy the dish/scene" prompt (image2.py --ref-mode style does this) and prefer
2-3 mixed refs over 1.

Usage:
  findref.py "卤肉饭 braised pork rice bowl delivery app photo" --n 3 --out ./refs
"""
import argparse
import html as html_mod
import json
import pathlib
import re
import sys
import urllib.parse
import urllib.request

UA = ("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/124.0 Safari/537.36")
# watermarked stock previews: bad style references + highest-risk category
BLOCK = re.compile(r"shutterstock|dreamstime|alamy|istockphoto|gettyimages|123rf|depositphotos")
MAGIC = {b"\xff\xd8\xff": ".jpg", b"\x89PNG\r\n\x1a\n": ".png", b"RIFF": ".webp"}


def get(url: str, referer: str | None = None, timeout: int = 20) -> bytes:
    req = urllib.request.Request(url, headers={"User-Agent": UA,
                                               **({"Referer": referer} if referer else {})})
    return urllib.request.urlopen(req, timeout=timeout).read()


def ddg_results(query: str) -> list[dict]:
    q = urllib.parse.quote(query)
    page = get(f"https://duckduckgo.com/?q={q}&iax=images&ia=images").decode("utf-8", "ignore")
    m = re.search(r'vqd="([\d-]+)"', page)
    if not m:
        return []
    data = json.loads(get(f"https://duckduckgo.com/i.js?l=us-en&o=json&q={q}&vqd={m.group(1)}",
                          referer="https://duckduckgo.com/"))
    return [{"url": r["image"], "w": r.get("width", 0), "h": r.get("height", 0)}
            for r in data.get("results", [])]


def bing_results(query: str) -> list[dict]:
    q = urllib.parse.quote(query)
    # minimal URL on purpose — extra params trigger Bing's junk cache for bots
    page = get(f"https://www.bing.com/images/search?q={q}").decode("utf-8", "ignore")
    urls = [html_mod.unescape(u) for u in re.findall(r"murl&quot;:&quot;(.*?)&quot;", page)]
    return [{"url": u, "w": 0, "h": 0} for u in urls]


def sniff_ext(blob: bytes) -> str | None:
    for magic, ext in MAGIC.items():
        if blob[:len(magic)] == magic:
            return ext
    return None


def main() -> None:
    ap = argparse.ArgumentParser(description="Download reference images for image2.py --ref")
    ap.add_argument("query", help='e.g. "卤肉饭 braised pork rice bowl delivery app photo"')
    ap.add_argument("--n", type=int, default=3, help="images to save (default 3)")
    ap.add_argument("--out", default="./refs", help="output dir (default ./refs)")
    ap.add_argument("--min-width", type=int, default=600,
                    help="skip results narrower than this when dimensions are known (default 600)")
    ap.add_argument("--prefix", default="ref", help="output filename prefix")
    args = ap.parse_args()

    outdir = pathlib.Path(args.out)
    outdir.mkdir(parents=True, exist_ok=True)

    candidates: list[dict] = []
    try:
        candidates += ddg_results(args.query)
        print(f"ddg: {len(candidates)} candidates", file=sys.stderr)
    except Exception as e:
        print(f"ddg failed: {e}", file=sys.stderr)
    if len(candidates) < args.n * 3:
        try:
            extra = bing_results(args.query)
            print(f"bing: +{len(extra)} candidates", file=sys.stderr)
            candidates += extra
        except Exception as e:
            print(f"bing failed: {e}", file=sys.stderr)

    saved: list[dict] = []
    seen: set[str] = set()
    for r in candidates:
        if len(saved) >= args.n:
            break
        url = r["url"]
        if url in seen or BLOCK.search(url):
            continue
        seen.add(url)
        if r["w"] and r["w"] < args.min_width:
            continue
        try:
            blob = get(url, referer="https://duckduckgo.com/")
        except Exception as e:
            print(f"  skip {url[:70]} ({e})", file=sys.stderr)
            continue
        ext = sniff_ext(blob)
        if not ext or len(blob) < 20_000:  # HTML error pages / thumbnails
            continue
        p = outdir / f"{args.prefix}{len(saved)+1}{ext}"
        p.write_bytes(blob)
        dim = f"{r['w']}x{r['h']}" if r["w"] else "?"
        print(f"  saved {p} ({len(blob)//1024}KB {dim}) <- {url[:80]}", file=sys.stderr)
        saved.append({"file": str(p.resolve()), "source_url": url, "width": r["w"], "height": r["h"]})

    print(json.dumps({"query": args.query, "saved": saved}, ensure_ascii=False, indent=2))
    sys.exit(0 if saved else 1)


if __name__ == "__main__":
    main()
