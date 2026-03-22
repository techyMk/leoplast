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

    # Look for the hero right container which has the huge lucide icon
    # <i data-lucide="..." style="width:6rem;height:6rem;color:...;"></i>
    
    # We will search for a div with reveal-delay-2 that contains the i data-lucide with width:6rem
    pattern = re.compile(
        r'(<div[^>]*class="[^"]*reveal-delay-2[^"]*"[^>]*>[\s\n]*)(<i data-lucide="[^"]+" style="width:6rem;height:6rem;[^"]+"></i>)([\s\n]*</div>)'
    )
    
    # Check if there is a match
    if pattern.search(content):
        print(f"Found target in {filename}. Replacing...")
        replacement = f'\\1<img src="{img_src}" alt="{alt_text}" style="max-height:220px;object-fit:contain;padding:1.5rem;max-width:100%;">\\3'
        new_content = pattern.sub(replacement, content, count=1)
        
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(new_content)
        print(f"Successfully updated {filename}")
    else:
        # Maybe it's not width:6rem but something else? Let's also check for size 4.5rem, 5rem etc.
        pattern_fallback = re.compile(
            r'(<div[^>]*class="[^"]*reveal-delay-2[^"]*"[^>]*>[\s\n]*)(<i data-lucide="[^"]+" style="width:[0-9.]+rem;height:[0-9.]+rem;[^"]+"></i>)([\s\n]*</div>)'
        )
        if pattern_fallback.search(content):
             print(f"Found target using fallback pattern in {filename}. Replacing...")
             replacement = f'\\1<img src="{img_src}" alt="{alt_text}" style="max-height:220px;object-fit:contain;padding:1.5rem;max-width:100%;">\\3'
             new_content = pattern_fallback.sub(replacement, content, count=1)
             with open(file_path, "w", encoding="utf-8") as f:
                 f.write(new_content)
             print(f"Successfully updated {filename}")
        else:
             print(f"No match found in {filename} (might already be an image)")

if __name__ == "__main__":
    for item in mapping.keys():
        process_file(item)
