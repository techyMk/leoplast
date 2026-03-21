import sys
import re

file_path = "c:/Users/shoba/OneDrive/Documents/leoplast-web-redesign/about.html"
with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# Pattern to find the entire slider block by its unique start
pattern = r'(<div class="reveal" style="margin-top:4rem;max-width:650px;margin-left:auto;margin-right:auto;overflow:hidden;position:relative;border-radius:1\.5rem;">.*?<\/style>\s*<\/div>)'

match = re.search(pattern, content, re.DOTALL)
if not match:
    print("Not found")
    sys.exit()

old_slider = match.group(1)

new_slider = """<div class="reveal" style="margin-top:5rem;max-width:950px;margin-left:auto;margin-right:auto;overflow:hidden;position:relative;border-radius:1.5rem;box-shadow:0 25px 50px -12px rgba(30,58,110,0.25);">
                <div style="display:flex;width:300%;animation: slideInfPremium 12s infinite;will-change:transform;">
                    
                    <!-- Image 1 -->
                    <div style="width:33.3333%;flex-shrink:0;position:relative;">
                        <img src="assets/about/slide1.webp" alt="Infrastructure 1" style="width:100%;height:100%;display:block;aspect-ratio:16/9;object-fit:cover;">
                        <div style="position:absolute;bottom:0;left:0;right:0;padding:2.5rem 2rem;background:linear-gradient(to top, rgba(0,0,0,0.85), transparent);color:white;">
                            <h3 style="font-size:1.75rem;font-weight:800;margin:0;">Advanced Production Facilities</h3>
                            <p style="color:#bfdbfe;margin:0.5rem 0 0 0;font-size:1.05rem;line-height:1.6;">Equipped with cutting-edge machinery designed for precise, consistent, and scalable high-volume manufacturing.</p>
                        </div>
                    </div>
                    
                    <!-- Image 2 -->
                    <div style="width:33.3333%;flex-shrink:0;position:relative;">
                        <img src="assets/about/slide2.webp" alt="Infrastructure 2" style="width:100%;height:100%;display:block;aspect-ratio:16/9;object-fit:cover;">
                        <div style="position:absolute;bottom:0;left:0;right:0;padding:2.5rem 2rem;background:linear-gradient(to top, rgba(0,0,0,0.85), transparent);color:white;">
                            <h3 style="font-size:1.75rem;font-weight:800;margin:0;">Precision & Quality Control</h3>
                            <p style="color:#bfdbfe;margin:0.5rem 0 0 0;font-size:1.05rem;line-height:1.6;">Every product undergoes rigorous, technology-driven testing protocols before reaching the hands of our clients.</p>
                        </div>
                    </div>
                    
                    <!-- Image 1 Clone -->
                    <div style="width:33.3333%;flex-shrink:0;position:relative;">
                        <img src="assets/about/slide1.webp" alt="Infrastructure 1 Clone" style="width:100%;height:100%;display:block;aspect-ratio:16/9;object-fit:cover;">
                        <div style="position:absolute;bottom:0;left:0;right:0;padding:2.5rem 2rem;background:linear-gradient(to top, rgba(0,0,0,0.85), transparent);color:white;">
                            <h3 style="font-size:1.75rem;font-weight:800;margin:0;">Advanced Production Facilities</h3>
                            <p style="color:#bfdbfe;margin:0.5rem 0 0 0;font-size:1.05rem;line-height:1.6;">Equipped with cutting-edge machinery designed for precise, consistent, and scalable high-volume manufacturing.</p>
                        </div>
                    </div>

                </div>
                <style>
                    @keyframes slideInfPremium {
                        0% { transform: translateX(0); }
                        35% { transform: translateX(0); animation-timing-function: cubic-bezier(0.645, 0.045, 0.355, 1); }
                        45% { transform: translateX(-33.3333%); }
                        85% { transform: translateX(-33.3333%); animation-timing-function: cubic-bezier(0.645, 0.045, 0.355, 1); }
                        95% { transform: translateX(-66.6666%); }
                        100% { transform: translateX(-66.6666%); }
                    }
                </style>
            </div>"""

content = content.replace(old_slider, new_slider)
with open(file_path, "w", encoding="utf-8") as f:
    f.write(content)

print("Updated slider perfectly.")
