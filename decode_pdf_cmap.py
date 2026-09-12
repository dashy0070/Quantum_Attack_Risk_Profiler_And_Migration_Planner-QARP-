import zlib, re

with open('test_paper.pdf', 'rb') as f:
    data = f.read()

# Find all streams and decompress
cmaps = {}
for m in re.finditer(rb'<<[^>]*?/ToUnicode\s+(\d+)\s+0\s+R[^>]*?>>\s*stream[\r\n]+(.*?)[\r\n]+endstream', data, re.DOTALL):
    pass

# Let's find all streams containing beginbfrange or beginbfchar
for m in re.finditer(rb'stream[\r\n]+(.*?)[\r\n]+endstream', data, re.DOTALL):
    raw = m.group(1)
    try:
        dec = zlib.decompress(raw)
        if b'beginbfchar' in dec or b'beginbfrange' in dec:
            lines = dec.decode('latin1', errors='ignore').splitlines()
            for l in lines:
                if '<' in l and '>' in l and len(l) < 50:
                    pass
    except:
        pass

# Let's check page 1 content stream
# Search for /Page <<
page_matches = list(re.finditer(rb'/Type\s*/Page\b[^>]*?>>', data))
print("Pages found:", len(page_matches))
if page_matches:
    p1 = page_matches[0].group(0)
    print("Page 1 dict:", p1.decode('latin1', errors='ignore'))
