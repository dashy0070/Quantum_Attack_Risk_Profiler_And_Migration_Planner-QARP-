import re

with open('test_paper.pdf', 'rb') as f:
    data = f.read()

print("PDF length:", len(data))
# Look for /Author or /Title or /Producer in the PDF info dictionary
for match in re.finditer(rb'/(Author|Title|Subject|Keywords|Creator|Producer)\s*(\([^\)]+\)|<[^>]+>)', data):
    key = match.group(1).decode('latin1')
    val = match.group(2).decode('latin1')
    print(f"{key}: {val}")
