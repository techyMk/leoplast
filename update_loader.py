import glob

html_files = glob.glob('c:/Users/shoba/OneDrive/Documents/leo-web/leoplast-web/*.html')

old_loader = """    <div id="loader" style="background:#f8faff; z-index: 99999; display: flex; justify-content: center; align-items: center; position: fixed; inset: 0;">
    <div class="loader-scene">
        <div class="falling-drops">
            <div class="drop drop-cyan"></div>
            <div class="drop drop-blue"></div>
            <div class="drop drop-navy"></div>
        </div>
        <img src="assets/logo.webp" class="reveal-logo" alt="Leoplast">
    </div>
</div>"""

new_loader = """    <div id="loader" style="background:#f8faff; z-index: 99999; display: flex; flex-direction: column; justify-content: center; align-items: center; gap: 2rem; position: fixed; inset: 0;">
    <div class="loader-scene">
        <div class="circle-lines out"></div>
        <div class="circle-lines in"></div>
        <img src="assets/logo.webp" class="loader-logo" alt="Leoplast">
    </div>
    <div class="dot-loader">
        <div class="dot"></div>
        <div class="dot"></div>
        <div class="dot"></div>
    </div>
</div>"""

for f in html_files:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    if old_loader in content:
        content = content.replace(old_loader, new_loader)
        with open(f, 'w', encoding='utf-8') as file:
            file.write(content)
        print(f'Updated {f}')
    else:
        print(f'Loader not found in {f}')
