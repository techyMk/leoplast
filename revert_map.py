import sys

file_path = "c:/Users/shoba/OneDrive/Documents/leoplast-web-redesign/contact.html"

with open(file_path, "r", encoding="utf-8") as f:
    c = f.read()

# Current map layout with map-card
start_marker = "<!-- ===== MAP ===== -->"
end_marker = "    <!-- ===== FOOTER ===== -->"

start_idx = c.find(start_marker)
end_idx = c.find(end_marker)

if start_idx == -1 or end_idx == -1:
    print("Could not find map block")
    sys.exit()

new_map = """<!-- ===== MAP ===== -->
            <div class="reveal"
                style="border-radius:1.5rem;overflow:hidden;box-shadow:0 8px 30px rgba(0,0,0,0.1);border:1px solid rgba(37,99,235,0.08);margin-top:2rem;">
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
                    src="https://maps.google.com/maps?q=Leo+Plast+Pipes+and+Fittings,+Sanniyasigundu+Rd,+Salem,+Tamil+Nadu+636015&t=&z=14&ie=UTF8&iwloc=&output=embed"
                    width="100%" height="450" style="border:0;display:block;" allowfullscreen="" loading="lazy"
                    referrerpolicy="no-referrer-when-downgrade" title="Leoplast Location">
                </iframe>
            </div>
        </div>
    </section>

"""

# Replace block
c = c[:start_idx] + new_map + c[end_idx:]

with open(file_path, "w", encoding="utf-8") as f:
    f.write(c)
print("Map completely reverted!")
