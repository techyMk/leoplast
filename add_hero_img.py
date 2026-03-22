import re

# These pages need a 2-column intro section added (they go straight to product cards)
pages = {
    "bath-fittings.html": {
        "img": "assets/products/bath-fittings.webp",
        "alt": "Bath Fittings",
        "bg": "linear-gradient(135deg,#e0e7ff,#c7d2fe)",
        "badge": "Premium Collection",
        "title": "M-Series Bath Fittings",
        "desc": "Leo Plast's M-Series offers a complete range of premium chrome-finished bath fittings designed for modern residential and commercial spaces. Each piece combines ergonomic design with robust polymer engineering for long-term performance.",
        # Insert the image div into the existing grid that currently has only 1 column
        "mode": "convert_grid"
    },
    "pvc-fittings.html": {
        "img": "assets/products/pvc-fittings-1.webp",
        "alt": "PVC Fittings",
        "bg": "linear-gradient(135deg,#dbeafe,#eff6ff)",
        "mode": "insert_after_hero_badge"
    },
    "solvents.html": {
        "img": "assets/products/Solvents.png",
        "alt": "Solvents",
        "bg": "linear-gradient(135deg,#fce7f3,#fbcfe8)",
        "mode": "insert_after_section_desc"
    },
    "flexible-hoses.html": {
        "img": "assets/products/flexible-hoses.webp",
        "alt": "Flexible Hoses",
        "bg": "linear-gradient(135deg,#f3e8ff,#e9d5ff)",
        "mode": "insert_before_product_grid"
    },
    "ball-valves.html": {
        "img": "assets/products/pvc-ballvalve-1.png",
        "alt": "Ball Valves",
        "bg": "linear-gradient(135deg,#fee2e2,#fecaca)",
        "mode": "insert_after_section_desc"
    },
    "sanitary-ware.html": {
        "img": "assets/products/seat-cover-1.png",
        "alt": "Sanitary Ware",
        "bg": "linear-gradient(135deg,#f8fafc,#e2e8f0)",
        "mode": "insert_after_section_desc"
    },
    "manhole-covers.html": {
        "img": "assets/products/manwhole-cover.png",
        "alt": "Manhole Covers",
        "bg": "linear-gradient(135deg,#f1f5f9,#e2e8f0)",
        "mode": "insert_after_section_desc"
    },
}

def make_hero_image_block(img, alt, bg):
    return f'''
            <div class="reveal reveal-delay-2"
                style="background:{bg};border-radius:1.5rem;display:flex;align-items:center;justify-content:center;min-height:260px;">
                <img src="{img}" alt="{alt}" style="max-height:220px;max-width:100%;object-fit:contain;padding:1.5rem;">
            </div>'''

for filename, cfg in pages.items():
    try:
        with open(filename, "r", encoding="utf-8") as f:
            content = f.read()
    except FileNotFoundError:
        print(f"File not found: {filename}")
        continue

    img_block = make_hero_image_block(cfg["img"], cfg["alt"], cfg["bg"])
    mode = cfg["mode"]
    changed = False

    if mode == "convert_grid":
        # bath-fittings: The intro has display:grid without 2 columns. 
        # Change the single column grid to 2 columns and add image block after the reveal div
        old = '<div style="display:grid;margin-bottom:5rem;">'
        new = '<div style="display:grid;grid-template-columns:1fr 1fr;gap:4rem;align-items:center;margin-bottom:5rem;">'
        if old in content:
            content = content.replace(old, new, 1)
            # Now insert the image block before the closing </div> of this grid
            # Find the </div> that closes the reveal div, and add image block after it
            # The pattern: </div>\n                \n            </div> (after the intro text)
            # We need to insert after the first </div>\n</div> pair in the section
            pattern = re.compile(r'(grid-template-columns:1fr 1fr;gap:4rem;align-items:center;margin-bottom:5rem;">\s*<div class="reveal">[\s\S]*?</div>\s*<div style="display:grid;grid-template-columns:repeat)')
            match = pattern.search(content)
            if match:
                # Insert before the product cards grid
                insert_point = content.find('</div>', content.find('margin-bottom:1.5rem;">') + 10)
                # Actually let's find the closing of the reveal div
                pass

            # Simpler: find '</div>\n                \n            </div>' after the M-Series text
            # Let me use a different approach: insert before the grid of product cards
            old2 = '                    <div style="display:grid;grid-template-columns:repeat(auto-fill,minmax(250px,1fr));gap:2rem;margin-top:2rem;">'
            if old2 in content:
                content = content.replace(old2, img_block + '\n                </div>\n                <div style="display:grid;grid-template-columns:repeat(auto-fill,minmax(250px,1fr));gap:2rem;margin-top:2rem;">', 1)
                changed = True
                print(f"Updated {filename} (convert_grid)")
            else:
                print(f"Could not find product grid in {filename}")
        else:
            print(f"Could not find grid marker in {filename}")

    elif mode == "insert_after_hero_badge":
        # pvc-fittings: add a 2-column intro section between the hero banner section and the blue banner
        anchor = '<div style="background:linear-gradient(135deg,#0c1f3f,#1e4d8c);border-radius:1.5rem;padding:2.5rem;margin-bottom:4rem;display:flex;align-items:center;gap:2rem;flex-wrap:wrap;"'
        intro_section = f'''<div style="display:grid;grid-template-columns:1fr 1fr;gap:4rem;align-items:center;margin-bottom:4rem;">
                <div class="reveal">
                    <div class="section-badge">200+ Variants</div>
                    <h2 style="font-size:2rem;font-weight:800;color:#0c1f3f;margin-bottom:1rem;">Leo Plast PVC Fittings</h2>
                    <p style="color:#4b5563;line-height:1.8;">Leo Plast is the ONLY manufacturer in Tamil Nadu with 200+ PVC fittings. Food-grade, ISI certified, UV resistant — locally crafted, high-quality products that meet the highest standards.</p>
                </div>{img_block}
            </div>
            '''
        if anchor in content:
            content = content.replace(anchor, intro_section + anchor, 1)
            changed = True
            print(f"Updated {filename} (insert_after_hero_badge)")
        else:
            print(f"Could not find anchor in {filename}")

    elif mode == "insert_after_section_desc" or mode == "insert_before_product_grid":
        # These pages have: section-badge → h2 → p → product grid
        # We need to convert the centered text intro into a 2-column layout
        # Find the section description closing </div> and add image after it
        
        # Find the centered intro div and convert to 2-col grid
        old_pattern = re.compile(
            r'(<div style="text-align:center;margin-bottom:3rem;" class="reveal">)([\s\S]*?)(</div>\s*</div>)'
        )
        match = old_pattern.search(content)
        if match:
            # Replace the centered div with a 2-column grid
            inner = match.group(2)
            replacement = f'<div style="display:grid;grid-template-columns:1fr 1fr;gap:4rem;align-items:center;margin-bottom:3rem;">\n                <div class="reveal">{inner}</div>{img_block}\n            </div>'
            content = content[:match.start()] + replacement + content[match.end():]
            changed = True
            print(f"Updated {filename} (insert_after_section_desc)")
        elif mode == "insert_before_product_grid":
            # flexible-hoses goes straight to product cards, no centered intro
            # Insert a 2-column block between </div> (page-hero close) and <section>
            anchor = '<section style="padding:5rem 1.5rem;background:white;">'
            intro_block = f'''<section style="padding:5rem 1.5rem 0;background:white;">
        <div style="max-width:1100px;margin:0 auto;">
            <div style="display:grid;grid-template-columns:1fr 1fr;gap:4rem;align-items:center;margin-bottom:3rem;">
                <div class="reveal">
                    <div class="section-badge">Fluid Transfer</div>
                    <h2 style="font-size:2rem;font-weight:800;color:#0c1f3f;margin-bottom:1rem;">Leo Plast Flexible Hoses</h2>
                    <p style="color:#4b5563;line-height:1.8;">Suction and braided hoses for versatile fluid transfer applications. High-pressure rated, kink-resistant design for agriculture, construction, and industrial use.</p>
                </div>{img_block}
            </div>
        </div>
    </section>
    '''
            if anchor in content:
                content = content.replace(anchor, intro_block + anchor, 1)
                changed = True
                print(f"Updated {filename} (insert_before_product_grid)")
            else:
                print(f"Could not find section anchor in {filename}")
        else:
            print(f"Could not find centered intro block in {filename}")

    if changed:
        with open(filename, "w", encoding="utf-8") as f:
            f.write(content)
    else:
        print(f"No changes made to {filename}")
