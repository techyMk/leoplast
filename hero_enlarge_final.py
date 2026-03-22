import os
import re

mapping = {
    "bath-fittings.html": {
        "img": "assets/products/bath-fittings.webp",
        "alt": "Bath Fittings",
        "bg": "linear-gradient(135deg,#e0e7ff,#c7d2fe)",
        "badge": "Premium Collection",
        "title": "Bath Fittings",
        "desc": "Leo Plast's bath fittings offer a complete range of premium finishes designed for modern spaces. Each piece combines ergonomic design with robust engineering for long-term performance."
    },
    "water-storage-tanks.html": {
        "img": "assets/products/Tank.png",
        "alt": "Water Storage Tanks",
        "bg": "linear-gradient(135deg,#dbeafe,#eff6ff)",
        "badge": "Advanced System",
        "title": "Leo Plast Water Storage Tanks",
        "desc": "Leo Plast's water storage tanks integrate advanced engineering with high-quality materials to provide durable, hygienic, and secure water storage solutions."
    },
    "rpvc-pipes.html": {
        "img": "assets/products/rPVC-Plumbing-and-Irrigation-Pipes.png",
        "alt": "rPVC Pipes & Irrigation",
        "bg": "linear-gradient(135deg,#e0f2fe,#bae6fd)",
        "badge": "Overview",
        "title": "rPVC Plumbing & Irrigation Pipes",
        "desc": "High-quality Lead-Free rPVC pipes designed for efficient agricultural water supply and potable water needs. Durable, reliable, and corrosion-resistant."
    },
    "pvc-fittings.html": {
        "img": "assets/products/pvc-fittings-1.webp",
        "alt": "PVC Fittings",
        "bg": "linear-gradient(135deg,#dbeafe,#eff6ff)",
        "badge": "200+ Variants",
        "title": "Leo Plast PVC Fittings",
        "desc": "The ONLY manufacturer in Tamil Nadu with 200+ PVC fittings. Food-grade, ISI certified, and engineered for heavy-duty, long-lasting performance."
    },
    "cpvc-system.html": {
        "img": "assets/products/cPVC-Plumbing-Systems.webp",
        "alt": "cPVC Plumbing Systems",
        "bg": "linear-gradient(135deg,#fef3c7,#fde68a)",
        "badge": "Hot & Cold Water System",
        "title": "cPVC Plumbing System",
        "desc": "High-performance cPVC pipes and fittings for both hot and cold water applications. Made from NSF-certified, lead-free materials for maximum safety."
    },
    "upvc-system.html": {
        "img": "assets/products/uPVC-Potable-Water-Plumbing-Systems.png",
        "alt": "uPVC Potable Water Plumbing Systems",
        "bg": "linear-gradient(135deg,#d1fae5,#a7f3d0)",
        "badge": "Potable Water System",
        "title": "uPVC Plumbing System",
        "desc": "Safe, lead-free, and non-toxic solutions for potable water applications. Ideal for residential, commercial, and agricultural plumbing needs."
    },
    "hdpe-system.html": {
        "img": "assets/products/HDPE-Irrigation-Systems-1.png",
        "alt": "HDPE Irrigation Systems",
        "bg": "linear-gradient(135deg,#dcfce7,#bbf7d0)",
        "badge": "Agricultural Solutions",
        "title": "HDPE Irrigation System",
        "desc": "Crafted using high-quality virgin materials to ensure robust performance in agricultural and irrigation applications. Durable, flexible, and chemical-resistant."
    },
    "solvents.html": {
        "img": "assets/products/Solvents.png",
        "alt": "Solvents",
        "bg": "linear-gradient(135deg,#fce7f3,#fbcfe8)",
        "badge": "Pipe Bonding Solutions",
        "title": "Complete Range of Solvents",
        "desc": "Specially formulated to provide the strongest, most reliable bonds for PVC, uPVC, and cPVC pipe joints. Ensures leak-proof connections in all plumbing applications."
    },
    "flexible-hoses.html": {
        "img": "assets/products/flexible-hoses.webp",
        "alt": "Flexible Hoses",
        "bg": "linear-gradient(135deg,#f3e8ff,#e9d5ff)",
        "badge": "Fluid Transfer",
        "title": "Flexible Hoses",
        "desc": "Suction and braided hoses for versatile fluid transfer applications. High-pressure rated and kink-resistant design for agriculture and industrial use."
    },
    "ball-valves.html": {
        "img": "assets/products/pvc-ballvalve-1.png",
        "alt": "Ball Valves",
        "bg": "linear-gradient(135deg,#fee2e2,#fecaca)",
        "badge": "Complete Valve Range",
        "title": "Ball Valves for Every Application",
        "desc": "Precision-engineered with full-bore design for minimal flow restriction. Available across all major pipe standards for complete system compatibility."
    },
    "sanitary-ware.html": {
        "img": "assets/products/seat-cover-1.png",
        "alt": "Sanitary Ware",
        "bg": "linear-gradient(135deg,#f8fafc,#e2e8f0)",
        "badge": "Classic Series",
        "title": "Quality Sanitary Solutions",
        "desc": "Combines functional design with robust polymer engineering for hygienic, durable solutions. Built for long-term reliability in every bathroom."
    },
    "manhole-covers.html": {
        "img": "assets/products/manwhole-cover.png",
        "alt": "Manhole Covers",
        "bg": "linear-gradient(135deg,#f1f5f9,#e2e8f0)",
        "badge": "Heavy Duty Solutions",
        "title": "FRP Manhole Covers",
        "desc": "Superior strength and durability for diverse infrastructure needs. Corrosion-resistant and engineered to withstand significant loads."
    }
}

def get_hero_content(html):
    # Try to find the first 1100px-max-width div inside the section
    match = re.search(r'<section[^>]*>[\s\S]*?<div style="max-width:1100px;margin:0 auto;">([\s\S]*?)</div>', html)
    if match:
        return match.group(1), match.start(1), match.end(1)
    return None, 0, 0

def process_file(filename, cfg):
    path = os.path.join(os.getcwd(), filename)
    if not os.path.exists(path):
        return

    with open(path, "r", encoding="utf-8") as f:
        html = f.read()

    # The goal is to replace the first intro grid row (or text block) with a standardized 2-col hero
    # This regex looks for the first 1100px div and its first major child until the next major feature/grid
    hero_inner, start, end = get_hero_content(html)
    if not hero_inner:
        print(f"Skipping {filename}: Hero content not found")
        return

    # Check if a 2-col grid already exists at the start
    grid_match = re.search(r'<div style="display:grid;grid-template-columns:1fr 1fr;gap:4rem;align-items:center;margin-bottom:[45]rem;">[\s\S]*?</div>[\s\S]*?</div>', hero_inner)
    
    # We want to replace the FIRST major chunk in the 1100px div
    # Usually it's either the 2-col grid OR a centered reveal block
    first_block_match = re.search(r'<div[^>]*class="reveal"[^>]*>[\s\S]*?</div>[\s\S]*?</div>', hero_inner)
    if not first_block_match:
        # Try a simpler match if it's just a text reveal
        first_block_match = re.search(r'<div[^>]*class="reveal"[^>]*>[\s\S]*?</div>', hero_inner)

    if not first_block_match:
        print(f"Skipping {filename}: First block not found")
        return

    new_hero = f'''
            <div style="display:grid;grid-template-columns:1fr 1fr;gap:4rem;align-items:center;margin-bottom:4rem;">
                <div class="reveal">
                    <div class="section-badge">{cfg["badge"]}</div>
                    <h2 style="font-size:2rem;font-weight:800;color:#0c1f3f;margin-bottom:1rem;">{cfg["title"]}</h2>
                    <p style="color:#4b5563;line-height:1.8;margin-bottom:1.25rem;">{cfg["desc"]}</p>
                </div>
                <div class="reveal reveal-delay-2"
                    style="background:{cfg["bg"]};border-radius:1.5rem;display:flex;align-items:center;justify-content:center;min-height:400px;">
                    <img src="{cfg["img"]}" alt="{cfg["alt"]}" style="max-height:360px;max-width:100%;object-fit:contain;padding:1rem;">
                </div>
            </div>'''

    new_hero_inner = hero_inner[:first_block_match.start()] + new_hero + hero_inner[first_block_match.end():]
    new_html = html[:start] + new_hero_inner + html[end:]

    with open(path, "w", encoding="utf-8") as f:
        f.write(new_html)
    print(f"Processed {filename}")

if __name__ == "__main__":
    for f, c in mapping.items():
        process_file(f, c)
print("Done!")
