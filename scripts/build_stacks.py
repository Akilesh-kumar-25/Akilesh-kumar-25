import urllib.request
import re

categories = [
    {"name": "Languages", "file": "stack-languages.svg", "icons": "java,python,c,js,html,css", "perline": 4},
    {"name": "Frameworks", "file": "stack-frameworks.svg", "icons": "react,nextjs,nodejs,spring", "perline": 3},
    {"name": "Databases", "file": "stack-databases.svg", "icons": "mysql,mongodb,aws", "perline": 3},
    {"name": "Tools", "file": "stack-tools.svg", "icons": "github,figma,vscode,ps", "perline": 3}
]

for cat in categories:
    url = f"https://skillicons.dev/icons?i={cat['icons']}&perline={cat['perline']}&theme=dark"
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    try:
        with urllib.request.urlopen(req) as response:
            svg_data = response.read().decode('utf-8')
            
            # Remove XML declaration and whitespace
            svg_data = re.sub(r'<\?xml.*?\?>', '', svg_data).strip()
            
            # Match the outer SVG tag only
            width_match = re.search(r'^<svg[^>]*?width="([\d.]+)"', svg_data)
            height_match = re.search(r'^<svg[^>]*?height="([\d.]+)"', svg_data)
            
            if width_match and height_match:
                icon_w = float(width_match.group(1))
                icon_h = float(height_match.group(1))
            else:
                icon_w = 200
                icon_h = 100
                
            canvas_w = 400
            canvas_h = 220
            
            offset_x = (canvas_w - icon_w) / 2
            offset_y = 70
            
            master_svg = f"""<svg xmlns="http://www.w3.org/2000/svg" width="{canvas_w}" height="{canvas_h}">
  <text x="{canvas_w//2}" y="40" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif" font-size="14" font-weight="400" fill="#e6e6e6" text-anchor="middle" letter-spacing="8">{cat['name'].upper()}</text>
  <line x1="{canvas_w//2 - 40}" y1="52" x2="{canvas_w//2 + 40}" y2="52" stroke="#333333" stroke-width="1"/>
  <g transform="translate({offset_x}, {offset_y})">
    {svg_data}
  </g>
</svg>"""
            
            with open(cat['file'], 'w', encoding='utf-8') as f:
                f.write(master_svg)
            print(f"Generated {cat['file']} with width {icon_w}")
    except Exception as e:
        print(f"Failed {cat['name']}: {e}")
