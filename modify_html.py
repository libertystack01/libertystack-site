import re

def update_nav_and_footer(filepath):
    with open(filepath, 'r') as f:
        content = f.read()

    # Add header buttons
    if '<div class="nav-actions">' not in content:
        content = content.replace('</ul>\n    </nav>', '</ul>\n        <div class="nav-actions">\n            <a href="index.html#contact" class="btn-outline">Schedule Consultation</a>\n            <a href="index.html#contact" class="btn-primary">Request Quote</a>\n        </div>\n    </nav>')

    # Add footer buttons
    if '<div class="footer-cta">' not in content:
        footer_cta = '''<div class="footer-cta">
            <a href="index.html#contact" class="btn-primary">Request a Quote</a>
            <a href="index.html#contact" class="btn-outline" style="border-color: #888; color: #888;">Schedule a Consultation</a>
        </div>\n        <strong>'''
        content = content.replace('<strong>', footer_cta)
        
    with open(filepath, 'w') as f:
        f.write(content)

for file in ['index.html', 'development.html', 'creative.html', 'operations.html']:
    update_nav_and_footer(file)

