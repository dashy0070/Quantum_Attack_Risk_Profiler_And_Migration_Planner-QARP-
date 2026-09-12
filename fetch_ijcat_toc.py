import urllib.request, ssl, re

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}

url = "https://ijcat.com/archieve/volume13/issue12/"
req = urllib.request.Request(url, headers=headers)
try:
    with urllib.request.urlopen(req, context=ctx, timeout=10) as resp:
        html = resp.read().decode('utf-8', errors='ignore')
        print(f"Page length: {len(html)}")
        for block in html.split('<tr'):
            if '1016' in block or 'Quantum' in block:
                print("ROW:")
                print(re.sub('<[^<]+?>', ' ', block).strip())
                print("="*60)
except Exception as e:
    print("Error:", e)
