import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Reorder sections
# Find the Roofing Section
roofing_pattern = re.compile(r'    <!-- ============================\n     ROOFING SECTION\n     ============================ -->.*?    <!-- ============================\n     FOOTER\n     ============================ -->', re.DOTALL)
roofing_match = roofing_pattern.search(content)

if roofing_match:
    full_match = roofing_match.group(0)
    footer_start = full_match.rfind('    <!-- ============================\n     FOOTER')
    roofing_content = full_match[:footer_start]
    
    # Remove roofing section from bottom
    content = content.replace(roofing_content, '')
    
    # Insert before why leoplast section
    why_section = '    <!-- ============================\n     WHY LEOPLAST SECTION'
    content = content.replace(why_section, roofing_content + why_section)
    print("Reordered roofing section.")
else:
    print("Roofing section not found.")

# 2. Replace YouTube iframe
iframe_pattern = re.compile(r'<iframe id=\"video-iframe\".*?</iframe>', re.DOTALL)
video_tag = '''<video id="video-iframe" class="video-iframe" controls style="width:100%; height:100%; object-fit:cover; display:none;">
                            <source src="assets/leoplast-video.mp4" type="video/mp4">
                            Your browser does not support the video tag.
                        </video>'''

content = iframe_pattern.sub(video_tag, content)
print("Replaced iframe video tag.")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Update complete.")
