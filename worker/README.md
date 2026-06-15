# img2-counter Worker — shared counter + cooldown gate

A tiny Cloudflare Worker (+ KV) that tracks image-generation counts across devices **and** a shared cooldown window, so any device/agent can check *before* generating whether the account is about to hit the gpt-image-2 / Codex silent throttle.

## Endpoints (all require `Authorization: Bearer <AUTH_TOKEN>`)

- `GET  /check` — read-only gate: `{safe, in_cooldown, recent_in_window, threshold, window_min, cooldown_remaining_sec, cooldown_until_iso}`
- `POST /gen {device}` — record one generation event; returns the gate status
- `POST /report {device,date,count}` — absolute daily count per device (idempotent, race-free)
- `GET  /day?date=YYYY-MM-DD` — sum across devices
- `GET  /week?end=YYYY-MM-DD` — last 7 days

## Cooldown model

≥ `COOLDOWN_THRESHOLD` (default **12**) generations in any `COOLDOWN_WINDOW_MIN` (**40**)-minute window → locked for `COOLDOWN_MIN` (**45**) minutes, **shared across all devices**. Tune via the Worker `vars`. This mirrors the empirical gpt-image-2/Codex anti-abuse throttle so you stop *before* the server silently refuses.

## Deploy your own

```bash
wrangler kv namespace create IMG2_COUNTER        # 1. make a KV namespace, copy the id
cp wrangler.toml.example wrangler.toml           # 2. paste the id into kv_namespaces.id
wrangler secret put AUTH_TOKEN                    # 3. set the shared bearer token
wrangler deploy                                   # 4. ship
```

Then on each device write `$CODEX_HOME/image2-counter.json` (never commit it):

```json
{"endpoint":"https://<your-worker>.workers.dev","token":"<AUTH_TOKEN>","device":"mac"}
```

`scripts/image2.py` then auto-records `/gen` after each image, warns at batch start if a shared cooldown is active, and shows the gate in `--usage`. The free Workers tier is plenty — counter/cooldown traffic is tiny.
