import fitz
import os
import cv2
import numpy as np

pdf_path = r"C:\Users\shoba\Downloads\Leo Plast_Roofings_Final-3.pdf"
out_path = r"c:\Users\shoba\OneDrive\Documents\leoplast-web-redesign\assets\roofing\profile_diagram_raw.png"
final_path = r"c:\Users\shoba\OneDrive\Documents\leoplast-web-redesign\assets\roofing\profile_diagram.png"

doc = fitz.open(pdf_path)
page = doc[2]

# Y bounds for the Profile Diagram dimension markers
crop_rect = fitz.Rect(80, 430, page.rect.width - 80, 500)

mat = fitz.Matrix(4.0, 4.0)
pix = page.get_pixmap(matrix=mat, clip=crop_rect)
pix.save(out_path)
print(f"Extracted raw region: {pix.width}x{pix.height}")

img = cv2.imread(out_path)
if img is not None:
    tmp = cv2.cvtColor(img, cv2.COLOR_BGR2BGRA)
    
    B = tmp[:,:,0].astype(np.int32)
    G = tmp[:,:,1].astype(np.int32)
    R = tmp[:,:,2].astype(np.int32)
    
    # Convert white/light background to transparent
    light_mask = (B > 190) & (G > 190) & (R > 190)
    tmp[light_mask] = [255, 255, 255, 0]
    
    cv2.imwrite(final_path, tmp)
    print("Post-processed background!")
else:
    print("Failed to read raw image.")
