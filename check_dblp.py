import urllib.request, urllib.parse, json, ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
headers = {'User-Agent': 'Mozilla/5.0'}

dblp_checks = [
    (10, "Verschuren Stebila Westerbaan"),
    (19, "Debroy Ghosh Basu"),
    (21, "Oder Schneider Pöppelmann"),
    (25, "Bürstinghaus-Steinbach Krauß Niederhagen"),
    (26, "Bandara Mitchell"),
    (27, "Mavrogiannopoulos Robinson Mavroeidis"),
    (37, "Paul Kannwischer Stebila Poppelmann")
]

for tag, q in dblp_checks:
    url = f"https://dblp.org/search/publ/api?q={urllib.parse.quote(q)}&format=json&h=3"
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, context=ctx, timeout=8) as resp:
            data = json.loads(resp.read().decode('utf-8'))
            hits = data.get('result', {}).get('hits', {}).get('hit', [])
            print(f"\n--- [{tag}] DBLP Query: {q} ---")
            if not hits:
                print("  => ZERO hits found on DBLP!")
            for h in hits:
                info = h.get('info', {})
                print(f"  * {info.get('title')} ({info.get('year')}) in {info.get('venue')} [DOI: {info.get('doi')}]")
    except Exception as e:
        print(f"[{tag}] Error: {e}")
