import zlib, re

with open('test_paper.pdf', 'rb') as f:
    data = f.read()

streams = re.findall(rb'stream[\r\n]+(.*?)[\r\n]+endstream', data, re.DOTALL)
print(f"Total streams found: {len(streams)}")

full_text = ""
for s in streams:
    try:
        decompressed = zlib.decompress(s).decode('latin1', errors='ignore')
        # Find TJ or Tj text
        texts = re.findall(r'\((.*?)\)\s*T[jJ]', decompressed)
        if texts:
            full_text += " ".join(texts) + "\n"
    except Exception:
        pass

lines = [line.strip() for line in full_text.splitlines() if line.strip()]
print("\n--- First 20 Extracted Lines from PDF ---")
for l in lines[:20]:
    print(l)
