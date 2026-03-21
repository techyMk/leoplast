import cv2
import numpy as np
import os

img_path = r"c:\Users\shoba\OneDrive\Documents\leoplast-web-redesign\assets\roofing\page7_full.png"
out_dir = r"c:\Users\shoba\OneDrive\Documents\leoplast-web-redesign\assets\roofing"

img = cv2.imread(img_path)
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# Red mask
lower_red1 = np.array([0, 50, 50])
upper_red1 = np.array([10, 255, 255])
mask1 = cv2.inRange(hsv, lower_red1, upper_red1)

lower_red2 = np.array([160, 50, 50])
upper_red2 = np.array([180, 255, 255])
mask2 = cv2.inRange(hsv, lower_red2, upper_red2)

mask = mask1 + mask2

# Use a MASSIVE dilation kernel. The red mask only sees the red icon strokes, 
# not the dark text underneath. So making this huge guarantees all floating
# pieces of the icon (like wheels, waves, disconnected lines) merge into one box.
kernel = np.ones((150, 150), np.uint8)
dilated = cv2.dilate(mask, kernel, iterations=1)

contours, _ = cv2.findContours(dilated, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

boxes = []
for cnt in contours:
    x, y, w, h = cv2.boundingRect(cnt)
    if 100 < w < 1000 and 100 < h < 1000:
        boxes.append((x, y, w, h))

boxes.sort(key=lambda b: (b[1] // 200, b[0]))

names = ["farming", "houses", "car-shed", "warehouse", "factories", "wall-cladding", "resorts"]

pad = 30
count = 0

for i, (x, y, w, h) in enumerate(boxes):
    if count >= len(names): break
    if y < 400 or y > 2500:
        continue

    x1 = max(0, x - pad)
    y1 = max(0, y - pad)
    x2 = min(img.shape[1], x + w + pad)
    y2 = min(img.shape[0], y + h + pad)
    
    cropped = img[y1:y2, x1:x2]
    
    tmp = cv2.cvtColor(cropped, cv2.COLOR_BGR2BGRA)
    
    # Make anything strictly white or light gray transparent
    white_mask = (tmp[:,:,0] > 220) & (tmp[:,:,1] > 220) & (tmp[:,:,2] > 220)
    tmp[white_mask] = [255, 255, 255, 0]

    out_path = os.path.join(out_dir, f"app_icon_{names[count]}.png")
    cv2.imwrite(out_path, tmp)
    print(f"Fixed & Saved {names[count]} -> {w}x{h}")
    count += 1
