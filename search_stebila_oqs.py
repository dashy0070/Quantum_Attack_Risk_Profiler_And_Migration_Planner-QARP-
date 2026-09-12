import urllib.request, re, ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
headers = {'User-Agent': 'Mozilla/5.0'}

url = "https://www.douglas.stebila.ca/research/papers/"
req = urllib.request.Request(url, headers=headers)
with urllib.request.urlopen(req, context=ctx, timeout=10) as resp:
    html = resp.read().decode('utf-8', errors='ignore')
    for block in html.split('<li'):
        if 'liboqs' in block.lower() or 'open quantum safe' in block.lower() or 'prototyping' in block.lower() or 'crockett' in block.lower() or 'fluhrer' in block.lower():
            clean = re.sub('<[^<]+?>', '', block).strip()
            print("PAPER BLOCK:")
            print(clean[:300])
            print("="*60)
