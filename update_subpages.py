import re

for file in ['development.html', 'creative.html']:
    with open(file, 'r') as f:
        content = f.read()
    
    # replace class="grid" with class="bento-grid"
    content = content.replace('class="grid"', 'class="bento-grid"')
    
    # replace class="card" with class="glass-card"
    content = content.replace('class="card"', 'class="glass-card"')
    
    with open(file, 'w') as f:
        f.write(content)
