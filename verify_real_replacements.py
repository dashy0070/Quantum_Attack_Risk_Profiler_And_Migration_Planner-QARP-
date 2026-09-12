import urllib.request, json, ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
headers = {'User-Agent': 'Mozilla/5.0'}

# Test Crockett Paquin Stebila on IACR ePrint
url_crockett = "https://eprint.iacr.org/2019/858"
req = urllib.request.Request(url_crockett, headers=headers)
with urllib.request.urlopen(req, context=ctx) as r:
    print(f"IACR ePrint 2019/858: HTTP {r.status} (Verified)")

# Test Paquin Stebila Tamvada DOI on CrossRef
url_tamvada = "https://api.crossref.org/works/10.1007/978-3-030-44223-1_5"
req2 = urllib.request.Request(url_tamvada, headers=headers)
with urllib.request.urlopen(req2, context=ctx) as r2:
    data = json.loads(r2.read().decode('utf-8'))['message']
    print(f"PQCrypto 2020: {data.get('title')} by {[a.get('family') for a in data.get('author', [])]}")
    print(f"DOI URL: {data.get('URL')}")
