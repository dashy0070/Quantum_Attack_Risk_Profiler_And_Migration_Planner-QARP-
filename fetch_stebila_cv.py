import urllib.request, re, ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
headers = {'User-Agent': 'Mozilla/5.0'}

url = "https://www.douglas.stebila.ca/research/papers/"
req = urllib.request.Request(url, headers=headers)
try:
    with urllib.request.urlopen(req, context=ctx, timeout=10) as resp:
        html = resp.read().decode('utf-8', errors='ignore')
        # Search for OpenSSL or liboqs or CCS 2017
        matches = [line for line in html.splitlines() if 'OpenSSL' in line or 'liboqs' in line or '2017' in line]
        print(f"Found {len(matches)} lines matching keywords.")
        for m in matches[:15]:
            clean = re.sub('<[^<]+?>', '', m).strip()
            if clean:
                print(" ->", clean)
except Exception as e:
    print("Error:", e)
