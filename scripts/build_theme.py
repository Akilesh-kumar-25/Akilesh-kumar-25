import os

def build_header(filename, text):
    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" width="400" height="70">
  <text x="200" y="45" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif" font-size="16" font-weight="300" fill="#e6e6e6" text-anchor="middle" letter-spacing="8">{text.upper()}</text>
  <line x1="160" y1="58" x2="240" y2="58" stroke="#333333" stroke-width="1"/>
</svg>"""
    with open(filename, "w", encoding="utf-8") as f:
        f.write(svg)

def build_connect(filename, text):
    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" width="170" height="60">
  <defs>
    <linearGradient id="luxury" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#1f2023" />
      <stop offset="100%" stop-color="#0d0e11" />
    </linearGradient>
    <filter id="softGlow">
      <feGaussianBlur stdDeviation="3" result="blur" />
      <feComponentTransfer in="blur" result="glow">
        <feFuncA type="linear" slope="0.3" />
      </feComponentTransfer>
      <feMerge>
        <feMergeNode in="glow" />
        <feMergeNode in="SourceGraphic" />
      </feMerge>
    </filter>
  </defs>
  <style>
    .btn {{ fill: url(#luxury); stroke: #333333; stroke-width: 1px; transition: all 0.4s ease; cursor: pointer; }}
    .txt {{ font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; font-size: 12px; font-weight: 400; fill: #8b949e; text-anchor: middle; pointer-events: none; transition: all 0.4s ease; letter-spacing: 2px; text-transform: uppercase; }}
    .group:hover .btn {{ stroke: #8b949e; filter: url(#softGlow); }}
    .group:hover .txt {{ fill: #ffffff; }}
  </style>
  <g class="group">
    <rect x="10" y="10" width="150" height="40" rx="20" class="btn" />
    <text x="85" y="34" class="txt">{text}</text>
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
build_connect("connect-portfolio.svg", "Portfolio")
build_connect("connect-linkedin.svg", "LinkedIn")
build_connect("connect-instagram.svg", "Instagram")
build_connect("connect-email.svg", "Email Me")

print("Luxury theme elements generated perfectly!")
