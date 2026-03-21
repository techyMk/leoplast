import sys

file_path = "c:/Users/shoba/OneDrive/Documents/leoplast-web-redesign/roofing.html"
with open(file_path, "r", encoding="utf-8") as f:
    c = f.read()

# Grab everything between <!-- Applications --> and </section>
start_marker = "<!-- Applications -->"
end_marker = "    <!-- Product Accessories -->"

# Wait, the Applications section is at the very bottom right before the CTA in my previous script?
# Let's check my `do_roofing_final.py` script.
# The structure was: 
# 1. Product Intro
# 2. 3-Layer Tech
# 3. Technical Specs
# 4. Product Advantages
# 5. Product Accessories
# 6. Installation Process
# 7. Applications
# 8. CTA

# So Applications is right before the CTA.
# Let's just find the generic pattern for Applications to the CTA:
app_start = '<section style="padding:6rem 2rem;background:white;">'
app_title = '<h2 style="font-size:2.5rem;font-weight:800;color:#0c1f3f;text-transform:uppercase;">Applications</h2>'

# I will just write a regex or simple replace for the grid.
# The grid starts with: <div style="display:flex;flex-wrap:wrap;justify-content:center;gap:3rem;">
start_grid = '<div style="display:flex;flex-wrap:wrap;justify-content:center;gap:3rem;">'
end_grid = '        </div>\n    </section>'

start_idx = c.find(start_grid)
end_idx = c.find(end_grid, start_idx)

if start_idx == -1 or end_idx == -1:
    print("Could not find Applications grid")
    sys.exit()

new_grid = """<div style="display:flex;flex-wrap:wrap;justify-content:center;gap:3rem;max-width:900px;margin:0 auto;">
                
                <div style="display:flex;flex-direction:column;align-items:center;width:140px;" class="reveal reveal-delay-1">
                    <img src="assets/roofing/app_icon_farming.png" alt="Farming" style="width:85px;height:auto;margin-bottom:1.25rem;transition:transform 0.35s ease;filter:drop-shadow(0 10px 15px rgba(220,38,38,0.15));" onmouseover="this.style.transform='translateY(-8px) scale(1.08)';" onmouseout="this.style.transform='translateY(0) scale(1)';">
                    <span style="font-weight:800;color:#0c1f3f;font-size:1.15rem;">Farming</span>
                </div>
                
                <div style="display:flex;flex-direction:column;align-items:center;width:140px;" class="reveal reveal-delay-2">
                    <img src="assets/roofing/app_icon_houses.png" alt="Houses" style="width:85px;height:auto;margin-bottom:1.25rem;transition:transform 0.35s ease;filter:drop-shadow(0 10px 15px rgba(220,38,38,0.15));" onmouseover="this.style.transform='translateY(-8px) scale(1.08)';" onmouseout="this.style.transform='translateY(0) scale(1)';">
                    <span style="font-weight:800;color:#0c1f3f;font-size:1.15rem;">Houses</span>
                </div>
                
                <div style="display:flex;flex-direction:column;align-items:center;width:140px;" class="reveal reveal-delay-3">
                    <img src="assets/roofing/app_icon_car-shed.png" alt="Car-Shed" style="width:85px;height:auto;margin-bottom:1.25rem;transition:transform 0.35s ease;filter:drop-shadow(0 10px 15px rgba(220,38,38,0.15));" onmouseover="this.style.transform='translateY(-8px) scale(1.08)';" onmouseout="this.style.transform='translateY(0) scale(1)';">
                    <span style="font-weight:800;color:#0c1f3f;font-size:1.15rem;">Car-Shed</span>
                </div>
                
                <div style="display:flex;flex-direction:column;align-items:center;width:140px;" class="reveal reveal-delay-4">
                    <img src="assets/roofing/app_icon_warehouse.png" alt="Warehouse" style="width:85px;height:auto;margin-bottom:1.25rem;transition:transform 0.35s ease;filter:drop-shadow(0 10px 15px rgba(220,38,38,0.15));" onmouseover="this.style.transform='translateY(-8px) scale(1.08)';" onmouseout="this.style.transform='translateY(0) scale(1)';">
                    <span style="font-weight:800;color:#0c1f3f;font-size:1.15rem;">Warehouse</span>
                </div>
                
                <div style="display:flex;flex-direction:column;align-items:center;width:140px;" class="reveal reveal-delay-1">
                    <img src="assets/roofing/app_icon_factories.png" alt="Factories" style="width:85px;height:auto;margin-bottom:1.25rem;transition:transform 0.35s ease;filter:drop-shadow(0 10px 15px rgba(220,38,38,0.15));" onmouseover="this.style.transform='translateY(-8px) scale(1.08)';" onmouseout="this.style.transform='translateY(0) scale(1)';">
                    <span style="font-weight:800;color:#0c1f3f;font-size:1.15rem;">Factories</span>
                </div>

                <div style="display:flex;flex-direction:column;align-items:center;width:140px;" class="reveal reveal-delay-2">
                    <img src="assets/roofing/app_icon_wall-cladding.png" alt="Wall-Cladding" style="width:85px;height:auto;margin-bottom:1.25rem;transition:transform 0.35s ease;filter:drop-shadow(0 10px 15px rgba(220,38,38,0.15));" onmouseover="this.style.transform='translateY(-8px) scale(1.08)';" onmouseout="this.style.transform='translateY(0) scale(1)';">
                    <span style="font-weight:800;color:#0c1f3f;font-size:1.15rem;">Wall-Cladding</span>
                </div>
                
                <div style="display:flex;flex-direction:column;align-items:center;width:140px;" class="reveal reveal-delay-3">
                    <img src="assets/roofing/app_icon_resorts.png" alt="Resorts" style="width:85px;height:auto;margin-bottom:1.25rem;transition:transform 0.35s ease;filter:drop-shadow(0 10px 15px rgba(220,38,38,0.15));" onmouseover="this.style.transform='translateY(-8px) scale(1.08)';" onmouseout="this.style.transform='translateY(0) scale(1)';">
                    <span style="font-weight:800;color:#0c1f3f;font-size:1.15rem;">Resorts</span>
                </div>
                
            </div>
"""

c = c[:start_idx] + new_grid + c[end_idx:]

with open(file_path, "w", encoding="utf-8") as f:
    f.write(c)
print("Icons successfully mapped.")
