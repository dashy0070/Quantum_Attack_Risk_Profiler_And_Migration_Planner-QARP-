import urllib.request, urllib.parse, json, ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}

url = "https://api.crossref.org/works?query=Burstinghaus-Steinbach&rows=5"
req = urllib.request.Request(url, headers=headers)
with urllib.request.urlopen(req, context=ctx) as r:
    data = json.loads(r.read().decode('utf-8'))
    items = data['message']['items']
    print(f"Found {len(items)} works for Burstinghaus-Steinbach:")
    for it in items:
        authors = [a.get('family', '') for a in it.get('author', [])]
        print(f"Title: {it.get('title', [''])[0]}")
        print(f"Authors: {', '.join(authors)}")
        print(f"Container: {it.get('container-title', [''])[0]}")
        print(f"DOI: {it.get('DOI')}\n")
