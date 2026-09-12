import urllib.request, urllib.parse, json, ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
headers = {'User-Agent': 'Mozilla/5.0'}

title = "Prototyping post-quantum key exchange on the Internet"
url = f"https://api.crossref.org/works?query.title={urllib.parse.quote(title)}&query.author=Stebila&rows=5"
req = urllib.request.Request(url, headers=headers)
with urllib.request.urlopen(req, context=ctx) as resp:
    data = json.loads(resp.read().decode('utf-8'))['message']['items']
    print(f"Found {len(data)} results:")
    for it in data:
        print("Title:", it.get('title'))
        print("Subtitle:", it.get('subtitle'))
        print("Authors:", [f"{a.get('given', '')} {a.get('family', '')}" for a in it.get('author', [])])
        print("DOI:", it.get('DOI'))
        print("URL:", it.get('URL'))
        print("Pages:", it.get('page'))
        print("Container:", it.get('container-title'))
        print("-" * 50)
