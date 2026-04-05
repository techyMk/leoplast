import os
import re

files = [
    'ball-valves.html', 'bath-fittings.html', 'cpvc-system.html', 
    'flexible-hoses.html', 'hdpe-system.html', 'manhole-covers.html', 
    'pvc-fittings.html', 'rpvc-pipes.html', 'sanitary-ware.html', 
    'solvents.html', 'upvc-system.html', 'water-storage-tanks.html', 
    'roofing.html'
]

directory = 'products'

# Regex patterns to find assets and pages that need to be moved up one level
# We look for paths that DON'T already start with ../
patterns = [
    # Assets
    (r'(src|href|url)\s*=\s*["\'](assets/)', r'\1="../\2'),
    (r'(url\()(["\']?)(assets/)', r'\1\2../\3'),
    
    # CSS/JS
    (r'href\s*=\s*["\'](?:\./)?(styles\.css|leoplast\.css)["\']', r'href="../\1"'),
    (r'src\s*=\s*["\'](?:\./)?(leoplast\.js)["\']', r'src="../\1"'),
    
    # Global Pages (Home, About, Products, Contact)
    # Be careful not to match products/X.html links which should NOT be changed
    (r'href\s*=\s*["\'](index\.html|about\.html|products\.html|contact\.html)["\']', r'href="../\1"'),
    
    # Favicon etc
    (r'href\s*=\s*["\'](assets/video-logo\.svg)["\']', r'href="../\1"'),
]

for filename in files:
    filepath = os.path.join(directory, filename)
    if not os.path.exists(filepath):
        print(f"Skipping {filename} - not found.")
        continue
        
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
        
    initial_content = content
    for pattern, replacement in patterns:
        content = re.sub(pattern, replacement, content)
        
    if content != initial_content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Regex-fixed {filename}")
    else:
        print(f"No changes needed for {filename}")
