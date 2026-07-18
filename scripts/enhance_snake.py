import re

def enhance():
    with open('github-snake-dark.svg', 'r', encoding='utf-8') as f:
        svg = f.read()

    # 1. Add custom CSS
    custom_css = """
    @keyframes pop {
        0% { opacity: 0; transform: scale(0.2); }
        60% { opacity: 1; transform: scale(1.1); }
        100% { opacity: 1; transform: scale(1); }
    }
    """
    # delay snake animations
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

    # 3. Wrap snake rects and convert to glowing circles
    def repl_snake(match):
        full_match = match.group(0)
        # Convert rounded corners to make it a perfect circle (rx=7.2, ry=7.2 because width is 14.4)
        full_match = re.sub(r'rx="[^"]*"', 'rx="7.2"', full_match)
        full_match = re.sub(r'ry="[^"]*"', 'ry="7.2"', full_match)
        return f'<g style="opacity:0; animation: pop 0.1s ease-out forwards; animation-delay: 3.9s; transform-box: fill-box; transform-origin: center; filter: drop-shadow(0 0 5px rgba(255,255,255,0.8));">{full_match}</g>'

    svg = re.sub(r'<rect class="[su][^"]*"[^>]*>', repl_snake, svg)

    with open('github-snake-dark-enhanced.svg', 'w', encoding='utf-8') as f:
        f.write(svg)
    print("Regex replace successful.")

enhance()
