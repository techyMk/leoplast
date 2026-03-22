import os
import re

mapping = {
    "bath-fittings.html": ("assets/products/bath-fittings.webp", "Bath Fittings"),
    "water-storage-tanks.html": ("assets/products/Tank.png", "Water Storage Tanks"),
    "rpvc-pipes.html": ("assets/products/rPVC-Plumbing-and-Irrigation-Pipes.png", "rPVC Pipes & Irrigation"),
    "pvc-fittings.html": ("assets/products/pvc-fittings-1.webp", "PVC Fittings"),
    "cpvc-system.html": ("assets/products/cPVC-Plumbing-Systems.webp", "cPVC Plumbing Systems"),
    "upvc-system.html": ("assets/products/uPVC-Potable-Water-Plumbing-Systems.png", "uPVC Potable Water Plumbing Systems"),
    "hdpe-system.html": ("assets/products/HDPE-Irrigation-Systems-1.png", "HDPE Irrigation Systems"),
    "solvents.html": ("assets/products/Solvents.png", "Solvents"),
    "flexible-hoses.html": ("assets/products/flexible-hoses.webp", "Flexible Hoses"),
    "ball-valves.html": ("assets/products/pvc-ballvalve-1.png", "Ball Valves"),
    "sanitary-ware.html": ("assets/products/seat-cover-1.png", "Sanitary Ware"),
    "manhole-covers.html": ("assets/products/manwhole-cover.png", "Manhole Covers")
}

def process_file(file_path):
    if not os.path.exists(file_path):
        print(f"File not found: {file_path}")
        return

    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    filename = os.path.basename(file_path)
    img_src, alt_text = mapping.get(filename, ("", ""))
    
    if not img_src:
        return

    # Look for the hero right container which has background:linear-gradient and reveal-delay-2
    pattern = re.compile(
        r'(<div[^>]*class="[^"]*reveal-delay-2[^"]*"[^>]*background:linear-gradient[^>]*>)([\s\S]*?)(</div>)'
    )
    
    # Check if there is a match
    match = pattern.search(content)
    if match:
        print(f"Found target in {filename}. Replacing...")
        replacement = f'\\1\n                    <img src="{img_src}" alt="{alt_text}" style="max-height:220px;max-width:100%;object-fit:contain;padding:1.5rem;">\n                \\3'
        new_content = pattern.sub(replacement, content, count=1)
        
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(new_content)
        print(f"Successfully updated {filename}")
    else:
        print(f"FAILED TO MATCH in {filename}")

if __name__ == "__main__":
    for item in mapping.keys():
        process_file(item)
