import zlib, re

with open('test_paper.pdf', 'rb') as f:
    data = f.read()

# Find all /ObjStm objects
obj_stms = re.findall(rb'<<[^>]*?/Type\s*/ObjStm[^>]*?>>\s*stream[\r\n]+(.*?)[\r\n]+endstream', data, re.DOTALL)
print("Found ObjStm count:", len(obj_stms))
for idx, s in enumerate(obj_stms):
    try:
        dec = zlib.decompress(s)
        # Search for text
        text_matches = re.findall(rb'\((.*?)\)', dec)
        text_strs = [m.decode('latin1', errors='ignore') for m in text_matches if len(m) > 3]
        if any('Quantum' in t or 'Payment' in t for t in text_strs):
            print(f"\n--- ObjStm {idx} has matches ---")
            for t in text_strs[:20]:
                print("  >", t)
    except Exception as e:
        pass
