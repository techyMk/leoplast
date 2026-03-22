import sys

file_path = "c:/Users/shoba/OneDrive/Documents/leoplast-web-redesign/upvc-system.html"

with open(file_path, "r", encoding="utf-8") as f:
    c = f.read()

mapping = [
    ('src="assets/products/uPVC-Potable-Water-Plumbing-Systems.png" alt="uPVC Pipes', 'src="assets/products/upvc-systems/UPVC-PIPES.webp" alt="uPVC Pipes'),
    ('src="" alt="Elbow 90°"', 'src="assets/products/upvc-systems/upvc-elbow-90.webp" alt="Elbow 90°"'),
    ('src="" alt="Tee"', 'src="assets/products/upvc-systems/upvc-tee.webp" alt="Tee"'),
    ('src="" alt="Coupler"', 'src="assets/products/upvc-systems/upvc-coupler.webp" alt="Coupler"'),
    ('src="" alt="End Cap"', 'src="assets/products/upvc-systems/upvc-end-cap.webp" alt="End Cap"'),
    ('src="" alt="MTA (Male Threaded Adapter)"', 'src="assets/products/upvc-systems/upvc-MTA.webp" alt="MTA (Male Threaded Adapter)"'),
    ('src="" alt="FTA (Female Threaded Adapter)"', 'src="assets/products/upvc-systems/upvc-FTA.webp" alt="FTA (Female Threaded Adapter)"'),
    ('src="" alt="Tank Nipple"', 'src="assets/products/upvc-systems/upvc-tank-nipple.webp" alt="Tank Nipple"'),
    ('src="" alt="Elbow 45°"', 'src="assets/products/upvc-systems/upvc-elbow-45.webp" alt="Elbow 45°"'),
    ('src="" alt="Reducer"', 'src="assets/products/upvc-systems/upvc-Reducer.webp" alt="Reducer"'),
    ('src="" alt="Union"', 'src="assets/products/upvc-systems/upvc-union.webp" alt="Union"'),
    ('src="" alt="Brass Elbow"', 'src="assets/products/upvc-systems/upvc-brass-elbow.webp" alt="Brass Elbow"'),
    ('src="" alt="Brass Tee"', 'src="assets/products/upvc-systems/upvc-brass-tee.webp" alt="Brass Tee"'),
    ('src="" alt="Brass FTA"', 'src="assets/products/upvc-systems/Brass-FTA.webp" alt="Brass FTA"'),
    ('src="" alt="cPVC to uPVC Connector"', 'src="assets/products/upvc-systems/upvc-cpvc-to-upvc-connecter.webp" alt="cPVC to uPVC Connector"')
]

original_c = c
for target, replacement in mapping:
    if target in c:
        c = c.replace(target, replacement)
    else:
        print(f"Warning: Could not find target: {target}")

if c != original_c:
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(c)
    print("All uPVC plumbing assets successfully mapped into the HTML.")
else:
    print("No changes were made. File might already be mapped.")
