import os

files = [
    'ball-valves.html', 'bath-fittings.html', 'cpvc-system.html', 
    'flexible-hoses.html', 'hdpe-system.html', 'manhole-covers.html', 
    'pvc-fittings.html', 'rpvc-pipes.html', 'sanitary-ware.html', 
    'solvents.html', 'upvc-system.html', 'water-storage-tanks.html', 
    'roofing.html'
]

directory = 'products'

replacements = {
    'href="./styles.css"': 'href="../styles.css"',
    'href="./leoplast.css"': 'href="../leoplast.css"',
    'src="./leoplast.js"': 'src="../leoplast.js"',
    'src="assets/': 'src="../assets/',
    'href="index.html"': 'href="../index.html"',
    'href="about.html"': 'href="../about.html"',
    'href="products.html"': 'href="../products.html"',
    'href="contact.html"': 'href="../contact.html"',
    'url(assets/': 'url(../assets/',
    'href="assets/': 'href="../assets/',
    'data-lucide': 'data-lucide' # Just a placeholder to ensure no accidental breaks
}

for filename in files:
    filepath = os.path.join(directory, filename)
    if not os.path.exists(filepath):
        print(f"Skipping {filename} - not found.")
        continue
        
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
        
    for old, new in replacements.items():
        content = content.replace(old, new)
        
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Updated {filename}")
