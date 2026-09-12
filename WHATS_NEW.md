# 🚀 What's New in QARP (Quantum Attack Risk Profiler)

> **Comprehensive Release Notes, Product Capabilities, Competitive Edge Analysis & Enterprise Deployment Guide**

---

## 📑 Table of Contents
1. [🌟 Complete Feature Matrix](#-complete-feature-matrix)
2. [⚔️ Competitive Advantage & Benchmark Comparison](#️-competitive-advantage--benchmark-comparison)
3. [🏗️ Enterprise Deployment Architectures](#️-enterprise-deployment-architectures)
4. [🔒 Security, Compliance & Air-Gap Assurance](#-security-compliance--air-gap-assurance)

---

## 🌟 Complete Feature Matrix

QARP provides an end-to-end cryptographic modernization cockpit tailored for Tier-1 core banking networks, interbank settlement switches, and financial payment gateways.

### 1. Ingress Telemetry & Zero-Dependency Binary PCAP Parser
* **Multi-Format Ingestion:** Ingests live and recorded JSON/CSV API gateway logs (NGINX, Envoy, HAProxy, Kong, F5 BIG-IP).
* **Pure-Python Binary PCAP Dissector:** Extracts and decodes raw `.pcap`, `.pcapng`, and `.cap` network traces without external dependencies like Wireshark/libpcap.
* **TLS 1.2/1.3 ClientHello Parser:** Dissects TLS record structures, extracts negotiated cipher suites (e.g., `0xC02F` ECDHE-RSA-AES128-GCM-SHA256, `0x1301` TLS_AES_128_GCM_SHA256), Server Name Indication (SNI) hostnames, and reconstructs REST/HTTP banking endpoints.
* **Promiscuous Live Network Sniffer:** Captures real-time packets from local/loopback interfaces for instant live vulnerability profiling.
* **Synthetic High-Throughput Stream:** Built-in 10,000-transaction generator with a real-time settlement load slider (1,000 to 15,000 TPS).

### 2. Physical & Logical Quantum Risk Profiler
* **Gidney-Ekerå (2021) Resource Estimations:** Accurate surface-code modeling of physical and logical qubit compromise thresholds for RSA (1024, 2048, 3072, 4096).
* **ECC Discrete Log Vulnerability:** Demonstrates why ECDSA P-256 / Ed25519 breaks at only **1,536 logical qubits** (~2,330 physical qubits), falling well before RSA.
* **Grover's Key Search Space Halving:** Quantifies symmetric security degradation under amplitude amplification, explaining why AES-128 is broken (effective 64-bit) while AES-256 remains permanently quantum-safe (effective 128-bit).

### 3. CycloneDX 1.6 Cryptographic Bill of Materials (CBOM)
* **Automated Asset Catalog:** Full compliance with the OWASP CycloneDX 1.6 CBOM standard.
* **Real-Time Search & Filtration:** Instant filtering across cryptographic primitives, key lengths, hardware roots (HSM/TPM), NIST post-quantum compliance, and vulnerability classifications.
* **Single-Click CSV Export:** Generates regulator-ready CBOM compliance reports for audit reviews (PCI-DSS 4.0, NIST, CNSA 2.0).

### 4. Enterprise Hardware Capacity Engine
* **Payment HSM Appliance Bottleneck Modeling:** Models physical HSM throughput degradation (~85% drop for ML-DSA-65 lattice signing) and computes true appliance expansion requirements (+525% cluster expansion).
* **Ethernet MTU 1500B Packet Fragmentation:** Calculates IP packet segmentation factors when transitioning from classical 512-byte handshakes to 4,484-byte PQC public keys/certificates.
* **Financial Infrastructure Cost Engine:** Models monthly datacenter bandwidth overhead and hardware CAPEX/OPEX deltas across varying transaction volumes.

### 5. Real-World Attack Vectors & Threat Exploit Simulator
* **Interactive 8-Algorithm Exploit Simulator:** Simulates attack lifecycles for `RSA-2048`, `ECDSA-P256`, `AES-128`, `ML-KEM-768`, `ML-DSA-65`, `SLH-DSA-128s`, `Falcon-512`, and `SHA-256`.
* **Step-by-Step Attack Walkthroughs:** Maps initial adversary reconnaissance, cryptanalytic execution, direct banking business outcomes (wire fraud, token forgery, ledger collision), and concrete countermeasures.
* **Post-Quantum Side-Channel & Fault Injection (SCA/FIA):** Evaluates Differential Power Analysis (DPA/CPA) on Number Theoretic Transform (NTT) multiplications and laser fault injection on signature nonce sampling.
* **Master Attack Taxonomy Matrix:** Full comparative matrix indexing mathematical complexity, attacker resource thresholds, and migration urgencies.

### 6. Strategic Migration Roadmap & CISO Mitigation Playbook
* **Interactive Mosca's Theorem Calculator:** Dynamic evaluation of $X$ (Data Shelf-Life) + $Y$ (Migration Time) vs. $Z$ (CRQC Arrival) to quantify exposure to *Harvest Now, Decrypt Later (HNDL)* attacks.
* **Cryptographic Viability Lifespan Gantt:** Clear horizontal timeline chart tracking cryptographic lifespans from 2025 to 2055+.
* **Hybrid TLS 1.3 & Dual Signature Architecture:** Detailed mathematical proofs of dual key derivation:
  $$\text{Shared\_Secret} = \text{HKDF-Extract}(\text{salt}, SS_{\text{ECDH}} \parallel SS_{\text{ML-KEM}})$$
* **Phased CISO Modernization Plan:** 4 color-coded milestone phases (2025–2034) with an interactive readiness tracking checklist.

### 7. Executive CISO Report & Visual Analytics
* **Executive Summary KPI Cards:** Instant board-level visibility into Shor/Grover vulnerability percentages, Q-Day runway, and projected monthly cost deltas.
* **Zero-Friction Dynamic Pie Charts:** 6 presentation-ready corporate charts with centered titles (`x=0.5`) and high-contrast color palettes.
* **One-Click Generator Toolbar:** Generate individual high-res focus charts or full 2-column presentation decks with a single click.
* **Unified CBOM-to-Endpoint Ledger:** Merges network endpoints with underlying cryptographic standards, hardware contexts, target NIST PQC algorithms, and appliance expansion deltas.

---

## ⚔️ Competitive Advantage & Benchmark Comparison

QARP addresses the critical architectural and operational gaps found in existing commercial discovery tools, which often focus exclusively on code scanning while ignoring on-premise hardware limits, HSM bottlenecks, and packet fragmentation.

| Feature / Capability | **QARP Framework** | **IBM Quantum Safe Explorer** | **SandboxAQ Security Suite** | **Entrust Crypto Assessment** | **Cisco Panoptica** |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **Execution Model** | **100% Local / Air-Gapped** | Cloud / SaaS Hybrid | Cloud SaaS Gateway | On-Premise Agent | Cloud-Native SaaS |
| **External Cloud Dependency** | **ZERO (Air-Gapped)** | Requires IBM Cloud | Requires Sandbox Cloud | Requires Vendor Portal | Requires AWS/Azure/GCP |
| **Raw Binary PCAP / Live Feeds** | **Yes (Pure Python)** | No (Static logs only) | Yes (eBPF Agent) | No (Config files only) | Network Mirroring |
| **Payment HSM Capacity Modeling** | **Yes (+525% Scaling)** | High-Level Sizing | Algorithmic only | Key Inventory only | No |
| **MTU 1500B Packet Fragmentation** | **Yes (Exact Packet Splits)** | No | No | No | Generic Network SLA |
| **Mosca's Theorem Risk Calculator** | **Yes (Interactive Slider)** | Static Calculation | Static Timeline | No | No |
| **PQC Physical Side-Channel (SCA/FIA)** | **Yes (NTT/Laser Exploits)** | Academic Overview | General Advisory | No | No |
| **Hybrid TLS 1.3 Dual-Key Proofs** | **Yes (HKDF Derivation)** | Architecture Docs | Hybrid Proxy Setup | Certificate Only | TLS Inspection |
| **CycloneDX 1.6 CBOM Export** | **Yes (Automated CSV/Excel)** | Yes (Proprietary format) | Yes | Yes (Proprietary) | Software SBOM only |
| **Procurement & License Cost** | **Open / Zero SaaS Tax** | High Enterprise Fee | High Annual License | High Consulting Retainer | Cloud Subscription |

### Why QARP Wins in Enterprise Banking:
1. **Zero Data Exfiltration Risk:** Core banking telemetry (account PANs, customer PII, SWIFT wire routing) never leaves the bank's secure perimeter.
2. **True Infrastructure Capacity Planning:** Commercial tools declare that an algorithm is vulnerable, but only QARP computes the physical payment HSM appliance scaling deficit and budget impact.
3. **Network Boundary Safety:** QARP predicts TCP packet drops and latency inflation before deploying PQC certificates on edge reverse proxies.

---

## 🏗️ Enterprise Deployment Architectures

QARP is designed for modular deployment across financial networks, from standalone security workstations to distributed container clusters.

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                       ENTERPRISE BANKING INFRASTRUCTURE                     │
│                                                                             │
│   [ API Gateways ]    [ SWIFT / RTGS ]    [ Core Banking ]   [ HSM Cluster] │
│   (NGINX/Envoy Logs)    (ISO 20022 XML)      (PCAP Feeds)    (PKCS#11/KMIP) │
└───────────┬───────────────────┬───────────────────┬─────────────────┬───────┘
            │                   │                   │                 │
            ▼                   ▼                   ▼                 ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│                          QARP MODERNIZATION ENGINE                          │
│                                                                             │
│   ┌───────────────────┐  ┌───────────────────┐  ┌───────────────────────┐   │
│   │ Telemetry Parser  │  │ Quantum Profiler  │  │ Hardware Sizing Model │   │
│   │ (JSON/CSV/PCAP)   │  │ (Shor / Grover)   │  │ (HSM / MTU / Costs)   │   │
│   └─────────┬─────────┘  └─────────┬─────────┘  └───────────┬───────────┘   │
│             │                      │                        │               │
│             └──────────────────────┼────────────────────────┘               │
│                                    ▼                                        │
│   ┌─────────────────────────────────────────────────────────────────────┐   │
│   │              EXECUTIVE CISO COCKPIT & STRATEGIC ROADMAP             │   │
│   │  - Mosca's Horizon   - Hybrid TLS 1.3   - CycloneDX 1.6 CBOM Export │   │
│   └─────────────────────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

### Deployment Model 1: On-Premise Air-Gapped Workstation / Server (Bare-Metal)

For secure audit labs and air-gapped financial networks:

1. **Copy the directory** to the target on-premise Linux (RHEL/Ubuntu) or Windows Server:
   ```bash
   git clone https://github.com/dashy0070/Quantum_Attack_Risk_Profiler_And_Migration_Planner-QARP-.git
   cd Quantum_Attack_Risk_Profiler_And_Migration_Planner-QARP-
   ```
2. **Install local dependencies:**
   ```bash
   pip install -r requirements.txt --no-index --find-links=./wheels
   ```
3. **Run as a systemd service (Linux):**
   ```ini
   # /etc/systemd/system/qarp.service
   [Unit]
   Description=QARP Quantum Attack Risk Profiler
   After=network.target

   [Service]
   Type=simple
   User=qarp-admin
   WorkingDirectory=/opt/qarp
   ExecStart=/usr/bin/python3 -m streamlit run app.py --server.port=8501 --server.address=0.0.0.0 --server.headless=true
   Restart=always

   [Install]
   WantedBy=multi-user.target
   ```
4. **Enable and start service:**
   ```bash
   sudo systemctl daemon-reload
   sudo systemctl enable --now qarp
   ```

---

### Deployment Model 2: Enterprise Docker Container

Create a secure, non-root, self-contained container image:

```dockerfile
# Dockerfile
FROM python:3.11-slim

WORKDIR /app

RUN useradd -m -u 1001 qarpuser && \
    apt-get update && \
    apt-get install -y --no-install-recommends libpcap-dev && \
    rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN chown -R qarpuser:qarpuser /app
USER qarpuser

EXPOSE 8501

HEALTHCHECK --interval=30s --timeout=5s --retries=3 \
  CMD curl --fail http://localhost:8501/_stcore/health || exit 1

ENTRYPOINT ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0", "--server.headless=true"]
```

**Build and Run:**
```bash
docker build -t qarp-profiler:latest .
docker run -d -p 8501:8501 --name qarp-instance --restart unless-stopped qarp-profiler:latest
```

---

### Deployment Model 3: Kubernetes / OpenShift Helm Deployment

For large-scale enterprise deployments across core banking Kubernetes clusters:

```yaml
# deployment.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: qarp-profiler
  namespace: security-pqc
  labels:
    app: qarp-profiler
spec:
  replicas: 2
  selector:
    matchLabels:
      app: qarp-profiler
  template:
    metadata:
      labels:
        app: qarp-profiler
    spec:
      containers:
      - name: qarp
        image: internal-registry.bank.local/security/qarp-profiler:latest
        ports:
        - containerPort: 8501
        resources:
          limits:
            cpu: "2"
            memory: "4Gi"
          requests:
            cpu: "500m"
            memory: "1Gi"
        securityContext:
          allowPrivilegeEscalation: false
          readOnlyRootFilesystem: true
          runAsNonRoot: true
          runAsUser: 1001
---
apiVersion: v1
kind: Service
metadata:
  name: qarp-service
  namespace: security-pqc
spec:
  selector:
    app: qarp-profiler
  ports:
  - protocol: TCP
    port: 80
    targetPort: 8501
  type: ClusterIP
```

---

### Deployment Model 4: Reverse Proxy & Enterprise Gateway Integration (NGINX)

Integrate QARP behind your corporate Single Sign-On (SSO) and mutual TLS gateway:

```nginx
# /etc/nginx/conf.d/qarp.conf
server {
    listen 443 ssl http2;
    server_name qarp.bank.internal;

    ssl_certificate /etc/ssl/certs/bank_internal_chain.crt;
    ssl_certificate_key /etc/ssl/private/bank_internal.key;
    ssl_protocols TLSv1.2 TLSv1.3;
    ssl_ciphers ECDHE-ECDSA-AES256-GCM-SHA384:ECDHE-RSA-AES256-GCM-SHA384;

    # Streamlit WebSocket and Reverse Proxy Support
    location / {
        proxy_pass http://127.0.0.1:8501;
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection "upgrade";
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
        proxy_read_timeout 86400;
    }
}
```

---

### Deployment Model 5: Automated CI/CD Cryptographic Pipeline Scan

Incorporate QARP's CLI sizing engine into your DevSecOps pipeline to fail builds if unapproved cryptographic primitives or unsafe MTU packet splits are detected:

```yaml
# .gitlab-ci.yml or .github/workflows/cbom-audit.yml
name: Cryptographic Post-Quantum Compliance Audit

on: [push, pull_request]

jobs:
  pqc-audit:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      
      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.11'
          
      - name: Install dependencies
        run: pip install -r requirements.txt
        
      - name: Execute QARP Ingress & Sizing Engine
        run: python pqc_log_parser_and_cost_engine.py --fail-on-shor
        
      - name: Validate Payment HSM Cryptographic Support
        run: python test_hsm_pqc_support.py
        
      - name: Archive CBOM Compliance Artifacts
        uses: actions/upload-artifact@v4
        with:
          name: cryptographic-bill-of-materials
          path: qarp_cryptographic_bill_of_materials.csv
```

---

## 🔒 Security, Compliance & Air-Gap Assurance

* **Zero Data Telemetry:** No outbound API requests, external fonts, remote scripts, or telemetry pings.
* **Pure Python Execution:** Operates strictly on local runtime dependencies.
* **Deterministic Calculations:** All physical qubit estimations, MTU fragmentation splits, and hardware capacity models are grounded in peer-reviewed academic literature and NIST standards.
