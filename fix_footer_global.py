import glob
import re
import os

html_files = glob.glob(r"c:\Users\shoba\OneDrive\Documents\leoplast-web-redesign\*.html")

devUrl = "https://portfolio-techymk.netlify.app/"

unified_footer_bottom = f"""
        <div style="margin-top:3rem;border-top:1px solid rgba(255,255,255,0.05);padding-top:1.5rem;font-size:0.85rem;color:#6b7280;display:flex;justify-content:center;align-items:center;gap:0.75rem;flex-wrap:wrap;">
            <span>Copyright © 2026 Leo Plast. All Rights Reserved.</span>
            <span style="color:#4b5563;font-size:0.8rem;">|</span>
            <span>Designed & Developed by <a href="{devUrl}" target="_blank" rel="noopener noreferrer" style="color:#60a5fa;text-decoration:none;font-weight:700;transition:color 0.2s;" onmouseover="this.style.color='#ffffff'" onmouseout="this.style.color='#60a5fa'">TechyMK</a></span>
        </div>
    </footer>"""

# Regex to find the <p> tag containing "All rights reserved" or similar
# e.g., <p style="...">© 2026 Leoplast Industries. All rights reserved.</p>
# or <p>© 2026 Leoplast Industries. All rights reserved.</p>
p_pattern = re.compile(r"<p[^>]*>.*?© 2026 Leo ?plast.*?All [rR]ights [rR]eserved.*?</p>", re.IGNORECASE | re.DOTALL)

count = 0
for fpath in html_files:
    with open(fpath, "r", encoding="utf-8") as f:
        c = f.read()
    
    original_c = c
    
    # 1. Remove the floating copyright <p> tag
    c = p_pattern.sub("", c)
    
    # 2. Check if we already injected the unified footer bottom
    if "Copyright © 2026 Leo Plast" not in c and "Designed & Developed by" not in c:
        # Replace </footer> with unified_footer_bottom
        # Note: some files might have </footer> with spaces. 
        c = re.sub(r'</footer>', unified_footer_bottom, c, count=1, flags=re.IGNORECASE)
    elif "Designed & Developed" in c and "Copyright" in c:
        # Probably already ran, let's just make sure
        pass

    if c != original_c:
        with open(fpath, "w", encoding="utf-8") as f:
            f.write(c)
        count += 1
        print(f"Updated {os.path.basename(fpath)}")

print(f"Total HTML files updated: {count}")

# 3. Clean up leoplast.js
js_path = r"c:\Users\shoba\OneDrive\Documents\leoplast-web-redesign\leoplast.js"
with open(js_path, "r", encoding="utf-8") as f:
    js = f.read()

# We look for the marker we left
if "// GLOBAL FOOTER CREDIT" in js:
    # Just strip it out completely. We appended it at the very bottom.
    idx = js.find("// ========================\n// GLOBAL FOOTER CREDIT")
    if idx != -1:
        js = js[:idx]
        with open(js_path, "w", encoding="utf-8") as f:
            f.write(js)
        print("Cleaned leoplast.js")

