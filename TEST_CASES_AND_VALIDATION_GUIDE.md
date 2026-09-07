# QARP (Quantum Attack Risk Profiler): Comprehensive Test Plan & Use Case Validation Guide

This document outlines the complete test plan, step-by-step test cases, expected inputs/outputs, and validation procedures for all modules of the **Quantum Attack Risk Profiler and Migration Planner (QARP)** system.

---

## 📋 Test Matrix & Use Case Overview

| Use Case ID | Test Category | Target Component | Description |
| :--- | :--- | :--- | :--- |
| **UC-01** | Telemetry Ingestion & Stream Parsing | `app.py` / `pqc_log_parser...` | Test live synthetic streaming (1,000–15,000 TPS) & custom file ingestion (JSON, CSV, XLSX). |
| **UC-02** | Quantum Risk & Qubit Estimation | `app.py` (Tab 2) | Validate Shor's (Gidney-Ekerå 2021) and Grover's algorithm resource estimation. |
| **UC-03** | CBOM Discovery & Agility Audit | `app.py` (Tab 3) / `xlsx` | Audit CycloneDX 1.6 CBOM, hardware roots of trust (TPM/HSM/KMIP), and compliance metrics. |
| **UC-04** | Enterprise Payment HSM Sizing | `app.py` (Tab 4) / `pqc_log_parser...` | Verify the **+525% physical HSM appliance cluster deficit** and monthly amortized cost deltas. |
| **UC-05** | MTU Fragmentation & Latency SLA | `app.py` / `pqc_log_parser...` | Validate 1500-byte Ethernet buffer splitting ($1 \rightarrow 3\text{ pkts}$) and 50 ms SLA breach detection. |
| **UC-06** | Phased Migration Planning | `app.py` (Tab 5) | Validate 4-phase transition roadmap (2025–2033) aligned with NIST and CNSA 2.0. |
| **UC-07** | Automated Report & Diagram Suite | Python CLI scripts | Verify execution of report generator, algorithm image builder, and threat modelers. |

---

## 🧪 Detailed Step-by-Step Test Cases

### 🔹 UC-01: Ingress Log Telemetry Ingestion & Stream Parsing

#### Test Case 1.1: Live Synthetic Telemetry Stream
* **Objective:** Verify real-time synthetic log generation and parameter reactivity.
* **Pre-conditions:** `streamlit run app.py` is running.
* **Test Steps:**
  1. Navigate to **"1. Ingestion & Telemetry Parser"**.
  2. Select **"⚡ Synthetic Live Core Banking Stream"**.
  3. Move the **Global Peak Settlement Volume** slider from `1,000` to `10,000 TPS`.
* **Expected Output:**
  * Endpoints (`/v1/settlement/credit-transfer`, `/v1/clearing/rtgs-instant`, `/v1/fapi/...`, `/v1/ledger/...`) update dynamically.
  * Total Ingested TPS metric updates to `10,000 tx/s`.
  * Bandwidth Delta scales proportionally to TPS volume.
* **Status:** `PASS`

#### Test Case 1.2: Custom JSON Log Ingestion
* **Objective:** Ingest and parse structured JSON access logs.
* **Test Steps:**
  1. Select **"📂 Upload Custom File or Load Project Files"**.
  2. Click **"📄 Load sample_banking_logs.json"** (or upload `sample_banking_logs.json`).
* **Expected Output:**
  * Success message: `✅ Successfully parsed sample_banking_logs.json (6 records loaded)`.
  * Parsed table renders 6 banking routes with active cipher detection.
  * Shor-Vulnerable metric displays `6 of 6 (100%)`.
* **Status:** `PASS`

#### Test Case 1.3: Custom CSV Log Ingestion
* **Objective:** Ingest comma-separated access logs with automated column normalization.
* **Test Steps:**
  1. Click **"📊 Load sample_banking_logs.csv"** (or upload `sample_banking_logs.csv`).
* **Expected Output:**
  * Success message: `✅ Successfully parsed sample_banking_logs.csv (6 records loaded)`.
  * Automatically maps columns (`endpoint`, `tls_cipher`, `protocol`, `tps`, `latency_ms`).
* **Status:** `PASS`

#### Test Case 1.4: Excel Inventory File Ingestion
* **Objective:** Ingest raw cryptographic algorithm catalogs (`.xlsx`).
* **Test Steps:**
  1. Click **"📑 Load cryptographic_algorithms_pqc.xlsx"**.
* **Expected Output:**
  * Automatically converts algorithm catalog entries into simulated enterprise service routes.
  * Profiles each algorithm against Shor's physical qubit complexity.
* **Status:** `PASS`

#### Test Case 1.5: Dynamic Report Export
* **Objective:** Export assessed risk telemetry to CSV.
* **Test Steps:**
  1. Click **"📥 Export Parsed Quantum Risk Assessment (CSV)"**.
* **Expected Output:**
  * Browser downloads `qarp_quantum_risk_profiling_report.csv` containing complete sizing telemetry.
* **Status:** `PASS`

---

### 🔹 UC-02: Quantum Vulnerability & Qubit Resource Estimation

#### Test Case 2.1: Shor's Algorithm Factoring Complexity (RSA vs. ECC)
* **Objective:** Validate mathematical calculation of logical and physical qubits under Gidney-Ekerå (2021) optimization.
* **Test Steps:**
  1. Navigate to **"2. Quantum Risk Profiler (Shor & Grover)"**.
  2. In the sidebar, verify **Cryptanalysis Model** is set to `Gidney-Ekerå (2021 Optimization)`.
  3. Inspect the Shor's Factoring table.
* **Expected Output:**
  * **RSA-2048:** $Q_{\text{logical}} = 2(2048) + 2 = \mathbf{4,098\text{ qubits}}$, $Q_{\text{physical}} \approx \mathbf{20,000,000\text{ qubits}}$, Runway: $\sim 9.9\text{ Years}$.
  * **RSA-4096:** $Q_{\text{logical}} = 2(4096) + 2 = \mathbf{8,194\text{ qubits}}$, $Q_{\text{physical}} \approx \mathbf{40,000,000\text{ qubits}}$, Runway: $\sim 4.8\text{ Years}$.
  * **ECDSA-P256:** $Q_{\text{logical}} = 6(256) = \mathbf{1,536\text{ qubits}}$, $Q_{\text{physical}} \approx \mathbf{5,376,000\text{ qubits}}$, Runway: $\sim 2.5\text{ Years}$.
* **Status:** `PASS`

#### Test Case 2.2: Grover's Quadratic Speedup on Symmetric Ciphers
* **Objective:** Verify security degradation for symmetric ciphers and hash functions.
* **Test Steps:**
  1. Inspect the Grover's Algorithm table in Tab 2.
* **Expected Output:**
  * **AES-128-GCM:** Degraded from 128-bit to **64-bit security** $\rightarrow$ Verdict: `❌ NON-COMPLIANT`.
  * **AES-256-GCM:** Degraded from 256-bit to **128-bit security** $\rightarrow$ Verdict: `✅ QUANTUM RESISTANT`.
  * **SHA-256:** Collision resistance reduced to **85.3 bits** $\rightarrow$ Verdict: `⚠️ MIGRATE TO SHA-384`.
  * **SHA-384:** Collision resistance reduced to **128 bits** $\rightarrow$ Verdict: `✅ QUANTUM RESISTANT`.
* **Status:** `PASS`

---

### 🔹 UC-03: Cryptographic Bill of Materials (CBOM) & Compliance Scanning

#### Test Case 3.1: CycloneDX 1.6 Project Excel Audit
* **Objective:** Validate multi-sheet inspection of `cryptographic_algorithms_pqc.xlsx`.
* **Test Steps:**
  1. Navigate to **"3. CBOM Compliance Matrix"**.
  2. Ensure **"📁 Project Excel Catalog"** is selected.
  3. Switch between sheets: `crypto_algos_with userc` $\leftrightarrow$ `cryptographic_algorithms_pqc_c`.
* **Expected Output:**
  * Table updates with all 50+ algorithm entries.
  * KPI Cards display: Total Assets (50+), PQC Quantum Safe %, Quantum Vulnerable %, and Hardware Roots (HSM/TPM).
* **Status:** `PASS`

#### Test Case 3.2: Live Search & Keyword Filtering
* **Objective:** Filter cryptographic assets by keyword.
* **Test Steps:**
  1. In the search box, enter `HSM`.
  2. Clear and enter `ML-KEM`.
* **Expected Output:**
  * Searching `HSM` returns only entries mapped to Hardware Security Modules (ZMK exchange, LMK master keys, PIN encryption).
  * Searching `ML-KEM` isolates FIPS 203 key encapsulation primitives.
* **Status:** `PASS`

---

### 🔹 UC-04: Enterprise Payment HSM Sizing & Hardware Capacity Planning

#### Test Case 4.1: Linear IT Sizing vs. PQC Reality (+525% Deficit)
* **Objective:** Demonstrate the appliance scaling deficit caused by lattice digital signature computation drops.
* **Test Steps:**
  1. Navigate to **"4. Enterprise Hardware Capacity Engine"**.
  2. Set **Target Peak Settlement TPS** to `5,000 TPS`.
  3. Verify the **Comparison Table** and **Bar Chart**.
* **Expected Output:**
  * **At 1,000 TPS:** Legacy: 2 HSMs (\$2,400/mo) vs. PQC: 6 HSMs (\$7,200/mo) $\rightarrow$ **+200.0% Deficit**.
  * **At 5,000 TPS:** Legacy: 5 HSMs (\$6,000/mo) vs. PQC: 28 HSMs (\$33,600/mo) $\rightarrow$ **+460.0% Deficit**.
  * **At 10,000 TPS:** Legacy: 9 HSMs (\$10,800/mo) vs. PQC: 56 HSMs (\$67,200/mo) $\rightarrow$ **+522.2% Deficit** (Unbudgeted variance: +\$56,400/mo).
  * Plotly bar chart visually displays the blue (Legacy) vs. red (PQC) appliance surge.
* **Status:** `PASS`

---

### 🔹 UC-05: Network MTU Packet Fragmentation & Latency SLA

#### Test Case 5.1: 1500-Byte Ethernet Buffer Splitting
* **Objective:** Validate calculation of packet segmentation factors ($\Phi$).
* **Calculation:**
  $$\Phi_{\text{Legacy}} = \left\lceil \frac{256 + 256}{1500} \right\rceil = 1 \text{ packet} \quad \text{vs.} \quad \Phi_{\text{PQC}} = \left\lceil \frac{1184 + 3300}{1500} \right\rceil = \mathbf{3\text{ packets}}$$
* **Expected Output in Profiler:**
  * `MTU Packets (1500B)` column explicitly reports `1 pkt -> 3 pkts`.
  * `Handshake Size Delta` reports `512B -> 4484B (+776%)`.
* **Status:** `PASS`

#### Test Case 5.2: Bank SLA Breach Detection
* **Objective:** Flag routes exceeding the 50 ms banking latency threshold.
* **Test Steps:**
  1. In Tab 1, observe `/v1/ledger/batch-reconciliation` (Base Latency: `46.0 ms`).
* **Expected Output:**
  * Projected PQC Latency: $46.0\text{ ms} + 4.4\text{ ms} = \mathbf{50.4\text{ ms}}$.
  * Triggers SLA breach warning ($>50\text{ ms}$).
* **Status:** `PASS`

---

### 🔹 UC-06: Strategic Post-Quantum Migration Roadmap

#### Test Case 6.1: Phased Transition Verification (2025–2033)
* **Objective:** Validate the 4-phase enterprise roadmap structure.
* **Test Steps:**
  1. Navigate to **"5. Strategic Migration Roadmap"**.
  2. Expand each phase accordion.
* **Expected Output:**
  * **Phase 1 (2025–2026):** Discovery, automated CBOM, AES-256 enforcement.
  * **Phase 2 (2026–2028):** Hybrid TLS 1.3 (X25519 + ML-KEM-768) on ingress gateways.
  * **Phase 3 (2028–2030):** Enterprise PKI & ISO 20022 dual-signature migration (ML-DSA-65).
  * **Phase 4 (2030–2033):** Core banking mainframe & Payment HSM full classical decommissioning.
* **Status:** `PASS`

---

### 🔹 UC-07: Automated Report Generation & Diagram Suite

#### Test Case 7.1: Standalone CLI Sizing Engine
* **Execution Command:** `python pqc_log_parser_and_cost_engine.py`
* **Expected Output:**
  * Outputs pure JSON telemetry profiling for credit transfers, RTGS, and batch reconciliation.
  * Exits with code `0`.
* **Status:** `PASS`

#### Test Case 7.2: High-Resolution Algorithm Image Generator
* **Execution Command:** `python generate_all_algorithm_images.py`
* **Expected Output:**
  * Generates all 4 algorithm images at 300 DPI:
    * `algorithm_1_pseudocode.png` & `.svg`
    * `algorithm_2_pseudocode.png` & `.svg`
    * `algorithm_3_pseudocode.png` & `.svg`
    * `algorithm_4_pseudocode.png` & `.svg`
  * Exits with code `0`.
* **Status:** `PASS`

#### Test Case 7.3: Complete Capstone Word Dissertation Compilation
* **Execution Command:** `python generate_capstone_report.py`
* **Expected Output:**
  * Compiles `2_CS_13_Capstone Project_..._v9_updated.docx` with:
    * All 12 Chapters with clean REVA University typography.
    * Embedded `Table 11.1: Cryptographic Algorithm PQC Compliance and Mitigation if not compliant`.
    * All 8 embedded figures and 18 IEEE references.
  * Exits with code `0`.
* **Status:** `PASS`

---

## 🏁 Summary of Test Results

| Total Test Cases | Passed | Failed | Blocked | Pass Rate |
| :---: | :---: | :---: | :---: | :---: |
| **15** | **15** | **0** | **0** | **100%** |
