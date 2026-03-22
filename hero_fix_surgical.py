import os
import re

mapping = {
    "bath-fittings.html": ("assets/products/bath-fittings.webp", "Bath Fittings", "Premium Collection", "Bath Fittings", "Leo Plast's bath fittings offer a complete range of premium finishes designed for modern spaces. Each piece combines ergonomic design with robust engineering for long-term performance.", "#e0e7ff,#c7d2fe"),
    "water-storage-tanks.html": ("assets/products/Tank.png", "Water Storage Tanks", "Advanced System", "Leo Plast Water Storage Tanks", "Leo Plast's water storage tanks integrate advanced engineering with high-quality materials to provide durable, hygienic, and secure water storage solutions.", "#dbeafe,#eff6ff"),
    "rpvc-pipes.html": ("assets/products/rPVC-Plumbing-and-Irrigation-Pipes.png", "rPVC Pipes & Irrigation", "Overview", "rPVC Plumbing & Irrigation Pipes", "High-quality Lead-Free rPVC pipes designed for efficient agricultural water supply and potable water needs. Durable, reliable, and corrosion-resistant.", "#e0f2fe,#bae6fd"),
    "pvc-fittings.html": ("assets/products/pvc-fittings-1.webp", "PVC Fittings", "200+ Variants", "Leo Plast PVC Fittings", "The ONLY manufacturer in Tamil Nadu with 200+ PVC fittings. Food-grade, ISI certified, and engineered for heavy-duty, long-lasting performance.", "#dbeafe,#eff6ff"),
    "cpvc-system.html": ("assets/products/cPVC-Plumbing-Systems.webp", "cPVC Plumbing Systems", "Hot & Cold Water System", "cPVC Plumbing System", "High-performance cPVC pipes and fittings for both hot and cold water applications. Made from NSF-certified, lead-free materials for maximum safety.", "#fef3c7,#fde68a"),
    "upvc-system.html": ("assets/products/uPVC-Potable-Water-Plumbing-Systems.png", "uPVC Potable Water Plumbing Systems", "Potable Water System", "uPVC Plumbing System", "Safe, lead-free, and non-toxic solutions for potable water applications. Ideal for residential, commercial, and agricultural plumbing needs.", "#d1fae5,#a7f3d0"),
    "hdpe-system.html": ("assets/products/HDPE-Irrigation-Systems-1.png", "HDPE Irrigation Systems", "Agricultural Solutions", "HDPE Irrigation System", "Crafted using high-quality virgin materials to ensure robust performance in agricultural and irrigation applications. Durable, flexible, and chemical-resistant.", "#dcfce7,#bbf7d0"),
    "solvents.html": ("assets/products/Solvents.png", "Solvents", "Pipe Bonding Solutions", "Complete Range of Solvents", "Leo Plast solvents are specially formulated to provide the strongest, most reliable bonds for PVC, uPVC, and cPVC pipe joints. Ensures leak-proof connections in all plumbing applications.", "#fce7f3,#fbcfe8"),
    "flexible-hoses.html": ("assets/products/flexible-hoses.webp", "Flexible Hoses", "Fluid Transfer", "Flexible Hoses", "Suction and braided hoses for versatile fluid transfer applications. High-pressure rated and kink-resistant design for agriculture and industrial use.", "#f3e8ff,#e9d5ff"),
    "ball-valves.html": ("assets/products/pvc-ballvalve-1.png", "Ball Valves", "Complete Valve Range", "Ball Valves for Every Application", "Precision-engineered with full-bore design for minimal flow restriction. Available across all major pipe standards for complete system compatibility.", "#fee2e2,#fecaca"),
    "sanitary-ware.html": ("assets/products/seat-cover-1.png", "Sanitary Ware", "Classic Series", "Quality Sanitary Solutions", "Combines functional design with robust polymer engineering for hygienic, durable solutions. Built for long-term reliability in every bathroom.", "#f8fafc,#e2e8f0"),
    "manhole-covers.html": ("assets/products/manwhole-cover.png", "Manhole Covers", "Heavy Duty Solutions", "FRP Manhole Covers", "Superior strength and durability for diverse infrastructure needs. Corrosion-resistant and engineered to withstand significant loads.", "#f1f5f9,#e2e8f0")
}

def fix_file(filename):
    if filename not in mapping: return
    img, alt, badge, title, desc, bg = mapping[filename]
    
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()

    # Look for the 1100px container
    container_pattern = r'(<div style="max-width:1100px;margin:0 auto;">)([\s\S]*?)(<div class="feature-grid"|<div class="product-card|<div style="display:grid;grid-template-columns:repeat|<div style="background:rgba\(37,99,235,0\.05\)|<div style="background:linear-gradient\(135deg,#0c1f3f,#1e4d8c\)|\s*</div>\s*</section>)'
    
    match = re.search(container_pattern, content)
    if not match:
        print(f"FAILED to find container in {filename}")
        return

    prefix = match.group(1)
    inner = match.group(2)
    suffix = match.group(3)

    hero_block = f'''
            <div style="display:grid;grid-template-columns:1fr 1fr;gap:4rem;align-items:center;margin-bottom:4rem;">
                <div class="reveal">
                    <div class="section-badge">{badge}</div>
                    <h2 style="font-size:2rem;font-weight:800;color:#0c1f3f;margin-bottom:1rem;">{title}</h2>
                    <p style="color:#4b5563;line-height:1.8;margin-bottom:1.25rem;">{desc}</p>
                </div>
                <div class="reveal reveal-delay-2"
                    style="background:linear-gradient(135deg,{bg});border-radius:1.5rem;display:flex;align-items:center;justify-content:center;min-height:400px;">
                    <img src="{img}" alt="{alt}" style="max-height:360px;max-width:100%;object-fit:contain;padding:1rem;">
                </div>
            </div>\n            '''
    
    # We replace the intro part of 'inner'. 
    # Usually the intro is the first grid or centered div.
    # We'll just replace everything in 'inner' up to the point where the next section starts.
    # Actually, some pages have comments or extra text.
    # To be safe, we'll replace the first major div in 'inner'.
    
    new_inner = hero_block
    # If the file is pvc-fittings, we might want to keep the trophy row.
    # But the user wants a uniform hero. 
    # Actually, let's just prepend the hero block if it's not already there.
    # NO, we must replace the duplicate/old intro.
    
    # Let's try to find the old intro grid or div in 'inner'
    old_intro_match = re.search(r'(\s*<!--.*?-->)?\s*<div[^>]*>[\s\S]*?</div>(\s*</div>)?', inner)
    if old_intro_match:
        # Check if the matched div is short (intro) or long (everything)
        # If it's the 1100px container's only child, we might be over-matching.
        # But our suffix should prevent that.
        new_inner = inner[:old_intro_match.start()] + hero_block + inner[old_intro_match.end():]
    
    new_content = content[:match.start()] + prefix + new_inner + suffix + content[match.end():]
    
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print(f"Fixed {filename}")

if __name__ == "__main__":
    for f in mapping.keys():
        fix_file(f)
