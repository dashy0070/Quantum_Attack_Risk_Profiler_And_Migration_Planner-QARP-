# Quantum Attack Risk Profiler and Migration Planner (QARP)
> Platform-Agnostic Enterprise Banking Sizing, Telemetry Profiling, and Cryptographic Modernization Framework
> 100% Local Execution | Zero External Cloud Dependency | NIST FIPS 203/204/205 & NSA CNSA 2.0 Compliant

---

## 1. Overview

The Quantum Attack Risk Profiler and Migration Planner (QARP) is an enterprise security engineering framework designed for Tier-1 core banking infrastructures, interbank payment switches (SWIFT, RTGS, ISO 20022), and financial API gateways. 

The framework evaluates cryptographic exposure against quantum cryptanalysis (Shor's and Grover's algorithms), models Payment Hardware Security Module (HSM) appliance scaling deficits (+525%), computes network MTU packet fragmentation across 1,500-byte boundaries, and delivers an interactive executive modernization roadmap with dynamic risk analytics.

---

## 2. Prerequisites

* Operating System: Windows 10/11, Linux (Ubuntu/RHEL/Debian), or macOS.
* Python Environment: Python 3.10, 3.11, or 3.12.
* Network Access: Zero internet connection required at runtime (fully air-gapped and on-premise compatible).

---

## 3. Execution Instructions

### Step 1: Clone and Navigate to Repository
```bash
git clone https://github.com/dashy0070/Quantum_Attack_Risk_Profiler_And_Migration_Planner-QARP-.git
cd Quantum_Attack_Risk_Profiler_And_Migration_Planner-QARP-
```

### Step 2: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 3: Launch Interactive GUI Cockpit
```bash
streamlit run app.py
```
*(Windows users can also double-click `run_demo.bat` or execute `.\run_demo.ps1`)*

The web application will open in the default browser at: `http://localhost:8501`

Navigational Views:
1. Ingestion & Telemetry Parser: Ingest JSON/CSV logs, synthetic transaction streams, or binary PCAP packet captures with TLS ClientHello dissection.
2. Quantum Risk Profiler: Gidney-Ekera (2021) physical qubit estimations and Grover symmetric key halving calculations.
3. CBOM Compliance Matrix: CycloneDX 1.6 Cryptographic Bill of Materials catalog with search, filter, and CSV export.
4. Hardware Capacity Engine: Payment HSM throughput degradation modeling and MTU 1500-byte packet fragmentation analysis.
5. Real-World Attack Vectors & Exploits: Mathematical, side-channel (DPA/CPA on NTT), and fault injection (FIA) exploit simulations across 8 cryptographic algorithms.
6. Strategic Migration Roadmap: Mosca's Theorem risk calculator, Hybrid TLS 1.3 dual key exchange proofs, and phased modernization plan.
7. Executive CISO Report & Analytics: Unified CBOM-to-endpoint ledger and centered visual pie charts with one-click generator controls.

---

### Step 4: Execute CLI Sizing and Cost Engine
To run automated batch sizing directly in the terminal:
```bash
python pqc_log_parser_and_cost_engine.py
```

---

### Step 5: Execute Test Scripts and Validation Tools (in `test/`)
```bash
# Run local CPU cycle benchmarks for ML-KEM-768 and ML-DSA-65
python test/test_liboqs_benchmarks.py

# Run Payment HSM cryptographic support validation
python test/test_hsm_pqc_support.py

# Generate STRIDE post-quantum threat model
python "test/Threat Model.py"

# Validate pure-Python binary PCAP packet dissector
python test/test_pcap_parser.py
```

---

## 4. Repository Structure

```text
├── app.py                             # Interactive Streamlit Application (7 Navigation Views)
├── pqc_log_parser_and_cost_engine.py  # Standalone Mathematical Sizing and Cost Analysis Engine
├── cryptographic_algorithms_pqc.xlsx  # CycloneDX 1.6 Cryptographic Bill of Materials Catalog
├── run_demo.bat                       # Windows Batch Launcher Script
├── run_demo.ps1                       # PowerShell Interactive Launcher Script
├── requirements.txt                   # Python Package Dependencies
├── README.md                          # Main Execution and Architecture Documentation
├── WHATS_NEW.md                       # Feature Matrix, Competitor Benchmarks, and Deployment Guide
├── TEST_CASES_AND_VALIDATION_GUIDE.md # Test Case Matrix and Validation Procedures
├── .gitignore                         # Git Exclusion Rules
│
└── test/                              # Test Scripts, Sample Inputs, Ingress Logs, and Traces
    ├── sample_banking_traffic.pcap    # Binary Wireshark Packet Capture (TLS ClientHello Handshakes)
    ├── sample_banking_logs.json       # Sample Ingress Telemetry (JSON Format - 6 Endpoints)
    ├── sample_banking_logs.csv        # Sample Ingress Telemetry (CSV Format)
    ├── synthetic_traffic_10k.json     # Synthetic High-Throughput Stream (10,000 Transactions)
    ├── test_liboqs_benchmarks.py      # Empirical Hardware Benchmark Tool
    ├── test_hsm_pqc_support.py        # Payment HSM Cryptographic Support Validator
    ├── Threat Model.py                # STRIDE Quantum Threat Model Generation Script
    ├── test_pcap_parser.py            # PCAP Binary Dissector Validation Tool
    ├── generate_sample_pcap.py        # PCAP Binary Synthesis Script
    ├── qarp_cryptographic_bill_of_materials.csv # Sample Output CBOM Inventory
    └── qarp_quantum_risk_profiling_report.csv   # Sample Output Quantum Risk Report
```

---

## 5. Standards and Regulatory Alignment

* NIST Post-Quantum Standards: FIPS 203 (ML-KEM), FIPS 204 (ML-DSA), FIPS 205 (SLH-DSA).
* National Security Agency: Commercial National Security Algorithm Suite 2.0 (NSA CNSA 2.0).
* Financial Industry Standards: PCI-DSS v4.0 (Requirements 3 & 4), SWIFT ISO 20022 (pacs.008, pacs.002, MT103).
* Supply Chain Security: OWASP CycloneDX v1.6 Cryptography Bill of Materials (CBOM).
