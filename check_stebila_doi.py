import urllib.request, urllib.parse, json, ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
headers = {'User-Agent': 'Mozilla/5.0'}

url = "https://api.crossref.org/works/10.1145/3133956.3138823"
req = urllib.request.Request(url, headers=headers)
with urllib.request.urlopen(req, context=ctx) as resp:
    data = json.loads(resp.read().decode('utf-8'))['message']
    print("Title:", data.get('title'))
    print("Subtitle:", data.get('subtitle'))
    print("Authors:", [f"{a.get('given', '')} {a.get('family', '')}" for a in data.get('author', [])])
    print("Container:", data.get('container-title'))
    print("Pages:", data.get('page'))
    print("DOI:", data.get('DOI'))
    print("URL:", data.get('URL'))
