import sys

js_path = r'c:\Users\shoba\OneDrive\Documents\leoplast-web-redesign\leoplast.js'
with open(js_path, 'r', encoding='utf-8') as f:
    js = f.read()

credit_code = """
// ========================
// GLOBAL FOOTER CREDIT
// ========================
document.addEventListener("DOMContentLoaded", function() {
    const footers = document.getElementsByTagName("footer");
    if (footers.length > 0) {
        const footer = footers[footers.length - 1]; // Use the last/main footer
        
        // Prevent duplicate injection
        if (!document.getElementById("dev-credit")) {
            
            // IF THE URL CHANGES IN THE FUTURE, YOU CAN EDIT THIS VARIABLE RIGHT HERE:
            const devUrl = "https://techymk.vercel.app/";
            
            const devHtml = `
            <div id="dev-credit" style="margin-top:3rem;border-top:1px solid rgba(255,255,255,0.05);padding-top:1.5rem;font-size:0.8rem;color:#6b7280;display:flex;justify-content:center;align-items:center;gap:0.4rem;flex-wrap:wrap;letter-spacing:0.02em;">
                <span>Designed & Developed by</span>
                <a href="${devUrl}" target="_blank" rel="noopener noreferrer" style="color:#60a5fa;text-decoration:none;font-weight:700;transition:color 0.2s;" onmouseover="this.style.color='#ffffff'" onmouseout="this.style.color='#60a5fa'">TechyMK</a>
            </div>`;
            
            footer.insertAdjacentHTML("beforeend", devHtml);
        }
    }
});
"""

if 'dev-credit' not in js:
    with open(js_path, 'a', encoding='utf-8') as f:
        f.write('\n' + credit_code + '\n')
    print('Global footer logic injected successfully.')
else:
    print('Footer logic already present.')
