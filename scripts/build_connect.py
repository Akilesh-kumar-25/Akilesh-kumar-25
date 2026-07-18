import os

links = [
    {"name": "Portfolio", "file": "link-portfolio.svg", "color": "#58a6ff", "bg1": "#091b33"},
    {"name": "LinkedIn", "file": "link-linkedin.svg", "color": "#0A66C2", "bg1": "#031525"},
    {"name": "Instagram", "file": "link-instagram.svg", "color": "#E1306C", "bg1": "#2d0815"},
    {"name": "Email Me", "file": "link-email.svg", "color": "#39d353", "bg1": "#092411"}
]

for l in links:
    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" width="160" height="60" viewBox="0 0 160 60">
  <defs>
    <linearGradient id="grad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="{l['bg1']}" />
      <stop offset="100%" stop-color="#0d1117" />
    </linearGradient>
    <filter id="glow">
      <feGaussianBlur stdDeviation="3" result="coloredBlur"/>
      <feMerge>
        <feMergeNode in="coloredBlur"/>
        <feMergeNode in="SourceGraphic"/>
      </feMerge>
    </filter>
  </defs>
  <style>
    .pill {{
      fill: url(#grad);
      stroke: {l['color']};
      stroke-width: 1px;
      transition: all 0.3s ease;
      cursor: pointer;
    }}
    .container:hover .pill {{
      stroke-width: 2px;
      filter: drop-shadow(0 0 8px {l['color']});
    }}
    .text {{
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
      font-size: 15px;
      font-weight: 700;
      fill: #ffffff;
      text-anchor: middle;
      pointer-events: none;
      transition: all 0.3s ease;
      letter-spacing: 0.5px;
    }}
    .container:hover .text {{
      filter: url(#glow);
    }}
  </style>
  <g class="container">
    <rect x="10" y="10" width="140" height="40" rx="20" class="pill" />
    <text x="80" y="35" class="text">{l['name']}</text>
  </g>
</svg>"""
    with open(l['file'], "w", encoding="utf-8") as f:
        f.write(svg)

print("Connect links built successfully!")
