import sys

file_path = "c:/Users/shoba/OneDrive/Documents/leoplast-web-redesign/roofing.html"
with open(file_path, "r", encoding="utf-8") as f:
    c = f.read()

# 1. Replace 3-Layer Tech with animated version
old_3_layer = """<!-- 3-Layer Tech -->
            <div style="background:linear-gradient(135deg,#f8faff,#eef4ff);border-radius:2rem;padding:4rem 2rem 5rem;text-align:center;box-shadow:0 10px 40px rgba(30,58,110,0.05);" class="reveal reveal-delay-2">
                <h3 style="font-size:2rem;font-weight:800;color:#0c1f3f;margin-bottom:0.5rem;text-transform:uppercase;">Leo Plast 3-Layer ASA uPVC Sheets</h3>
                <p style="color:#1a56db;font-weight:700;letter-spacing:0.1em;text-transform:uppercase;margin-bottom:5rem;">Layer Explanation</p>
                
                <div style="display:flex;flex-direction:column;align-items:center;max-width:700px;margin:0 auto;">
                    <div style="width:100%;min-height:90px;background:#dc2626;padding:1.5rem;border-radius:1.5rem;color:white;box-shadow:0 10px 20px rgba(220,38,38,0.25);position:relative;z-index:3;display:flex;flex-direction:column;justify-content:center;">
                        <h4 style="font-size:1.25rem;font-weight:800;margin:0;letter-spacing:0.05em;">LAYER-1:</h4>
                        <p style="margin:0.25rem 0 0;font-size:1rem;font-weight:600;">ASA - High Weather Resistance & Anti-aging Protection</p>
                    </div>

                    <div style="width:90%;min-height:90px;background:#991b1b;padding:1.5rem;border-radius:0 0 1.5rem 1.5rem;color:white;box-shadow:0 8px 15px rgba(0,0,0,0.15);position:relative;z-index:2;margin-top:-1.5rem;padding-top:2.5rem;display:flex;flex-direction:column;justify-content:center;">
                        <h4 style="font-size:1.15rem;font-weight:800;margin:0;letter-spacing:0.05em;">LAYER-2:</h4>
                        <p style="margin:0.25rem 0 0;font-size:0.95rem;font-weight:600;">Reinforced & Sun light insulation Layer</p>
                    </div>

                    <div style="width:80%;min-height:90px;background:white;border:2px solid #e5e7eb;padding:1.5rem;border-radius:0 0 1.5rem 1.5rem;color:#0c1f3f;box-shadow:0 4px 10px rgba(0,0,0,0.05);position:relative;z-index:1;margin-top:-1.5rem;padding-top:2.5rem;display:flex;flex-direction:column;justify-content:center;">
                        <h4 style="font-size:1.15rem;font-weight:800;margin:0;letter-spacing:0.05em;color:#1e3a6e;">LAYER-3:</h4>
                        <p style="margin:0.25rem 0 0;font-size:0.95rem;font-weight:600;color:#4b5563;">White Colored - High Strength & Rigidity Layer</p>
                    </div>
                </div>
            </div>"""

new_3_layer = """<!-- 3-Layer Tech -->
            <div id="layer-container" style="background:linear-gradient(135deg,#f8faff,#eef4ff);border-radius:2rem;padding:4rem 2rem 5rem;text-align:center;box-shadow:0 10px 40px rgba(30,58,110,0.05);" class="reveal reveal-delay-2 layer-reveal-container">
                <style>
                    /* Premium interactive layout unfold animation */
                    #layer-container .layer-stack { transition: transform 0.8s cubic-bezier(0.34, 1.56, 0.64, 1), opacity 0.8s ease, box-shadow 0.3s; will-change: transform, opacity; }
                    /* Start positions (compressed) */
                    #layer-container:not(.visible) .l2 { transform: translateY(-70px); opacity:0; }
                    #layer-container:not(.visible) .l3 { transform: translateY(-130px); opacity:0; }
                    /* End positions (Expanded cascading down) */
                    #layer-container.visible .l2 { transform: translateY(0); opacity:1; transition-delay:0.25s; }
                    #layer-container.visible .l3 { transform: translateY(0); opacity:1; transition-delay:0.5s; }
                    
                    /* Hover pop out interactivity */
                    #layer-container .layer-stack:hover { transform: translateY(-12px) scale(1.02) !important; box-shadow:0 25px 50px rgba(0,0,0,0.2) !important; z-index:10 !important; cursor:pointer;}
                </style>

                <h3 style="font-size:2rem;font-weight:800;color:#0c1f3f;margin-bottom:0.5rem;text-transform:uppercase;">Leo Plast 3-Layer ASA uPVC Sheets</h3>
                <p style="color:#1a56db;font-weight:700;letter-spacing:0.1em;text-transform:uppercase;margin-bottom:6rem;">Interactive Layer Explanation</p>
                
                <div style="display:flex;flex-direction:column;align-items:center;max-width:700px;margin:0 auto;perspective:1000px;">
                    <div class="layer-stack l1" style="width:100%;min-height:90px;background:#dc2626;padding:1.5rem;border-radius:1.5rem;color:white;box-shadow:0 10px 20px rgba(220,38,38,0.25);position:relative;z-index:3;display:flex;flex-direction:column;justify-content:center;">
                        <h4 style="font-size:1.25rem;font-weight:800;margin:0;letter-spacing:0.05em;">LAYER-1:</h4>
                        <p style="margin:0.25rem 0 0;font-size:1rem;font-weight:600;">ASA - High Weather Resistance & Anti-aging Protection</p>
                    </div>

                    <div class="layer-stack l2" style="width:90%;min-height:90px;background:#991b1b;padding:1.5rem;border-radius:0 0 1.5rem 1.5rem;color:white;box-shadow:0 8px 15px rgba(0,0,0,0.15);position:relative;z-index:2;margin-top:-1.5rem;padding-top:2.5rem;display:flex;flex-direction:column;justify-content:center;">
                        <h4 style="font-size:1.15rem;font-weight:800;margin:0;letter-spacing:0.05em;">LAYER-2:</h4>
                        <p style="margin:0.25rem 0 0;font-size:0.95rem;font-weight:600;">Reinforced & Sunlight Insulation Layer</p>
                    </div>

                    <div class="layer-stack l3" style="width:80%;min-height:90px;background:white;border:2px solid #e5e7eb;padding:1.5rem;border-radius:0 0 1.5rem 1.5rem;color:#0c1f3f;box-shadow:0 4px 10px rgba(0,0,0,0.05);position:relative;z-index:1;margin-top:-1.5rem;padding-top:2.5rem;display:flex;flex-direction:column;justify-content:center;">
                        <h4 style="font-size:1.15rem;font-weight:800;margin:0;letter-spacing:0.05em;color:#1e3a6e;">LAYER-3:</h4>
                        <p style="margin:0.25rem 0 0;font-size:0.95rem;font-weight:600;color:#4b5563;">White Colored - High Strength & Rigidity Layer</p>
                    </div>
                </div>
            </div>"""

if old_3_layer in c:
    c = c.replace(old_3_layer, new_3_layer)
else:
    print("Layer format not matching perfectly, skipping injection to prevent breakage. ")

# 2. Insert Installation + Applications before the CTA block
cta_marker = '<div style="max-width:1100px;margin:6rem auto 0;" class="reveal">'
extras = """<!-- Installation Process -->
    <section style="padding:4rem 2rem 2rem;background:#fafafa;">
        <div style="max-width:1100px;margin:0 auto;">
            <div style="text-align:center;margin-bottom:4rem;" class="reveal">
                <div class="section-badge red">Process</div>
                <h2 style="font-size:2.5rem;font-weight:800;color:#0c1f3f;text-transform:uppercase;">Installation Process</h2>
            </div>
            
            <div style="display:grid;grid-template-columns:1fr 1.2fr;gap:4rem;align-items:center;">
                <!-- Left: Image & Note -->
                <div class="reveal">
                    <div style="background:white;padding:1.5rem;border-radius:1.5rem;box-shadow:0 10px 30px rgba(0,0,0,0.06);margin-bottom:2.5rem;">
                        <div style="width:100%;aspect-ratio:4/3;background:#f9fafb;border-radius:1rem;display:flex;align-items:center;justify-content:center;color:#9ca3af;border:2px dashed #e5e7eb;">
                            <div style="text-align:center;">
                                <i data-lucide="image" style="width:48px;height:48px;margin:0 auto 0.5rem;color:#dc2626;"></i>
                                <span style="font-size:0.95rem;font-weight:600;display:block;">Architecture Diagram Pending</span>
                            </div>
                        </div>
                    </div>
                    <div style="background:linear-gradient(135deg,#1e3a8a,#1e40af);color:white;padding:2rem 2.5rem;border-radius:1.5rem;box-shadow:0 15px 30px rgba(30,58,138,0.3);position:relative;overflow:hidden;">
                        <!-- Background glow effect -->
                        <div style="position:absolute;top:-20px;right:-20px;width:100px;height:100px;background:rgba(255,255,255,0.1);border-radius:50%;filter:blur(20px);"></div>
                        <h4 style="font-weight:800;font-size:1.35rem;margin-bottom:1rem;display:flex;align-items:center;gap:0.75rem;">
                            <i data-lucide="info" style="width:24px;height:24px;color:#93c5fd;"></i> Note:
                        </h4>
                        <p style="margin:0;font-size:1.05rem;line-height:1.7;color:#dbeafe;">The purlin span is related to the workshop temperature. The higher the workshop temperature, the smaller the purlin span. Otherwise it will lead to tile deformation.</p>
                    </div>
                </div>

                <!-- Right: Steps -->
                <div class="reveal reveal-delay-1">
                    <ul style="list-style:none;padding:0;margin:0;display:flex;flex-direction:column;gap:2rem;">
                        
                        <li style="display:flex;gap:1.5rem;align-items:flex-start;background:white;padding:1.5rem 2rem;border-radius:1.25rem;box-shadow:0 4px 15px rgba(0,0,0,0.03);border-left:4px solid #dc2626;">
                            <div style="width:44px;height:44px;background:#fef2f2;border-radius:50%;display:flex;align-items:center;justify-content:center;color:#dc2626;flex-shrink:0;">
                                <span style="font-weight:800;font-size:1.2rem;">1</span>
                            </div>
                            <div>
                                <p style="margin:0;color:#4b5563;font-size:1rem;line-height:1.7;"><strong>Purlines</strong> can be square pipe (60mmx40mmx3mm) or C-shaped steel (100mmx50mmx20 mmx3mm) or corrosion-resistant wood beam (60x40mm). The purline spacing is <strong>660mm</strong>, arranged from bottom to top.</p>
                            </div>
                        </li>

                        <li style="display:flex;gap:1.5rem;align-items:flex-start;background:white;padding:1.5rem 2rem;border-radius:1.25rem;box-shadow:0 4px 15px rgba(0,0,0,0.03);border-left:4px solid #b91c1c;">
                            <div style="width:44px;height:44px;background:#fef2f2;border-radius:50%;display:flex;align-items:center;justify-content:center;color:#dc2626;flex-shrink:0;">
                                <span style="font-weight:800;font-size:1.2rem;">2</span>
                            </div>
                            <div>
                                <p style="margin:0;color:#4b5563;font-size:1rem;line-height:1.7;"><strong>Main tile</strong> should be installed according to local wind direction, to be opposite to wind direction. Lap with a tile wave, with both sides done at the same time. When installing main ridge tiles, please cut out a section of the first tile before installing.</p>
                            </div>
                        </li>

                        <li style="display:flex;gap:1.5rem;align-items:flex-start;background:white;padding:1.5rem 2rem;border-radius:1.25rem;box-shadow:0 4px 15px rgba(0,0,0,0.03);border-left:4px solid #991b1b;">
                            <div style="width:44px;height:44px;background:#fef2f2;border-radius:50%;display:flex;align-items:center;justify-content:center;color:#dc2626;flex-shrink:0;">
                                <span style="font-weight:800;font-size:1.2rem;">3</span>
                            </div>
                            <div>
                                <p style="margin:0;color:#4b5563;font-size:1rem;line-height:1.7;">The lap joints of the main ridge tiles and the slope ridge tiles should be neatened. Install the tee-joint tiles after completion of installation of the main ridge tiles and the slope ridge tiles.</p>
                            </div>
                        </li>

                        <li style="display:flex;gap:1.5rem;align-items:flex-start;background:white;padding:1.5rem 2rem;border-radius:1.25rem;box-shadow:0 4px 15px rgba(0,0,0,0.03);border-left:4px solid #7f1d1d;">
                            <div style="width:44px;height:44px;background:#fef2f2;border-radius:50%;display:flex;align-items:center;justify-content:center;color:#dc2626;flex-shrink:0;">
                                <span style="font-weight:800;font-size:1.2rem;">4</span>
                            </div>
                            <div>
                                <p style="margin:0;color:#4b5563;font-size:1rem;line-height:1.7;"><strong>Fixing parts</strong> are special parts. When fixing, first use electric drill to make holes and keep the hole diameter 2mm bigger than screw. Tapping screws with diameter of 6.3mm are recommended.</p>
                            </div>
                        </li>

                    </ul>
                </div>
            </div>
        </div>
    </section>

    <!-- Applications -->
    <section style="padding:6rem 2rem;background:white;">
        <div style="max-width:1100px;margin:0 auto;" class="reveal">
            <div style="text-align:center;margin-bottom:4rem;">
                <h2 style="font-size:2.5rem;font-weight:800;color:#0c1f3f;text-transform:uppercase;">Applications</h2>
            </div>
            
            <div style="display:flex;flex-wrap:wrap;justify-content:center;gap:3rem;">
                
                <div style="display:flex;flex-direction:column;align-items:center;width:120px;" class="reveal reveal-delay-1">
                    <div style="width:85px;height:85px;border:2.5px solid #dc2626;border-radius:1.25rem;display:flex;align-items:center;justify-content:center;color:#dc2626;margin-bottom:1rem;transition:all 0.35s ease;box-shadow:0 4px 15px rgba(0,0,0,0.05);" onmouseover="this.style.background='#dc2626';this.style.color='white';this.style.transform='translateY(-5px) scale(1.05)';" onmouseout="this.style.background='white';this.style.color='#dc2626';this.style.transform='translateY(0) scale(1)';">
                        <i data-lucide="tractor" style="width:42px;height:42px;"></i>
                    </div>
                    <span style="font-weight:800;color:#4b5563;font-size:1.05rem;">Farming</span>
                </div>
                
                <div style="display:flex;flex-direction:column;align-items:center;width:120px;" class="reveal reveal-delay-2">
                    <div style="width:85px;height:85px;border:2.5px solid #dc2626;border-radius:1.25rem;display:flex;align-items:center;justify-content:center;color:#dc2626;margin-bottom:1rem;transition:all 0.35s ease;box-shadow:0 4px 15px rgba(0,0,0,0.05);" onmouseover="this.style.background='#dc2626';this.style.color='white';this.style.transform='translateY(-5px) scale(1.05)';" onmouseout="this.style.background='white';this.style.color='#dc2626';this.style.transform='translateY(0) scale(1)';">
                        <i data-lucide="home" style="width:42px;height:42px;"></i>
                    </div>
                    <span style="font-weight:800;color:#4b5563;font-size:1.05rem;">Houses</span>
                </div>
                
                <div style="display:flex;flex-direction:column;align-items:center;width:120px;" class="reveal reveal-delay-3">
                    <div style="width:85px;height:85px;border:2.5px solid #dc2626;border-radius:1.25rem;display:flex;align-items:center;justify-content:center;color:#dc2626;margin-bottom:1rem;transition:all 0.35s ease;box-shadow:0 4px 15px rgba(0,0,0,0.05);" onmouseover="this.style.background='#dc2626';this.style.color='white';this.style.transform='translateY(-5px) scale(1.05)';" onmouseout="this.style.background='white';this.style.color='#dc2626';this.style.transform='translateY(0) scale(1)';">
                        <i data-lucide="car-front" style="width:42px;height:42px;"></i>
                    </div>
                    <span style="font-weight:800;color:#4b5563;font-size:1.05rem;">Car-Shed</span>
                </div>
                
                <div style="display:flex;flex-direction:column;align-items:center;width:120px;" class="reveal reveal-delay-4">
                    <div style="width:85px;height:85px;border:2.5px solid #dc2626;border-radius:1.25rem;display:flex;align-items:center;justify-content:center;color:#dc2626;margin-bottom:1rem;transition:all 0.35s ease;box-shadow:0 4px 15px rgba(0,0,0,0.05);" onmouseover="this.style.background='#dc2626';this.style.color='white';this.style.transform='translateY(-5px) scale(1.05)';" onmouseout="this.style.background='white';this.style.color='#dc2626';this.style.transform='translateY(0) scale(1)';">
                        <i data-lucide="warehouse" style="width:42px;height:42px;"></i>
                    </div>
                    <span style="font-weight:800;color:#4b5563;font-size:1.05rem;">Warehouse</span>
                </div>
                
                <div style="display:flex;flex-direction:column;align-items:center;width:120px;" class="reveal reveal-delay-1">
                    <div style="width:85px;height:85px;border:2.5px solid #dc2626;border-radius:1.25rem;display:flex;align-items:center;justify-content:center;color:#dc2626;margin-bottom:1rem;transition:all 0.35s ease;box-shadow:0 4px 15px rgba(0,0,0,0.05);" onmouseover="this.style.background='#dc2626';this.style.color='white';this.style.transform='translateY(-5px) scale(1.05)';" onmouseout="this.style.background='white';this.style.color='#dc2626';this.style.transform='translateY(0) scale(1)';">
                        <i data-lucide="factory" style="width:42px;height:42px;"></i>
                    </div>
                    <span style="font-weight:800;color:#4b5563;font-size:1.05rem;">Factories</span>
                </div>

                <div style="display:flex;flex-direction:column;align-items:center;width:120px;" class="reveal reveal-delay-2">
                    <div style="width:85px;height:85px;border:2.5px solid #dc2626;border-radius:1.25rem;display:flex;align-items:center;justify-content:center;color:#dc2626;margin-bottom:1rem;transition:all 0.35s ease;box-shadow:0 4px 15px rgba(0,0,0,0.05);" onmouseover="this.style.background='#dc2626';this.style.color='white';this.style.transform='translateY(-5px) scale(1.05)';" onmouseout="this.style.background='white';this.style.color='#dc2626';this.style.transform='translateY(0) scale(1)';">
                        <i data-lucide="layers" style="width:42px;height:42px;"></i>
                    </div>
                    <span style="font-weight:800;color:#4b5563;font-size:1.05rem;">Wall-Cladding</span>
                </div>
                
                <div style="display:flex;flex-direction:column;align-items:center;width:120px;" class="reveal reveal-delay-3">
                    <div style="width:85px;height:85px;border:2.5px solid #dc2626;border-radius:1.25rem;display:flex;align-items:center;justify-content:center;color:#dc2626;margin-bottom:1rem;transition:all 0.35s ease;box-shadow:0 4px 15px rgba(0,0,0,0.05);" onmouseover="this.style.background='#dc2626';this.style.color='white';this.style.transform='translateY(-5px) scale(1.05)';" onmouseout="this.style.background='white';this.style.color='#dc2626';this.style.transform='translateY(0) scale(1)';">
                        <i data-lucide="palmtree" style="width:42px;height:42px;"></i>
                    </div>
                    <span style="font-weight:800;color:#4b5563;font-size:1.05rem;">Resorts</span>
                </div>
                
            </div>
        </div>
    </section>

    """
if cta_marker in c:
    c = c.replace(cta_marker, extras + cta_marker)
else:
    print("CTA marker not found.")

with open(file_path, "w", encoding="utf-8") as f:
    f.write(c)
print("Update final completed.")
