"""
Quantum Attack Risk Profiler and Migration Planner (QARP)
Interactive Streamlit Demo - 100% Local / Zero Cloud Dependency
"""

import streamlit as st
import pandas as pd
import numpy as np
import math
import json
import plotly.express as px
import plotly.graph_objects as go

# ---------------------------------------------------------
# Page Configuration & Styling
# ---------------------------------------------------------
st.set_page_config(
    page_title="QARP - Quantum Attack Risk Profiler",
    page_icon="🏦",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
<style>
    .main-header {
        font-size: 2.1rem;
        font-weight: 700;
        color: #002060;
        margin-bottom: 0px;
    }
    .sub-header {
        font-size: 1.05rem;
        color: #4A5568;
        margin-bottom: 1.5rem;
    }
    .metric-card {
        background-color: #F8FAFC;
        border: 1px solid #E2E8F0;
        border-radius: 8px;
        padding: 1rem;
        box-shadow: 0 1px 3px rgba(0,0,0,0.05);
    }
    .status-badge-vuln {
        background-color: #FEE2E2;
        color: #991B1B;
        padding: 2px 8px;
        border-radius: 4px;
        font-weight: bold;
    }
    .status-badge-safe {
        background-color: #DCFCE7;
        color: #166534;
        padding: 2px 8px;
        border-radius: 4px;
        font-weight: bold;
    }
</style>
""", unsafe_allow_html=True)

# ---------------------------------------------------------
# Mathematical and Architectural Kernels
# ---------------------------------------------------------
def calculate_shor_qubits(bits: int, algo_type: str = "RSA", model: str = "Gidney-Ekerå (2021)"):
    """
    Computes required logical and physical qubits using Shor's algorithm variants.
    """
    if algo_type == "RSA":
        if "Gidney" in model:
            logical_qubits = (2 * bits) + 2
            # 20M physical qubits for 4098 logical qubits with surface code (~4900 physical/logical)
            physical_qubits = int(logical_qubits * 4880)
            years_runway = max(3.0, round(2035.0 - (bits / 400.0), 1))
        else:
            logical_qubits = 2 * bits
            physical_qubits = logical_qubits * 10000
            years_runway = max(5.0, round(2038.0 - (bits / 300.0), 1))
    else: # ECC / ECDSA
        logical_qubits = int(6 * bits) # ~1536 logical for P-256
        physical_qubits = int(logical_qubits * 3500)
        years_runway = max(2.5, round(2033.0 - (bits / 100.0), 1))
        
    return logical_qubits, physical_qubits, years_runway


# Reference Cryptographic Inventory Catalog
CBOM_CATALOG = [
    {"Algorithm": "RSA-2048", "Standard": "PKCS#1 v2.2", "Role": "TLS Ingress / Signature / KEK Wrap", "PQC Status": "Vulnerable (Shor)", "Replacement": "ML-KEM-768 / ML-DSA-65"},
    {"Algorithm": "RSA-4096", "Standard": "PKCS#1 v2.2", "Role": "Bank Root CA / Audit Logging", "PQC Status": "Vulnerable (Shor)", "Replacement": "ML-DSA-87 / SLH-DSA-256"},
    {"Algorithm": "ECDSA-P256", "Standard": "FIPS 186-4", "Role": "Mobile Banking / FedNow Ingress", "PQC Status": "Vulnerable (Shor)", "Replacement": "ML-DSA-44"},
    {"Algorithm": "ECDH-X25519", "Standard": "RFC 7748", "Role": "Ephemeral TLS 1.3 Key Agreement", "PQC Status": "Vulnerable (Shor)", "Replacement": "Hybrid X25519 + ML-KEM-768"},
    {"Algorithm": "AES-128-GCM", "Standard": "FIPS 197", "Role": "Database Encryption / Transient Tokens", "PQC Status": "Vulnerable (Grover 64-bit)", "Replacement": "AES-256-GCM"},
    {"Algorithm": "AES-256-GCM", "Standard": "FIPS 197", "Role": "PCI-DSS Database TDE / DEKs", "PQC Status": "PQC Compliant (128-bit)", "Replacement": "Retain (No change needed)"},
    {"Algorithm": "SHA-256", "Standard": "FIPS 180-4", "Role": "Cert Hashing / Audit Trails", "PQC Status": "Marginal (~85-128b collision)", "Replacement": "SHA-384 / SHA-512 / SHA3"},
    {"Algorithm": "ML-KEM-768", "Standard": "NIST FIPS 203", "Role": "Post-Quantum Key Encapsulation", "PQC Status": "PQC Standard", "Replacement": "Primary Migration Target"},
    {"Algorithm": "ML-DSA-65", "Standard": "NIST FIPS 204", "Role": "Post-Quantum Digital Signatures", "PQC Status": "PQC Standard", "Replacement": "Primary Migration Target"},
    {"Algorithm": "SLH-DSA-128s", "Standard": "NIST FIPS 205", "Role": "Stateless Hash-Based Root of Trust", "PQC Status": "PQC Standard", "Replacement": "Firmware & Root CA Fallback"}
]

# Hardware Characteristics
CRYPTO_HARDWARE_SPECS = {
    "RSA-2048": {"pub_bytes": 256, "sig_bytes": 256, "hsm_ops_sec": 1200, "relative_cpu": 1.0},
    "ECDSA-P256": {"pub_bytes": 64, "sig_bytes": 64, "hsm_ops_sec": 3500, "relative_cpu": 0.45},
    "ML-KEM-768": {"pub_bytes": 1184, "sig_bytes": 1088, "hsm_ops_sec": 450, "relative_cpu": 0.20},
    "ML-DSA-65": {"pub_bytes": 1952, "sig_bytes": 3300, "hsm_ops_sec": 180, "relative_cpu": 1.35},
}

# ---------------------------------------------------------
# Sidebar Configuration
# ---------------------------------------------------------
st.sidebar.image("https://img.icons8.com/fluency/96/bank-building.png", width=64)
st.sidebar.title("QARP Configuration")
st.sidebar.markdown("---")

app_mode = st.sidebar.radio(
    "Navigation View",
    ["1. Ingestion & Telemetry Parser", "2. Quantum Risk Profiler (Shor & Grover)", "3. CBOM Compliance Matrix", "4. Enterprise Hardware Capacity Engine", "5. Strategic Migration Roadmap"]
)

st.sidebar.markdown("---")
st.sidebar.subheader("Migration Targets (NIST FIPS)")
sel_kem = st.sidebar.selectbox("Target KEM Standard", ["ML-KEM-768 (NIST Level 3)", "ML-KEM-1024 (NIST Level 5)", "ML-KEM-512 (NIST Level 1)"], index=0)
sel_sig = st.sidebar.selectbox("Target Digital Signature", ["ML-DSA-65 (NIST Level 3)", "ML-DSA-87 (NIST Level 5)", "ML-DSA-44 (NIST Level 2)"], index=0)
shor_optimization = st.sidebar.selectbox("Cryptanalysis Model", ["Gidney-Ekerå (2021 Optimization)", "Standard Shor (1994)"], index=0)

# ---------------------------------------------------------
# Header Area
# ---------------------------------------------------------
st.markdown('<div class="main-header">Quantum Attack Risk Profiler & Migration Planner (QARP)</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-header">Platform-Agnostic Enterprise Banking Sizing, Telemetry Profiling & Cryptographic Modernization Framework</div>', unsafe_allow_html=True)

# ---------------------------------------------------------
# View 1: Ingestion & Telemetry Parser
# ---------------------------------------------------------
if app_mode == "1. Ingestion & Telemetry Parser":
    st.subheader("📡 Live / Synthetic Banking Ingress Telemetry")
    st.write("Ingests streaming access logs from enterprise API gateways (NGINX, HAProxy, Envoy, Kong) and payment switches (ISO 20022).")
    
    st.markdown("### 📥 Ingestion Source & Telemetry Mode")
    
    log_source = st.radio(
        "Choose Telemetry Input Method", 
        [
            "📂 Upload Custom File or Load Project Files (JSON / CSV / Excel .xlsx)",
            "⚡ Synthetic Live Core Banking Stream (Simulated Fedwire / RTGS / FAPI)"
        ],
        horizontal=True
    )
    
    sample_logs = []
    
    if "Upload Custom File" in log_source:
        st.info("💡 **Upload or Select an Ingestion File:** You can upload your own `.json`, `.csv`, or `.xlsx` file, or click one of the pre-loaded project files below.")
        
        up_col1, up_col2 = st.columns([2.5, 1.5])
        with up_col1:
            uploaded_file = st.file_uploader(
                "Drag and drop or browse for a log / inventory file", 
                type=["json", "csv", "log", "xlsx", "xls"],
                help="Accepts JSON, CSV, or Excel files containing cryptographic algorithms or banking endpoints."
            )
        with up_col2:
            st.markdown("**Quick Load Pre-Existing Project Files:**")
            use_project_excel = st.button("📑 Load cryptographic_algorithms_pqc.xlsx", use_container_width=True)
            use_sample_json = st.button("📄 Load sample_banking_logs.json", use_container_width=True)
            use_sample_csv = st.button("📊 Load sample_banking_logs.csv", use_container_width=True)
            
        raw_df = None
        
        if uploaded_file is not None:
            file_name = uploaded_file.name.lower()
            try:
                if file_name.endswith(".json"):
                    content = uploaded_file.read().decode("utf-8")
                    try:
                        parsed_json = json.loads(content)
                        if isinstance(parsed_json, dict):
                            parsed_json = [parsed_json]
                    except json.JSONDecodeError:
                        # Try line-delimited JSON
                        parsed_json = [json.loads(line) for line in content.strip().splitlines() if line.strip()]
                    raw_df = pd.DataFrame(parsed_json)
                elif file_name.endswith(".csv") or file_name.endswith(".log"):
                    raw_df = pd.read_csv(uploaded_file)
                elif file_name.endswith(".xlsx") or file_name.endswith(".xls"):
                    excel_data = pd.ExcelFile(uploaded_file)
                    selected_sheet = excel_data.sheet_names[0]
                    raw_df = pd.read_excel(uploaded_file, sheet_name=selected_sheet)
                    raw_df = raw_df.dropna(how='all')
                st.success(f"✅ Successfully parsed `{uploaded_file.name}` ({len(raw_df)} records loaded)")
            except Exception as e:
                st.error(f"❌ Error parsing uploaded file: {str(e)}")
        elif use_sample_json:
            try:
                with open("sample_banking_logs.json", "r") as f:
                    raw_df = pd.DataFrame(json.load(f))
                st.info("Loaded `sample_banking_logs.json` (6 banking endpoints)")
            except Exception as e:
                st.error(f"Error loading sample JSON: {e}")
        elif use_sample_csv:
            try:
                raw_df = pd.read_csv("sample_banking_logs.csv")
                st.info("Loaded `sample_banking_logs.csv` (6 banking endpoints)")
            except Exception as e:
                st.error(f"Error loading sample CSV: {e}")
        elif use_project_excel:
            try:
                excel_data = pd.ExcelFile("cryptographic_algorithms_pqc.xlsx")
                raw_df = pd.read_excel("cryptographic_algorithms_pqc.xlsx", sheet_name=excel_data.sheet_names[0])
                raw_df = raw_df.dropna(subset=['Algorithm'])
                st.info(f"Loaded `cryptographic_algorithms_pqc.xlsx` (Sheet: `{excel_data.sheet_names[0]}`, {len(raw_df)} algorithm entries)")
            except Exception as e:
                st.error(f"Error loading project Excel file: {e}")
                
        if raw_df is not None and not raw_df.empty:
            # Check if this is an algorithm inventory sheet (like cryptographic_algorithms_pqc.xlsx)
            if "Algorithm" in raw_df.columns and "endpoint" not in [c.lower() for c in raw_df.columns]:
                # Convert algorithm inventory rows into simulated banking workloads
                converted_logs = []
                for idx, row in raw_df.iterrows():
                    algo_name = str(row.get("Algorithm", "")).strip()
                    if not algo_name or algo_name == "nan":
                        continue
                    func_ctx = str(row.get("Banking Function & Hardware Context (TPM / HSM / KMS / KEK)", row.get("Mitigation", "Core Banking Service")))
                    clean_endpoint = f"/v1/crypto/{algo_name.lower().replace(' ', '-').replace('/', '-')}"
                    
                    if "RSA" in algo_name:
                        cipher = f"TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256"
                    elif "ECC" in algo_name or "ECDSA" in algo_name or "ECDH" in algo_name:
                        cipher = f"TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384"
                    elif "AES-128" in algo_name or "3DES" in algo_name or "DES" in algo_name:
                        cipher = f"TLS_RSA_WITH_AES_128_CBC_SHA"
                    else:
                        cipher = f"TLS_AES_256_GCM_SHA384"
                        
                    converted_logs.append({
                        "endpoint": clean_endpoint,
                        "tls_cipher": cipher,
                        "protocol": func_ctx[:45] if func_ctx and func_ctx != "nan" else "Enterprise Service",
                        "tps": 1500 if "RSA" in algo_name else (3000 if "ECC" in algo_name else 1000),
                        "latency_ms": 12.0
                    })
                sample_logs = converted_logs
                raw_df = pd.DataFrame(sample_logs)
            else:
                # Normalize column names for standard access logs
                col_map = {}
                for col in raw_df.columns:
                    c_low = col.lower().strip()
                    if c_low in ["endpoint", "path", "uri", "url"]:
                        col_map[col] = "endpoint"
                    elif c_low in ["tls_cipher", "cipher", "ssl_cipher", "ciphersuite"]:
                        col_map[col] = "tls_cipher"
                    elif c_low in ["protocol", "proto", "type"]:
                        col_map[col] = "protocol"
                    elif c_low in ["tps", "throughput", "requests", "count", "rate"]:
                        col_map[col] = "tps"
                    elif c_low in ["latency_ms", "latency", "response_time", "duration"]:
                        col_map[col] = "latency_ms"
                    elif c_low in ["timestamp", "time", "date"]:
                        col_map[col] = "timestamp"
                raw_df = raw_df.rename(columns=col_map)
                
                # Fill default values for missing columns
                if "endpoint" not in raw_df.columns:
                    raw_df["endpoint"] = [f"/api/v1/endpoint_{i+1}" for i in range(len(raw_df))]
                if "tls_cipher" not in raw_df.columns:
                    raw_df["tls_cipher"] = "TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256"
                if "protocol" not in raw_df.columns:
                    raw_df["protocol"] = "REST / HTTPS"
                if "tps" not in raw_df.columns:
                    raw_df["tps"] = 1000
                else:
                    raw_df["tps"] = pd.to_numeric(raw_df["tps"], errors="coerce").fillna(1000).astype(int)
                if "latency_ms" not in raw_df.columns:
                    raw_df["latency_ms"] = 15.0
                else:
                    raw_df["latency_ms"] = pd.to_numeric(raw_df["latency_ms"], errors="coerce").fillna(15.0).astype(float)
                    
                sample_logs = raw_df.to_dict(orient="records")
            
            with st.expander("🔍 View Raw Ingested Records", expanded=False):
                st.dataframe(raw_df, use_container_width=True)
        else:
            simulated_load = 5000
            st.info("ℹ️ Awaiting upload. Displaying default baseline banking stream. Upload a file above or click any 'Quick Load' button.")
            sample_logs = [
                {"timestamp": "2026-09-07T01:00:15Z", "endpoint": "/v1/settlement/credit-transfer", "tls_cipher": "TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256", "protocol": "ISO 20022 pacs.008", "tps": int(simulated_load * 0.45), "latency_ms": 14.2},
                {"timestamp": "2026-09-07T01:00:15Z", "endpoint": "/v1/clearing/rtgs-instant", "tls_cipher": "TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384", "protocol": "ISO 20022 pacs.002", "tps": int(simulated_load * 0.35), "latency_ms": 8.5},
                {"timestamp": "2026-09-07T01:00:15Z", "endpoint": "/v1/fapi/open-banking/consent", "tls_cipher": "TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256", "protocol": "REST / OAuth2 FAPI", "tps": int(simulated_load * 0.15), "latency_ms": 18.0},
                {"timestamp": "2026-09-07T01:00:15Z", "endpoint": "/v1/ledger/batch-reconciliation", "tls_cipher": "TLS_RSA_WITH_AES_128_CBC_SHA", "protocol": "SWIFT MT103 XML", "tps": int(simulated_load * 0.05), "latency_ms": 46.0}
            ]
    else:
        simulated_load = st.slider("Global Peak Settlement Volume (TPS)", min_value=1000, max_value=15000, value=5000, step=500)
        sample_logs = [
            {"timestamp": "2026-09-07T01:00:15Z", "endpoint": "/v1/settlement/credit-transfer", "tls_cipher": "TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256", "protocol": "ISO 20022 pacs.008", "tps": int(simulated_load * 0.45), "latency_ms": 14.2},
            {"timestamp": "2026-09-07T01:00:15Z", "endpoint": "/v1/clearing/rtgs-instant", "tls_cipher": "TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384", "protocol": "ISO 20022 pacs.002", "tps": int(simulated_load * 0.35), "latency_ms": 8.5},
            {"timestamp": "2026-09-07T01:00:15Z", "endpoint": "/v1/fapi/open-banking/consent", "tls_cipher": "TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256", "protocol": "REST / OAuth2 FAPI", "tps": int(simulated_load * 0.15), "latency_ms": 18.0},
            {"timestamp": "2026-09-07T01:00:15Z", "endpoint": "/v1/ledger/batch-reconciliation", "tls_cipher": "TLS_RSA_WITH_AES_128_CBC_SHA", "protocol": "SWIFT MT103 XML", "tps": int(simulated_load * 0.05), "latency_ms": 46.0}
        ]
    
    df_logs = pd.DataFrame(sample_logs)
    
    # Process Telemetry
    results = []
    shor_vulnerable_count = 0
    grover_vulnerable_count = 0
    total_tx_volume = 0
    total_monthly_bw_gb = 0.0
    
    for row in sample_logs:
        c = str(row.get("tls_cipher", "TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256"))
        asym = "RSA-2048" if "RSA" in c else ("ECDSA-P256" if ("ECDSA" in c or "ECDH" in c) else "RSA-2048")
        sym = "AES-128" if "128" in c else "AES-256"
        bits = 2048 if asym == "RSA-2048" else 256
        log_q, phys_q, runway = calculate_shor_qubits(bits, "RSA" if asym == "RSA-2048" else "ECC", shor_optimization)
        
        if asym in ["RSA-2048", "ECDSA-P256"]:
            shor_vulnerable_count += 1
        if sym == "AES-128":
            grover_vulnerable_count += 1
            
        tps_val = int(row.get("tps", 1000))
        total_tx_volume += tps_val
        
        legacy_bytes = CRYPTO_HARDWARE_SPECS[asym]["pub_bytes"] + CRYPTO_HARDWARE_SPECS[asym]["sig_bytes"]
        pqc_bytes = CRYPTO_HARDWARE_SPECS["ML-KEM-768"]["pub_bytes"] + CRYPTO_HARDWARE_SPECS["ML-DSA-65"]["sig_bytes"]
        
        leg_pkts = math.ceil(legacy_bytes / 1500)
        pqc_pkts = math.ceil(pqc_bytes / 1500)
        
        # Monthly volume
        monthly_tx = tps_val * 86400 * 30
        monthly_gb_delta = (monthly_tx * (pqc_bytes - legacy_bytes)) / (1024**3)
        total_monthly_bw_gb += monthly_gb_delta
        
        base_lat = float(row.get("latency_ms", 15.0))
        proj_lat = round(base_lat + (pqc_pkts - leg_pkts) * 2.2, 1)
        
        results.append({
            "Endpoint": row.get("endpoint", "/api"),
            "Protocol": row.get("protocol", "REST/HTTPS"),
            "TPS": tps_val,
            "Active Cipher": c,
            "Legacy Asymmetric": asym,
            "Symmetric": sym,
            "Shor Qubits (Phys)": f"{phys_q:,}",
            "Compromise Runway": f"{runway} Yrs",
            "Handshake Size Delta": f"{legacy_bytes}B -> {pqc_bytes}B (+{round((pqc_bytes-legacy_bytes)/legacy_bytes*100)}%)",
            "MTU Packets (1500B)": f"{leg_pkts} pkt -> {pqc_pkts} pkts",
            "Base Latency": f"{base_lat:.1f} ms",
            "Projected PQC Latency": f"{proj_lat:.1f} ms",
            "Monthly Bandwidth Delta": f"+{round(monthly_gb_delta, 1):,} GB"
        })
        
    df_parsed = pd.DataFrame(results)
    
    st.dataframe(df_parsed, use_container_width=True)
    
    # Download parsed report
    csv_export = df_parsed.to_csv(index=False).encode('utf-8')
    st.download_button(
        "📥 Export Parsed Quantum Risk Assessment (CSV)",
        data=csv_export,
        file_name="qarp_quantum_risk_profiling_report.csv",
        mime="text/csv"
    )
    
    total_endpoints = max(1, len(results))
    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Total Ingested TPS", f"{total_tx_volume:,} tx/s")
    c2.metric("Shor-Vulnerable Endpoints", f"{shor_vulnerable_count} of {total_endpoints} ({round(shor_vulnerable_count/total_endpoints*100)}%)", delta="-Critical Risk", delta_color="inverse")
    c3.metric("Grover-Vulnerable (AES-128)", f"{grover_vulnerable_count} of {total_endpoints} ({round(grover_vulnerable_count/total_endpoints*100)}%)", delta="-Upgrade to AES-256", delta_color="inverse")
    c4.metric("Total Monthly Bandwidth Delta", f"+{round(total_monthly_bw_gb, 1):,} GB", delta="-Expansion Overhead", delta_color="inverse")


# ---------------------------------------------------------
# View 2: Quantum Risk Profiler (Shor & Grover)
# ---------------------------------------------------------
elif app_mode == "2. Quantum Risk Profiler (Shor & Grover)":
    st.subheader("⚛️ Quantum Vulnerability & Qubit Resource Estimation")
    st.write("Evaluates algorithmic vulnerability against Shor's and Grover's cryptanalysis under physical error-corrected quantum computing assumptions.")
    
    col_a, col_b = st.columns(2)
    
    with col_a:
        st.markdown("### 🔓 Shor's Algorithm: Asymmetric Cryptanalysis")
        st.markdown("""
        **Shor's algorithm** solves prime factorization (RSA) and discrete logarithms (ECDSA/ECDH) in polynomial time:
        - **RSA-2048**: Requires **4,098 logical qubits** (using Gidney-Ekerå 2021 modular addition optimizations) and ~20 million physical qubits.
        - **ECDSA P-256**: Requires **1,536 logical qubits**; breaks faster than RSA due to smaller group representations.
        """)
        
        rsa_lengths = [1024, 2048, 3072, 4096]
        shor_data = []
        for l in rsa_lengths:
            l_q, p_q, r_y = calculate_shor_qubits(l, "RSA", shor_optimization)
            shor_data.append({"Key Size": f"RSA-{l}", "Logical Qubits": l_q, "Physical Qubits": p_q, "Years to Viable Attack": r_y})
            
        st.table(pd.DataFrame(shor_data))
        
    with col_b:
        st.markdown("### 🔍 Grover's Algorithm: Symmetric & Hash Security Halving")
        st.markdown(r"""
        **Grover's algorithm** speeds up unstructured database search in $\mathcal{O}(\sqrt{N})$:
        - **AES-128**: Effective security reduced from 128-bit to **64-bit** (computationally viable to brute-force on quantum computers).
        - **AES-256**: Effective security reduced from 256-bit to **128-bit** (**Quantum Safe**; requires $2^{128}$ operations).
        - **SHA-256**: Collision resistance drops to **85–128 bits**; migrate to SHA-384 / SHA-512 / SHA3.
        """)
        
        grover_data = [
            {"Algorithm": "AES-128-GCM", "Classical Security": "128 bits", "Post-Quantum Security": "64 bits", "Verdict": "❌ NON-COMPLIANT"},
            {"Algorithm": "AES-256-GCM", "Classical Security": "256 bits", "Post-Quantum Security": "128 bits", "Verdict": "✅ QUANTUM RESISTANT"},
            {"Algorithm": "SHA-256", "Classical Collision": "128 bits", "Quantum Collision": "85.3 bits", "Verdict": "⚠️ MIGRATE TO SHA-384"},
            {"Algorithm": "SHA-384", "Classical Collision": "192 bits", "Quantum Collision": "128 bits", "Verdict": "✅ QUANTUM RESISTANT"}
        ]
        st.table(pd.DataFrame(grover_data))

# ---------------------------------------------------------
# View 3: CBOM Compliance Matrix
# ---------------------------------------------------------
elif app_mode == "3. CBOM Compliance Matrix":
    st.subheader("📋 Cryptographic Bill of Materials (CBOM) & Compliance")
    st.write("CycloneDX 1.6 compliant Cryptographic Inventory mapped against NIST FIPS 203/204/205 & NSA CNSA 2.0 guidelines.")
    
    cbom_source = st.radio(
        "CBOM Data Source",
        ["📁 Project Excel Catalog (cryptographic_algorithms_pqc.xlsx)", "🌐 Baseline Reference CBOM Catalog (CycloneDX 1.6)", "⬆️ Upload Custom CBOM (.xlsx, .csv, .json)"],
        horizontal=True
    )
    
    cbom_df = None
    
    if "Project Excel" in cbom_source:
        try:
            excel_path = "cryptographic_algorithms_pqc.xlsx"
            xls = pd.ExcelFile(excel_path)
            sheet = st.selectbox("Select Excel Sheet", xls.sheet_names, index=0)
            df_raw = pd.read_excel(excel_path, sheet_name=sheet)
            cbom_df = df_raw.dropna(subset=['Algorithm'] if 'Algorithm' in df_raw.columns else df_raw.columns[0]).reset_index(drop=True)
            st.success(f"Loaded `{sheet}` from `cryptographic_algorithms_pqc.xlsx` ({len(cbom_df)} algorithms)")
        except Exception as e:
            st.error(f"Error loading Excel file: {e}")
            cbom_df = pd.DataFrame(CBOM_CATALOG)
    elif "Upload Custom" in cbom_source:
        up_cbom = st.file_uploader("Upload CBOM File", type=["xlsx", "xls", "csv", "json"])
        if up_cbom is not None:
            try:
                if up_cbom.name.endswith((".xlsx", ".xls")):
                    x = pd.ExcelFile(up_cbom)
                    s = st.selectbox("Sheet", x.sheet_names)
                    cbom_df = pd.read_excel(up_cbom, sheet_name=s).dropna(how='all')
                elif up_cbom.name.endswith(".csv"):
                    cbom_df = pd.read_csv(up_cbom).dropna(how='all')
                elif up_cbom.name.endswith(".json"):
                    cbom_df = pd.DataFrame(json.load(up_cbom))
                st.success(f"Loaded {len(cbom_df)} records from `{up_cbom.name}`")
            except Exception as e:
                st.error(f"Error reading file: {e}")
        if cbom_df is None:
            cbom_df = pd.DataFrame(CBOM_CATALOG)
    else:
        cbom_df = pd.DataFrame(CBOM_CATALOG)
        
    if cbom_df is not None and not cbom_df.empty:
        # Search filter
        search_query = st.text_input("🔍 Search / Filter Cryptographic Assets (e.g. RSA, AES, HSM, TPM, ML-KEM, Broken)", "")
        if search_query:
            mask = cbom_df.astype(str).apply(lambda row: row.str.contains(search_query, case=False).any(), axis=1)
            display_df = cbom_df[mask]
        else:
            display_df = cbom_df
            
        # Summary Metrics
        tot = len(display_df)
        pqc_compliant_col = [c for c in display_df.columns if "pqc" in c.lower() or "compliant" in c.lower() or "status" in c.lower()]
        
        c_pqc = 0
        c_broken = 0
        if pqc_compliant_col:
            pqc_series = display_df[pqc_compliant_col[0]].astype(str).str.lower()
            c_pqc = pqc_series.str.contains("yes|compliant|standard|safe").sum()
            c_broken = pqc_series.str.contains("no|broken|vulnerable|non").sum()
            
        m1, m2, m3, m4 = st.columns(4)
        m1.metric("Cryptographic Assets", f"{tot} items")
        m2.metric("PQC Quantum Safe", f"{c_pqc} ({round(c_pqc/max(1,tot)*100)}%)" if pqc_compliant_col else "N/A")
        m3.metric("Quantum Vulnerable", f"{c_broken} ({round(c_broken/max(1,tot)*100)}%)" if pqc_compliant_col else "N/A", delta="-Action Required", delta_color="inverse")
        m4.metric("Hardware Roots (HSM/TPM)", f"{display_df.astype(str).apply(lambda r: r.str.contains('HSM|TPM|KMIP|KEK', case=False).any(), axis=1).sum()} items")
        
        st.dataframe(display_df, use_container_width=True)
        
        # Download filtered CBOM
        csv_cbom = display_df.to_csv(index=False).encode('utf-8')
        st.download_button(
            "📥 Export Filtered CBOM (CSV)",
            data=csv_cbom,
            file_name="qarp_cryptographic_bill_of_materials.csv",
            mime="text/csv"
        )
        
    st.info("💡 **Architectural Note:** In banking systems, Data Encryption Keys (DEKs) are typically AES-256 (which is quantum resistant). The critical vulnerability lies in the **Key Encrypting Keys (KEKs)** wrapping those DEKs, which frequently use RSA-2048 or ECDSA.")


# ---------------------------------------------------------
# View 4: Enterprise Hardware Capacity Engine
# ---------------------------------------------------------
elif app_mode == "4. Enterprise Hardware Capacity Engine":
    st.subheader("🏢 Enterprise Hardware Appliance Capacity Planning")
    st.write("Calculates physical Payment HSM appliance requirements, CPU core loads, and network bandwidth overhead under PQC workloads.")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        target_tps = st.number_input("Target Peak Settlement TPS", min_value=500, max_value=25000, value=5000, step=500)
    with col2:
        hsm_cost = st.number_input("Monthly Amortized Cost per HSM ($)", value=1200.0, step=100.0)
    with col3:
        bandwidth_cost_per_gb = st.number_input("Datacenter Bandwidth ($/GB)", value=0.05, step=0.01)
        
    tps_range = [1000, 2500, 5000, 7500, 10000, 15000]
    comparison_data = []
    
    for t in tps_range:
        leg_hsm = max(2, math.ceil(t / CRYPTO_HARDWARE_SPECS["RSA-2048"]["hsm_ops_sec"]))
        pqc_hsm = max(2, math.ceil(t / CRYPTO_HARDWARE_SPECS["ML-DSA-65"]["hsm_ops_sec"]))
        leg_cost = leg_hsm * hsm_cost
        pqc_cost = pqc_hsm * hsm_cost
        deficit = pqc_cost - leg_cost
        pct_increase = round(((pqc_hsm - leg_hsm) / leg_hsm) * 100, 1)
        
        comparison_data.append({
            "Settlement Volume (TPS)": f"{t:,} TPS",
            "Legacy RSA-2048 HSMs": f"{leg_hsm} Units",
            "Legacy Monthly Cost": f"${leg_cost:,.2f}",
            "PQC ML-DSA-65 HSMs": f"{pqc_hsm} Units",
            "PQC Monthly Cost": f"${pqc_cost:,.2f}",
            "Appliance Deficit": f"+{pct_increase}% (+${deficit:,.2f}/mo)"
        })
        
    st.markdown("### 📊 Static IT Planning vs PQC Hardware Reality")
    st.table(pd.DataFrame(comparison_data))
    
    # Chart
    df_chart = pd.DataFrame({
        "TPS": tps_range,
        "Legacy RSA HSMs": [max(2, math.ceil(t / 1200)) for t in tps_range],
        "PQC ML-DSA HSMs": [max(2, math.ceil(t / 180)) for t in tps_range]
    })
    
    fig = go.Figure()
    fig.add_trace(go.Bar(x=df_chart["TPS"], y=df_chart["Legacy RSA HSMs"], name="Legacy RSA-2048 HSM Units", marker_color="#1D4ED8"))
    fig.add_trace(go.Bar(x=df_chart["TPS"], y=df_chart["PQC ML-DSA HSMs"], name="Required PQC ML-DSA-65 HSM Units", marker_color="#DC2626"))
    fig.update_layout(
        title="Hardware Security Module (HSM) Capacity Explosion (Due to ~85% PQC Signing Deficit)",
        xaxis_title="Settlement Transactions Per Second (TPS)",
        yaxis_title="Required Physical HSM Appliance Units",
        barmode="group",
        height=420
    )
    st.plotly_chart(fig, use_container_width=True)

# ---------------------------------------------------------
# View 5: Strategic Migration Roadmap
# ---------------------------------------------------------
elif app_mode == "5. Strategic Migration Roadmap":
    st.subheader("🗺️ Enterprise Post-Quantum Migration Roadmap (2025–2033)")
    st.write("Structured phased transition framework aligned with NIST, CNSA 2.0, and PCI-DSS compliance milestones.")
    
    phases = [
        {"Phase": "Phase 1: Discovery & CBOM (2025–2026)", "Focus": "Discovery & Inventory", "Actions": "Deploy passive telemetry parsers; generate automated CBOM; deprecate 3DES, SHA-1, MD5; enforce AES-256 for all stored data."},
        {"Phase": "Phase 2: Hybrid Ingress (2026–2028)", "Focus": "Transport Security", "Actions": "Enable hybrid TLS 1.3 (X25519 + ML-KEM-768) on edge API gateways & web portals to block Harvest Now, Decrypt Later (HNDL)."},
        {"Phase": "Phase 3: Digital Signatures & PKI (2028–2030)", "Focus": "Authentication & Non-Repudiation", "Actions": "Upgrade enterprise CAs and payment messaging (ISO 20022) to ML-DSA-65 with dual-signature certificates."},
        {"Phase": "Phase 4: Full Quantum Resistance (2030–2033)", "Focus": "Core Infrastructure", "Actions": "Decommission all classical asymmetric keys (RSA/ECC) across payment HSMs, TPM 2.0 roots of trust, and mainframe backbones."}
    ]
    
    for p in phases:
        with st.expander(p["Phase"], expanded=True):
            st.markdown(f"**Core Focus:** `{p['Focus']}`")
            st.write(p["Actions"])

st.markdown("---")
st.caption("M.Tech Cybersecurity Capstone-2 Artifact | REVA University | Anirban Dasgupta (SRN: R24MTCYS013)")
