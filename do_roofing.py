import re
import sys

file_path = "c:/Users/shoba/OneDrive/Documents/leoplast-web-redesign/roofing.html"
with open(file_path, "r", encoding="utf-8") as f:
    c = f.read()

start_marker = "<!-- Hero — Red Theme -->"
end_marker = "<footer style=\"background:#111827"

if start_marker not in c or end_marker not in c:
    print("Markers not found.")
    sys.exit()

start_idx = c.find(start_marker)
end_idx = c.find(end_marker)

new_content = """<!-- Hero — Red Theme -->
    <div class="page-hero roofing-hero" style="padding:9rem 1.5rem 6rem;">
        <div style="position:absolute;inset:0;background:radial-gradient(ellipse at 60% 50%,rgba(220,38,38,0.2),transparent 65%);"></div>
        <div style="position:relative;z-index:2;text-align:center;">
            <div class="breadcrumb" style="margin-bottom:1.25rem;"><a href="index.html" style="color:rgba(252,165,165,0.7);">Home</a> <span style="color:rgba(252,165,165,0.5);">›</span> <span style="color:white;">Roofing</span></div>
            <div class="section-badge red" style="margin-bottom:1rem;">Leoplast Roofings</div>
            <h1 style="font-size:clamp(2.5rem,6vw,4.5rem);font-weight:800;color:white;margin-bottom:1rem;line-height:1.15;">
                ASA <span class="gradient-text-red">uPVC Sheets</span>
            </h1>
            
            <div style="display:flex;justify-content:center;gap:1.5rem;flex-wrap:wrap;max-width:800px;margin:2rem auto 2.5rem;">
                <div style="display:flex;flex-direction:column;align-items:center;gap:0.5rem;color:white;background:rgba(0,0,0,0.2);padding:1.5rem 2rem;border-radius:1rem;border:1px solid rgba(255,255,255,0.1);backdrop-filter:blur(10px);">
                    <div style="font-size:1.5rem;">🔊</div><span style="font-weight:700;font-size:0.9rem;">Sound Proof</span></div>
                <div style="display:flex;flex-direction:column;align-items:center;gap:0.5rem;color:white;background:rgba(0,0,0,0.2);padding:1.5rem 2rem;border-radius:1rem;border:1px solid rgba(255,255,255,0.1);backdrop-filter:blur(10px);">
                    <div style="font-size:1.5rem;">🔥</div><span style="font-weight:700;font-size:0.9rem;">Fire Resistant</span></div>
                <div style="display:flex;flex-direction:column;align-items:center;gap:0.5rem;color:white;background:rgba(0,0,0,0.2);padding:1.5rem 2rem;border-radius:1rem;border:1px solid rgba(255,255,255,0.1);backdrop-filter:blur(10px);">
                    <div style="font-size:1.5rem;">💧</div><span style="font-weight:700;font-size:0.9rem;">100% Water Proof</span></div>
                <div style="display:flex;flex-direction:column;align-items:center;gap:0.5rem;color:white;background:rgba(0,0,0,0.2);padding:1.5rem 2rem;border-radius:1rem;border:1px solid rgba(255,255,255,0.1);backdrop-filter:blur(10px);">
                    <div style="font-size:1.5rem;">🛡️</div><span style="font-weight:700;font-size:0.9rem;">High Impact</span></div>
                <div style="display:flex;flex-direction:column;align-items:center;gap:0.5rem;color:white;background:rgba(0,0,0,0.2);padding:1.5rem 2rem;border-radius:1rem;border:1px solid rgba(255,255,255,0.1);backdrop-filter:blur(10px);">
                    <div style="font-size:1.5rem;">🌡️</div><span style="font-weight:700;font-size:0.9rem;">Thermal Control</span></div>
            </div>

            <div style="display:flex;gap:1rem;justify-content:center;flex-wrap:wrap;">
                <a href="contact.html" style="padding:0.875rem 2rem;background:white;color:#7f1d1d;border-radius:9999px;font-weight:700;text-decoration:none;box-shadow:0 8px 25px rgba(0,0,0,0.3);">Get a Quote</a>
                <a href="#intro" style="padding:0.875rem 2rem;background:rgba(255,255,255,0.12);color:white;border:1.5px solid rgba(255,255,255,0.3);border-radius:9999px;font-weight:600;text-decoration:none;backdrop-filter:blur(6px);">Learn More</a>
            </div>
        </div>
    </div>

    <!-- Product Intro -->
    <section id="intro" style="padding:6rem 2rem;background:white;">
        <div style="max-width:1100px;margin:0 auto;">
            <div style="text-align:center;margin-bottom:6rem;" class="reveal">
                <div class="section-badge red">Introduction</div>
                <h2 style="font-size:2.5rem;font-weight:800;color:#0c1f3f;margin-bottom:1.5rem;text-transform:uppercase;">Product Introduction</h2>
                <p style="color:#4b5563;font-size:1.1rem;line-height:1.9;max-width:900px;margin:0 auto;text-align:justify;text-align-last:center;">
                    <strong>UPVC Roofing Sheets</strong> are the perfect choice for a variety of roofing applications. Our UPVC Roofing Sheets are made from high quality <strong>Acrylonitrile Styrene Acrylate (ASA)</strong> and UPVC material and are designed to provide superior protection against the elements. The sheets are lightweight and easy to install, and they come in a variety of sizes to fit any roofing project. Our UPVC Roofing Sheets are resistant to corrosion, weathering, and UV radiation, making them perfect for long-term use. The usage of high weather resistant engineering plastic helps to reduce heat transfer and prevents sound. They are also fire retardant and energy efficient, helping to reduce energy costs. Our UPVC Roofing Sheets are available in a variety of colors and patterns to suit any aesthetic.
                </p>
            </div>

            <!-- 3-Layer Tech -->
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
            </div>
        </div>
    </section>

    <!-- Technical Specs -->
    <section style="padding:6rem 2rem;background:#fafafa;">
        <div style="max-width:1100px;margin:0 auto;">
            <div style="text-align:center;margin-bottom:4rem;" class="reveal">
                <div class="section-badge red">Technical Data</div>
                <h2 style="font-size:2.5rem;font-weight:800;color:#0c1f3f;">Product Specification</h2>
            </div>
            
            <div style="display:grid;grid-template-columns:1fr 1fr;gap:3rem;align-items:start;">
                
                <!-- Base Specs -->
                <div class="reveal reveal-delay-1">
                    <div style="background:white;border-radius:1.5rem;overflow:hidden;box-shadow:0 10px 30px rgba(0,0,0,0.06);">
                        <table style="width:100%;border-collapse:collapse;text-align:left;">
                            <tbody>
                                <tr style="border-bottom:1px solid #f3f4f6;">
                                    <td style="padding:1.5rem 2rem;font-weight:700;color:#991b1b;background:#fef2f2;width:50%;">Thickness</td>
                                    <td style="padding:1.5rem 2rem;color:#374151;font-weight:600;">2.5 - 3 mm</td>
                                </tr>
                                <tr style="border-bottom:1px solid #f3f4f6;">
                                    <td style="padding:1.5rem 2rem;font-weight:700;color:#991b1b;background:#fef2f2;">Width / Effective Width</td>
                                    <td style="padding:1.5rem 2rem;color:#374151;font-weight:600;">1050mm</td>
                                </tr>
                                <tr style="border-bottom:1px solid #f3f4f6;">
                                    <td style="padding:1.5rem 2rem;font-weight:700;color:#991b1b;background:#fef2f2;">Wave Spacing</td>
                                    <td style="padding:1.5rem 2rem;color:#374151;font-weight:600;">160mm</td>
                                </tr>
                                <tr style="border-bottom:1px solid #f3f4f6;">
                                    <td style="padding:1.5rem 2rem;font-weight:700;color:#991b1b;background:#fef2f2;">Wave Height</td>
                                    <td style="padding:1.5rem 2rem;color:#374151;font-weight:600;">28mm</td>
                                </tr>
                                <tr>
                                    <td style="padding:1.5rem 2rem;font-weight:700;color:#991b1b;background:#fef2f2;">Tile Length</td>
                                    <td style="padding:1.5rem 2rem;color:#374151;font-weight:600;">220mm</td>
                                </tr>
                            </tbody>
                        </table>
                    </div>
                    
                    <div style="margin-top:3rem;text-align:center;">
                        <h4 style="font-size:1.5rem;font-weight:800;color:#0c1f3f;margin-bottom:1.5rem;">Profile Diagram</h4>
                        <div style="background:white;border-radius:1.5rem;padding:2.5rem;box-shadow:0 10px 30px rgba(0,0,0,0.06);position:relative;">
                            <div style="font-size:0.9rem;font-weight:700;color:#4b5563;margin-bottom:0.5rem;">Total Width: <span style="color:#991b1b;">1050mm</span></div>
                            <svg width="100%" height="80" viewBox="0 0 500 80" preserveAspectRatio="none">
                                <path d="M0,50 Q25,20 50,50 T100,50 T150,50 T200,50 T250,50 T300,50 T350,50 T400,50 T450,50 T500,50" fill="none" stroke="#dc2626" stroke-width="3"/>
                            </svg>
                            <div style="display:flex;justify-content:space-around;margin-top:1rem;font-size:0.85rem;font-weight:700;color:#6b7280;">
                                <div><span style="display:block;margin-bottom:0.25rem;">← Wave Spacing →</span><span style="color:#991b1b;">160mm</span></div>
                                <div><span style="display:block;margin-bottom:0.25rem;">↕ Height</span><span style="color:#991b1b;">28mm</span></div>
                            </div>
                        </div>
                    </div>
                </div>

                <!-- Length Table -->
                <div class="reveal reveal-delay-2">
                    <h4 style="font-size:1.75rem;font-weight:800;color:#0c1f3f;margin-bottom:1.5rem;text-align:center;">Standard Sheet Length</h4>
                    <div style="background:white;border-radius:1.5rem;overflow:hidden;box-shadow:0 10px 30px rgba(0,0,0,0.06);">
                        <table style="width:100%;border-collapse:collapse;text-align:center;">
                            <thead>
                                <tr style="background:#1e3a6e;color:white;">
                                    <th style="padding:1.25rem;font-weight:700;">Feet</th>
                                    <th style="padding:1.25rem;font-weight:700;">Millimeter</th>
                                    <th style="padding:1.25rem;font-weight:700;">Spans</th>
                                </tr>
                            </thead>
                            <tbody>
                                <tr style="border-bottom:1px solid #f3f4f6;"><td style="padding:1rem;">6.5</td><td style="padding:1rem;">1971</td><td style="padding:1rem;">9</td></tr>
                                <tr style="border-bottom:1px solid #f3f4f6;background:#f8faff;"><td style="padding:1rem;">8</td><td style="padding:1rem;">2410</td><td style="padding:1rem;">11</td></tr>
                                <tr style="border-bottom:1px solid #f3f4f6;"><td style="padding:1rem;">10</td><td style="padding:1rem;">3065</td><td style="padding:1rem;">14</td></tr>
                                <tr style="border-bottom:1px solid #f3f4f6;background:#f8faff;"><td style="padding:1rem;">12</td><td style="padding:1rem;">3721</td><td style="padding:1rem;">17</td></tr>
                                <tr style="border-bottom:1px solid #f3f4f6;"><td style="padding:1rem;">14</td><td style="padding:1rem;">4380</td><td style="padding:1rem;">20</td></tr>
                                <tr style="border-bottom:1px solid #f3f4f6;background:#f8faff;"><td style="padding:1rem;">16.5</td><td style="padding:1rem;">5036</td><td style="padding:1rem;">23</td></tr>
                                <tr style="border-bottom:1px solid #f3f4f6;"><td style="padding:1rem;">18</td><td style="padding:1rem;">5475</td><td style="padding:1rem;">25</td></tr>
                                <tr style="border-bottom:1px solid #f3f4f6;background:#f8faff;"><td style="padding:1rem;">20</td><td style="padding:1rem;">6131</td><td style="padding:1rem;">28</td></tr>
                                <tr><td style="padding:1rem;">24</td><td style="padding:1rem;">7445</td><td style="padding:1rem;">34</td></tr>
                            </tbody>
                        </table>
                    </div>
                </div>

            </div>
        </div>
    </section>

    <!-- Product Advantages -->
    <section style="padding:6rem 2rem;background:linear-gradient(135deg,#fff5f5,#fee2e2);">
        <div style="max-width:1100px;margin:0 auto;">
            <div style="text-align:center;margin-bottom:4.5rem;" class="reveal">
                <h2 style="font-size:2.5rem;font-weight:800;color:#7f1d1d;text-transform:uppercase;">Product Advantage</h2>
            </div>
            
            <div style="display:flex;flex-direction:column;gap:2rem;max-width:900px;margin:0 auto;">
                
                <div class="reveal" style="display:flex;gap:1.5rem;align-items:center;">
                    <div style="width:100px;height:100px;background:#991b1b;border-radius:50%;display:flex;align-items:center;justify-content:center;color:white;font-weight:800;font-size:0.9rem;text-align:center;line-height:1.2;flex-shrink:0;box-shadow:0 10px 20px rgba(153,27,27,0.3);border:4px solid white;">Long <br>Lasting<br>color</div>
                    <div style="background:white;padding:2rem 2.5rem;border-radius:1.5rem;flex:1;box-shadow:0 4px 15px rgba(0,0,0,0.05);">
                        <h4 style="font-weight:800;color:#0c1f3f;margin-bottom:0.5rem;font-size:1.25rem;">Ultra-high weather resistance</h4>
                        <p style="font-size:0.95rem;color:#4b5563;line-height:1.7;margin:0;">Synthetic resin tile surface material is made of imported ultra-high weather-resistant engineering resin. It has extraordinary durability in the natural environment. It can maintain its color stability even if it is exposed to harsh conditions such as ultraviolet, moisture, heat and cold for a long time.</p>
                    </div>
                </div>

                <div class="reveal reveal-delay-1" style="display:flex;gap:1.5rem;align-items:center;">
                    <div style="width:100px;height:100px;background:#991b1b;border-radius:50%;display:flex;align-items:center;justify-content:center;color:white;font-weight:800;font-size:0.9rem;text-align:center;line-height:1.2;flex-shrink:0;box-shadow:0 10px 20px rgba(153,27,27,0.3);border:4px solid white;">Load-<br>Resistance</div>
                    <div style="background:white;padding:2rem 2.5rem;border-radius:1.5rem;flex:1;box-shadow:0 4px 15px rgba(0,0,0,0.05);">
                        <h4 style="font-weight:800;color:#0c1f3f;margin-bottom:0.5rem;font-size:1.25rem;">Excellent load resistance</h4>
                        <p style="font-size:0.95rem;color:#4b5563;line-height:1.7;margin:0;">Synthetic resin tile has good bearing capacity. In areas with low temperature, even if the roof is covered with snow all the year round, the synthetic resin tile will not cause surface damage and fracture. According to the test, when the support spacing is 660 mm and the load is 150 kg, the tile will not produce cracks and damage.</p>
                    </div>
                </div>

                <div class="reveal" style="display:flex;gap:1.5rem;align-items:center;">
                    <div style="width:100px;height:100px;background:#991b1b;border-radius:50%;display:flex;align-items:center;justify-content:center;color:white;font-weight:800;font-size:0.9rem;text-align:center;line-height:1.2;flex-shrink:0;box-shadow:0 10px 20px rgba(153,27,27,0.3);border:4px solid white;">Corrosion-<br>Resistance</div>
                    <div style="background:white;padding:2rem 2.5rem;border-radius:1.5rem;flex:1;box-shadow:0 4px 15px rgba(0,0,0,0.05);">
                        <h4 style="font-weight:800;color:#0c1f3f;margin-bottom:0.5rem;font-size:1.25rem;">Excellent corrosion resistance</h4>
                        <p style="font-size:0.95rem;color:#4b5563;line-height:1.7;margin:0;">Synthetic resin tile can resist the corrosion of acid, alkali, salt and other chemicals for a long time. The experiment shows that there is no chemical reaction after soaking in salt, alkali and various acids below 60% for 24 hours. It is very suitable for use in acid rain prone areas and coastal areas, and the effect is particularly significant.</p>
                    </div>
                </div>

                <div class="reveal reveal-delay-1" style="display:flex;gap:1.5rem;align-items:center;">
                    <div style="width:100px;height:100px;background:#991b1b;border-radius:50%;display:flex;align-items:center;justify-content:center;color:white;font-weight:800;font-size:0.9rem;text-align:center;line-height:1.2;flex-shrink:0;box-shadow:0 10px 20px rgba(153,27,27,0.3);border:4px solid white;">Impact-<br>Resistance</div>
                    <div style="background:white;padding:2rem 2.5rem;border-radius:1.5rem;flex:1;box-shadow:0 4px 15px rgba(0,0,0,0.05);">
                        <h4 style="font-weight:800;color:#0c1f3f;margin-bottom:0.5rem;font-size:1.25rem;">Good impact and low temperature resistance</h4>
                        <p style="font-size:0.95rem;color:#4b5563;line-height:1.7;margin:0;">Synthetic resin tile has good impact and low temperature resistance. The weight of 1 kg steel hammer is 1.5 meters high and falls freely on the tile surface without cracks. After 10 freeze-thaw cycles, the product has no hollowing, blistering, peeling and cracking.</p>
                    </div>
                </div>

                <div class="reveal" style="display:flex;gap:1.5rem;align-items:center;">
                    <div style="width:100px;height:100px;background:#991b1b;border-radius:50%;display:flex;align-items:center;justify-content:center;color:white;font-weight:800;font-size:0.9rem;text-align:center;line-height:1.2;flex-shrink:0;box-shadow:0 10px 20px rgba(153,27,27,0.3);border:4px solid white;">Self<br>Cleaning</div>
                    <div style="background:white;padding:2rem 2.5rem;border-radius:1.5rem;flex:1;box-shadow:0 4px 15px rgba(0,0,0,0.05);">
                        <h4 style="font-weight:800;color:#0c1f3f;margin-bottom:0.5rem;font-size:1.25rem;">Excellent self-cleaning performance</h4>
                        <p style="font-size:0.95rem;color:#4b5563;line-height:1.7;margin:0;">The surface of synthetic resin tile is compact and smooth, with "lotus leaf effect". It is not easy to absorb dust. Once washed by rain, it will be as clean as new. The dirt on the tile surface will not appear mottled after being washed by rain, and it is not easy to hang snow, reducing the risk of collapse due to heavy snow load.</p>
                    </div>
                </div>

                <div class="reveal reveal-delay-1" style="display:flex;gap:1.5rem;align-items:center;">
                    <div style="width:100px;height:100px;background:#991b1b;border-radius:50%;display:flex;align-items:center;justify-content:center;color:white;font-weight:800;font-size:0.9rem;text-align:center;line-height:1.2;flex-shrink:0;box-shadow:0 10px 20px rgba(153,27,27,0.3);border:4px solid white;">Heat<br>Insulation</div>
                    <div style="background:white;padding:2rem 2.5rem;border-radius:1.5rem;flex:1;box-shadow:0 4px 15px rgba(0,0,0,0.05);">
                        <h4 style="font-weight:800;color:#0c1f3f;margin-bottom:0.5rem;font-size:1.25rem;">Excellent thermal insulation performance</h4>
                        <p style="font-size:0.95rem;color:#4b5563;line-height:1.7;margin:0;">The thermal conductivity of synthetic resin tile is 0.325w/m.k, about 1/310 of clay tile, 1/5 of cement tile, and 1/2000 of 0.5mm thick color steel tile. Therefore, the thermal insulation performance of synthetic resin tile can still reach the best without considering the addition of thermal insulation layer.</p>
                    </div>
                </div>

            </div>
        </div>
    </section>

    <!-- Product Accessories -->
    <section style="padding:6rem 2rem;background:white;">
        <div style="max-width:1100px;margin:0 auto;" class="reveal">
            <h2 style="font-size:2.5rem;font-weight:800;color:#0c1f3f;text-align:center;margin-bottom:3rem;text-transform:uppercase;">Product Accessories</h2>
            <div style="display:grid;grid-template-columns:repeat(auto-fill, minmax(220px, 1fr));gap:2rem;">
                
                <div style="background:white;border-radius:1.5rem;padding:2.5rem 2rem;text-align:center;box-shadow:0 10px 30px rgba(0,0,0,0.06);border:1px solid #f3f4f6;">
                    <div style="height:120px;background:#fef2f2;border-radius:1rem;display:flex;align-items:center;justify-content:center;margin-bottom:1.5rem;color:#dc2626;">
                        <i data-lucide="image" style="width:40px;height:40px;"></i>
                    </div>
                    <h4 style="font-weight:800;color:#0c1f3f;font-size:1.15rem;">Top Ridge Tile</h4>
                </div>
                <div style="background:white;border-radius:1.5rem;padding:2.5rem 2rem;text-align:center;box-shadow:0 10px 30px rgba(0,0,0,0.06);border:1px solid #f3f4f6;">
                    <div style="height:120px;background:#fef2f2;border-radius:1rem;display:flex;align-items:center;justify-content:center;margin-bottom:1.5rem;color:#dc2626;">
                        <i data-lucide="image" style="width:40px;height:40px;"></i>
                    </div>
                    <h4 style="font-weight:800;color:#0c1f3f;font-size:1.15rem;">Side Ridge</h4>
                </div>
                <div style="background:white;border-radius:1.5rem;padding:2.5rem 2rem;text-align:center;box-shadow:0 10px 30px rgba(0,0,0,0.06);border:1px solid #f3f4f6;">
                    <div style="height:120px;background:#fef2f2;border-radius:1rem;display:flex;align-items:center;justify-content:center;margin-bottom:1.5rem;color:#dc2626;">
                        <i data-lucide="image" style="width:40px;height:40px;"></i>
                    </div>
                    <h4 style="font-weight:800;color:#0c1f3f;font-size:1.15rem;">Three Way Ridge</h4>
                </div>
                <div style="background:white;border-radius:1.5rem;padding:2.5rem 2rem;text-align:center;box-shadow:0 10px 30px rgba(0,0,0,0.06);border:1px solid #f3f4f6;">
                    <div style="height:120px;background:#fef2f2;border-radius:1rem;display:flex;align-items:center;justify-content:center;margin-bottom:1.5rem;color:#dc2626;">
                        <i data-lucide="image" style="width:40px;height:40px;"></i>
                    </div>
                    <h4 style="font-weight:800;color:#0c1f3f;font-size:1.15rem;">Ridge Tile</h4>
                </div>
                <div style="background:white;border-radius:1.5rem;padding:2.5rem 2rem;text-align:center;box-shadow:0 10px 30px rgba(0,0,0,0.06);border:1px solid #f3f4f6;">
                    <div style="height:120px;background:#fef2f2;border-radius:1rem;display:flex;align-items:center;justify-content:center;margin-bottom:1.5rem;color:#dc2626;">
                        <i data-lucide="image" style="width:40px;height:40px;"></i>
                    </div>
                    <h4 style="font-weight:800;color:#0c1f3f;font-size:1.15rem;">End Cap Side Ridge</h4>
                </div>
                <div style="background:white;border-radius:1.5rem;padding:2.5rem 2rem;text-align:center;box-shadow:0 10px 30px rgba(0,0,0,0.06);border:1px solid #f3f4f6;">
                    <div style="height:120px;background:#fef2f2;border-radius:1rem;display:flex;align-items:center;justify-content:center;margin-bottom:1.5rem;color:#dc2626;">
                        <i data-lucide="image" style="width:40px;height:40px;"></i>
                    </div>
                    <h4 style="font-weight:800;color:#0c1f3f;font-size:1.15rem;">Screw Cap</h4>
                </div>
                <div style="background:white;border-radius:1.5rem;padding:2.5rem 2rem;text-align:center;box-shadow:0 10px 30px rgba(0,0,0,0.06);border:1px solid #f3f4f6;">
                    <div style="height:120px;background:#fef2f2;border-radius:1rem;display:flex;align-items:center;justify-content:center;margin-bottom:1.5rem;color:#dc2626;">
                        <i data-lucide="image" style="width:40px;height:40px;"></i>
                    </div>
                    <h4 style="font-weight:800;color:#0c1f3f;font-size:1.15rem;">Top Ridge End Cap</h4>
                </div>

            </div>
        </div>
        
        <div style="max-width:1100px;margin:6rem auto 0;" class="reveal">
            <!-- CTA -->
            <div style="background:linear-gradient(135deg,#7f1d1d,#991b1b);border-radius:2rem;padding:4rem;text-align:center;position:relative;overflow:hidden;box-shadow:0 20px 40px rgba(127,29,29,0.3);">
                <div style="position:absolute;top:-40px;left:-40px;width:300px;height:300px;border-radius:50%;background:rgba(255,255,255,0.03);"></div>
                <div style="position:relative;z-index:1;">
                    <h3 style="font-size:2.25rem;font-weight:800;color:white;margin-bottom:1rem;">Ready to Upgrade Your Roof?</h3>
                    <p style="color:rgba(254,226,226,0.85);margin-bottom:2.5rem;max-width:550px;margin-left:auto;margin-right:auto;font-size:1.1rem;line-height:1.7;">
                        Contact our experts for site assessment, specifications, and custom quotes for your project.</p>
                    <a href="contact.html" style="display:inline-block;padding:1rem 3rem;background:white;color:#7f1d1d;border-radius:9999px;font-size:1.1rem;font-weight:800;text-decoration:none;box-shadow:0 10px 30px rgba(0,0,0,0.3);transition:transform 0.3s;" onmouseover="this.style.transform='translateY(-4px)'" onmouseout="this.style.transform='translateY(0)'">Get a Free Consultation →</a>
                </div>
            </div>
        </div>
    </section>
"""

c = c[:start_idx] + new_content + "\n    " + c[end_idx:]
with open(file_path, "w", encoding="utf-8") as f:
    f.write(c)
print("Updated roofing.html")
