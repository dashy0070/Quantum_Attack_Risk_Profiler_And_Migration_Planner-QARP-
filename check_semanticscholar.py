import urllib.request, urllib.parse, json, ssl, time

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
headers = {'User-Agent': 'Mozilla/5.0'}

queries = [
    (10, 'Verschuren Stebila Westerbaan'),
    (14, 'Kumar Quantum-Safe Key Exchange in Legacy Banking Systems'),
    (19, 'Hardware-Root-of-Trust and cryptographic agility for post-quantum financial'),
    (21, 'Post-quantum cryptography in hardware security modules: Bottlenecks Oder'),
    (23, 'Assessing the impact of Shor algorithm on RSA ECC Patel'),
    (25, 'Post-quantum TLS on enterprise middleboxes: Packet loss Burstinghaus'),
    (26, 'Bandara Mitchell Packet fragmentation in post-quantum network protocols'),
    (27, 'Mavrogiannopoulos CBOM: Toward automated cryptographic bill of materials'),
    (30, 'Chen AES-256 resilience against Grover'),
    (36, 'ISO 20022 Financial Messaging Managing Cryptographic Agility'),
    (37, 'Paul Kannwischer Stebila Poppelmann Performance analysis and benchmarking')
]

for tag, q in queries:
    url = f"https://api.semanticscholar.org/graph/v1/paper/search?query={urllib.parse.quote(q)}&limit=3"
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, context=ctx, timeout=10) as resp:
            data = json.loads(resp.read().decode('utf-8'))
            papers = data.get('data', [])
            if papers:
                p = papers[0]
                print(f"[{tag}] S2 Match: {p.get('title')}")
            else:
                print(f"[{tag}] S2 ZERO RESULTS")
    except Exception as e:
        print(f"[{tag}] Error: {e}")
    time.sleep(1.2)
