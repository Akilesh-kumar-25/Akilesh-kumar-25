#!/usr/bin/env python3
"""Generate an animated GitHub-streak SVG (squares light up one by one).
Works standalone; designed to run in a GitHub Action daily to stay live.
Usage: python generate_streak_svg.py [username] [output.svg]
"""
import sys, json, os, datetime, urllib.request

USER = sys.argv[1] if len(sys.argv) > 1 else "Akilesh-kumar-25"
OUT  = sys.argv[2] if len(sys.argv) > 2 else "streak.svg"

def get_data(user):
    # First, try to use the locally scraped real contributions data from GitHub
    for p in [
        os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "data", "contributions.json"),
        "data/contributions.json",
    ]:
        if os.path.exists(p):
            try:
                with open(p, "r", encoding="utf-8") as f:
                    local_data = json.load(f)
                return {
                    "total": {"lastYear": local_data.get("total_contributions", 0)},
                    "contributions": local_data.get("days", []),
                }
            except Exception as e:
                print(f"Failed reading local contributions ({e}); trying API...")

    url = f"https://github-contributions-api.jogruber.de/v4/{user}?y=last"
    try:
        with urllib.request.urlopen(url, timeout=25) as r:
            return json.loads(r.read().decode())
    except Exception as e:
        # fallback to a local snapshot if the API is unreachable
        here = os.path.join(os.path.dirname(os.path.abspath(__file__)), "contrib.json")
        if os.path.exists(here):
            print("API failed (%s); using local contrib.json" % e)
            return json.load(open(here))
        raise

data = get_data(USER)
contribs = data["contributions"]
total = data["total"]["lastYear"]

# ---- layout ----
CELL, GAP, RAD, LEFT, TOP = 13, 3, 2.5, 34, 24
COLORS = ["#161b22", "#0e4429", "#006d32", "#26a641", "#39d353"]
FLASH = "#b4ffaa"
GRAY = "#7d8590"
MONTHS = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]

n = len(contribs)
sd = datetime.date.fromisoformat(contribs[0]["date"])
start_sunday = sd - datetime.timedelta(days=(sd.weekday() + 1) % 7)
ed = datetime.date.fromisoformat(contribs[-1]["date"])
NW = (ed - start_sunday).days // 7 + 1
W = LEFT + NW*(CELL+GAP) + 6
H = TOP + 7*(CELL+GAP) + 22

# timing (seconds)
REVEAL, DUR = 3.6, 0.55
maxorder = (NW-1) + 6*0.55

rects, labels = [], []
last_m = None
for wk in range(NW):
    d = start_sunday + datetime.timedelta(days=wk*7)
    if d.month != last_m:
        last_m = d.month
        labels.append(f'<text class="lbl" x="{LEFT+wk*(CELL+GAP)}" y="{TOP-8}">{MONTHS[d.month-1]}</text>')
for name, r in [("Mon",1),("Wed",3),("Fri",5)]:
    labels.append(f'<text class="lbl" x="2" y="{TOP+r*(CELL+GAP)+CELL-2}">{name}</text>')

for i, c in enumerate(contribs):
    d = datetime.date.fromisoformat(c["date"])
    wk = (d - start_sunday).days // 7
    row = (d.weekday() + 1) % 7
    lvl = c.get("level", 0 if c.get("count", 0) == 0 else min(4, max(1, (c.get("count", 0) + 2) // 5)))
    x = LEFT + wk*(CELL+GAP); y = TOP + row*(CELL+GAP)
    delay = round((wk + row*0.55)/maxorder * REVEAL, 3)
    cls = "c g" if lvl >= 1 else "c e"
    rects.append(
        f'<rect class="{cls}" x="{x}" y="{y}" width="{CELL}" height="{CELL}" rx="{RAD}" '
        f'fill="{COLORS[lvl]}" style="animation-delay:{delay}s">'
        f'<title>{c.get("count", 0)} contributions on {c["date"]}</title></rect>'
    )

svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" font-family="-apple-system,Segoe UI,Helvetica,Arial,sans-serif">
<style>
  text.lbl {{ fill:{GRAY}; font-size:13px; font-weight:600; }}
  text.total {{ fill:#e6edf3; font-size:15px; font-weight:700; }}
  .c {{ transform-box:fill-box; transform-origin:center; opacity:0; animation:pop {DUR}s ease-out both; }}
  .g {{ animation:pop {DUR}s ease-out both, flash {DUR+0.15}s ease-out both; }}
  @keyframes pop {{ 0%{{opacity:0;transform:scale(.2)}} 60%{{opacity:1;transform:scale(1.1)}} 100%{{opacity:1;transform:scale(1)}} }}
  @keyframes flash {{ 0%{{filter:brightness(2.4)}} 45%{{filter:brightness(2.4)}} 100%{{filter:brightness(1)}} }}
  @media (prefers-reduced-motion: reduce) {{ .c {{ opacity:1 !important; animation:none !important; }} }}
</style>
<rect width="{W}" height="{H}" fill="none"/>
{''.join(labels)}
{''.join(rects)}
<text class="total" x="{LEFT}" y="{H-6}">{total:,} contributions in the last year</text>
</svg>'''

open(OUT, "w").write(svg)
print(f"Wrote {OUT}: {n} days, {total:,} contributions, {len(svg)//1024} KB")
