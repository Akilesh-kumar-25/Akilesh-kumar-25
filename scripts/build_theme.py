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
    .btn {{ fill: url(#luxury); stroke: #333333; stroke-width: 1.5px; transition: all 0.4s ease; cursor: pointer; }}
    .txt {{ font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; font-size: 11px; font-weight: 600; fill: #8b949e; pointer-events: none; transition: all 0.4s ease; letter-spacing: 2px; text-transform: uppercase; }}
    .icon {{ fill: {color}; stroke: none; transition: all 0.4s ease; pointer-events: none; }}
    .group:hover .btn {{ stroke: #8b949e; filter: url(#softGlow); }}
    .group:hover .txt {{ fill: #ffffff; }}
    .group:hover .icon {{ filter: url(#softGlow); }}
  </style>
  <g class="group">
    <rect x="5" y="10" width="150" height="40" rx="20" class="btn" />
    <svg x="16" y="20" width="20" height="20" viewBox="0 0 24 24">
      <g class="icon">
        {path_data}
      </g>
    </svg>
    <text x="50" y="34" class="txt">{text}</text>
  </g>
</svg>"""
    with open(filename, "w", encoding="utf-8") as f:
        f.write(svg)

path_portfolio = '<path d="M12 0C5.37 0 0 5.37 0 12s5.37 12 12 12 12-5.37 12-12S18.63 0 12 0zm0 2.4c3.34 0 6.27 1.74 7.96 4.37h-3.88c-.6-1.84-1.58-3.44-2.85-4.65C12.83 2.15 12.42 2.22 12 2.4zm-1.84.14c1.18 1.15 2.08 2.68 2.64 4.43H11.2V2.54zM9.8 2.54v4.43H6.84c.56-1.75 1.46-3.28 2.64-4.43h.32zM3.46 8.37h4.08c-.28 1.17-.44 2.4-.44 3.63s.16 2.46.44 3.63H3.46c-.46-1.12-.73-2.35-.73-3.63s.27-2.51.73-3.63zm1.18 8.86h3.88c.6 1.84 1.58 3.44 2.85 4.65-1.96-.28-3.7-.99-5.12-2.01-1.01-.84-1.86-1.87-2.51-3.03zm7.36 4.23c-1.18-1.15-2.08-2.68-2.64-4.43h2.96v4.43zm1.4 0v-4.43h2.96c-.56 1.75-1.46 3.28-2.64 4.43h-.32zm1.6-6.83H11.2V9.9h3.8c.27 1.16.42 2.38.42 3.63 0 1.25-.15 2.47-.42 3.63zm3.74-.9h-4.08c.28-1.17.44-2.4.44-3.63s-.16-2.46-.44-3.63h4.08c.46 1.12.73 2.35.73 3.63s-.27 2.51-.73 3.63z" />'
path_linkedin = '<path d="M20.447 20.452h-3.554v-5.569c0-1.328-.027-3.037-1.852-3.037-1.853 0-2.136 1.445-2.136 2.939v5.667H9.351V9h3.414v1.561h.046c.477-.9 1.637-1.85 3.37-1.85 3.601 0 4.267 2.37 4.267 5.455v6.286zM5.337 7.433c-1.144 0-2.063-.926-2.063-2.065 0-1.138.92-2.063 2.063-2.063 1.14 0 2.064.925 2.064 2.063 0 1.139-.925 2.065-2.064 2.065zm1.782 13.019H3.555V9h3.564v11.452zM22.225 0H1.771C.792 0 0 .774 0 1.729v20.542C0 23.227.792 24 1.771 24h20.451C23.2 24 24 23.227 24 22.271V1.729C24 .774 23.2 0 22.222 0h.003z" />'
path_instagram = '<path d="M12 2.163c3.204 0 3.584.012 4.85.07 3.252.148 4.771 1.691 4.919 4.919.058 1.265.069 1.645.069 4.849 0 3.205-.012 3.584-.069 4.849-.149 3.225-1.664 4.771-4.919 4.919-1.266.058-1.644.07-4.85.07-3.204 0-3.584-.012-4.849-.07-3.26-.149-4.771-1.699-4.919-4.92-.058-1.265-.07-1.644-.07-4.849 0-3.204.013-3.583.07-4.849.149-3.227 1.664-4.771 4.919-4.919 1.266-.057 1.645-.069 4.849-.069zm0-2.163c-3.259 0-3.667.014-4.947.072-4.358.2-6.78 2.618-6.98 6.98-.059 1.281-.073 1.689-.073 4.948 0 3.259.014 3.668.072 4.948.2 4.358 2.618 6.78 6.98 6.98 1.281.058 1.689.072 4.948.072 3.259 0 3.668-.014 4.948-.072 4.354-.2 6.782-2.618 6.979-6.98.059-1.28.073-1.689.073-4.948 0-3.259-.014-3.667-.072-4.947-.196-4.354-2.617-6.78-6.979-6.98-1.281-.059-1.69-.073-4.949-.073zm0 5.838c-3.403 0-6.162 2.759-6.162 6.162s2.759 6.163 6.162 6.163 6.162-2.759 6.162-6.163c0-3.403-2.759-6.162-6.162-6.162zm0 10.162c-2.209 0-4-1.79-4-4 0-2.209 1.791-4 4-4s4 1.791 4 4c0 2.21-1.791 4-4 4zm6.406-11.845c-.796 0-1.441.645-1.441 1.44s.645 1.44 1.441 1.44c.795 0 1.439-.645 1.439-1.44s-.644-1.44-1.439-1.44z" />'
path_email = '<path d="M24 5.457v13.909c0 .904-.732 1.636-1.636 1.636h-3.819V11.73L12 16.64l-6.545-4.91v9.273H1.636A1.636 1.636 0 0 1 0 19.366V5.457c0-2.023 2.309-3.178 3.927-1.964L5.455 4.64 12 9.548l6.545-4.91 1.528-1.145C21.69 2.28 24 3.434 24 5.457z" />'

build_connect("connect-portfolio.svg", "Portfolio", path_portfolio, "#58a6ff") # GitHub Blue
build_connect("connect-linkedin.svg", "LinkedIn", path_linkedin, "#0a66c2") # LinkedIn Blue
build_connect("connect-instagram.svg", "Instagram", path_instagram, "#e1306c") # Instagram Pink
build_connect("connect-email.svg", "Email Me", path_email, "#39D353") # GitHub Green

print("Solid colored Connect elements generated perfectly!")
