import re

# Fix the 4 pages where the hero image block was incorrectly injected inside the product cards grid
# We need to: 
# 1. Remove the misplaced hero image block from inside the product cards
# 2. Close the text reveal div properly
# 3. Add the hero image block as a sibling of the text reveal div (inside the 2-col grid)
# 4. Close the 2-col grid
# 5. Then have the product cards grid as a separate block

files_to_fix = {
    "ball-valves.html": {
        "img": "assets/products/pvc-ballvalve-1.png",
        "alt": "Ball Valves", 
        "bg": "linear-gradient(135deg,#fee2e2,#fecaca)"
    },
    "solvents.html": {
        "img": "assets/products/Solvents.png",
        "alt": "Solvents",
        "bg": "linear-gradient(135deg,#fce7f3,#fbcfe8)"
    },
    "sanitary-ware.html": {
        "img": "assets/products/seat-cover-1.png",
        "alt": "Sanitary Ware",
        "bg": "linear-gradient(135deg,#f8fafc,#e2e8f0)"
    },
    "manhole-covers.html": {
        "img": "assets/products/manwhole-cover.png",
        "alt": "Manhole Covers",
        "bg": "linear-gradient(135deg,#f1f5f9,#e2e8f0)"
    }
}

for filename, cfg in files_to_fix.items():
    with open(filename, "r", encoding="utf-8") as f:
        content = f.read()

    # The broken structure looks like:
    # <div style="display:grid;grid-template-columns:1fr 1fr;...">   <-- 2-col grid (correct)
    #     <div class="reveal">                                        <-- text column (correct)
    #         ...section-badge, h2, p...
    #     </div>                                                      <-- MISSING: close reveal, add image, close grid
    #     <div style="display:grid;...">                              <-- product cards grid start (correct)
    #         <div class="product-card ...">                          <-- first product card
    #             ...
    #         </div>
    #     <div class="reveal reveal-delay-2"...>                      <-- MISPLACED hero image (BAD)
    #         <img src="..."/>
    #     </div>
    #     </div>                                                      <-- extra closing div

    # We need to:
    # 1. Find and remove the misplaced hero image block
    # 2. Insert it properly between the reveal text div and the product cards grid
    
    # Step 1: Remove the misplaced hero image block
    hero_pattern = re.compile(
        r'\s*<div class="reveal reveal-delay-2"\s*'
        r'style="background:' + re.escape(cfg["bg"]) + r';border-radius:1\.5rem;display:flex;align-items:center;justify-content:center;min-height:260px;">\s*'
        r'<img src="' + re.escape(cfg["img"]) + r'"[^>]*>\s*'
        r'</div>\s*'
        r'</div>'
    )
    
    match = hero_pattern.search(content)
    if match:
        # Remove the misplaced block
        content = content[:match.start()] + '\n                </div>' + content[match.end():]
        print(f"  Removed misplaced hero block from {filename}")
    else:
        print(f"  WARNING: Could not find misplaced hero block in {filename}")
        continue
    
    # Step 2: Now insert the hero image block properly
    # Find the closing </div> of the reveal text, which is followed by the product cards grid
    # The structure should now be:
    # <div style="...1fr 1fr...">
    #     <div class="reveal">
    #         ...
    #     </div>             <--- this is where we are now
    #     <div style="display:grid;grid-template-columns:repeat(...)">  <--- product cards
    
    # Find the </div> that closes the reveal div, right before the product grid
    reveal_close_pattern = re.compile(
        r'(</div>\s*)'
        r'(<div style="display:grid;grid-template-columns:repeat)'
    )
    
    match2 = reveal_close_pattern.search(content)
    if match2:
        hero_img = f'''
            <div class="reveal reveal-delay-2"
                style="background:{cfg["bg"]};border-radius:1.5rem;display:flex;align-items:center;justify-content:center;min-height:260px;">
                <img src="{cfg["img"]}" alt="{cfg["alt"]}" style="max-height:220px;max-width:100%;object-fit:contain;padding:1.5rem;">
            </div>
            </div>
            '''
        content = content[:match2.start()] + match2.group(1) + hero_img + match2.group(2) + content[match2.end():]
        print(f"  Inserted hero image block correctly in {filename}")
    else:
        print(f"  WARNING: Could not find insertion point in {filename}")
        continue

    with open(filename, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"  Fixed {filename} successfully!")
