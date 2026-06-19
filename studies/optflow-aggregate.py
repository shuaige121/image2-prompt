#!/usr/bin/env python3
# Aggregate optflow A/B blind scores -> OPT vs naive baselines.
import json, sys
from collections import defaultdict
KEY = json.load(open("/tmp/optflow/blind/key.json"))
RAW = json.load(open(sys.argv[1]))
def find_results(o):
    if isinstance(o, list) and o and isinstance(o[0], dict) and "scores" in o[0]: return o
    if isinstance(o, dict):
        for k in ("result", "results", "raters"):
            if k in o:
                r = find_results(o[k])
                if r: return r
        for v in o.values():
            r = find_results(v)
            if r: return r
    return None
res = find_results(RAW); assert res, "no rater sheets"
DIMS = ["realism","depth","light","emotion","technical","overall"]
ARMS = ["n1","n2","opt"]; LAB = {"n1":"N1 裸写","n2":"N2 垃圾词","opt":"OPT 优化"}
raw = defaultdict(lambda: defaultdict(list))
dopt_n1 = defaultdict(list); dopt_n2 = defaultdict(list)
subj_overall = defaultdict(lambda: defaultdict(list))
n_sheets = 0; opt_wins = 0; opt_total = 0
for sheet in res:
    g = sheet["group"]; n_sheets += 1
    byL = {str(s["id"]).strip().upper()[:1]: s for s in sheet["scores"]}
    arm_scores = defaultdict(list)
    for kk, tag in KEY.items():
        grp, L = kk.split("/")
        if grp != g: continue
        s = byL.get(L)
        if s: arm_scores[tag.split("_")[0]].append(s)
    for arm, lst in arm_scores.items():
        for s in lst:
            for d in DIMS:
                if isinstance(s.get(d), (int, float)):
                    raw[arm][d].append(s[d])
                    if d == "overall": subj_overall[g][arm].append(s[d])
    def m(arm, d):
        v = [s[d] for s in arm_scores.get(arm, []) if isinstance(s.get(d), (int, float))]
        return sum(v)/len(v) if v else None
    for d in DIMS:
        mo, m1, m2 = m("opt", d), m("n1", d), m("n2", d)
        if mo is not None and m1 is not None: dopt_n1[d].append(mo - m1)
        if mo is not None and m2 is not None: dopt_n2[d].append(mo - m2)
    mo, m1, m2 = m("opt","overall"), m("n1","overall"), m("n2","overall")
    if None not in (mo, m1, m2):
        opt_total += 1
        if mo >= max(m1, m2): opt_wins += 1
mean = lambda xs: sum(xs)/len(xs) if xs else float("nan")
print(f"rater sheets: {n_sheets}\n")
print("=== ABSOLUTE mean ===")
print(f"{'arm':11}" + "".join(f"{d[:5]:>7}" for d in DIMS))
for a in ARMS: print(f"{LAB[a]:11}" + "".join(f"{mean(raw[a][d]):7.2f}" for d in DIMS))
print("\n=== OPT − N1 (vs 裸写) ===")
print(f"{'Δ':11}" + "".join(f"{mean(dopt_n1[d]):+7.2f}" for d in DIMS))
print("=== OPT − N2 (vs 垃圾词) ===")
print(f"{'Δ':11}" + "".join(f"{mean(dopt_n2[d]):+7.2f}" for d in DIMS))
print(f"\n=== per-subject OPT overall vs best baseline ===")
for g in sorted(subj_overall):
    o, n1, n2 = mean(subj_overall[g]["opt"]), mean(subj_overall[g]["n1"]), mean(subj_overall[g]["n2"])
    print(f"  {g}: OPT {o:.2f} | N1 {n1:.2f} | N2 {n2:.2f} | OPT−best {o-max(n1,n2):+.2f}")
print(f"\nOPT >= both baselines in {opt_wins}/{opt_total} rater-group cells")
