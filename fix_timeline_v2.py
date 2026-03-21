import sys

file_path = "c:/Users/shoba/OneDrive/Documents/leoplast-web-redesign/about.html"
try:
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Find the roadmap block indices regardless of line endings (\n vs \r\n)
    marker = "ROADMAP / TIMELINE"
    idx = content.find(marker)
    if idx == -1:
        print("Marker not found")
        sys.exit()
        
    start_idx = content.rfind("<!--", 0, idx)
    end_idx = content.find("</section>", idx) + len("</section>")
    
    if start_idx == -1 or end_idx < len("</section>"):
        print("Valid bounds not found")
        sys.exit()

    new_roadmap = """<!-- ============================
     ROADMAP / TIMELINE
     ============================ -->
    <section style="padding:5rem 2rem;background:linear-gradient(135deg,#fcfcfd,#f8faff);">
        <div style="max-width:900px;margin:0 auto;">
            <div style="text-align:center;margin-bottom:5rem;" class="reveal">
                <div class="section-badge">Our Journey</div>
                <h2 style="font-size:2.2rem;font-weight:800;color:#0c1f3f;margin-top:1rem;">Leo Plast Roadmap</h2>
                <p style="color:#4b5563;margin-top:0.75rem;line-height:1.8;font-size:1.05rem;">From a small polymer business to an industry-defining manufacturer in four decades.</p>
            </div>

            <!-- Bulletproof CSS Flex Timeline -->
            <div style="display:flex;flex-direction:column;width:100%; position:relative;">
                
                <!-- 1986 -->
                <div class="reveal" style="display:flex;align-items:stretch;width:100%;">
                    <div style="width:120px;text-align:right;padding-right:2rem;padding-top:10px;flex-shrink:0;">
                        <span style="font-size:1.6rem;font-weight:800;color:#1e3a6e;">1986</span>
                    </div>
                    <div style="display:flex;flex-direction:column;align-items:center;position:relative;width:24px;flex-shrink:0;">
                        <div style="position:absolute;top:18px;bottom:0;width:3px;background:linear-gradient(to bottom, #1e3a6e, #1a56db);border-radius:3px;"></div>
                        <div style="width:16px;height:16px;border-radius:50%;background:#1e3a6e;border:4px solid white;box-shadow:0 0 0 4px #1e3a6e;position:relative;z-index:2;margin-top:10px;box-sizing:content-box;"></div>
                    </div>
                    <div style="flex:1;padding-left:2.5rem;padding-bottom:3.5rem;">
                        <div style="background:white;border-radius:1.25rem;padding:2rem 2.25rem;box-shadow:0 4px 20px rgba(30,58,110,0.06);border:1px solid rgba(30,58,110,0.05);transition:transform 0.3s, box-shadow 0.3s;" onmouseover="this.style.transform='translateY(-6px)';this.style.boxShadow='0 12px 30px rgba(30,58,110,0.12)';" onmouseout="this.style.transform='translateY(0)';this.style.boxShadow='0 4px 20px rgba(30,58,110,0.06)';">
                            <span style="font-size:0.85rem;font-weight:700;color:#1a56db;text-transform:uppercase;letter-spacing:0.08em;display:block;margin-bottom:0.6rem;">The Beginning</span>
                            <h4 style="font-size:1.25rem;font-weight:800;color:#0c1f3f;margin:0 0 0.5rem 0;">Establishment of Sankar Polymers</h4>
                            <p style="color:#4b5563;font-size:1rem;line-height:1.7;margin:0;">The journey begins — marking Leo Plast's entry into the plastics industry with a vision to build lasting quality.</p>
                        </div>
                    </div>
                </div>

                <!-- 1996 -->
                <div class="reveal reveal-delay-1" style="display:flex;align-items:stretch;width:100%;">
                    <div style="width:120px;text-align:right;padding-right:2rem;padding-top:10px;flex-shrink:0;">
                        <span style="font-size:1.6rem;font-weight:800;color:#1a56db;">1996</span>
                    </div>
                    <div style="display:flex;flex-direction:column;align-items:center;position:relative;width:24px;flex-shrink:0;">
                        <div style="position:absolute;top:0;bottom:0;width:3px;background:linear-gradient(to bottom, #1a56db, #2563eb);border-radius:3px;"></div>
                        <div style="width:16px;height:16px;border-radius:50%;background:#1a56db;border:4px solid white;box-shadow:0 0 0 4px #1a56db;position:relative;z-index:2;margin-top:10px;box-sizing:content-box;"></div>
                    </div>
                    <div style="flex:1;padding-left:2.5rem;padding-bottom:3.5rem;">
                        <div style="background:white;border-radius:1.25rem;padding:2rem 2.25rem;box-shadow:0 4px 20px rgba(30,58,110,0.06);border:1px solid rgba(30,58,110,0.05);transition:transform 0.3s, box-shadow 0.3s;" onmouseover="this.style.transform='translateY(-6px)';this.style.boxShadow='0 12px 30px rgba(30,58,110,0.12)';" onmouseout="this.style.transform='translateY(0)';this.style.boxShadow='0 4px 20px rgba(30,58,110,0.06)';">
                            <span style="font-size:0.85rem;font-weight:700;color:#1a56db;text-transform:uppercase;letter-spacing:0.08em;display:block;margin-bottom:0.6rem;">Expansion</span>
                            <h4 style="font-size:1.25rem;font-weight:800;color:#0c1f3f;margin:0 0 0.5rem 0;">Launch of Senthil Plastics</h4>
                            <p style="color:#4b5563;font-size:1rem;line-height:1.7;margin:0;">A pivotal step in expanding operations, focusing on high-quality plastic manufacturing and production efficiency.</p>
                        </div>
                    </div>
                </div>

                <!-- 2005 -->
                <div class="reveal reveal-delay-2" style="display:flex;align-items:stretch;width:100%;">
                    <div style="width:120px;text-align:right;padding-right:2rem;padding-top:10px;flex-shrink:0;">
                        <span style="font-size:1.6rem;font-weight:800;color:#2563eb;">2005</span>
                    </div>
                    <div style="display:flex;flex-direction:column;align-items:center;position:relative;width:24px;flex-shrink:0;">
                        <div style="position:absolute;top:0;bottom:0;width:3px;background:linear-gradient(to bottom, #2563eb, #3b82f6);border-radius:3px;"></div>
                        <div style="width:16px;height:16px;border-radius:50%;background:#2563eb;border:4px solid white;box-shadow:0 0 0 4px #2563eb;position:relative;z-index:2;margin-top:10px;box-sizing:content-box;"></div>
                    </div>
                    <div style="flex:1;padding-left:2.5rem;padding-bottom:3.5rem;">
                        <div style="background:white;border-radius:1.25rem;padding:2rem 2.25rem;box-shadow:0 4px 20px rgba(30,58,110,0.06);border:1px solid rgba(30,58,110,0.05);transition:transform 0.3s, box-shadow 0.3s;" onmouseover="this.style.transform='translateY(-6px)';this.style.boxShadow='0 12px 30px rgba(30,58,110,0.12)';" onmouseout="this.style.transform='translateY(0)';this.style.boxShadow='0 4px 20px rgba(30,58,110,0.06)';">
                            <span style="font-size:0.85rem;font-weight:700;color:#2563eb;text-transform:uppercase;letter-spacing:0.08em;display:block;margin-bottom:0.6rem;">Innovation</span>
                            <h4 style="font-size:1.25rem;font-weight:800;color:#0c1f3f;margin:0 0 0.5rem 0;">Santech HDPE Hose Introduced</h4>
                            <p style="color:#4b5563;font-size:1rem;line-height:1.7;margin:0;">Leo Plast introduces an innovative HDPE Hose solution designed specifically for irrigation and industrial applications.</p>
                        </div>
                    </div>
                </div>

                <!-- 2012 -->
                <div class="reveal reveal-delay-3" style="display:flex;align-items:stretch;width:100%;">
                    <div style="width:120px;text-align:right;padding-right:2rem;padding-top:10px;flex-shrink:0;">
                        <span style="font-size:1.6rem;font-weight:800;color:#3b82f6;">2012</span>
                    </div>
                    <div style="display:flex;flex-direction:column;align-items:center;position:relative;width:24px;flex-shrink:0;">
                        <div style="position:absolute;top:0;bottom:0;width:3px;background:linear-gradient(to bottom, #3b82f6, #60a5fa);border-radius:3px;"></div>
                        <div style="width:16px;height:16px;border-radius:50%;background:#3b82f6;border:4px solid white;box-shadow:0 0 0 4px #3b82f6;position:relative;z-index:2;margin-top:10px;box-sizing:content-box;"></div>
                    </div>
                    <div style="flex:1;padding-left:2.5rem;padding-bottom:3.5rem;">
                        <div style="background:white;border-radius:1.25rem;padding:2rem 2.25rem;box-shadow:0 4px 20px rgba(30,58,110,0.06);border:1px solid rgba(30,58,110,0.05);transition:transform 0.3s, box-shadow 0.3s;" onmouseover="this.style.transform='translateY(-6px)';this.style.boxShadow='0 12px 30px rgba(30,58,110,0.12)';" onmouseout="this.style.transform='translateY(0)';this.style.boxShadow='0 4px 20px rgba(30,58,110,0.06)';">
                            <span style="font-size:0.85rem;font-weight:700;color:#3b82f6;text-transform:uppercase;letter-spacing:0.08em;display:block;margin-bottom:0.6rem;">Product Growth</span>
                            <h4 style="font-size:1.25rem;font-weight:800;color:#0c1f3f;margin:0 0 0.5rem 0;">PVC Pipes Line Launched</h4>
                            <p style="color:#4b5563;font-size:1rem;line-height:1.7;margin:0;">The product range expands with the introduction of PVC pipes, designed specifically for durability and long-term reliability.</p>
                        </div>
                    </div>
                </div>

                <!-- 2018 -->
                <div class="reveal reveal-delay-4" style="display:flex;align-items:stretch;width:100%;">
                    <div style="width:120px;text-align:right;padding-right:2rem;padding-top:10px;flex-shrink:0;">
                        <span style="font-size:1.6rem;font-weight:800;color:#60a5fa;">2018</span>
                    </div>
                    <div style="display:flex;flex-direction:column;align-items:center;position:relative;width:24px;flex-shrink:0;">
                        <div style="position:absolute;top:0;bottom:0;width:3px;background:linear-gradient(to bottom, #60a5fa, #93c5fd);border-radius:3px;"></div>
                        <div style="width:16px;height:16px;border-radius:50%;background:#60a5fa;border:4px solid white;box-shadow:0 0 0 4px #60a5fa;position:relative;z-index:2;margin-top:10px;box-sizing:content-box;"></div>
                    </div>
                    <div style="flex:1;padding-left:2.5rem;padding-bottom:3.5rem;">
                        <div style="background:white;border-radius:1.25rem;padding:2rem 2.25rem;box-shadow:0 4px 20px rgba(30,58,110,0.06);border:1px solid rgba(30,58,110,0.05);transition:transform 0.3s, box-shadow 0.3s;" onmouseover="this.style.transform='translateY(-6px)';this.style.boxShadow='0 12px 30px rgba(30,58,110,0.12)';" onmouseout="this.style.transform='translateY(0)';this.style.boxShadow='0 4px 20px rgba(30,58,110,0.06)';">
                            <span style="font-size:0.85rem;font-weight:700;color:#60a5fa;text-transform:uppercase;letter-spacing:0.08em;display:block;margin-bottom:0.6rem;">Full Portfolio</span>
                            <h4 style="font-size:1.25rem;font-weight:800;color:#0c1f3f;margin:0 0 0.5rem 0;">Complete PVC, cPVC & uPVC Range</h4>
                            <p style="color:#4b5563;font-size:1rem;line-height:1.7;margin:0;">The range grows with a full suite of PVC, cPVC, and uPVC fittings — offering comprehensive, certified plumbing solutions.</p>
                        </div>
                    </div>
                </div>

                <!-- 2021 -->
                <div class="reveal" style="display:flex;align-items:stretch;width:100%;">
                    <div style="width:120px;text-align:right;padding-right:2rem;padding-top:10px;flex-shrink:0;">
                        <span style="font-size:1.6rem;font-weight:800;color:#93c5fd;">2021</span>
                    </div>
                    <div style="display:flex;flex-direction:column;align-items:center;position:relative;width:24px;flex-shrink:0;">
                        <div style="position:absolute;top:0;bottom:0;width:3px;background:linear-gradient(to bottom, #93c5fd, #bfdbfe);border-radius:3px;"></div>
                        <div style="width:16px;height:16px;border-radius:50%;background:#93c5fd;border:4px solid white;box-shadow:0 0 0 4px #93c5fd;position:relative;z-index:2;margin-top:10px;box-sizing:content-box;"></div>
                    </div>
                    <div style="flex:1;padding-left:2.5rem;padding-bottom:3.5rem;">
                        <div style="background:white;border-radius:1.25rem;padding:2rem 2.25rem;box-shadow:0 4px 20px rgba(30,58,110,0.06);border:1px solid rgba(30,58,110,0.05);transition:transform 0.3s, box-shadow 0.3s;" onmouseover="this.style.transform='translateY(-6px)';this.style.boxShadow='0 12px 30px rgba(30,58,110,0.12)';" onmouseout="this.style.transform='translateY(0)';this.style.boxShadow='0 4px 20px rgba(30,58,110,0.06)';">
                            <span style="font-size:0.85rem;font-weight:700;color:#2563eb;text-transform:uppercase;letter-spacing:0.08em;display:block;margin-bottom:0.6rem;">Expansion</span>
                            <h4 style="font-size:1.25rem;font-weight:800;color:#0c1f3f;margin:0 0 0.5rem 0;">New Branch in Trichy</h4>
                            <p style="color:#4b5563;font-size:1rem;line-height:1.7;margin:0;">Expanding reach with a new branch in Trichy — improving service and distribution capabilities across Tamil Nadu.</p>
                        </div>
                    </div>
                </div>

                <!-- 2024 -->
                <div class="reveal reveal-delay-1" style="display:flex;align-items:stretch;width:100%;">
                    <div style="width:120px;text-align:right;padding-right:2rem;padding-top:10px;flex-shrink:0;">
                        <span style="font-size:1.6rem;font-weight:800;color:#2563eb;">2024</span>
                    </div>
                    <div style="display:flex;flex-direction:column;align-items:center;position:relative;width:24px;flex-shrink:0;">
                        <div style="width:16px;height:16px;border-radius:50%;background:#bfdbfe;border:4px solid white;box-shadow:0 0 0 4px #2563eb;position:relative;z-index:2;margin-top:10px;box-sizing:content-box;"></div>
                    </div>
                    <div style="flex:1;padding-left:2.5rem;padding-bottom:0;">
                        <div style="background:linear-gradient(135deg,#eff6ff,#dbeafe);border-radius:1.25rem;padding:2.25rem;box-shadow:0 10px 30px rgba(37,99,235,0.15);border:1.5px solid #bfdbfe;transition:transform 0.3s;" onmouseover="this.style.transform='translateY(-6px)';" onmouseout="this.style.transform='translateY(0)';">
                            <span style="font-size:0.85rem;font-weight:700;color:#1a56db;text-transform:uppercase;letter-spacing:0.08em;display:block;margin-bottom:0.6rem;">Today & Beyond</span>
                            <h4 style="font-size:1.25rem;font-weight:800;color:#0c1f3f;margin:0 0 0.5rem 0;">Prime Roto Mould Tanks & Madurai Facility</h4>
                            <p style="color:#4b5563;font-size:1rem;line-height:1.7;margin:0;">Leo Plast introduces Prime Roto Mould Tanks and opens a stock point in Madurai, reinforcing its commitment to high-quality storage solutions and availability.</p>
                        </div>
                    </div>
                </div>

            </div>
        </div>
    </section>"""

    new_content = content[:start_idx] + new_roadmap + content[end_idx:]
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(new_content)
    print("Replaced elegantly.")
except Exception as e:
    print(e)
