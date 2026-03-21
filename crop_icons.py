import cv2
import numpy as np
import os

img_path = r"c:\Users\shoba\OneDrive\Documents\leoplast-web-redesign\assets\roofing\page7_full.png"
out_dir = r"c:\Users\shoba\OneDrive\Documents\leoplast-web-redesign\assets\roofing"

img = cv2.imread(img_path)
if img is None:
    print("Could not read image.")
    exit()

hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# Red mask (handling hue wrap-around at 0/180)
lower_red1 = np.array([0, 50, 50])
upper_red1 = np.array([10, 255, 255])
mask1 = cv2.inRange(hsv, lower_red1, upper_red1)

lower_red2 = np.array([160, 50, 50])
upper_red2 = np.array([180, 255, 255])
mask2 = cv2.inRange(hsv, lower_red2, upper_red2)

mask = mask1 + mask2

# Dilate heavily so the disconnected strokes of an icon merge into one giant glob
kernel = np.ones((50, 50), np.uint8)
dilated = cv2.dilate(mask, kernel, iterations=1)

contours, _ = cv2.findContours(dilated, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

boxes = []
for cnt in contours:
    x, y, w, h = cv2.boundingRect(cnt)
    # The application icons are line-art squares roughly 200px-500px on the page scale.
    # Exclude text or huge banners.
    if 100 < w < 800 and 100 < h < 800:
        boxes.append((x, y, w, h))

if not boxes:
    print("No bounding boxes found. Try adjusting parameters.")
    exit()

# Sort boxes top-to-bottom, left-to-right to guarantee correct mapping.
# The grid has row heights that are distinct. We group them by Y with a tolerance.
boxes.sort(key=lambda b: (b[1] // 150, b[0]))

names = ["farming", "houses", "car-shed", "warehouse", "factories", "wall-cladding", "resorts"]

pad = 25
count = 0

for i, (x, y, w, h) in enumerate(boxes):
    if count >= len(names): break
    
    # We don't want to crop random red text up top or bottom.
    # The application icons usually reside in the middle of the page (Y > 500)
    if y < 400 or y > 2500:
        continue

    x1 = max(0, x - pad)
    y1 = max(0, y - pad)
    x2 = min(img.shape[1], x + w + pad)
    y2 = min(img.shape[0], y + h + pad)
    
    cropped = img[y1:y2, x1:x2]
    
    # Convert BGR to BGRA
    tmp = cv2.cvtColor(cropped, cv2.COLOR_BGR2BGRA)
    
    # Make strictly white or very light colors transparent
    white_mask = (tmp[:,:,0] > 220) & (tmp[:,:,1] > 220) & (tmp[:,:,2] > 220)
    tmp[white_mask] = [255, 255, 255, 0]
    
    # Just to be safe and remove text beneath it if any got caught (text is dark blue, not red).
    # You know what, transparent white deals with the background perfectly!

    out_path = os.path.join(out_dir, f"app_icon_{names[count]}.png")
    cv2.imwrite(out_path, tmp)
    print(f"Saved {names[count]} icon -> {w}x{h}")
    count += 1

print(f"Total extracted: {count}")
