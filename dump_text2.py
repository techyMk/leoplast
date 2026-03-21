import fitz
pdf_path = r"C:\Users\shoba\Downloads\Leo Plast_Roofings_Final-3.pdf"
doc = fitz.open(pdf_path)
page = doc[2] # 3rd page 

for b in page.get_text("blocks"):
    text = b[4].strip()
    if "Profile" in text or "Standard" in text:
        print(f"FOUND: '{text}' at Y0: {b[1]}, Y1: {b[3]}")
