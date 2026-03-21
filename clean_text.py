import cv2
import numpy as np
import glob
import os

out_dir = r"c:\Users\shoba\OneDrive\Documents\leoplast-web-redesign\assets\roofing"
files = glob.glob(os.path.join(out_dir, "app_icon_*.png"))

for f in files:
    img = cv2.imread(f, cv2.IMREAD_UNCHANGED)
    if img is None: continue
    
    if img.shape[2] == 3:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2BGRA)
    
    B = img[:,:,0].astype(np.int32)
    G = img[:,:,1].astype(np.int32)
    R = img[:,:,2].astype(np.int32)
    
    max_bg = np.maximum(B, G)
    not_red = (R - max_bg) < 15
    
    img[not_red] = [255, 255, 255, 0]
    
    cv2.imwrite(f, img)
    print("Cleaned", f)

print("All text eliminated.")
