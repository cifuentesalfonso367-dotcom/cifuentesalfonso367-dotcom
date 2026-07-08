import urllib.request
import os
import random

icons = {
    "html": "https://skillicons.dev/icons?i=html",
    "css": "https://skillicons.dev/icons?i=css",
    "ts": "https://skillicons.dev/icons?i=ts",
    "next": "https://skillicons.dev/icons?i=next",
    "bootstrap": "https://skillicons.dev/icons?i=bootstrap",
    "py": "https://skillicons.dev/icons?i=py",
    "nodejs": "https://skillicons.dev/icons?i=nodejs",
    "postgres": "https://skillicons.dev/icons?i=postgres",
    "git": "https://skillicons.dev/icons?i=git",
    "react": "https://skillicons.dev/icons?i=react",
    "tailwind": "https://skillicons.dev/icons?i=tailwind",
    "mongo": "https://skillicons.dev/icons?i=mongo",
    "docker": "https://skillicons.dev/icons?i=docker",
    "express": "https://skillicons.dev/icons?i=express",
    "postman": "https://skillicons.dev/icons?i=postman",
    "js": "https://skillicons.dev/icons?i=js"
}

out_dir = os.path.join(os.path.dirname(__file__), "animated-icons")
os.makedirs(out_dir, exist_ok=True)

for name, url in icons.items():
    print(f"Downloading {name}...")
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    try:
        response = urllib.request.urlopen(req)
        svg_content = response.read().decode('utf-8')
        
        delay = round(random.uniform(0, 3), 1)
        
        style = f"""
<style>
    @keyframes float {{
        0% {{ transform: translateY(0px); }}
        50% {{ transform: translateY(-3px); }}
        100% {{ transform: translateY(0px); }}
    }}
    svg {{
        animation: float 3s ease-in-out infinite;
        animation-delay: -{delay}s;
        overflow: visible;
    }}
    .hover-target {{
        transition: all 0.3s ease;
        transform-origin: 128px 128px;
    }}
    svg:hover .hover-target {{
        transform: scale(1.15);
        filter: drop-shadow(0px 10px 10px rgba(0,0,0,0.3)) brightness(1.1);
    }}
</style>
"""
        
        # Add hover-target class
        svg_content = svg_content.replace('<g transform="translate(0, 0)">', '<g transform="translate(0, 0)" class="hover-target">')
        
        # Inject style before the LAST </svg>
        idx = svg_content.rfind("</svg>")
        if idx != -1:
            svg_content = svg_content[:idx] + style + svg_content[idx:]
            
            with open(os.path.join(out_dir, f"{name}.svg"), "w") as f:
                f.write(svg_content)
            print(f"Saved {name}.svg with delay -{delay}s")
        else:
            print(f"Failed to find </svg> in {name}")
    except Exception as e:
        print(f"Error fetching {name}: {e}")
