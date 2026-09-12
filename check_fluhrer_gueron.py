import urllib.request, urllib.parse, json, ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
headers = {'User-Agent': 'Mozilla/5.0'}

# Search DBLP for Fluhrer
url = "https://dblp.org/search/publ/api?q=Fluhrer+Gueron&format=json"
req = urllib.request.Request(url, headers=headers)
try:
    with urllib.request.urlopen(req, context=ctx) as resp:
        data = json.loads(resp.read().decode('utf-8'))
        hits = data.get('result', {}).get('hits', {}).get('hit', [])
        print(f"DBLP Fluhrer+Gueron hits: {len(hits)}")
        for h in hits:
            info = h.get('info', {})
            print(f" * Title: {info.get('title')}")
            print(f"   Venue: {info.get('venue')}, {info.get('year')}")
            print(f"   DOI: {info.get('doi')}")
            print(f"   URL: {info.get('ee')}\n")
except Exception as e:
    print("Error:", e)
