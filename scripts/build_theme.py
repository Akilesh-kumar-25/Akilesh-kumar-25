import os

def build_header(filename, text):
    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" width="400" height="60">
  <defs>
    <filter id="neon">
      <feGaussianBlur stdDeviation="3" result="blur" />
      <feMerge>
        <feMergeNode in="blur" />
        <feMergeNode in="SourceGraphic" />
      </feMerge>
    </filter>
  </defs>
  <text x="200" y="40" font-family="'Courier New', Consolas, monospace" font-size="24" font-weight="bold" fill="#39D353" text-anchor="middle" filter="url(#neon)" letter-spacing="4">&lt; {text} /&gt;</text>
</svg>"""
    with open(filename, "w", encoding="utf-8") as f:
        f.write(svg)

def build_connect(filename, text, color):
    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" width="180" height="60">
  <defs>
    <filter id="glow">
      <feGaussianBlur stdDeviation="2" result="blur" />
      <feMerge>
        <feMergeNode in="blur" />
        <feMergeNode in="SourceGraphic" />
      </feMerge>
    </filter>
  </defs>
  <style>
    .btn {{ fill: transparent; stroke: {color}; stroke-width: 2; transition: all 0.3s ease; cursor: pointer; }}
    .txt {{ font-family: 'Courier New', Consolas, monospace; font-size: 16px; font-weight: bold; fill: {color}; text-anchor: middle; pointer-events: none; transition: all 0.3s ease; }}
    .group:hover .btn {{ fill: {color}; filter: url(#glow); }}
    .group:hover .txt {{ fill: #0d1117; }}
  </style>
  <g class="group">
    <rect x="5" y="10" width="170" height="40" rx="4" class="btn" />
    <text x="90" y="35" class="txt">[ {text} ]</text>
  </g>
</svg>"""
    with open(filename, "w", encoding="utf-8") as f:
        f.write(svg)

# Headers
build_header("header-languages.svg", "Languages")
build_header("header-frameworks.svg", "Frameworks")
build_header("header-databases.svg", "Databases")
build_header("header-tools.svg", "Tools")

# Connect
# unified theme: #39D353 (GitHub neon green)
build_connect("connect-portfolio.svg", "Portfolio", "#39D353")
build_connect("connect-linkedin.svg", "LinkedIn", "#39D353")
build_connect("connect-instagram.svg", "Instagram", "#39D353")
build_connect("connect-email.svg", "Email", "#39D353")

print("Theme elements generated perfectly!")
