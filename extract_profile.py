import fitz
import os
import cv2
import numpy as np

pdf_path = r"C:\Users\shoba\Downloads\Leo Plast_Roofings_Final-3.pdf"
out_path = r"c:\Users\shoba\OneDrive\Documents\leoplast-web-redesign\assets\roofing\profile_diagram_raw.png"
final_path = r"c:\Users\shoba\OneDrive\Documents\leoplast-web-redesign\assets\roofing\profile_diagram.png"

doc = fitz.open(pdf_path)
page = doc[2] # 3rd page 

# Locate bounding texts
title_rects = page.search_for("Profile Diagram")
bottom_rects = page.search_for("Standard Sheet Length")

if not title_rects or not bottom_rects:
    print("Could not find text markers.")
    exit()

r_top = title_rects[0]
r_bot = bottom_rects[0]

# Give some padding to the crop box. Left/Right can be the full page width except for small margins.
crop_rect = fitz.Rect(40, r_top.y1 + 5, page.rect.width - 40, r_bot.y0 - 5)

# High-res rendering
mat = fitz.Matrix(4.0, 4.0)
pix = page.get_pixmap(matrix=mat, clip=crop_rect)
pix.save(out_path)
print(f"Extracted raw region: {pix.width}x{pix.height}")

# Post-processing: Make background transparent and remove faint watermark.
img = cv2.imread(out_path)
if img is not None:
    # Convert to BGRA
    tmp = cv2.cvtColor(img, cv2.COLOR_BGR2BGRA)
    
    # We want to keep the red line and the dark blue/black arrows/text.
    # We want to eliminate the white background and faint gray watermark lines.
    # The watermark is very light gray/beige.
    
    # Let's assess pixel values:
    B = tmp[:,:,0].astype(np.int32)
    G = tmp[:,:,1].astype(np.int32)
    R = tmp[:,:,2].astype(np.int32)
    
    # Dark text goes down to B=~50, G=~50, R=~50 (or blueish)
    # Red line has high R (>150), low G/B
    # White background is >240 everywhere
    # Faint watermark lines are usually > 210
    
    # Condition to REMOVE: 
    # If the pixel is very light (B > 200, G > 200, R > 200) -> Transparent
    light_mask = (B > 190) & (G > 190) & (R > 190)
    
    tmp[light_mask] = [255, 255, 255, 0]
    
    cv2.imwrite(final_path, tmp)
    print("Post-processed to transparent background!")
else:
    print("Failed to read raw image.")
