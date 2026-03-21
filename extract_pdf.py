import fitz
import os

pdf_path = r"C:\Users\shoba\Downloads\Leo Plast_Roofings_Final-3.pdf"
out_dir = r"c:\Users\shoba\OneDrive\Documents\leoplast-web-redesign\assets\roofing"
os.makedirs(out_dir, exist_ok=True)

doc = fitz.open(pdf_path)
page = doc[6] # Page 7 

# The icons are arranged in 3 rows or similar. We can just render the whole page and then crop using PIL, or use fitz.
# Let's render the entire page at high DPI.
mat = fitz.Matrix(4.0, 4.0) # 4x scale for high crisp resolution
pix = page.get_pixmap(matrix=mat)
img_path = os.path.join(out_dir, "page7_full.png")
pix.save(img_path)

print(f"Saved full page to {img_path}")
print(f"Page dimensions: {pix.width}x{pix.height}")
