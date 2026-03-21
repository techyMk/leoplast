import sys

file_path = "c:/Users/shoba/OneDrive/Documents/leoplast-web-redesign/roofing.html"
with open(file_path, "r", encoding="utf-8") as f:
    c = f.read()

# Replace the specific CSS causing the misalignment.
c = c.replace("width:85px;height:auto;", "width:85px;height:75px;object-fit:contain;")

with open(file_path, "w", encoding="utf-8") as f:
    f.write(c)

print("Alignment fixed.")
