import urllib.request, urllib.parse, json, ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
headers = {'User-Agent': 'Mozilla/5.0'}

# Search CrossRef for exact title
title = "Post-quantum Key Encapsulation and Signatures in Open Quantum Safe: Benchmarking Transport Layer Performance and Cryptographic Overheads"
url = f"https://api.crossref.org/works?query.title={urllib.parse.quote(title)}&rows=3"
req = urllib.request.Request(url, headers=headers)
with urllib.request.urlopen(req, context=ctx) as resp:
    data = json.loads(resp.read().decode('utf-8'))['message']['items']
    print("CrossRef search for title:")
    for it in data:
        print(" ->", it.get('title'), it.get('DOI'))

# Search CrossRef for Westerbaan in SECRYPT
url2 = "https://api.crossref.org/works?query.author=Westerbaan&query=SECRYPT&rows=3"
req2 = urllib.request.Request(url2, headers=headers)
with urllib.request.urlopen(req2, context=ctx) as resp2:
    data2 = json.loads(resp2.read().decode('utf-8'))['message']['items']
    print("\nCrossRef search for Westerbaan + SECRYPT:")
    for it in data2:
        print(" ->", it.get('title'), it.get('DOI'))
