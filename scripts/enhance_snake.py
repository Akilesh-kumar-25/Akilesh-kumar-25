import re
import json

def enhance():
    # Get total contributions
    try:
        with open('data/contributions.json', 'r', encoding='utf-8') as f:
            data = json.load(f)
            total = data.get("total_contributions", 0)
    except:
        total = 0

    with open('github-snake-dark.svg', 'r', encoding='utf-8') as f:
        svg = f.read()

    # 1. Add custom CSS and text styles
    custom_css = """
    @keyframes pop {
        0% { opacity: 0; transform: scale(0.2); }
        60% { opacity: 1; transform: scale(1.1); }
        100% { opacity: 1; transform: scale(1); }
    }
    .total-text { fill: #ffffff; font-family: system-ui, -apple-system, sans-serif; font-size: 16px; font-weight: 600; animation: pop 0.5s ease-out forwards; animation-delay: 3s; opacity: 0; }
    """
    svg = svg.replace('.c{', '.c{animation-delay:4s !important;')
    svg = svg.replace('.s{', '.s{animation-delay:4s !important;')
    svg = svg.replace('.u{', '.u{animation-delay:4s !important;')
    svg = svg.replace('</style>', custom_css + '</style>')

    # 2. Wrap background rects
    def repl_bg(match):
        full_match = match.group(0)
        x_m = re.search(r'x="([\d.]+)"', full_match)
        y_m = re.search(r'y="([\d.]+)"', full_match)
        if x_m and y_m:
            x = float(x_m.group(1))
            y = float(y_m.group(1))
            wk = (x - 2) / 16
            row = (y - 2) / 16
            delay = round((wk + row*0.55)/55 * 3.6, 3)
            return f'<g style="opacity:0; animation: pop 0.5s ease-out forwards; animation-delay: {delay}s; transform-box: fill-box; transform-origin: center;">{full_match}</g>'
        return full_match

    svg = re.sub(r'<rect class="c[^"]*"[^>]*>', repl_bg, svg)

    # 3. Wrap snake body rects and make them glowing cyan orbs
    def repl_snake(match):
        full_match = match.group(0)
        # Convert to circle
        full_match = re.sub(r'rx="[^"]*"', 'rx="10"', full_match)
        full_match = re.sub(r'ry="[^"]*"', 'ry="10"', full_match)
        # Add massive neon glow and scale it up slightly
        return f'<g style="opacity:0; animation: pop 0.1s ease-out forwards; animation-delay: 3.9s; transform-box: fill-box; transform-origin: center; filter: drop-shadow(0 0 6px #00ffff) drop-shadow(0 0 12px #00ffff); transform: scale(1.4);">{full_match}</g>'

    svg = re.sub(r'<rect class="s[^"]*"[^>]*>', repl_snake, svg)

    # Wrap unvisited path (u) just to delay it, do not glow or scale
    def repl_unvisited(match):
        full_match = match.group(0)
        return f'<g style="opacity:0; animation: pop 0.1s ease-out forwards; animation-delay: 3.9s;">{full_match}</g>'

    svg = re.sub(r'<rect class="u[^"]*"[^>]*>', repl_unvisited, svg)

    # 4. Modify dimensions and add total text
    # Original SVG usually has height="192" or something similar. Let's add 80px to height.
    def repl_svg(match):
        h = float(match.group(1)) + 80
        return f'height="{h}"'
    svg = re.sub(r'height="([\d.]+)"', repl_svg, svg, count=1)
    
    def repl_viewbox(match):
        parts = match.group(1).split()
        parts[3] = str(float(parts[3]) + 80)
        return f'viewBox="{" ".join(parts)}"'
    svg = re.sub(r'viewBox="([^"]+)"', repl_viewbox, svg, count=1)
    
    # Append the text just before </svg>
    text_element = f'<text class="total-text" x="0" y="230">Overall Contributions: {total:,}</text>'
    svg = svg.replace('</svg>', f'{text_element}</svg>')

    # Write to enhanced so BOTH files exist, making the user happy
    with open('github-snake-dark-enhanced.svg', 'w', encoding='utf-8') as f:
        f.write(svg)
    print(f"Regex replace successful. Total contributions: {total}")

enhance()
