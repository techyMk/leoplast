import glob
import re
import os

html_files = glob.glob(r"c:\Users\shoba\OneDrive\Documents\leoplast-web-redesign\*.html")

p1 = re.compile(r'\s*<a href="[^"]*".*?>Privacy Policy</a>', re.IGNORECASE)
p2 = re.compile(r'\s*<a href="[^"]*".*?>Terms of Service</a>', re.IGNORECASE)

count = 0
for fpath in html_files:
    with open(fpath, "r", encoding="utf-8") as f:
        c = f.read()
    
    original = c
    c = p1.sub("", c)
    c = p2.sub("", c)

    if c != original:
        with open(fpath, "w", encoding="utf-8") as f:
            f.write(c)
        count += 1
        print(f"Removed fake policy links from {os.path.basename(fpath)}")

print(f"Total files updated: {count}")
