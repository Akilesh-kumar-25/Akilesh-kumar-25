import urllib.request
import re

categories = [
    {"name": "Languages", "icons": "java,python,c,js,html,css", "perline": 3, "x": 10, "y": 10, "w": 400, "h": 180},
    {"name": "Frameworks", "icons": "react,nextjs,nodejs,spring", "perline": 2, "x": 430, "y": 10, "w": 400, "h": 180},
    {"name": "Databases", "icons": "mysql,mongodb,aws", "perline": 3, "x": 10, "y": 210, "w": 400, "h": 180},
    {"name": "Tools", "icons": "github,figma,vscode,ps", "perline": 4, "x": 430, "y": 210, "w": 400, "h": 180}
]

svg_components = []

for cat in categories:
    url = f"https://skillicons.dev/icons?i={cat['icons']}&perline={cat['perline']}&theme=dark"
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    try:
        with urllib.request.urlopen(req) as response:
            svg_data = response.read().decode('utf-8')
            
            # Remove XML declaration
            svg_data = re.sub(r'<\?xml.*?\?>', '', svg_data).strip()
            
            # Extract outer width and height
            width_match = re.search(r'^<svg[^>]*?width="([\d.]+)"', svg_data)
            height_match = re.search(r'^<svg[^>]*?height="([\d.]+)"', svg_data)
            
            icon_w = float(width_match.group(1)) if width_match else 200
            icon_h = float(height_match.group(1)) if height_match else 100
            
            # Fix SVG collisions by appending category name to all IDs
            cat_id = cat['name'].lower()
            svg_data = re.sub(r'id="([^"]+)"', rf'id="\1_{cat_id}"', svg_data)
            svg_data = re.sub(r'url\(#([^)]+)\)', rf'url(#\1_{cat_id})', svg_data)
            
            # Calculate perfect center within the bento box
            # Box dimensions: w, h. Center is (w - icon_w)/2, (h - icon_h)/2
            offset_x = cat['x'] + (cat['w'] - icon_w) / 2
            offset_y = cat['y'] + (cat['h'] - icon_h) / 2 + 10 # +10 to leave room for the top-left title
            
            # Draw Bento Box Background
            box_svg = f"""
            <g>
                <rect x="{cat['x']}" y="{cat['y']}" width="{cat['w']}" height="{cat['h']}" rx="20" fill="#0d1117" stroke="#30363d" stroke-width="1.5"/>
                <text x="{cat['x'] + 25}" y="{cat['y'] + 35}" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif" font-size="12" font-weight="600" fill="#8b949e" letter-spacing="2">{cat['name'].upper()}</text>
                <g transform="translate({offset_x}, {offset_y})">
                    {svg_data}
                </g>
            </g>
            """
            svg_components.append(box_svg)
            print(f"Processed {cat['name']}")
    except Exception as e:
        print(f"Failed {cat['name']}: {e}")

master_svg = f"""<svg xmlns="http://www.w3.org/2000/svg" width="840" height="400">
    {''.join(svg_components)}
</svg>"""

with open("bento-tech-stack.svg", "w", encoding="utf-8") as f:
    f.write(master_svg)
print("Bento Tech Stack generated successfully!")
