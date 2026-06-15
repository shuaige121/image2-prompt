// img2-counter — shared cross-device image-gen counter + cooldown gate.
// Endpoints (all require Bearer AUTH_TOKEN):
//   POST /gen {device?}              record ONE generation event, return fresh status
//   GET  /check                      read-only: is it safe to generate now?
//   POST /report {device,date,count} absolute daily count per device (idempotent)
//   GET  /day?date / GET /week
//
// Cooldown = pure SLIDING WINDOW: at most THRESH generations per WINDOW, shared
// across all devices. cooldown_until is anchored to the EVENT timestamps (not call
// time) so it counts down monotonically. Events live in ONE KV key (read-your-write
// = fast, accurate for the sequential case). Tune THRESH/WINDOW_MIN below.
const THRESH = 12;
const WINDOW_MIN = 45;
const WINDOW_MS = WINDOW_MIN * 60000;

export default {
  async fetch(req, env) {
    const auth = req.headers.get("authorization") || "";
    if (auth !== `Bearer ${env.AUTH_TOKEN}`) return new Response("unauthorized", { status: 401 });
    const url = new URL(req.url);

    const getRecent = async () => {
      const raw = await env.KV.get("gen:recent");
      const cutoff = Date.now() - WINDOW_MS - 600000; // keep window + 10min slack
      return (raw ? JSON.parse(raw) : []).filter((t) => t >= cutoff).sort((a, b) => a - b);
    };

    const status = async () => {
      const now = Date.now();
      const win = (await getRecent()).filter((t) => t >= now - WINDOW_MS);
      const n = win.length;
      const hit = n >= THRESH;
      // count drops below THRESH once win[n-THRESH] ages out of the window:
      const cdUntil = hit ? win[n - THRESH] + WINDOW_MS : 0;
      const inCooldown = now < cdUntil;
      return {
        safe: !inCooldown,
        in_cooldown: inCooldown,
        cooldown_until: inCooldown ? cdUntil : 0,
        cooldown_until_iso: inCooldown ? new Date(cdUntil).toISOString() : null,
        cooldown_remaining_sec: inCooldown ? Math.ceil((cdUntil - now) / 1000) : 0,
        recent_in_window: n,
        threshold: THRESH,
        window_min: WINDOW_MIN,
        now,
      };
    };

    if (req.method === "POST" && url.pathname === "/gen") {
      const arr = await getRecent();
      arr.push(Date.now());
      await env.KV.put("gen:recent", JSON.stringify(arr), { expirationTtl: 7200 });
      return Response.json(await status());
    }
    if (req.method === "GET" && url.pathname === "/check") return Response.json(await status());

    // ---- existing daily counter (unchanged) ----
    if (req.method === "POST" && url.pathname === "/report") {
      let body;
      try { body = await req.json(); } catch { return new Response("bad json", { status: 400 }); }
      const { device, date, count } = body || {};
      if (!device || !/^\d{4}-\d{2}-\d{2}$/.test(date || "") || typeof count !== "number") {
        return new Response("bad request", { status: 400 });
      }
      await env.KV.put(`c:${date}:${device}`, String(Math.max(0, Math.floor(count))), { expirationTtl: 60 * 60 * 24 * 40 });
      return Response.json({ ok: true, device, date, count });
    }
    if (req.method === "GET" && url.pathname === "/day") {
      const date = url.searchParams.get("date") || new Date(Date.now() + 8 * 3600 * 1000).toISOString().slice(0, 10);
      const list = await env.KV.list({ prefix: `c:${date}:` });
      const devices = {}; let total = 0;
      for (const k of list.keys) {
        const v = parseInt((await env.KV.get(k.name)) || "0", 10);
        devices[k.name.slice(`c:${date}:`.length)] = v; total += v;
      }
      return Response.json({ date, total, devices });
    }
    if (req.method === "GET" && url.pathname === "/week") {
      const end = url.searchParams.get("end") || new Date(Date.now() + 8 * 3600 * 1000).toISOString().slice(0, 10);
      const endMs = Date.parse(end + "T00:00:00Z");
      const days = {}; let total = 0;
      for (let i = 0; i < 7; i++) {
        const d = new Date(endMs - i * 86400 * 1000).toISOString().slice(0, 10);
        const list = await env.KV.list({ prefix: `c:${d}:` });
        let day = 0;
        for (const k of list.keys) day += parseInt((await env.KV.get(k.name)) || "0", 10);
        if (day > 0) days[d] = day; total += day;
      }
      return Response.json({ end, total, days });
    }

    return new Response("not found", { status: 404 });
  },
};
