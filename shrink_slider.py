import sys

file_path = "c:/Users/shoba/OneDrive/Documents/leoplast-web-redesign/about.html"
with open(file_path, "r", encoding="utf-8") as f:
    c = f.read()

c = c.replace("max-width:950px;margin-left:auto;margin-right:auto;overflow:hidden;position:relative;border-radius:1.5rem;box-shadow:0 25px 50px -12px rgba(30,58,110,0.25);", "max-width:700px;margin-left:auto;margin-right:auto;overflow:hidden;position:relative;border-radius:1.5rem;box-shadow:0 25px 50px -12px rgba(30,58,110,0.25);")
with open(file_path, "w", encoding="utf-8") as f:
    f.write(c)
print("Shrinked.")
