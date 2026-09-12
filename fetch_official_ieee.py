import urllib.request, json, ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

dois = [
    ("10.1007/978-3-319-69453-5_2", "SAC 2016 (Stebila & Mosca)"),
    ("10.1109/MSP.2018.3761723", "IEEE S&P 2018 (Mosca)"),
    ("10.22331/q-2021-04-15-433", "Quantum 2021 (Gidney & Ekera)"),
    ("10.1145/3372297.3423350", "ACM CCS 2020 (Schwabe, Stebila, Wiggers)"),
    ("10.1007/978-3-030-44223-1_5", "PQCrypto 2020 (Paquin, Stebila, Tamvada)"),
    ("10.1145/3386367.3431309", "ACM CoNEXT 2020 (Sikeridis, Kampanakis, Devetsikiotis)"),
    ("10.1016/j.comcom.2023.11.010", "Comput. Commun. 2024 (Rubio Garcia et al.)"),
    ("10.1007/978-3-031-25319-5_14", "CARDIS 2022 (Bettale et al.)"),
    ("10.6028/NIST.FIPS.203", "NIST FIPS 203"),
    ("10.6028/NIST.FIPS.204", "NIST FIPS 204"),
    ("10.38124/ijsrmt.v4i6.594", "IJSRMT 2025 (Ogundola)"),
    ("10.54660/.ijmrge.2025.6.4.1426-1433", "IJMRGE 2025 (Gummadi)"),
    ("10.7753/ijcatr1312.1016", "IJCATR 2026 (Quantum-Resilient Infrastructure)")
]

print("Fetching official IEEE citations directly from doi.org content negotiation...\n")
for doi, label in dois:
    url = f"https://doi.org/{doi}"
    req = urllib.request.Request(url, headers={'Accept': 'text/bibliography; style=ieee', 'User-Agent': 'Mozilla/5.0'})
    try:
        with urllib.request.urlopen(req, context=ctx, timeout=10) as resp:
            content = resp.read().decode('utf-8').strip()
            print(f"[{label}]")
            print(content)
            print("-" * 60)
    except Exception as e:
        print(f"[{label}] Error: {e}\n")
