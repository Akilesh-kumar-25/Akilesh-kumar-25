import os

def build_connect(filename, text, path_data, color):
    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" width="160" height="60">
  <defs>
    <linearGradient id="luxury" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#1f2023" />
      <stop offset="100%" stop-color="#0d0e11" />
    </linearGradient>
    <filter id="softGlow">
      <feGaussianBlur stdDeviation="3" result="blur" />
      <feComponentTransfer in="blur" result="glow">
        <feFuncA type="linear" slope="0.4" />
      </feComponentTransfer>
      <feMerge>
        <feMergeNode in="glow" />
        <feMergeNode in="SourceGraphic" />
      </feMerge>
    </filter>
  </defs>
  <style>
    .btn {{ fill: url(#luxury); stroke: {color}; stroke-width: 1.5px; transition: all 0.4s ease; cursor: pointer; }}
    .txt {{ font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; font-size: 11px; font-weight: 600; fill: {color}; pointer-events: none; transition: all 0.4s ease; letter-spacing: 2px; text-transform: uppercase; }}
    .icon {{ stroke: {color}; fill: none; stroke-width: 2; stroke-linecap: round; stroke-linejoin: round; transition: all 0.4s ease; pointer-events: none; }}
    .group:hover .btn {{ stroke: {color}; filter: url(#softGlow); fill: {color}; fill-opacity: 0.1; }}
    .group:hover .txt {{ fill: #ffffff; }}
    .group:hover .icon {{ stroke: #ffffff; }}
  </style>
  <g class="group">
    <rect x="5" y="10" width="150" height="40" rx="20" class="btn" />
    <svg x="20" y="20" width="20" height="20" viewBox="0 0 24 24">
      <g class="icon">
        {path_data}
      </g>
    </svg>
    <text x="50" y="34" class="txt">{text}</text>
  </g>
</svg>"""
    with open(filename, "w", encoding="utf-8") as f:
        f.write(svg)

path_portfolio = '<circle cx="12" cy="12" r="10"></circle><line x1="2" y1="12" x2="22" y2="12"></line><path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"></path>'
path_linkedin = '<path d="M16 8a6 6 0 0 1 6 6v7h-4v-7a2 2 0 0 0-2-2 2 2 0 0 0-2 2v7h-4v-7a6 6 0 0 1 6-6z"></path><rect x="2" y="9" width="4" height="12"></rect><circle cx="4" cy="4" r="2"></circle>'
path_instagram = '<rect x="2" y="2" width="20" height="20" rx="5" ry="5"></rect><path d="M16 11.37A4 4 0 1 1 12.63 8 4 4 0 0 1 16 11.37z"></path><line x1="17.5" y1="6.5" x2="17.51" y2="6.5"></line>'
path_email = '<path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"></path><polyline points="22,6 12,13 2,6"></polyline>'

build_connect("connect-portfolio.svg", "Portfolio", path_portfolio, "#58a6ff") # GitHub Blue
build_connect("connect-linkedin.svg", "LinkedIn", path_linkedin, "#0077b5") # LinkedIn Blue
build_connect("connect-instagram.svg", "Instagram", path_instagram, "#e1306c") # Instagram Pink
build_connect("connect-email.svg", "Email Me", path_email, "#39D353") # GitHub Green

print("Colored Connect elements generated perfectly!")
