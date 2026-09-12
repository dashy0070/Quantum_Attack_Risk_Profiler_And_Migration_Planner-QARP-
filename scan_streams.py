import zlib, re

with open('test_paper.pdf', 'rb') as f:
    data = f.read()

streams = re.findall(rb'stream[\r\n]+(.*?)[\r\n]+endstream', data, re.DOTALL)
for i, s in enumerate(streams):
    try:
        dec = zlib.decompress(s).decode('latin1', errors='ignore')
        if "Quantum" in dec or "Payment" in dec or "Author" in dec or "Abstract" in dec or "ijcat" in dec.lower():
            print(f"Stream {i} has relevant keywords:")
            # print printable characters
            print(dec[:400])
            print("="*60)
    except:
        pass
