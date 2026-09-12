import urllib.request, urllib.parse, json, ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}

titles_to_check = [
    (1, "I. B. M. Q. Team", "Quantum attack simulations on TLS handshakes"),
    (4, "M. E. Smid", "Transitioning from legacy algorithms: A framework for discovering, categorizing, and retiring non-quantum-safe algorithms in banking data pipelines"),
    (7, "Utimaco", "Post-quantum protocols for banking applications"),
    (8, "L. Bettale, M. De Oliveira, and E. Dottax", "Post-quantum protocols for banking applications"),
    (9, "B. Jones and C. Lee", "Hybrid TLS 1.3 with lattice-based KEMs"),
    (10, "S. R. Verschuren, R. Stebila, and B. Westerbaan", "Post-quantum Key Encapsulation and Signatures in Open Quantum Safe: Benchmarking Transport Layer Performance and Cryptographic Overheads"),
    (14, "D. Kumar", "Quantum-Safe Key Exchange in Legacy Banking Systems"),
    (19, "A. P. Debroy, S. Ghosh, and K. Basu", "Hardware-Root-of-Trust and cryptographic agility for post-quantum financial appliances"),
    (20, "FFIEC", "Architecture, Infrastructure, and Operations: Preparing for Quantum-Resistant Cryptographic Standards"),
    (21, "T. Oder, T. Schneider, and M. Pöppelmann", "Post-quantum cryptography in hardware security modules: Bottlenecks, throughput constraints, and acceleration architectures"),
    (23, "E. Patel", "Assessing the impact of Shor’s algorithm on RSA/ECC"),
    (24, "T. Wiggers", "KEMTLS: Post-quantum TLS without handshake signatures"),
    (25, "K. Bürstinghaus-Steinbach, C. Krauß, and R. Niederhagen", "Post-quantum TLS on enterprise middleboxes: Packet loss, fragmentation, and latency overheads"),
    (26, "K. A. S. S. Bandara and C. J. Mitchell", "Packet fragmentation in post-quantum network protocols: Impact on transaction throughput and timeouts in core banking backbones"),
    (27, "N. V Mavrogiannopoulos, P. Robinson, and V. Mavroeidis", "CBOM: Toward automated cryptographic bill of materials for post-quantum migration audits"),
    (30, "F. Chen", "AES-256 resilience against Grover’s algorithm"),
    (36, "SWIFT Standards Committee", "ISO 20022 Financial Messaging: Managing Cryptographic Agility in pacs.008 and pain.001 Payment Clearings"),
    (37, "S. Paul, B. Kannwischer, D. Stebila, and T. Poppelmann", "Performance analysis and benchmarking of post-quantum cryptographic algorithms across heterogeneous computing platforms")
]

print("Starting CrossRef Title Search Audit...")
for num, author, title in titles_to_check:
    q = urllib.parse.quote(title)
    url = f"https://api.crossref.org/works?query.title={q}&rows=3"
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, context=ctx, timeout=8) as resp:
            res = json.loads(resp.read().decode('utf-8'))
            items = res['message']['items']
            found = False
            for item in items:
                cand_title = item.get('title', [''])[0]
                # Compare similarity
                words_title = set(title.lower().split())
                words_cand = set(cand_title.lower().split())
                overlap = len(words_title.intersection(words_cand)) / max(len(words_title), 1)
                if overlap > 0.65:
                    print(f"[{num}] MATCH FOUND ({overlap*100:.0f}% overlap):")
                    print(f"     Title: {cand_title}")
                    print(f"     DOI:   {item.get('DOI')}")
                    print(f"     Container: {item.get('container-title', [''])[0]}")
                    found = True
                    break
            if not found:
                top_cand = items[0].get('title', [''])[0] if items else "None"
                print(f"[{num}] NO MATCH for: \"{title[:50]}...\" (Top result was: \"{top_cand[:50]}...\")")
    except Exception as e:
        print(f"[{num}] Error querying: {e}")
