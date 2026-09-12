# 🏦 Quantum Attack Risk Profiler & Migration Planner (QARP)
> **Enterprise Banking Sizing, Telemetry Profiling & Cryptographic Modernization Framework**  
> *100% Local Execution • Zero External Cloud Dependency • NIST FIPS 203/204/205 & NSA CNSA 2.0 Compliant*

---

## 📌 Overview

**QARP (Quantum Attack Risk Profiler and Migration Planner)** is an enterprise security engineering framework designed for Tier-1 core banking infrastructures, interbank payment switches (SWIFT, RTGS, ISO 20022), and financial API gateways. It evaluates quantum cryptanalysis exposure (Shor's and Grover's algorithms), models **Hardware Security Module (HSM) appliance deficits (+525%)**, computes **network MTU packet fragmentation (1500B)**, and provides an executive CISO roadmap with dynamic visual analytics.

---

## ⚡ Prerequisites

* **Operating System:** Windows 10/11, Linux (Ubuntu/RHEL/Debian), or macOS.
* **Python:** Python 3.10, 3.11, or 3.12 installed.
* **Network:** Zero internet connectivity required at runtime (100% air-gapped / on-premise).

---

## 🚀 Steps to Execute

### 1. Clone & Navigate to Repository
```bash
git clone https://github.com/dashy0070/Quantum_Attack_Risk_Profiler_And_Migration_Planner-QARP-.git
cd Quantum_Attack_Risk_Profiler_And_Migration_Planner-QARP-
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```
*(Dependencies: `streamlit`, `pandas`, `numpy`, `plotly`, `openpyxl`, `python-docx`)*

### 3. Launch Interactive Streamlit Cockpit
```bash
streamlit run app.py
```
*(Windows users can also double-click `run_demo.bat` or run `.\run_demo.ps1`)*

* The application automatically opens in your browser at: **`http://localhost:8501`**
* **Available Modules (7 Navigational Views):**
  1. **Ingestion & Telemetry Parser:** Ingest JSON/CSV gateway logs, synthetic 10k streams, or raw binary PCAP packet captures with ClientHello dissection.
  2. **Quantum Risk Profiler:** Gidney-Ekerå 2021 physical qubit models and Grover symmetric key halving calculations.
  3. **CBOM Compliance Matrix:** CycloneDX 1.6 Cryptographic Bill of Materials catalog with real-time search and export.
  4. **Hardware Capacity Engine:** Physical Payment HSM appliance scaling deficits and network MTU fragmentation curves.
  5. **Real-World Attack Vectors & Exploits:** Mathematical and side-channel exploit simulator across 8 cryptographic algorithms.
  6. **Strategic Migration Roadmap:** Mosca's Theorem risk calculator, Hybrid TLS 1.3 dual-key architecture, and phased CISO action plan.
  7. **Executive CISO Report & Analytics:** Board-ready KPIs, merged CBOM ledger, and dynamic one-click centered pie charts.

---

### 4. CLI Backend Sizing & Cost Engine
To run automated batch log analysis directly in your terminal:
```bash
python pqc_log_parser_and_cost_engine.py
```

### 5. Hardware & Cryptographic Validation Scripts
```bash
# Empirical CPU benchmarks for ML-KEM-768 and ML-DSA-65
python test_liboqs_benchmarks.py

# Payment HSM cryptographic firmware validation test
python test_hsm_pqc_support.py

# STRIDE post-quantum threat model generator
python "Threat Model.py"

# PCAP binary dissector standalone test
python test_pcap_parser.py
```

---

## 📁 Repository Structure

```text
├── app.py                             # 🌟 Interactive Streamlit Cockpit (7 Views)
├── pqc_log_parser_and_cost_engine.py  # ⚙️ Standalone Mathematical Sizing & Cost Engine
├── sample_banking_logs.json           # 📄 Ingress Telemetry (JSON Format - 6 Core Endpoints)
├── sample_banking_logs.csv            # 📊 Ingress Telemetry (CSV Format)
├── sample_banking_traffic.pcap        # 📦 Binary Wireshark Packet Capture (TLS ClientHello)
├── synthetic_traffic_10k.json         # ⚡ High-Throughput Synthetic Banking Stream (10k tx)
├── cryptographic_algorithms_pqc.xlsx  # 📑 CycloneDX 1.6 CBOM Excel Catalog
├── test_liboqs_benchmarks.py          # 🔬 Empirical Hardware Benchmark Tool
├── test_hsm_pqc_support.py            # 🛡️ Payment HSM Cryptographic Support Validator
├── Threat Model.py                    # 🎯 STRIDE Quantum Threat Modeling Generator
├── test_pcap_parser.py                # 🔬 PCAP Binary Dissector Validation Tool
├── generate_sample_pcap.py            # ⚙️ PCAP Synthesis Utility
├── run_demo.bat                       # 🚀 Windows One-Click Batch Launcher
├── run_demo.ps1                       # 🚀 PowerShell Interactive Launcher
├── WHATS_NEW.md                       # 📖 Feature Matrix, Competitor Benchmarks & Enterprise Deployment Guide
├── TEST_CASES_AND_VALIDATION_GUIDE.md # 🧪 Test Cases & Validation Walkthrough
├── requirements.txt                   # 📦 Python Package Dependencies
└── README.md                          # 📖 Direct Execution Guide
```

---

## 📜 Standards & Compliance Alignment

* **NIST PQC Standards:** FIPS 203 (`ML-KEM`), FIPS 204 (`ML-DSA`), FIPS 205 (`SLH-DSA`).
* **National Security:** NSA Commercial National Security Algorithm Suite 2.0 (CNSA 2.0).
* **Payment & Banking:** PCI-DSS v4.0 Requirement 3 & 4, SWIFT ISO 20022 (`pacs.008`, `pacs.002`).
* **Software Supply Chain:** OWASP CycloneDX v1.6 Cryptographic Bill of Materials (CBOM).
