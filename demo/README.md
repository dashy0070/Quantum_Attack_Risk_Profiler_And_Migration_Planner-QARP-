# 🏦 Quantum Attack Risk Profiler & Migration Planner (QARP) — Demo Package

> **Master's Capstone Project (REVA University — SRN: R24MTCYS013)**  
> **Platform-Agnostic Enterprise Banking Sizing, Telemetry Profiling & Cryptographic Modernization Framework**  
> *100% Local Execution • Zero External Cloud Dependency • NIST FIPS 203/204/205 & NSA CNSA 2.0 Compliant*

---

## 📌 Executive Summary

The **Quantum Attack Risk Profiler and Migration Planner (QARP)** is an enterprise-grade security engineering framework designed for Tier-1 Core Banking and Payment infrastructures. It bridges the gap between quantum cryptanalysis theory (Shor's and Grover's algorithms) and practical IT infrastructure modernization by:

1. **Ingesting live and synthetic banking access telemetry** (ISO 20022 `pacs.008`, `pacs.002`, SWIFT MT103, REST / OAuth2 FAPI, POS Switches).
2. **Generating automated Cryptographic Bills of Materials (CBOM)** mapped to physical and logical qubit compromise thresholds.
3. **Evaluating post-quantum Ethernet MTU packet fragmentation** (1,500-byte boundary splits) and Payment HSM appliance capacity bottlenecks.
4. **Providing an Executive CISO Cockpit** with unified CBOM-to-Endpoint risk mapping and dynamic, zero-friction visual pie/donut charts.

---

## 📁 Demo Package Directory Structure

This `demo/` package is strictly curated for live presentations and examiner evaluations, containing only demonstration-critical assets:

```text
demo/
├── app.py                             # 🌟 Interactive Streamlit Cockpit (6 Navigational Views)
├── pqc_log_parser_and_cost_engine.py  # ⚙️ Standalone Python Sizing & Cost Analysis Engine
├── sample_banking_logs.json           # 📄 Sample Ingress Telemetry (JSON format - 6 endpoints)
├── sample_banking_logs.csv            # 📊 Sample Ingress Telemetry (CSV format)
├── synthetic_traffic_10k.json         # ⚡ High-Throughput Synthetic Banking Stream (10k tx)
├── cryptographic_algorithms_pqc.xlsx  # 📑 Comprehensive CycloneDX 1.6 CBOM Excel Catalog
├── qarp_cryptographic_bill_of_materials.csv # 📋 Exported Cryptographic Bill of Materials
├── qarp_quantum_risk_profiling_report.csv   # 📥 Sample Quantum Risk Assessment Output
├── test_liboqs_benchmarks.py          # 🔬 Empirical Hardware Benchmark Tool (ML-KEM & ML-DSA)
├── test_hsm_pqc_support.py            # 🛡️ Payment HSM Cryptographic Support Validator
├── Threat Model.py                    # 🎯 STRIDE Quantum Threat Modeling Generator
├── requirements.txt                   # 📦 Python Package Dependencies
├── run_demo.bat                       # 🚀 Windows One-Click Double-Click Launcher
├── run_demo.ps1                       # 🚀 PowerShell Interactive Launcher
└── README.md                          # 📖 Step-by-Step Execution Guide (This file)
```

---

## ⚡ Prerequisites & Environment Setup

### 1. System Requirements
- **Python**: Python 3.10 or higher installed.
- **Operating System**: Windows 10/11, macOS, or Linux.
- **RAM**: Minimum 4 GB RAM.
- **Browser**: Chrome, Edge, Firefox, or Safari.

### 2. Install Dependencies
Open your terminal (PowerShell, Command Prompt, or Bash) in the `demo/` directory and install the required dependencies:

```powershell
cd demo
pip install -r requirements.txt
```

*(Dependencies: `streamlit`, `pandas`, `numpy`, `plotly`, `matplotlib`, `openpyxl`, `python-docx`)*

---

## 🚀 Step-by-Step Execution Guide

### Option A: One-Click Launch (Windows)
Double-click `run_demo.bat` or run:
```powershell
.\run_demo.ps1
```

### Option B: Manual Command-Line Launch
Run the Streamlit application using Python:
```powershell
python -m streamlit run app.py
```
The browser will automatically open at: **`http://localhost:8501`**

---

## 🧭 Live Demo Walkthrough (7 Interactive Views)

Use the left sidebar navigation radio buttons to explore all 7 modules:

### 📡 View 1: Ingestion & Telemetry Parser (JSON, CSV & Binary PCAP / Live Feed)
- **What it does**: Ingests enterprise API gateway logs (NGINX, Envoy, HAProxy, Kong), raw network packet captures (`.pcap`, `.pcapng`, `.cap`), and promiscuous live network feeds.
- **How to demo**:
  1. **PCAP Packet Capture**: Click **"📦 Load sample_banking_traffic.pcap"** or upload your own `.pcap` capture file. The built-in pure-Python binary packet parser decodes Ethernet/IP/TCP headers, dissects TLS 1.2/1.3 ClientHello records, extracts negotiated cipher suites (e.g. `0xC02F` ECDHE-RSA-AES128-GCM-SHA256), parses SNI hostnames, and reconstructs HTTP/REST API endpoints.
  2. **Live Promiscuous Sniffer**: Select **"🔴 Live Network Packet Sniffer (Promiscuous PCAP Feed)"**, choose your network interface (or Loopback), set the packet count (e.g. 10–50 packets), and click **"▶️ Start Live Packet Capture"**.
  3. **Structured Ingress**: Click **"Load sample_banking_logs.json"** or **"Load sample_banking_logs.csv"** to instantly ingest 6 core banking endpoints (Credit Transfer, RTGS Instant Clearing, FAPI Consent, SWIFT MT103, Token Exchange, POS Switch).
  4. **High-Throughput Simulation**: Click **"Load synthetic_traffic_10k.json"** or switch to **"⚡ Synthetic Live Core Banking Stream"** and drag the settlement slider to simulate up to **15,000 TPS**.
  5. **Real-Time Engineering Metrics**: View the breakdown of **Physical Shor Qubits**, **Compromise Runway**, **MTU Packet Splits (1500B)**, and **Monthly Bandwidth Delta**.
  6. Click **"Export Parsed Quantum Risk Assessment (CSV)"** to demonstrate reporting compliance.

---

### ⚛️ View 2: Quantum Risk Profiler (Shor & Grover)
- **What it does**: Evaluates algorithmic vulnerability against Shor's and Grover's cryptanalysis under physical error-corrected quantum computing models.
- **How to demo**:
  1. Review the **Gidney-Ekerå (2021)** resource estimation table for RSA (1024, 2048, 3072, 4096).
  2. Explain why **RSA-2048 requires 4,098 logical qubits** (~20 million physical qubits) while **ECDSA P-256 requires only 1,536 logical qubits**, breaking earlier.
  3. Review the **Grover's Algorithm** symmetric key halving table explaining why **AES-128 is broken (effective 64-bit)** while **AES-256 remains quantum-resistant (effective 128-bit)**.

---

### 📋 View 3: CBOM Compliance Matrix
- **What it does**: Displays the CycloneDX 1.6 compliant Cryptographic Bill of Materials mapped against NIST FIPS 203/204/205 & NSA CNSA 2.0.
- **How to demo**:
  1. Choose **"📁 Project Excel Catalog (cryptographic_algorithms_pqc.xlsx)"**.
  2. Use the **Search bar** to type `RSA`, `AES`, `HSM`, or `Broken` to filter the entire enterprise asset catalog in real-time.
  3. Highlight the KPI badges: **Total Cryptographic Assets**, **PQC Quantum Safe count**, **Quantum Vulnerable count**, and **Hardware Roots (HSM/TPM)**.
  4. Export the filtered inventory using **"Export Filtered CBOM (CSV)"**.

---

### 🏢 View 4: Enterprise Hardware Capacity Engine
- **What it does**: Models physical Payment HSM appliance scaling deficits, CPU loads, and datacenter bandwidth costs.
- **How to demo**:
  1. Adjust the **Target Peak Settlement TPS** (e.g., set to `5,000` or `10,000 TPS`).
  2. Show the comparison table revealing the **~85% throughput penalty** of post-quantum lattice signing (ML-DSA-65) compared to legacy RSA-2048.
  3. Point out the dynamic Plotly grouped bar chart showing the required physical HSM appliance count exploding under PQC workloads.

---

### 💥 View 5: Real-World Quantum & PQC Attack Vectors & Threat Exploits [NEW]
- **What it does**: In-depth threat exploit simulator across all susceptible classical and post-quantum cryptographic primitives. Covers exact mathematical attack mechanics, hardware/side-channel exploits, practical exploit scenarios, direct banking business outcomes, and concrete engineering countermeasures.
- **How to demo**:
  1. **Tab 1: 🎯 Interactive Exploit & Outcome Simulator**:
     - Select from 8 cryptographic algorithms (`RSA-2048`, `ECDSA-P256 / Ed25519`, `AES-128`, `ML-KEM-768`, `ML-DSA-65`, `SLH-DSA-128s`, `Falcon-512`, `SHA-256`).
     - Inspect dynamic metrics: *Primary Attack Vector*, *Attacker Complexity*, *Time to Compromise*, and *Exploit Feasibility*.
     - Walk through the **Step-by-Step Exploit Scenario Walkthrough**, direct **Catastrophic Business Outcomes**, and actionable **Prescribed Engineering Countermeasures**.
  2. **Tab 2: ⚛️ Classical Vulnerabilities (Shor & Grover)**:
     - Review detailed cards for RSA Modular Order Finding, Elliptic Curve Discrete Logarithm (ECDLP), AES-128 Quadratic Search Space Halving, and SHA-256 Quantum Collision Search (BHT Algorithm).
  3. **Tab 3: 🔬 Post-Quantum Attack Vectors (SCA, FIA & Lattice)**:
     - Review physical and implementation vulnerabilities in PQC algorithms:
       - *Differential Power Analysis (DPA/CPA) on NTT Multiplications* (recovering ML-KEM / ML-DSA secret keys from EM leakage).
       - *Laser & Voltage Fault Injection (FIA) on Signing Nonce ($y$)* (single-fault total key recovery).
       - *Decryption Failure Rate (DFR) Exploitation & CCA2 Chosen-Ciphertext Leakage* in LWE schemes.
       - *Floating-Point FFT Cache Timing & Precision Leakage* (Falcon Gaussian sampler side channels).
  4. **Tab 4: 📊 Master Attack Taxonomy & Exploit Matrix**:
     - Explore the full interactive comparative dataframe indexing all algorithms, attack vectors, outcomes, complexity, and migration urgency.

---

### 🗺️ View 6: Strategic Migration Roadmap & CISO Mitigation Playbook
- **What it does**: Comprehensive CISO-level modernization cockpit featuring 5 interactive sub-tabs with color-coded executive strategies, attack timelines, vibrant blue Hybrid TLS 1.3 architecture, and deep analysis of open cryptanalytic questions.
- **How to demo**:
  1. **Tab 1: ⏳ Attack Horizons & Mosca's Theorem**:
     - Review the comparative breakdown of attack timelines: Classical Asymmetric (2029–2034 Shor break window, HNDL active today) vs. Legacy Symmetric (2032–2036 Grover break window) vs. Hybrid Protocols (2025–2040+ failsafe window) vs. PQC Compliant (2050+ quantum safe).
     - Interactive **Mosca's Theorem Risk Calculator**: Adjust sliders for $X$ (Data Shelf-Life), $Y$ (Migration Time), and $Z$ (Years to CRQC) to compute immediate security exposure deficits in real-time.
     - View the interactive Gantt chart illustrating cryptographic viability lifespans from 2025 to 2050+.
  2. **Tab 2: 🛡️ Hybrid TLS 1.3 & Dual Signatures (Enriched Corporate Blue Styling)**:
     - Inspect the mathematical dual key derivation formula: $\text{Shared\_Secret} = \text{HKDF-Extract}(\text{salt}, SS_{\text{ECDH}} \parallel SS_{\text{ML-KEM}})$.
     - Explain why hybrid key exchange provides a mathematical failsafe (adversary must break both ECDLP and M-LWE to decrypt).
     - Review the dual/composite digital signature architecture (Draft-IETF-LAMPS) for zero-downtime B2B banking migration.
  3. **Tab 3: 🔬 Open Questions: Can ML-KEM and ML-DSA Be Attacked?**:
     - Deep-dive into the 4 key cryptanalytic attack surfaces: Lattice Basis Reduction (BKZ 2.0 / SVP), Algebraic Module Weaknesses, Side-Channel / Fault Injection, and Decryption Failure Rate (DFR).
  4. **Tab 4: 📋 Phased CISO Action Plan (2025–2034)**:
     - Explore the 4 color-coded gradient phase cards (Phase 1: Discovery & CBOM, Phase 2: Hybrid Ingress, Phase 3: PKI & Payment Switches, Phase 4: Full PQC Modernization).
     - Check items in the **Interactive CISO Modernization Readiness Checklist** to track progress with a live compliance meter.
  5. **Tab 5: 🔄 Cryptographic Agility Playbook**:
     - Review the 5 Golden Rules of Enterprise Cryptographic Agility and the Standard vs. PQC Specification Reference Matrix.

---

### 👔 View 7: Executive CISO Report & Visual Analytics
- **What it does**: Provides a board-ready CISO risk cockpit merging the Cryptographic Bill of Materials (CBOM) with connected banking endpoints, alongside zero-friction dynamic pie/donut charts.
- **How to demo**:
  1. **Executive KPI Cards**: Immediately observe the executive summary metrics:
     - *Ingested Endpoints & Peak TPS*
     - *Shor Vulnerability Exposure Rate (%)*
     - *Grover Vulnerability Rate (%)*
     - *Estimated Q-Day Runway*
     - *Monthly Infrastructure Deficit ($/mo)*
  2. **Zero-Friction Dynamic Visual Statistics**:
     - By default, all 6 executive charts are rendered simultaneously in a clean 2-column grid:
       - 🥧 **Post-Quantum Vulnerability Distribution** (Critical vs High vs Medium vs Safe)
       - 🥧 **Cryptographic Primitive Distribution** (RSA vs ECC vs AES-128 vs AES-256 vs PQC)
       - 🥧 **Connected Banking Protocols Share** (ISO 20022, RTGS, REST FAPI, SWIFT MT103, POS Switch)
       - 🥧 **Network MTU Packet Fragmentation Risk** (Single Packet Safe vs Multi-Packet Fragmented)
       - 🥧 **Strategic Migration Horizon Prioritization** (Phase 1 Immediate, Phase 2, Phase 3, Phase 4)
       - 🥧 **Infrastructure Cost Allocation Split** (Payment HSM Hardware vs Datacenter Bandwidth)
     - Toggle between **"All Executive Charts (Grid View)"** and **"Single Focused Chart"**.
     - Toggle the **"🍩 Donut Chart Style"** checkbox to change chart appearance dynamically.
  3. **Merged CBOM & Connected Endpoints Ledger Table**:
     - Show the unified ledger combining Endpoint URI + Banking Context + Active Primitive + Matched CBOM Standard + Hardware Context + Shor/Grover Risk + Target NIST PQC Standard + HSM Unit Expansion + Monthly Cost Delta.
  4. **Single-Click Export**:
     - Click **"📥 Export Unified CISO Merged CBOM & Endpoint Report (CSV)"** to save the executive audit file.
  5. **Executive Action Summary**:
     - Expand the CISO Briefing section summarizing key findings and actionable board recommendations.

---

## 🧪 CLI Verification & Backend Benchmark Tools

In addition to the interactive web application, you can execute the backend sizing engines and empirical benchmark scripts directly from the terminal:

### 1. Run the Backend Sizing & Cost Analysis Engine
```powershell
python pqc_log_parser_and_cost_engine.py
```
*Outputs structured JSON analysis with packet fragmentation factors, projected latency, and hardware appliance scaling deltas.*

### 2. Run Empirical Hardware Benchmarks (ML-KEM & ML-DSA)
```powershell
python test_liboqs_benchmarks.py
```
*Measures local host CPU cycle timings for key generation, encapsulation, decapsulation, and digital signing.*

### 3. Run Payment HSM PQC Validation Test
```powershell
python test_hsm_pqc_support.py
```
*Validates HSM cryptographic firmware compatibility and throughput constraints under PQC algorithm suites.*

### 4. Generate STRIDE Quantum Threat Model
```powershell
python "Threat Model.py"
```
*Builds the STRIDE post-quantum risk matrix across banking trust boundaries.*

---

## 🎓 Academic Attribution

- **Project**: Quantum Attack Risk Profiler and Migration Planner (QARP)
- **Author**: Anirban Dasgupta (SRN: `R24MTCYS013`)
- **Degree**: Master of Technology (M.Tech) in Cybersecurity
- **Institution**: School of Computer Science and Engineering, REVA University, Bengaluru
- **Standard Alignment**: NIST FIPS 203 (`ML-KEM`), FIPS 204 (`ML-DSA`), FIPS 205 (`SLH-DSA`), NSA CNSA 2.0, PCI-DSS 4.0, CycloneDX 1.6 CBOM.
