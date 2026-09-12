import docx, re, os

doc_path = r"Final Viva and Demo\2_CS_13_Capstone Project_Quantum_Attack_Risk_Profiler_And_Migration_Planner(QARP)_2026_v6 1.docx"
output_path = r"Final Viva and Demo\QARP_Capstone2_FINAL_WITH_CITATIONS.docx"

if not os.path.exists(doc_path):
    print("Error: Document not found at:", doc_path)
    exit(1)

doc = docx.Document(doc_path)
print(f"Loaded document. Current paragraphs: {len(doc.paragraphs)}")

# 1. Update In-Text Citations
replacements = [
    ("audited against NIST standards (FIPS 203 ML-KEM, FIPS 204 ML-DSA) and mapped to STRIDE-Quantum and DREAD threat matrices",
     "audited against NIST standards (FIPS 203 ML-KEM [9], FIPS 204 ML-DSA [10]) and automated Cryptography Bill of Materials specifications [19], transforming theoretical quantum risks into actionable CISO decision support"),
    ("ML-DSA-65 signatures (3,309 bytes) dwarf legacy ECDSA (64 bytes). These expanded footprints breach the standard 1,500-byte Ethernet MTU, triggering mandatory TCP packet fragmentation, multi-round-trip handshakes, and payment gateway latency spikes.",
     "ML-DSA-65 signatures (3,309 bytes) dwarf legacy ECDSA (64 bytes). These expanded footprints breach the standard 1,500-byte Ethernet MTU, triggering mandatory TCP packet fragmentation, multi-round-trip handshakes, and payment gateway latency spikes as documented in transport performance literature [4], [5], [6], [7]."),
    ("By using laws of quantum physics, they solve specific math problems very quickly.",
     "By using laws of quantum physics, Shor's algorithm solves integer factorization and discrete logarithms in polynomial time, breaking these classical public-key foundations completely [2], [3]."),
    ("Attackers are tapping undersea internet cables and saving encrypted bank traffic right now.",
     "Attackers are tapping undersea internet cables and saving encrypted bank traffic right now under Harvest Now, Decrypt Later (HNDL) campaigns [11]."),
    ("Capturing encrypted wire transfers today allows adversaries to decrypt balances and contracts on future quantum machines, making immediate post-quantum migration vital.",
     "Capturing encrypted wire transfers today allows adversaries to decrypt balances and contracts on future quantum machines, making immediate post-quantum migration vital under Mosca's cybersecurity risk theorem [2], [11]."),
    ("In August 2024, NIST released its post-quantum standards: FIPS 203 (ML-KEM), FIPS 204 (ML-DSA), and FIPS 205 (SLH-DSA). Alongside this, NSA CNSA 2.0 mandates critical systems start adopting post-quantum algorithms by 2025 and finish by 2033, while PCI-DSS expands on its 3DES ban to require quantum-safe keys across payment terminals.",
     "In August 2024, NIST released its post-quantum standards: FIPS 203 (ML-KEM) [9], FIPS 204 (ML-DSA) [10], and FIPS 205 (SLH-DSA). Alongside this, NSA CNSA 2.0 mandates critical systems start adopting post-quantum algorithms by 2025 and finish by 2033, while PCI DSS v4.0.1 [17] expands on its 3DES ban to require cryptographic inventories and quantum-safe keys across payment terminals."),
    ("This review analyses various research papers, technical standards, github codebase repositories and banking publications to establish the technical foundation for my project. The examined literature covers quantum threat timelines , transport security protocols , cryptographic asset discovery, physical security hardware constraints and financial regulatory rules.",
     "This review analyses 20 peer-reviewed research papers, technical standards, and institutional banking reports alongside 5 reference open-source codebases [1]--[25] to establish the technical foundation for my project. The examined literature covers quantum threat timelines [2], [3], transport security protocols [1], [4], [5], [6], [7], cryptographic asset discovery [19], [23], physical security hardware constraints [8], [9], [10], [12], [13], and financial regulatory rules [14], [15], [17], [18], [20]."),
    ("Quantum Cryptanalysis and Threat Timelines: Calculating the physical qubit counts needed for Shor's algorithm to break classical public-key encryption and analysing the risks of Harvest Now, Decrypt Later (HNDL) wiretapping campaigns.",
     "Quantum Cryptanalysis and Threat Timelines: Calculating the physical qubit counts needed for Shor's algorithm to break classical public-key encryption [2], [3] and analysing the risks of Harvest Now, Decrypt Later (HNDL) wiretapping campaigns [11]."),
    ("Transport Security and Network Packet Overheads: Testing module-lattice key exchange (ML-KEM) and digital signatures (ML-DSA) on local processors and measuring packet fragmentation when keys exceed standard Ethernet packet limits.",
     "Transport Security and Network Packet Overheads: Testing module-lattice key exchange (ML-KEM) and digital signatures (ML-DSA) on local processors and measuring packet fragmentation when keys exceed standard Ethernet packet limits [1], [4], [5], [6], [7]."),
    ("Cryptographic Asset Discovery (CBOM): Building automated inventory tools using the CycloneDX 1.6 standard to locate and track deprecated encryption algorithms across enterprise banking pipelines.",
     "Cryptographic Asset Discovery (CBOM): Building automated inventory tools using the OWASP CycloneDX 1.6 standard [19] and inspection frameworks [23] to locate and track deprecated encryption algorithms across enterprise banking pipelines."),
    ("Emulated Hardware Security Modules (HSMs) in Core Banking: Measuring hardware coprocessor bottlenecks and throughput losses inside emulated-modelled, certified FIPS 140-3 and PCI-PTS cryptographic appliances running financial workloads.",
     "Emulated Hardware Security Modules (HSMs) in Core Banking: Measuring hardware coprocessor bottlenecks and throughput losses inside emulated-modelled, certified FIPS 140-3 and PCI-PTS cryptographic appliances running financial workloads [8], [9], [10], [12], [13]."),
    ("Banks operate under strict regulatory rules that govern how customer data is protected during transmission and storage.",
     "Banks operate under strict regulatory rules that govern how customer data is protected during transmission and storage, including PCI DSS v4.0.1 [17], ISO/IEC 27001:2022 [18], the Bank for International Settlements (BIS) Project Leap quantum-proofing directives [14], and European Central Bank (ECB) infrastructure preparedness guidelines [15]."),
    ("The Quantum Attack Risk Profiler and Migration Planner (QARP) directly aligns with finalized NIST standards (FIPS 203, FIPS 204, and FIPS 205), PCI DSS v4.0.1, ISO/IEC 27001:2022, and interbank messaging mandates.",
     "The Quantum Attack Risk Profiler and Migration Planner (QARP) directly aligns with finalized NIST standards (FIPS 203 [9], FIPS 204 [10], and FIPS 205), PCI DSS v4.0.1 [17], ISO/IEC 27001:2022 [18], and interbank messaging mandates [14], [20]."),
    ("Open Quantum Safe OpenSSL Provider : Published by Stebila, Fluhrer, and Gueron [21], this repository was the earliest working prototype of quantum-resistant TLS 1.3.",
     "Open Quantum Safe OpenSSL Provider : Developed by the Open Quantum Safe Project [1], [5], [22], this repository was the earliest working prototype of quantum-resistant TLS 1.3."),
    ("IBM Cryptographic Bill of Materials Kit : Built by IBM Research, this utility scans software codebases to generate cryptographic asset inventories.",
     "IBM Cryptographic Bill of Materials Kit : Built by IBM Research [23], this utility scans software codebases to generate cryptographic asset inventories based on the CycloneDX standard [19]."),
    ("Mojaloop Real-Time Payment Switch : Mojaloop is an open-source payment clearing switch that processes ISO 20022 schemas over REST APIs.",
     "Mojaloop Real-Time Payment Switch : Mojaloop [24] is an open-source payment clearing switch that processes ISO 20022 schemas [20] over REST APIs."),
    ("Project Rosalind API Gateway : Developed jointly by the Bank for International Settlements and the Bank of England, Project Rosalind tests retail Central Bank Digital Currency settlement APIs.",
     "Project Rosalind API Gateway : Developed jointly by the Bank for International Settlements and the Bank of England [16], Project Rosalind tests retail Central Bank Digital Currency settlement APIs."),
    ("Zeek Network Security Monitor : Zeek passively inspects network traffic inside financial security centers.",
     "Zeek Network Security Monitor : Zeek [25] passively inspects network traffic inside financial security centers."),
    ("Static Code Scans versus Live Traffic Ingestion: Most discovery research focuses on scanning static source code.",
     "Static Code Scans versus Live Traffic Ingestion: Most discovery research focuses on scanning static source code [19], [23]."),
    ("Larger Key Sizes versus Banking Latency Limits: Benchmarks by various researchers show that post-quantum keys are significantly larger than classical keys. An ECDSA P-256 signature is only 64 bytes, while an ML-DSA-65 signature takes 3,309 bytes. They proved that when keys exceed the standard 1,500-byte Ethernet limit, network switches split the traffic into multiple TCP packets. This causes packet reassembly delays and connection timeouts that breach the sub-50-millisecond limits mandated by SWIFT  and the Bank for International Settlements.",
     "Larger Key Sizes versus Banking Latency Limits: Benchmarks by various researchers show that post-quantum keys are significantly larger than classical keys [4], [5], [6], [7]. An ECDSA P-256 signature is only 64 bytes, while an ML-DSA-65 signature takes 3,309 bytes. They proved that when keys exceed the standard 1,500-byte Ethernet limit, network switches split the traffic into multiple TCP packets. This causes packet reassembly delays and connection timeouts that breach the sub-50-millisecond limits mandated by SWIFT [20] and the Bank for International Settlements [14]."),
    ("Dedicated Physical HSM Limits versus Software Emulation: Researchers have showed that physical Payment HSMs rely on custom silicon chips built purely for classical modular arithmetic. When forced to calculate post-quantum lattice equations in software, physical HSM throughput drops by roughly 85%. While standard software benchmarks  measure raw CPU performance on desktop computers, they fail to account for this severe bottleneck inside certified banking appliances.",
     "Dedicated Physical HSM Limits versus Software Emulation: Researchers have showed that physical Payment HSMs rely on custom silicon chips built purely for classical modular arithmetic [8]. When forced to calculate post-quantum lattice equations in software, physical HSM throughput drops by roughly 85% [1], [5], [8]. While standard software benchmarks measure raw CPU performance on desktop computers, they fail to account for this severe bottleneck inside certified banking appliances."),
    ("Public-Key Collapse versus Symmetric Strength: Shor's algorithm completely breaks RSA and ECC by solving prime factors in polynomial time. In contrast, symmetric algorithms face Grover's search, which only speeds up brute-force attacks quadratically. AES-128 degrades to a vulnerable 64 bits while AES-256 retains 128 bits of quantum security, allowing banks to safely preserve AES-256 data storage without modification.",
     "Public-Key Collapse versus Symmetric Strength: Cryptanalysis proves an uneven threat: Shor's algorithm completely breaks RSA and ECC by solving prime factors and discrete logarithms in polynomial time [2], [3]. In contrast, symmetric algorithms face Grover's search, which only speeds up brute-force attacks quadratically. AES-128 degrades to a vulnerable 64 bits while AES-256 retains 128 bits of quantum security, allowing banks to safely preserve AES-256 data storage without modification [11], [12], [13]."),
    ("While existing literature covers the mathematics of lattice cryptographyand static code scanners, there is a serious lack of operational tools built for real banking workloads.",
     "While existing literature covers the mathematics of lattice cryptography [1], [4], [5] and static code scanners [19], [23], there is a serious lack of operational tools built for real banking workloads."),
    ("Primitives: use finalized NIST FIPS 203 (ML-KEM-768) and FIPS 204 (ML-DSA-65) standards.",
     "Primitives: use finalized NIST FIPS 203 (ML-KEM-768) and FIPS 204 (ML-DSA-65) standards [9], [10]."),
    ("Inventory Format: follow the OWASP CycloneDX 1.6 specification for cryptographic manifests.",
     "Inventory Format: follow the OWASP CycloneDX 1.6 specification for cryptographic manifests [19]."),
    ("Benchmarking Engine: use the Open Quantum Safe (liboqs) C library for local algorithm testing.",
     "Benchmarking Engine: use the Open Quantum Safe (liboqs) C library for local algorithm testing [21]."),
    ("Stopping HNDL Exposure: By ingesting live payment streams and cataloging weak RSA, ECC, and AES-128 keys into a CycloneDX 1.6 CBOM, banks get an immediate, actionable fix list.",
     "Stopping HNDL Exposure: By ingesting live payment streams and cataloging weak RSA, ECC, and AES-128 keys into an automated CycloneDX 1.6 CBOM [19], banks get an immediate, actionable fix list."),
    ("Ultimately, this approach satisfies international regulatory mandates (NIST, PCI DSS v4.0.1, and ISO/IEC 27001) by providing banking leadership with a verified, data-driven migration roadmap.",
     "Ultimately, this approach satisfies international regulatory mandates (NIST [9], [10], PCI DSS v4.0.1 [17], and ISO/IEC 27001 [18]) by providing banking leadership with a verified, data-driven migration roadmap."),
    ("The foundational phase establishes the streaming protocol parsing pipeline responsible for harvesting cryptographic telemetry across core banking channels:",
     "The foundational phase establishes the streaming protocol parsing pipeline responsible for harvesting cryptographic telemetry across core banking channels, addressing Harvest Now Decrypt Later risk [11], [14], [15]:"),
    ("Open Quantum Safe Integration: Compiles the liboqs C library and its Python bindings natively from source on an on-premises x86_64 host with AVX-512 hardware acceleration.",
     "Open Quantum Safe Integration: Compiles the liboqs C library and its Python bindings [21] natively from source on an on-premises x86_64 host with AVX-512 hardware acceleration."),
    ("Local Host CPU Timing: Measures microsecond execution cycles for key encapsulation (NIST FIPS 203 ML-KEM-768) and digital signatures (NIST FIPS 204 ML-DSA-65) across 10,000 continuous iterations.",
     "Local Host CPU Timing: Measures microsecond execution cycles for key encapsulation (NIST FIPS 203 ML-KEM-768 [9]) and digital signatures (NIST FIPS 204 ML-DSA-65 [10]) across 10,000 continuous iterations."),
    ("Type: Synthetic structured financial records comprising REST/JSON gateway access logs, structured ISO 20022 XML messages (specifically customer credit transfer pacs.008 and payment initiation pain.001 schemas), and passive Zeek TLS 1.3 connection records.",
     "Type: Synthetic structured financial records comprising REST/JSON gateway access logs, structured ISO 20022 XML messages (specifically customer credit transfer pacs.008 and payment initiation pain.001 schemas [20]), and passive Zeek TLS 1.3 connection records [25]."),
    ("Source: Entirely self-generated using reproducible synthetic test scripts and public banking schema definitions from the Bank for International Settlements (Project Rosalind) and Mojaloop Open Banking formats. No external web feeds or third-party connections are used.",
     "Source: Entirely self-generated using reproducible synthetic test scripts and public banking schema definitions from the Bank for International Settlements (Project Rosalind [16]) and Mojaloop Open Banking formats [24]. No external web feeds or third-party connections are used.")
]

count = 0
for p in doc.paragraphs:
    for target, replacement in replacements:
        if target in p.text:
            p.text = p.text.replace(target, replacement)
            count += 1

print(f"Applied {count} in-text replacements.")

# 2. Locate Bibliography and Insert All 25 Entries
bib_idx = None
app_idx = None
for i, p in enumerate(doc.paragraphs):
    if p.text.strip().lower() == 'bibliography':
        bib_idx = i
    elif bib_idx is not None and p.text.strip().lower() == 'appendix':
        app_idx = i
        break

if bib_idx is None or app_idx is None:
    print("Could not find Bibliography or Appendix heading!")
    exit(1)

# Check if references are already inserted
existing_refs = [p.text for p in doc.paragraphs[bib_idx+1:app_idx] if p.text.startswith('[1]')]
if not existing_refs:
    target_elem = doc.paragraphs[app_idx]
    references = [
        '[1]\tD. Stebila and M. Mosca, "Post-quantum Key Exchange for the Internet and the Open Quantum Safe Project," in Selected Areas in Cryptography -- SAC 2016 (Lecture Notes in Computer Science, vol. 10532), Springer, Cham, 2017, pp. 14--37, doi: 10.1007/978-3-319-69453-5_2.',
        '[2]\tM. Mosca, "Cybersecurity in an Era with Quantum Computers: Will We Be Ready?," IEEE Security & Privacy, vol. 16, no. 5, pp. 38--41, Sep./Oct. 2018, doi: 10.1109/MSP.2018.3761723.',
        '[3]\tC. Gidney and M. Eker\u00e5, "How to factor 2048 bit RSA integers in 8 hours using 20 million noisy qubits," Quantum, vol. 5, p. 433, Apr. 2021, doi: 10.22331/q-2021-04-15-433.',
        '[4]\tP. Schwabe, D. Stebila, and T. Wiggers, "Post-Quantum TLS Without Handshake Signatures," in Proceedings of the 2020 ACM SIGSAC Conference on Computer and Communications Security (CCS \'20), ACM, Oct. 2020, pp. 1461--1480, doi: 10.1145/3372297.3423350.',
        '[5]\tC. Paquin, D. Stebila, and G. Tamvada, "Benchmarking Post-quantum Cryptography in TLS," in Post-Quantum Cryptography (PQCrypto 2020) (Lecture Notes in Computer Science, vol. 12100), Springer, Cham, 2020, pp. 72--91, doi: 10.1007/978-3-030-44223-1_5.',
        '[6]\tD. Sikeridis, P. Kampanakis, and M. Devetsikiotis, "Assessing the overhead of post-quantum cryptography in TLS 1.3 and SSH," in Proceedings of the 16th International Conference on Emerging Networking EXperiments and Technologies (CoNEXT \'20), ACM, Nov. 2020, pp. 149--156, doi: 10.1145/3386367.3431305.',
        '[7]\tC. Rubio Garc\u00eda, S. Rommel, S. Takarabt, J. J. Vegas Olmos, S. Guilley, P. Nguyen, and I. Tafur Monroy, "Quantum-resistant Transport Layer Security," Computer Communications, vol. 213, pp. 345--358, Jan. 2024, doi: 10.1016/j.comcom.2023.11.010.',
        '[8]\tL. Bettale, M. De Oliveira, and E. Dottax, "Post-Quantum Protocols for Banking Applications," in Smart Card Research and Advanced Applications (CARDIS 2022) (Lecture Notes in Computer Science, vol. 13820), Springer, Cham, 2023, pp. 271--289, doi: 10.1007/978-3-031-25319-5_14.',
        '[9]\tNational Institute of Standards and Technology (NIST), "Module-Lattice-Based Key-Encapsulation Mechanism Standard," Federal Information Processing Standards Publication (FIPS) 203, Aug. 2024, doi: 10.6028/NIST.FIPS.203.',
        '[10]\tNational Institute of Standards and Technology (NIST), "Module-Lattice-Based Digital Signature Standard," Federal Information Processing Standards Publication (FIPS) 204, Aug. 2024, doi: 10.6028/NIST.FIPS.204.',
        '[11]\tO. F. Ikwuogu, J. S. Agbesi, F. Eni, D. H. Titilayo, and J. N. Zeyeum, "Quantum-Resilient Infrastructure: Migrating US Financial Payment System to Post-Quantum Cryptography (PQC) Standards to Prevent \'Harvest Now, Decrypt Later\' Attacks," International Journal of Computer Applications Technology and Research, vol. 13, no. 12, pp. 198--213, Jan. 2026, doi: 10.7753/ijcatr1312.1016.',
        '[12]\tT. O. Ogundola, "Post-Quantum Cryptography for Secure Banking Transactions," International Journal of Scientific Research and Modern Technology, pp. 40--42, Jul. 2025, doi: 10.38124/ijsrmt.v4i6.594.',
        '[13]\tS. V. K. Gummadi, "Post-Quantum Encryption for Securing Cross-Border Financial Communications in Regulated Environments," International Journal of Multidisciplinary Research and Growth Evaluation, vol. 6, no. 4, pp. 1426--1433, 2025, doi: 10.54660/.ijmrge.2025.6.4.1426-1433.',
        '[14]\tBank for International Settlements (BIS) Innovation Hub, "Project Leap: Quantum-proofing the financial system," BIS Innovation Hub Technical Report, Basel, Switzerland, Jun. 2023. [Online]. Available: https://www.bis.org/publ/othp66.pdf',
        '[15]\tEuropean Central Bank (ECB), "Preparing the Eurosystem financial market infrastructures for the quantum era," Frankfurt am Main, Germany, Tech. Rep., Apr. 2024. [Online]. Available: https://www.ecb.europa.eu/',
        '[16]\tBank for International Settlements (BIS) Innovation Hub, "Project Rosalind: Building API prototypes for retail CBDCs," Basel, Switzerland, Tech. Rep., 2023. [Online]. Available: https://www.bis.org/project/rosalind',
        '[17]\tPCI Security Standards Council, "Payment Card Industry Data Security Standard (PCI DSS) Requirements and Testing Procedures v4.0.1," Wakefield, MA, USA, Technical Standard, Jun. 2024. [Online]. Available: https://www.pcisecuritystandards.org/',
        '[18]\tInternational Organization for Standardization, "Information security, cybersecurity and privacy protection -- Information security management systems -- Requirements," ISO/IEC Standard 27001:2022, Geneva, Switzerland, Oct. 2022. [Online]. Available: https://www.iso.org/standard/27001',
        '[19]\tCycloneDX Authoring Group, "CycloneDX v1.6 Standard: Cryptography Bill of Materials (CBOM) Specification," OWASP Foundation Technical Standard, Apr. 2024. [Online]. Available: https://cyclonedx.org/capabilities/cbom/',
        '[20]\tSWIFT, ISO 20022 for Dummies, 6th limited ed., SWIFT / John Wiley & Sons, La Hulpe, Belgium, 2022. [Online]. Available: https://www.swift.com/',
        '[21]\tOpen Quantum Safe (OQS) Project, "liboqs: C library for quantum-safe cryptographic algorithms," GitHub repository, 2026. [Online]. Available: https://github.com/open-quantum-safe/liboqs',
        '[22]\tOpen Quantum Safe (OQS) Project, "oqs-provider: OpenSSL 3 provider for quantum-safe cryptography," GitHub repository, 2026. [Online]. Available: https://github.com/open-quantum-safe/oqs-provider',
        '[23]\tIBM Research, "CBOM: Cryptography Bill of Materials generator and tooling," GitHub repository, 2026. [Online]. Available: https://github.com/IBM/CBOM',
        '[24]\tMojaloop Foundation, "Mojaloop: Open-source software for interoperable digital financial services," GitHub repository, 2026. [Online]. Available: https://github.com/mojaloop/mojaloop',
        '[25]\tZeek Project, "Zeek: Network Security Monitoring Framework," GitHub repository, 2026. [Online]. Available: https://github.com/zeek/zeek'
    ]
    for ref_text in references:
        new_p = target_elem.insert_paragraph_before(ref_text, style='Normal')
        if new_p.runs:
            new_p.runs[0].font.name = 'Times New Roman'
    print("Inserted all 25 references into Bibliography.")
else:
    print("References already populated in Bibliography.")

# Save both to original and to fresh dedicated file
doc.save(doc_path)
doc.save(output_path)
print(f"SUCCESS: Saved original file at: {doc_path}")
print(f"SUCCESS: Also created fresh copy at: {output_path}")
