import urllib.request, urllib.parse, json, ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
headers = {'User-Agent': 'Mozilla/5.0'}

authors = ['Burstinghaus', 'Buerstinghaus', 'Niederhagen', 'Mavroeidis', 'Kannwischer']
for author in authors:
    url = f"https://api.crossref.org/works?query.author={author}&query=post-quantum&rows=3"
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, context=ctx, timeout=8) as resp:
            data = json.loads(resp.read().decode('utf-8'))
            items = data['message']['items']
            print(f"\n--- Author: {author} (PQC query) ---")
            for it in items:
                t = it.get('title', [''])[0]
                doi = it.get('DOI', '')
                print(f"  * {t} [DOI: {doi}]")
    except Exception as e:
        print(f"Error for {author}: {e}")
