import urllib.request, json, ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
headers = {'User-Agent': 'Mozilla/5.0'}

url = "https://api.crossref.org/works?query=Westerbaan+Verschuren&rows=3"
req = urllib.request.Request(url, headers=headers)
with urllib.request.urlopen(req, context=ctx) as resp:
    data = json.loads(resp.read().decode('utf-8'))['message']['items']
    print(f"Works matching Westerbaan + Verschuren: {len(data)}")
    for it in data:
        print(it.get('title'))
        print(it.get('DOI'))
