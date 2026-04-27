import re

with open('operations.html', 'r') as f:
    content = f.read()

new_content = """    <div class="container" id="services">
        <div class="section-header">
            <h2 class="section-title">Operations Services</h2>
        </div>
        <div class="bento-grid">
            <div class="glass-card">
                <h3>Customer Support Outsourcing (L1/L2)</h3>
                <p>Dedicated teams ready to assist your clients, ensuring satisfaction and loyalty with multi-tiered support systems operating as a direct extension of your core business.</p>
                <button class="btn btn-primary" onclick="openModal('supportModal')" style="margin-top:auto; align-self: flex-start; border:none; cursor:pointer;">Learn More</button>
            </div>
            <div class="glass-card">
                <h3>Order Management Systems</h3>
                <p>Streamlined logistics and processing to keep your business running smoothly. We bridge the gap between procurement, inventory tracking, and final delivery.</p>
                <button class="btn btn-primary" onclick="openModal('omsModal')" style="margin-top:auto; align-self: flex-start; border:none; cursor:pointer;">Learn More</button>
            </div>
        </div>
    </div>

    <!-- The Modals -->
    <div id="supportModal" class="modal">
        <div class="modal-content">
            <span class="close-btn" onclick="closeModal('supportModal')">&times;</span>
            <h2 style="color:var(--primary-navy);">Strategic Managed Support Contracts (L1/L2)</h2>
            <p>Our comprehensive managed support services are designed to elevate your client experience through dedicated, multi-tiered support systems. We specialize in establishing seamless Level 1 (L1) and Level 2 (L2) technical and customer service operations that operate as a direct extension of your core business.</p>
            <p>By leveraging scalable resource allocation, ongoing training protocols, and rigorous quality assurance, we ensure SLA compliance and rapid issue resolution. Our global capabilities allow us to manage complex inquiries, providing robust coverage tailored specifically to your enterprise requirements.</p>
        </div>
    </div>

    <div id="omsModal" class="modal">
        <div class="modal-content">
            <span class="close-btn" onclick="closeModal('omsModal')">&times;</span>
            <h2 style="color:var(--primary-navy);">Order Fulfillment & Management Systems</h2>
            <p>We deploy structured, automated workflows to optimize the complete lifecycle of international e-commerce orders and intricate supply chain contracts. Our robust management systems bridge the gap between procurement, inventory tracking, and final delivery.</p>
            <p>Through process automation and meticulous data synchronization, we eliminate bottlenecks in cross-border logistics. We provide our enterprise clients with real-time visibility, reducing overhead costs and ensuring unparalleled accuracy and speed in global fulfillment operations.</p>
        </div>
    </div>

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

pattern = re.compile(r'<div class="container">.*?(?=<footer>)', re.DOTALL)
content = pattern.sub(new_content, content)

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
        
        function openModal(id) {
            document.getElementById(id).style.display = "block";
        }
        function closeModal(id) {
            document.getElementById(id).style.display = "none";
        }
        window.onclick = function(event) {
            if (event.target.classList.contains('modal')) {
                event.target.style.display = "none";
            }
        }
    </script>
</body>"""
content = content.replace('</body>', script)

with open('operations.html', 'w') as f:
    f.write(content)
