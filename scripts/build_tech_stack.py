import urllib.request
import json
import re

categories = [
    {"name": "Languages", "icons": "java,python,c,js,php,html,css", "y": 40},
    {"name": "Frameworks & Backend", "icons": "react,nextjs,nodejs,spring", "y": 140},
    {"name": "Databases & Cloud", "icons": "mysql,mongodb,aws", "y": 240},
    {"name": "Tools & Design", "icons": "github,figma,vscode,ps", "y": 340}
]

svg_out = """<svg xmlns="http://www.w3.org/2000/svg" width="860" height="460" viewBox="0 0 860 460">
  <defs>
    <filter id="glow">
      <feGaussianBlur stdDeviation="4" result="coloredBlur"/>
      <feMerge>
        <feMergeNode in="coloredBlur"/>
        <feMergeNode in="SourceGraphic"/>
      </feMerge>
    </filter>
    <style>
      .bg { fill: transparent; }
      .category-title {
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
        font-size: 16px;
        font-weight: 700;
        fill: #39d353;
        letter-spacing: 1px;
        text-transform: uppercase;
      }
      .panel {
        fill: rgba(255, 255, 255, 0.03);
        stroke: rgba(255, 255, 255, 0.1);
        stroke-width: 1px;
      }
    </style>
  </defs>
  <rect width="100%" height="100%" class="bg" />
"""

for cat in categories:
    svg_out += f'  <text x="30" y="{cat["y"]}" class="category-title" filter="url(#glow)">{cat["name"]}</text>\n'
    svg_out += f'  <rect x="30" y="{cat["y"] + 15}" width="800" height="70" rx="10" class="panel" />\n'
    
    # fetch icons
    url = f"https://skillicons.dev/icons?i={cat['icons']}&theme=dark"
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    try:
        with urllib.request.urlopen(req) as response:
            svg_data = response.read().decode('utf-8')
            
            # extract the raw svg tag and modify its x/y coordinates
            # Skillicons sets width/height on the <svg> element.
            # We want to place it inside our group.
            svg_data = svg_data.replace('<svg ', f'<svg x="45" y="{cat["y"] + 25}" height="50" ')
            # remove XML declaration if present
            svg_data = re.sub(r'<\?xml.*?\?>', '', svg_data)
            
            svg_out += "  " + svg_data + "\n"
    except Exception as e:
        print(f"Failed to fetch {cat['name']}: {e}")

svg_out += "</svg>"

with open("tech-stack.svg", "w", encoding="utf-8") as f:
    f.write(svg_out)
print("tech-stack.svg built successfully!")
