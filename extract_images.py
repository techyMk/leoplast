import fitz
import os

pdf_path = r"C:\Users\shoba\Downloads\Leo Plast_Roofings_Final-3.pdf"
doc = fitz.open(pdf_path)
page = doc[6] # Page 7 

images = page.get_images(full=True)
print(f"Found {len(images)} embedded images on page 7.")
for i, img in enumerate(images):
    xref = img[0]
    pix = fitz.Pixmap(doc, xref)
    # ignore extremely large background images
    if pix.width < 1000 and pix.height < 1000:
        pix.save(f"c:/Users/shoba/OneDrive/Documents/leoplast-web-redesign/assets/roofing/extracted_img_{i}.png")
        print(f"Saved extracted_img_{i}.png ({pix.width}x{pix.height})")
