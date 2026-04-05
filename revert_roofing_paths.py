import os
import re

root_files = ['index.html', 'about.html', 'products.html', 'contact.html']
products_dir = 'products'
product_files = [f for f in os.listdir(products_dir) if f.endswith('.html')]

# 1. Update Root Files
for filename in root_files:
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
        content = content.replace('href="products/roofing.html"', 'href="roofing.html"')
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated root file: {filename}")

# 2. Update Nested Files (products/*.html)
for filename in product_files:
    filepath = os.path.join(products_dir, filename)
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    # If it was linking to roofing.html (sibling), it now needs to link to ../roofing.html
    content = content.replace('href="roofing.html"', 'href="../roofing.html"')
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Updated product file: {filename}")

# 3. Patch roofing.html (now in root)
if os.path.exists('roofing.html'):
    with open('roofing.html', 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Revert asset paths: ../ -> ./ (or root)
    content = content.replace('href="../', 'href="')
    content = content.replace('src="../', 'src="')
    content = content.replace('url(../', 'url(')
    
    # Fix self-link if any (though usually it's roofing.html)
    # Also fix links to other products (now they need products/ prefix)
    # Since we previously updated them TO products/X.html when it was in products/... wait.
    # When roofing was in products/, it linked to bath-fittings.html as a sibling.
    # Now in root, it needs to link to products/bath-fittings.html.
    
    # Actually, my regex v2 script might have changed them. Let's check.
    # If roofing.html was in products/, it used href="bath-fittings.html".
    # Now in root, it needs href="products/bath-fittings.html".
    
    product_list = [
        'ball-valves.html', 'bath-fittings.html', 'cpvc-system.html', 
        'flexible-hoses.html', 'hdpe-system.html', 'manhole-covers.html', 
        'pvc-fittings.html', 'rpvc-pipes.html', 'sanitary-ware.html', 
        'solvents.html', 'upvc-system.html', 'water-storage-tanks.html'
    ]
    for p in product_list:
        content = content.replace(f'href="{p}"', f'href="products/{p}"')

    with open('roofing.html', 'w', encoding='utf-8') as f:
        f.write(content)
    print("Updated roofing.html")
