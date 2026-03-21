import sys

file_path = "c:/Users/shoba/OneDrive/Documents/leoplast-web-redesign/about.html"
with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# 1. Update Hero Text
old_hero = "40 years of trust, innovation, and excellence in plumbing solutions across Tamil Nadu."
new_hero = "With nearly 40 years of experience, Leo Plast is a trusted leader in plumbing solutions, dedicated to quality and innovation. As Tamil Nadu’s premier manufacturer, we offer a diverse range of products, including PVC, uPVC, and cPVC pipes and fittings, HDPE pipes, water tanks, and valves. Our certified products meet the highest standards, catering to residential and agricultural needs with reliability and excellence."
content = content.replace(old_hero, new_hero)
# Make the max-width larger for the longer paragraph
content = content.replace("max-width:500px;margin:0 auto;line-height:1.7;", "max-width:800px;margin:0 auto;line-height:1.7;")


# 2. Update Who Are We
old_who1 = "At Leo Plast, we believe that plumbing solutions should be more than just functional — they should inspire confidence and create lasting value. With nearly <strong>40 years of commitment to excellence</strong>, Leo Plast Pipes & Fittings has evolved into one of Tamil Nadu's leading manufacturers, specializing in a comprehensive range of high-quality piping and water storage solutions."
new_who1 = "\"Quality and trust are the foundations of every successful relationship.\" At Leo Plast, we believe that plumbing solutions should be more than just functional—they should inspire confidence and create lasting value. With nearly <strong>40 years of commitment to excellence</strong>, Leo Plast Pipes & Fittings has evolved into one of Tamil Nadu’s leading manufacturers, specializing in a comprehensive range of high-quality piping and water storage solutions."

old_who2 = "Our extensive product portfolio includes <strong>PVC, cPVC, and uPVC (ASTM) pipes and fittings</strong>, alongside durable water storage tanks crafted using advanced blow-molding and roto-molding techniques. We also offer HDPE hoses for efficient irrigation and PTMT water taps."
new_who2 = "Our extensive product portfolio includes <strong>PVC, cPVC, and uPVC (ASTM) pipes and fittings</strong>, alongside durable water storage tanks crafted using advanced blow-molding and roto-molding techniques. Additionally, we offer HDPE hoses designed for efficient irrigation and PTMT water taps, providing a versatile selection tailored to meet the diverse needs of residential, commercial, and agricultural sectors across Tamil Nadu."

old_who3 = "Driven by a passion for quality, our journey starts with sourcing the finest raw materials and culminates in the delivery of reliable, certified products directly to your doorstep — each meticulously crafted with safety and durability in mind."
new_who3 = "Driven by a passion for quality, our journey starts with sourcing the finest raw materials and culminates in the delivery of reliable, certified products directly to your doorstep. Each product that leaves our facilities is meticulously crafted with safety and durability in mind, backed by cutting-edge technology and a skilled workforce. We’re proud to serve homes and businesses with solutions that make a real difference."

new_who4 = "<br><br>\n                    <p style=\"color:#4b5563;line-height:1.9;\">At Leo Plast, our commitment goes beyond products; it’s about building trust, delivering peace of mind, and fostering lasting relationships with every connection. Choose Leo Plast for quality, dependability, and a legacy of excellence in piping and water storage solutions.</p>"

content = content.replace(old_who1, new_who1)
content = content.replace(old_who2, new_who2)
content = content.replace(old_who3, new_who3 + new_who4)


# 3. Update Infrastructure
old_infra = "Backed by advanced manufacturing units and a nationwide dealer network, we deliver quality at scale."
new_infra = "Backed by a team of over 250 employees and a network of 2,000+ dealers, Leo Plast operates two advanced manufacturing units with industry-standard machinery. Our world-class infrastructure supports 14 diverse product categories, enabling us to deliver reliable piping and water storage solutions across Tamil Nadu and beyond."
content = content.replace(old_infra, new_infra)
content = content.replace("max-width:600px;margin:1rem auto 0;line-height:1.8;", "max-width:850px;margin:1rem auto 0;line-height:1.8;")


# 4. Update Roadmap
# Extract roadmap block
import re
pattern = r"(<!-- Bulletproof CSS Flex Timeline -->.*?)(?:\n\s*</section>\s*\n)"
match = re.search(pattern, content, re.DOTALL)
if match:
    old_roadmap_full = match.group(1)

    timeline_items = [
        ("2000", "Launch of HDPE Hose", "Leo Plast introduces the HDPE Hose, an innovative solution for irrigation applications.", "#1e3a6e", "#1a56db"),
        ("2016", "Launch of Leo Plast PVC Pipes", "Leo Plast expands its product line with the introduction of PVC pipes, designed for durability and reliability.", "#1a56db", "#2563eb"),
        ("2019", "Launch of PVC, cPVC, and uPVC Fittings", "The product range grows with a full suite of PVC, cPVC, and uPVC fittings, offering comprehensive plumbing solutions.", "#2563eb", "#3b82f6"),
        ("2021", "Establishment of Leo Plast Trichy Stock Point", "Expanding reach with a new stock point in Trichy, improving service and distribution capabilities across Tamil Nadu.", "#3b82f6", "#60a5fa"),
        ("2023", "Launch of Leo Plast Prime Roto Mould Tanks", "Continuing innovation, Leo Plast introduces Prime Roto Mould Tanks, reinforcing its commitment to advanced, high-quality storage solutions.", "#60a5fa", "#2563eb"),
        ("2024", "Establishment of Leo Plast Madurai Stock Point", "Enhancing accessibility with a new stock point in Madurai, strengthening service and distribution capabilities across Tamil Nadu.", "#2563eb", None), # Last item
    ]

    new_roadmap = "<!-- Bulletproof CSS Flex Timeline -->\n            <div style=\"display:flex;flex-direction:column;width:100%; position:relative;\">\n"
    
    for i, (year, title, desc, bg, next_bg) in enumerate(timeline_items):
        is_last = (i == len(timeline_items) - 1)
        delay_class = f" reveal-delay-{i%5}" if i > 0 else ""
        
        line_html = ""
        if is_last:
            pass # No line descending from last item
        elif i == 0:
            line_html = f'<div style="position:absolute;top:18px;bottom:0;width:3px;background:linear-gradient(to bottom, {bg}, {next_bg});border-radius:3px;"></div>'
        else:
            line_html = f'<div style="position:absolute;top:0;bottom:0;width:3px;background:linear-gradient(to bottom, {bg}, {next_bg});border-radius:3px;"></div>'
        
        card_style = ""
        card_tag_style = ""
        tag_text = ""
        
        # Styles mapping based on original gradient choices
        if is_last:
            card_style = "background:linear-gradient(135deg,#eff6ff,#dbeafe);border-radius:1.25rem;padding:2.25rem;box-shadow:0 10px 30px rgba(37,99,235,0.15);border:1.5px solid #bfdbfe;transition:transform 0.3s;"
            card_tag_style = "color:#1a56db;"
            tag_text = "Today & Beyond"
            circle_bg = "#bfdbfe"
            circle_border = "#2563eb"
        else:
            card_style = "background:white;border-radius:1.25rem;padding:2rem 2.25rem;box-shadow:0 4px 20px rgba(30,58,110,0.06);border:1px solid rgba(30,58,110,0.05);transition:transform 0.3s, box-shadow 0.3s;"
            card_tag_style = f"color:{bg};"
            tag_text = "Milestone"
            background_text_modifiers = {
                "2000": "Innovation",
                "2016": "Product Growth",
                "2019": "Full Portfolio",
                "2021": "Expansion",
                "2023": "Innovation"
            }
            tag_text = background_text_modifiers.get(year, "Milestone")
            circle_bg = bg
            circle_border = bg
        
        hover_style = "onmouseover=\"this.style.transform='translateY(-6px)';this.style.boxShadow='0 12px 30px rgba(30,58,110,0.12)';\" onmouseout=\"this.style.transform='translateY(0)';this.style.boxShadow='0 4px 20px rgba(30,58,110,0.06)';\"" if not is_last else "onmouseover=\"this.style.transform='translateY(-6px)';\" onmouseout=\"this.style.transform='translateY(0)';\""

        bot_pad = "0" if is_last else "3.5rem"

        item_html = f"""
                <!-- {year} -->
                <div class="reveal{delay_class}" style="display:flex;align-items:stretch;width:100%;">
                    <div style="width:120px;text-align:right;padding-right:2rem;padding-top:10px;flex-shrink:0;">
                        <span style="font-size:1.6rem;font-weight:800;color:{bg};">{year}</span>
                    </div>
                    <div style="display:flex;flex-direction:column;align-items:center;position:relative;width:24px;flex-shrink:0;">
                        {line_html}
                        <div style="width:16px;height:16px;border-radius:50%;background:{circle_bg};border:4px solid white;box-shadow:0 0 0 4px {circle_border};position:relative;z-index:2;margin-top:10px;box-sizing:content-box;"></div>
                    </div>
                    <div style="flex:1;padding-left:2.5rem;padding-bottom:{bot_pad};">
                        <div style="{card_style}" {hover_style}>
                            <span style="font-size:0.85rem;font-weight:700;{card_tag_style}text-transform:uppercase;letter-spacing:0.08em;display:block;margin-bottom:0.6rem;">{tag_text}</span>
                            <h4 style="font-size:1.25rem;font-weight:800;color:#0c1f3f;margin:0 0 0.5rem 0;">{title}</h4>
                            <p style="color:#4b5563;font-size:1rem;line-height:1.7;margin:0;">{desc}</p>
                        </div>
                    </div>
                </div>
"""
        new_roadmap += item_html
    
    new_roadmap += "\n            </div>"
    
    content = content.replace(old_roadmap_full, new_roadmap)


with open(file_path, "w", encoding="utf-8") as f:
    f.write(content)

print("Copy successfully updated.")
