import fitz
pdf_path = r"C:\Users\shoba\Downloads\Leo Plast_Roofings_Final-3.pdf"
doc = fitz.open(pdf_path)
page = doc[2] # 3rd page 

blocks = page.get_text("blocks")
for b in blocks:
    print(b[:4], b[4].strip())
