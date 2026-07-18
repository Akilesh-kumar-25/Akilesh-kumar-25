import re
import urllib.request

def fetch_all_time_total():
    total = 0
    # Fetch from year 2010 to 2027 to cover everything
    for year in range(2015, 2027):
        url = f"https://github.com/users/Akilesh-kumar-25/contributions?from={year}-01-01&to={year}-12-31"
        try:
            html = urllib.request.urlopen(url).read().decode('utf-8')
            m = re.search(r'(\d{1,3}(?:,\d{3})*)\s+contributions\s+in\s+' + str(year), html)
            if m:
                total += int(m.group(1).replace(',', ''))
        except:
            pass
    return total

def enhance():
    total = fetch_all_time_total()
    if total == 0:
        total = 221 # fallback

    with open('github-snake-dark.svg', 'r', encoding='utf-8') as f:
        svg = f.read()

    # 1. Add custom CSS and text styles
    custom_css = """
    @keyframes pop {
        0% { opacity: 0; transform: scale(0.2); }
        60% { opacity: 1; transform: scale(1.1); }
        100% { opacity: 1; transform: scale(1); }
    }
    .total-text { fill: #8b949e; font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif; font-size: 15px; font-weight: 500; letter-spacing: 0.5px; animation: pop 0.5s ease-out forwards; animation-delay: 3s; opacity: 0; }
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

    # 3. Wrap snake rects
    def repl_snake(match):
        full_match = match.group(0)
        # Convert to circle
        full_match = re.sub(r'rx="[^"]*"', 'rx="10"', full_match)
        full_match = re.sub(r'ry="[^"]*"', 'ry="10"', full_match)
        # Force the snake fill color to pure white so it isn't purple
        full_match = full_match.replace('<rect ', '<rect style="fill: #ffffff !important;" ')
        # Make the snake itself a bright solid glowing orb (using GitHub bright green glow)
        return f'<g style="opacity:0; animation: pop 0.1s ease-out forwards; animation-delay: 3.9s; transform-box: fill-box; transform-origin: center; filter: drop-shadow(0 0 6px #39d353) drop-shadow(0 0 12px #39d353); transform: scale(1.4);">{full_match}</g>'

    svg = re.sub(r'<rect class="s[^"]*"[^>]*>', repl_snake, svg)

    # Wrap unvisited path (u) and make it assemble left-to-right like a normal continuous bar
    def repl_unvisited(match):
        full_match = match.group(0)
        
        # Calculate staggering delay for the left-to-right fill effect
        x_m = re.search(r'x="([\d.]+)"', full_match)
        y_m = re.search(r'y="([\d.]+)"', full_match)
        delay = 3.9 # fallback delay
        if x_m and y_m:
            x = float(x_m.group(1))
            y = float(y_m.group(1))
            wk = (x - 2) / 16
            row = (y - 2) / 16
            delay = round(3.9 + (wk + row*0.55)/55 * 1.5, 3)
            
        return f'<g style="opacity:0; animation: pop 0.3s ease-out forwards; animation-delay: {delay}s; transform-box: fill-box; transform-origin: center;">{full_match}</g>'

    svg = re.sub(r'<rect class="u[^"]*"[^>]*>', repl_unvisited, svg)

    # 4. Modify dimensions and add total text
    def repl_svg(match):
        h = float(match.group(1)) + 60
        return f'height="{h}"'
    svg = re.sub(r'height="([\d.]+)"', repl_svg, svg, count=1)
    
    def repl_viewbox(match):
        parts = match.group(1).split()
        parts[3] = str(float(parts[3]) + 60)
        return f'viewBox="{" ".join(parts)}"'
    svg = re.sub(r'viewBox="([^"]+)"', repl_viewbox, svg, count=1)
    
    # Add text and force SVG background to dark mode
    text_element = f'<text class="total-text" x="0" y="210">Overall Contributions: {total:,}</text>'
    svg = svg.replace('</svg>', f'{text_element}</svg>')
    
    # Force dark background so it looks perfect on light mode too
    svg = svg.replace('<svg', '<svg style="background-color: #0d1117;"')

    with open('github-snake-dark-enhanced.svg', 'w', encoding='utf-8') as f:
        f.write(svg)
    print(f"Regex replace successful. All-Time Total contributions: {total}")

enhance()
