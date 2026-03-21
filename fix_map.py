import sys

file_path = "c:/Users/shoba/OneDrive/Documents/leoplast-web-redesign/contact.html"

with open(file_path, "r", encoding="utf-8") as f:
    c = f.read()

# I need to add CSS for the floating card specifically for mobile responsiveness.
css_injection = """
        /* Map Card Responsive */
        @media (max-width: 768px) {
            .map-card {
                position: relative !important;
                top: 0 !important;
                left: 0 !important;
                max-width: 100% !important;
                border-radius: 0 !important;
                box-shadow: none !important;
                border-bottom: 1px solid #e5e7eb;
            }
            .map-container {
                height: 600px !important;
                display: flex !important;
                flex-direction: column !important;
            }
            .map-iframe-wrapper {
                flex: 1 !important;
            }
        }
"""

c = c.replace("</style>", css_injection + "\n    </style>")

# Find the map block
old_map = """<!-- ===== MAP ===== -->
            <div class="reveal"
                style="border-radius:1.5rem;overflow:hidden;box-shadow:0 8px 30px rgba(0,0,0,0.1);border:1px solid rgba(37,99,235,0.08);">
                <div
                    style="background:linear-gradient(135deg,#0c1f3f,#1e4d8c);padding:1.25rem 2rem;display:flex;gap:1.5rem;align-items:center;">
                    <i data-lucide="map-pin" style="width:2rem;height:2rem;color:#7eb3f5;flex-shrink:0;"></i>
                    <div>
                        <h3 style="color:white;font-weight:700;margin:0 0 0.2rem 0;font-size:1.1rem;">Leo Plast Industries</h3>
                        <p style="color:#7eb3f5;font-size:0.85rem;margin:0;">Sanniyasigundu Rd, Salem, Tamil Nadu
                        </p>
                    </div>
                </div>
                <iframe
                    src="https://www.google.com/maps?cid=8383691654192911045&g_mp=CiVnb29nbGUubWFwcy5wbGFjZXMudjEuUGxhY2VzLkdldFBsYWNlEAEYASAB&hl=en&gl=IN&source=embed"
                    width="100%" height="380" style="border:0;display:block;" allowfullscreen="" loading="lazy"
                    referrerpolicy="no-referrer-when-downgrade" title="Leoplast Location">
                </iframe>
            </div>"""

new_map = """<!-- ===== MAP ===== -->
            <div class="reveal map-container" style="position:relative;border-radius:1.5rem;overflow:hidden;box-shadow:0 10px 40px rgba(0,0,0,0.08);height:500px;margin-top:2rem;border:1px solid rgba(0,0,0,0.05);background:white;">
                
                <!-- Floating Map Card Overlay -->
                <div class="map-card" style="position:absolute;top:2.5rem;left:2.5rem;background:white;padding:2rem;border-radius:1.25rem;box-shadow:0 15px 35px rgba(0,0,0,0.12);max-width:340px;z-index:10;border:1px solid rgba(0,0,0,0.03);">
                    <div style="display:flex;align-items:center;gap:0.75rem;margin-bottom:1.5rem;">
                        <img src="assets/video-logo.svg" alt="Leo Plast" style="width:28px;height:28px;">
                        <h3 style="color:#0c1f3f;font-weight:800;font-size:1.35rem;margin:0;">Leoplast</h3>
                    </div>
                    
                    <div style="display:flex;flex-direction:column;gap:1.25rem;">
                        <div style="display:flex;gap:1rem;align-items:flex-start;">
                            <i data-lucide="map-pin" style="width:1.25rem;height:1.25rem;color:#dc2626;flex-shrink:0;margin-top:0.15rem;"></i>
                            <p style="color:#4b5563;font-size:0.95rem;margin:0;line-height:1.6;">Sanniyasigundu Rd, Salem,<br>Tamil Nadu 636015</p>
                        </div>
                        <div style="display:flex;gap:1rem;align-items:center;">
                            <i data-lucide="phone" style="width:1.25rem;height:1.25rem;color:#dc2626;flex-shrink:0;"></i>
                            <a href="tel:+917845801233" style="color:#4b5563;font-size:0.95rem;text-decoration:none;font-weight:600;transition:color 0.2s;" onmouseover="this.style.color='#dc2626';" onmouseout="this.style.color='#4b5563';">+91 78458 01233</a>
                        </div>
                        <div style="display:flex;gap:1rem;align-items:center;">
                            <i data-lucide="mail" style="width:1.25rem;height:1.25rem;color:#dc2626;flex-shrink:0;"></i>
                            <a href="mailto:leoplastpipes@gmail.com" style="color:#4b5563;font-size:0.95rem;text-decoration:none;transition:color 0.2s;" onmouseover="this.style.color='#dc2626';" onmouseout="this.style.color='#4b5563';">leoplastpipes@gmail.com</a>
                        </div>
                        <div style="display:flex;gap:1rem;align-items:flex-start;">
                            <i data-lucide="clock" style="width:1.25rem;height:1.25rem;color:#dc2626;flex-shrink:0;margin-top:0.15rem;"></i>
                            <p style="color:#4b5563;font-size:0.95rem;margin:0;line-height:1.6;">Mon-Sat: 10:00 AM – 7:00 PM<br>Sun: Closed</p>
                        </div>
                    </div>
                </div>

                <div class="map-iframe-wrapper" style="width:100%;height:100%;">
                    <iframe
                        src="https://maps.google.com/maps?q=Leo+Plast+Pipes+and+Fittings,+Sanniyasigundu+Rd,+Salem,+Tamil+Nadu+636015&t=&z=14&ie=UTF8&iwloc=&output=embed"
                        width="100%" height="100%" style="border:0;display:block;" allowfullscreen="" loading="lazy"
                        referrerpolicy="no-referrer-when-downgrade" title="Leoplast Location">
                    </iframe>
                </div>
            </div>"""

if old_map in c:
    c = c.replace(old_map, new_map)
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(c)
    print("Map successfully updated.")
else:
    print("Map block not found exactly as written.")
