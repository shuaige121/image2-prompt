// img2-counter — shared cross-device image-gen counter + cooldown gate.
// Endpoints (all require Bearer AUTH_TOKEN):
//   POST /report {device,date,count}   absolute daily count per device (idempotent)
//   GET  /day?date=YYYY-MM-DD          sum across devices
//   GET  /week?end=YYYY-MM-DD          last 7 days
//   GET  /check                        read-only: is it safe to generate now?
//   POST /gen {device?}                record ONE generation event, return fresh status
// Cooldown model (matches gpt-image-2 / Codex empirical anti-abuse throttle):
//   if >= THRESHOLD gens in the last WINDOW minutes  -> locked for COOLDOWN minutes.
export default {
  async fetch(req, env) {
    const auth = req.headers.get("authorization") || "";
    if (auth !== `Bearer ${env.AUTH_TOKEN}`) return new Response("unauthorized", { status: 401 });
    const url = new URL(req.url);

    const THRESH = parseInt(env.COOLDOWN_THRESHOLD || "12", 10);
    const WINDOW_MS = parseInt(env.COOLDOWN_WINDOW_MIN || "40", 10) * 60000;
    const COOLDOWN_MS = parseInt(env.COOLDOWN_MIN || "45", 10) * 60000;

    const getRecent = async () => {
      const raw = await env.KV.get("gen:recent");
      const cutoff = Date.now() - 3600000; // keep last hour
      return (raw ? JSON.parse(raw) : []).filter((t) => t >= cutoff);
    };
    const status = async () => {
      const now = Date.now();
      const arr = await getRecent();
      const inWin = arr.filter((t) => t >= now - WINDOW_MS).length;
      const storedUntil = parseInt((await env.KV.get("cooldown:until")) || "0", 10);
      const hitThresh = inWin >= THRESH;
      const cdUntil = hitThresh ? Math.max(storedUntil, now + COOLDOWN_MS) : storedUntil;
      const inCooldown = now < cdUntil;
      return {
        safe: !inCooldown,
        in_cooldown: inCooldown,
        cooldown_until: cdUntil,
        cooldown_until_iso: cdUntil ? new Date(cdUntil).toISOString() : null,
        cooldown_remaining_sec: Math.max(0, Math.ceil((cdUntil - now) / 1000)),
        recent_in_window: inWin,
        window_min: WINDOW_MS / 60000,
        threshold: THRESH,
        suggest_wait_sec: inCooldown ? Math.max(0, Math.ceil((cdUntil - now) / 1000)) : 0,
        now,
      };
    };

    // POST /gen — record an event then return status
    if (req.method === "POST" && url.pathname === "/gen") {
      const arr = await getRecent();
      arr.push(Date.now());
      await env.KV.put("gen:recent", JSON.stringify(arr), { expirationTtl: 7200 });
      const st = await status();
      if (st.in_cooldown) await env.KV.put("cooldown:until", String(st.cooldown_until), { expirationTtl: 7200 });
      return Response.json(st);
    }
    // GET /check — read-only gate
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
      let date = url.searchParams.get("date") || new Date(Date.now() + 8 * 3600 * 1000).toISOString().slice(0, 10);
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
