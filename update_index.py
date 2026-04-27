import re

with open('index.html', 'r') as f:
    content = f.read()

services_bento = """<div class="bento-grid">
            <div class="glass-card">
                <h3>Technical Development</h3>
                <p>Advanced web architecture and custom coding solutions (Python, Shopify). We build high-performance systems for a digital-first world.</p>
                <a href="development.html" class="btn" style="margin-top:auto; padding: 10px 20px; align-self: flex-start;">Explore</a>
            </div>
            <div class="glass-card">
                <h3>Creative Production</h3>
                <p>Professional video editing and visual branding designed to capture attention in international markets.</p>
                <a href="creative.html" class="btn" style="margin-top:auto; padding: 10px 20px; align-self: flex-start;">Explore</a>
            </div>
            <div class="glass-card">
                <h3>Business Operations</h3>
                <p>Strategic customer support and order management contracts to streamline your enterprise workflow.</p>
                <a href="operations.html" class="btn" style="margin-top:auto; padding: 10px 20px; align-self: flex-start;">Explore</a>
            </div>
        </div>"""

content = re.sub(r'<div class="grid">.*?</div>\s*</div>', services_bento + '\n    </div>', content, flags=re.DOTALL)

faq_section = """
    <div class="container faq-section" id="faq">
        <div class="section-header">
            <h2 class="section-title">Frequently Asked Questions</h2>
        </div>
        
        <button class="accordion">1. What types of eCommerce platforms do you specialize in?</button>
        <div class="panel">
            <p>We specialize in custom Shopify development, enabling businesses to scale efficiently in international markets with tailored themes, custom apps, and seamless third-party integrations.</p>
        </div>

        <button class="accordion">2. Can you handle complex backend integrations?</button>
        <div class="panel">
            <p>Yes. Our team of Python developers excels at building robust backend architectures, custom APIs, and automating enterprise workflows to ensure your operations run smoothly.</p>
        </div>

        <button class="accordion">3. What does your Customer Support Outsourcing entail?</button>
        <div class="panel">
            <p>Our L1/L2 customer support services provide professional, multi-channel assistance for international clients, ensuring high customer satisfaction and efficient ticket resolution around the clock.</p>
        </div>

        <button class="accordion">4. How do you manage international order processing?</button>
        <div class="panel">
            <p>We leverage advanced Order Management Systems (OMS) to streamline inventory tracking, order fulfillment, and international shipping logistics, reducing errors and turnaround times.</p>
        </div>

        <button class="accordion">5. Do you provide customized service packages?</button>
        <div class="panel">
            <p>Absolutely. LibertyStack Solutions offers flexible BPO and technical service packages tailored to your specific operational needs and growth objectives.</p>
        </div>
    </div>
"""

# Insert FAQ before contact section
content = content.replace('<section class="contact-section"', faq_section + '\n    <section class="contact-section"')

# Add script at the end of body
script = """
    <script>
        var acc = document.getElementsByClassName("accordion");
        for (var i = 0; i < acc.length; i++) {
            acc[i].addEventListener("click", function() {
                this.classList.toggle("active");
                var panel = this.nextElementSibling;
                if (panel.style.maxHeight) {
                    panel.style.maxHeight = null;
                } else {
                    panel.style.maxHeight = panel.scrollHeight + "px";
                } 
            });
        }
    </script>
</body>"""
content = content.replace('</body>', script)

with open('index.html', 'w') as f:
    f.write(content)
