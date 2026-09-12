import urllib.request, urllib.parse, json, ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
headers = {'User-Agent': 'Mozilla/5.0'}

url = "https://api.crossref.org/works?query=liboqs+OpenSSL+CCS&rows=5"
req = urllib.request.Request(url, headers=headers)
with urllib.request.urlopen(req, context=ctx) as resp:
    data = json.loads(resp.read().decode('utf-8'))['message']['items']
    for it in data:
        print("Title:", it.get('title'))
        print("Authors:", [f"{a.get('given', '')} {a.get('family', '')}" for a in it.get('author', [])])
        print("Container:", it.get('container-title'))
        print("DOI:", it.get('DOI'))
        print("URL:", it.get('URL'))
        print("-" * 50)
