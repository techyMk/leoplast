import sys

file_path = "c:/Users/shoba/OneDrive/Documents/leoplast-web-redesign/cpvc-system.html"

with open(file_path, "r", encoding="utf-8") as f:
    c = f.read()

mapping = [
    ('src="assets/products/cPVC-Plumbing-Systems.webp" alt="cPVC Pipes', 'src="assets/products/cpvc-systems/CPVC-Pipes-SDR-11-SDR-13.5.webp" alt="cPVC Pipes'),
    ('src="" alt="Elbow 90°"', 'src="assets/products/cpvc-systems/elbow-90.png" alt="Elbow 90°"'),
    ('src="" alt="Tee"', 'src="assets/products/cpvc-systems/tee-1.webp" alt="Tee"'),
    ('src="" alt="Coupler"', 'src="assets/products/cpvc-systems/coupler-1-1.webp" alt="Coupler"'),
    ('src="" alt="End Cap"', 'src="assets/products/cpvc-systems/end-cap.webp" alt="End Cap"'),
    ('src="" alt="FTA (Female Threaded Adapter)"', 'src="assets/products/cpvc-systems/FTA.webp" alt="FTA (Female Threaded Adapter)"'),
    ('src="" alt="MTA (Male Threaded Adapter)"', 'src="assets/products/cpvc-systems/MTA-1.webp" alt="MTA (Male Threaded Adapter)"'),
    ('src="" alt="Union"', 'src="assets/products/cpvc-systems/union-1.webp" alt="Union"'),
    ('src="" alt="Tank Nipple"', 'src="assets/products/cpvc-systems/tank-nipple-1.webp" alt="Tank Nipple"'),
    ('src="" alt="Reducer"', 'src="assets/products/cpvc-systems/reducer.webp" alt="Reducer"'),
    ('src="" alt="Brass Elbow"', 'src="assets/products/cpvc-systems/brass-elbow-1.webp" alt="Brass Elbow"'),
    ('src="" alt="Brass Tee"', 'src="assets/products/cpvc-systems/brass-tee-1.webp" alt="Brass Tee"'),
    ('src="" alt="Brass FTA"', 'src="assets/products/cpvc-systems/brass-FTA-1.webp" alt="Brass FTA"'),
    ('src="" alt="Brass MTA"', 'src="assets/products/cpvc-systems/MTA-2.webp" alt="Brass MTA"'),
    ('src="" alt="Elbow 45°"', 'src="assets/products/cpvc-systems/Shoe.webp" alt="Elbow 45°"'),
    ('src="" alt="Bush"', 'src="assets/products/cpvc-systems/bush.webp" alt="Bush"'),
    ('src="" alt="Concealed Valve"', 'src="assets/products/cpvc-systems/Concealed-Valve.webp" alt="Concealed Valve"')
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
    print("All cPVC plumbing assets successfully mapped into the HTML.")
else:
    print("No changes were made. File might already be mapped.")
