import os
import re

def cleanup_duplications(filename):
    path = os.path.join(os.getcwd(), filename)
    if not os.path.exists(path): return

    with open(path, "r", encoding="utf-8") as f:
        html = f.read()

    # The new hero block ends with:
    # <div class="reveal reveal-delay-2"\s+style="[^"]*min-height:400px;">\s+<img src="[^"]*" alt="[^"]*" style="max-height:360px;[^"]*">\s+</div>\s+</div>
    
    # We want to remove everything from that point until the next major block
    # Major blocks: <div class="feature-grid", <div class="product-card", <div style="display:grid;grid-template-columns:repeat
    
    hero_end_pattern = re.compile(r'(<div class="reveal reveal-delay-2"\s+style="[^"]*min-height:400px;">\s+<img src="[^"]*" alt="[^"]*" style="max-height:360px;[^"]*">\s+</div>\s+</div>\s*)')
    
    match = hero_end_pattern.search(html)
    if not match:
        return # Not processed by the enlarge script yet?

    end_pos = match.end()
    
    # Next major block pattern
    next_block_pattern = re.compile(r'(<div class="feature-grid"|<div class="product-card"|<div style="display:grid;grid-template-columns:repeat|<div style="background:rgba\(37,99,235,0\.05\)|<div style="background:linear-gradient\(135deg,#0c1f3f,#1e4d8c\)|\s*</div>\s*</section>)')
    
    match_next = next_block_pattern.search(html, end_pos)
    if not match_next:
        print(f"FAILED to find next block pos in {filename}")
        return

    # Everything between end_pos and match_next.start() is redundant
    redundant = html[end_pos:match_next.start()]
    
    if len(redundant.strip()) > 0:
        new_html = html[:end_pos] + html[match_next.start():]
        with open(path, "w", encoding="utf-8") as f:
            f.write(new_html)
        print(f"Cleaned up {filename}")
    else:
        print(f"No cleanup needed for {filename}")

if __name__ == "__main__":
    files = ["bath-fittings.html", "water-storage-tanks.html", "rpvc-pipes.html", "pvc-fittings.html", "cpvc-system.html", "upvc-system.html", "hdpe-system.html", "solvents.html", "flexible-hoses.html", "ball-valves.html", "sanitary-ware.html", "manhole-covers.html"]
    for f in files:
        cleanup_duplications(f)
print("Done!")
