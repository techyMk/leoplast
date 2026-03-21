import sys

file_path = "c:/Users/shoba/OneDrive/Documents/leoplast-web-redesign/roofing.html"

with open(file_path, "r", encoding="utf-8") as f:
    c = f.read()

start_marker = '<h4 style="font-size:1.65rem;font-weight:800;color:#0c1f3f;margin-bottom:2rem;text-align:center;">Profile Diagram</h4>'
end_marker = '<!-- Right: Sheet Length -->'

start_idx = c.find(start_marker)
end_idx = c.find(end_marker)

if start_idx == -1 or end_idx == -1:
    print("Could not find profile diagram block.")
    sys.exit()

new_block = """<h4 style="font-size:1.65rem;font-weight:800;color:#0c1f3f;margin-bottom:2rem;text-align:center;">Profile Diagram</h4>
                        <div style="background:white;border-radius:1.5rem;padding:2rem;text-align:center;box-shadow:0 10px 30px rgba(0,0,0,0.05);margin-bottom:2rem;display:flex;align-items:center;justify-content:center;">
                            <img src="assets/roofing/profile_diagram.png" alt="Profile Diagram Dimensions" style="width:100%;max-width:850px;height:auto;filter:drop-shadow(0 4px 6px rgba(0,0,0,0.05));">
                        </div>
                        """

c = c[:start_idx] + new_block + c[end_idx:]

with open(file_path, "w", encoding="utf-8") as f:
    f.write(c)

print("Profile Diagram swapped!")
