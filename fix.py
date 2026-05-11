import sys

with open('experiment.html', 'r') as f:
    content = f.read()

content = content.replace('\\`', '`')
content = content.replace('\\${', '${')

with open('experiment.html', 'w') as f:
    f.write(content)
