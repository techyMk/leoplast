import sys

file_path = "c:/Users/shoba/OneDrive/Documents/leoplast-web-redesign/roofing.html"

with open(file_path, "r", encoding="utf-8") as f:
    c = f.read()

target = """                    <div style="margin-top:3rem;text-align:center;">
                        <h4 style="font-size:1.5rem;font-weight:800;color:#0c1f3f;margin-bottom:1.5rem;">Profile Diagram</h4>
                        <div style="background:white;border-radius:1.5rem;padding:2.5rem;box-shadow:0 10px 30px rgba(0,0,0,0.06);position:relative;">
                            <div style="font-size:0.9rem;font-weight:700;color:#4b5563;margin-bottom:0.5rem;">Total Width: <span style="color:#991b1b;">1050mm</span></div>
                            <svg width="100%" height="80" viewBox="0 0 500 80" preserveAspectRatio="none">
                                <path d="M0,50 Q25,20 50,50 T100,50 T150,50 T200,50 T250,50 T300,50 T350,50 T400,50 T450,50 T500,50" fill="none" stroke="#dc2626" stroke-width="3"/>
                            </svg>
                            <div style="display:flex;justify-content:space-around;margin-top:1rem;font-size:0.85rem;font-weight:700;color:#6b7280;">
                                <div><span style="display:block;margin-bottom:0.25rem;">← Wave Spacing →</span><span style="color:#991b1b;">160mm</span></div>
                                <div><span style="display:block;margin-bottom:0.25rem;">↕ Height</span><span style="color:#991b1b;">28mm</span></div>
                            </div>
                        </div>
                    </div>"""

replacement = """                    <div style="margin-top:3rem;text-align:center;">
                        <h4 style="font-size:1.5rem;font-weight:800;color:#0c1f3f;margin-bottom:1.5rem;">Profile Diagram</h4>
                        <div style="background:white;border-radius:1.5rem;padding:2rem;box-shadow:0 10px 30px rgba(0,0,0,0.06);display:flex;align-items:center;justify-content:center;min-height:180px;">
                            <img src="assets/roofing/profile_diagram.png" alt="Profile Diagram Dimensions" style="width:100%;max-width:850px;height:auto;filter:drop-shadow(0 4px 6px rgba(0,0,0,0.05));">
                        </div>
                    </div>"""

if target in c:
    c = c.replace(target, replacement)
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(c)
    print("Profile diagram injected perfectly.")
else:
    print("Target block not found in file.")
