"""
Generates high-resolution, extra-large dissertation-style Algorithm Pseudocode Images
for all 4 core non-cloud QARP algorithms.
"""

import os
import matplotlib
matplotlib.rcParams['svg.fonttype'] = 'none'
import matplotlib.pyplot as plt

TNR = 'Times New Roman'
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def draw_algorithm_box(filename_base, title_num, title_text, inputs, outputs, steps, complexity_text):
    # Large 20 x 24 inches canvas at 300 DPI
    fig, ax = plt.subplots(figsize=(20, 24), dpi=300)
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 105)
    ax.axis('off')
    
    fig.patch.set_facecolor('#FFFFFF')
    ax.set_facecolor('#FFFFFF')

    def txt(x, y, s, fs=16.5, bold=False, color='#0F172A', ha='left', va='center', italic=False):
        ax.text(x, y, s, fontsize=fs, color=color, ha=ha, va=va,
                fontweight='bold' if bold else 'normal',
                fontstyle='italic' if italic else 'normal',
                fontfamily=TNR)

    # 1. Header rules
    ax.plot([3, 97], [99.0, 99.0], color='#002060', lw=4.5)
    ax.plot([3, 97], [98.0, 98.0], color='#002060', lw=2.0)
    
    # Title
    txt(3.5, 94.8, title_num, fs=23.0, bold=True, color='#002060')
    txt(18.5, 94.8, title_text, fs=20.5, bold=True, color='#0F172A')
    
    # Mid rule
    ax.plot([3, 97], [91.8, 91.8], color='#002060', lw=2.5)
    
    # 2. Input / Output Block
    curr_y = 88.5
    txt(4.5, curr_y, "Input:", fs=18.0, bold=True, color='#002060')
    txt(14.0, curr_y, inputs[0], fs=17.0, italic=True)
    
    for inp in inputs[1:]:
        curr_y -= 3.2
        txt(14.0, curr_y, inp, fs=16.5)
        
    curr_y -= 3.6
    txt(4.5, curr_y, "Output:", fs=18.0, bold=True, color='#002060')
    txt(14.0, curr_y, outputs[0], fs=17.0, italic=True)
    for out in outputs[1:]:
        curr_y -= 3.2
        txt(14.0, curr_y, out, fs=16.5)
        
    # Separator rule
    curr_y -= 2.6
    ax.plot([3, 97], [curr_y, curr_y], color='#94A3B8', lw=1.8)
    
    # 3. Algorithm Body
    curr_y -= 3.2
    for num, code, indent, is_keyword in steps:
        # Line number
        txt(4.5, curr_y, f"{num:2d}:", fs=16.0, bold=True, color='#475569')
        
        # Indent
        x_indent = 10.5 + (indent * 4.2)
        
        if code.startswith("//"):
            txt(x_indent, curr_y, code, fs=16.0, bold=False, color='#059669', italic=True)
        elif "CRITICAL" in code or "DEFICIT" in code or "VULNERABLE" in code:
            txt(x_indent, curr_y, code, fs=16.5, bold=True, color='#DC2626')
        elif "COMPLIANT" in code or "SAFE" in code or "RESISTANT" in code:
            txt(x_indent, curr_y, code, fs=16.5, bold=True, color='#16A34A')
        elif is_keyword:
            txt(x_indent, curr_y, code, fs=16.8, bold=True, color='#002060')
        else:
            txt(x_indent, curr_y, code, fs=16.5, bold=False, color='#0F172A')
            
        curr_y -= 2.45

    # Bottom rule
    curr_y += 0.5
    ax.plot([3, 97], [curr_y, curr_y], color='#002060', lw=3.5)

    # Complexity
    curr_y -= 2.6
    txt(4.5, curr_y, "Complexity Analysis:", fs=16.0, bold=True, color='#002060')
    txt(23.0, curr_y, complexity_text, fs=15.5, italic=True, color='#334155')

    plt.tight_layout()
    
    png_path = os.path.join(BASE_DIR, f"{filename_base}.png")
    svg_path = os.path.join(BASE_DIR, f"{filename_base}.svg")
    
    plt.savefig(png_path, dpi=300, bbox_inches='tight', facecolor='#FFFFFF')
    plt.savefig(svg_path, bbox_inches='tight', facecolor='#FFFFFF')
    plt.close('all')
    print(f"Generated: {png_path}")

def generate_all():
    # -------------------------------------------------------------
    # ALGORITHM 1: PQC Network Bandwidth & Latency Overhead Profiler
    # -------------------------------------------------------------
    draw_algorithm_box(
        filename_base="algorithm_1_pseudocode",
        title_num="Algorithm 1:",
        title_text="PQC Network Bandwidth & Latency Overhead Profiler",
        inputs=[
            "API Traces T = { (e_i, C_i, tps_i, L_base,i) } for i = 1, ..., N",
            "Target PQC Primitives: KEM K (e.g., ML-KEM-768), Signature S (e.g., ML-DSA-65)",
            "Hardware Specs: PubKeySize(c), SigSize(c), Ethernet MTU = 1500 bytes",
            "Operational Constraints: Bank SLA Limit = 50.0 ms, Expansion Threshold = 3.0x"
        ],
        outputs=[
            "Sizing Assessment Matrix M = { (e_i, tps_i, BW_leg, BW_pqc, Gamma_i, Phi_i, L_pqc, Risk_i) }"
        ],
        steps=[
            (1, "Initialize empty output assessment matrix: M <- []", 0, False),
            (2, "Extract Target PQC Key & Signature Sizes from Specification:", 0, False),
            (3, "S_pqc <- PubKeySize(K) + SigSize(S)    // ML-KEM-768 + ML-DSA-65: 1184 + 3300 = 4484 B", 1, False),
            (4, "Compute PQC Handshake MTU Packet Fragmentation Factor:", 0, False),
            (5, "Phi_pqc <- ceil( S_pqc / MTU )             // ceil( 4484 / 1500 ) = 3 TCP packets", 1, False),
            (6, "for each trace t_i in API Traces T do", 0, True),
            (7, "C_leg <- t_i.C_i                          // e.g., RSA-2048 or ECDSA-P256", 1, False),
            (8, "S_leg <- PubKeySize(C_leg) + SigSize(C_leg) // e.g., 256 + 256 = 512 bytes", 1, False),
            (9, "Phi_leg <- ceil( S_leg / MTU )           // ceil( 512 / 1500 ) = 1 TCP packet", 1, False),
            (10, "// Compute Ingress Bandwidth Requirements in Megabytes/sec (MB/s)", 1, True),
            (11, "BW_leg <- ( t_i.tps_i * S_leg ) / ( 1024 * 1024 )", 1, False),
            (12, "BW_pqc <- ( t_i.tps_i * S_pqc ) / ( 1024 * 1024 )", 1, False),
            (13, "Gamma_i <- BW_pqc / max( 1.0, BW_leg )       // Bandwidth Expansion Scale Factor", 1, False),
            (14, "// Model TCP Multi-Packet Serialization Latency & Network Overhead", 1, True),
            (15, "Delta_L <- ( Phi_pqc - Phi_leg ) * 2.2 ms + ( S_pqc / MTU ) * 1.5 ms", 1, False),
            (16, "L_pqc <- t_i.L_base,i + Delta_L             // Projected Post-Quantum Handshake Latency", 1, False),
            (17, "// Evaluate Banking Service Level Agreement (SLA) & Bottleneck Risk", 1, True),
            (18, "if ( Gamma_i > 3.0 ) OR ( L_pqc > 50.0 ms ) then", 1, True),
            (19, "Risk_i <- CRITICAL_RISK ( Handshake Latency Spike & HSM Deficit )", 2, False),
            (20, "else", 1, True),
            (21, "Risk_i <- COMPLIANT_MANAGED ( Within Latency Budget & Capacity )", 2, False),
            (22, "end if", 1, True),
            (23, "Record_i <- ( t_i.e_i, t_i.tps_i, BW_leg, BW_pqc, Gamma_i, Phi_pqc, L_pqc, Risk_i )", 1, False),
            (24, "M.append( Record_i )", 1, False),
            (25, "end for", 0, True),
            (26, "return M", 0, True)
        ],
        complexity_text="Time Complexity: O(N) linear scan over API endpoints | Space Complexity: O(N) for assessment matrix M"
    )

    # -------------------------------------------------------------
    # ALGORITHM 2: Enterprise Payment HSM Capacity & Sizing Engine
    # -------------------------------------------------------------
    draw_algorithm_box(
        filename_base="algorithm_2_pseudocode",
        title_num="Algorithm 2:",
        title_text="Physical Payment HSM Appliance Capacity & Cluster Sizing Engine",
        inputs=[
            "Enterprise Banking Endpoints E = { (e_j, tps_j, c_j) } for j = 1, ..., M",
            "Hardware Sizing Parameters: Alpha_headroom = 0.20 (20%), Cost_unit = $1,200.00 / month",
            "HSM Physical Capacity: Cap_RSA2048 = 1,200 ops/s/HSM, Cap_MLDSA65 = 180 ops/s/HSM"
        ],
        outputs=[
            "Hardware Cluster Sizing Plan H = ( Units_leg, Units_pqc, Deficit_pct, Delta_Cost, Sizing_Verdict )"
        ],
        steps=[
            (1, "Compute Aggregate Peak Settlement Volume: TPS_total <- sum( tps_j for j in 1..M )", 0, False),
            (2, "Apply Enterprise Redundancy & High-Availability Headroom Factor:", 0, False),
            (3, "TPS_effective <- TPS_total * ( 1.0 + Alpha_headroom )", 1, False),
            (4, "// Calculate Required Physical HSM Appliance Units for Legacy vs PQC", 0, True),
            (5, "Units_leg <- max( 2, ceil( TPS_effective / Cap_RSA2048 ) )   // N+1 High Availability", 1, False),
            (6, "Units_pqc <- max( 2, ceil( TPS_effective / Cap_MLDSA65 ) )   // Due to 85% PQC signing deficit", 1, False),
            (7, "// Compute Cluster Hardware Deficit Percentage and Cost Delta", 0, True),
            (8, "Delta_units <- Units_pqc - Units_leg", 1, False),
            (9, "Deficit_pct <- ( Delta_units / Units_leg ) * 100.0          // e.g., +525% Hardware Deficit", 1, False),
            (10, "Cost_leg <- Units_leg * Cost_unit                         // Monthly Amortized Hardware Cost", 1, False),
            (11, "Cost_pqc <- Units_pqc * Cost_unit", 1, False),
            (12, "Delta_Cost <- Cost_pqc - Cost_leg", 1, False),
            (13, "// Evaluate Static Linear Planning Gap", 0, True),
            (14, "if Deficit_pct > 100.0 then", 1, True),
            (15, "Sizing_Verdict <- CRITICAL_HARDWARE_DEFICIT ( Static IT Linear Sizing Fails )", 2, False),
            (16, "else", 1, True),
            (17, "Sizing_Verdict <- COMPLIANT_LINEAR_SCALING", 2, False),
            (18, "end if", 1, True),
            (19, "H <- ( Units_leg, Units_pqc, Deficit_pct, Delta_Cost, Sizing_Verdict )", 1, False),
            (20, "return H", 0, True)
        ],
        complexity_text="Time Complexity: O(M) over endpoint cluster | Space Complexity: O(1) constant operational registers"
    )

    # -------------------------------------------------------------
    # ALGORITHM 3: Shor's & Grover's Quantum Risk Estimator
    # -------------------------------------------------------------
    draw_algorithm_box(
        filename_base="algorithm_3_pseudocode",
        title_num="Algorithm 3:",
        title_text="Quantum Factoring & Qubit Resource Estimation Engine",
        inputs=[
            "Cryptographic Asset A = ( Algo_Name, Algo_Type, Key_Bits b )",
            "Quantum Error-Correction Model: Gidney-Ekerå (2021) Surface Code (d = 27, p = 0.001)",
            "CRQC Attack Runway Baseline: Reference Year = 2035, Classical Lifespan X_years"
        ],
        outputs=[
            "Quantum Risk Profile R = ( Q_logical, Q_physical, Effective_Security, Runway_Years, Vulnerability )"
        ],
        steps=[
            (1, "if Algo_Type is 'RSA' then", 0, True),
            (2, "Q_logical <- 2 * b + 2                          // e.g., 4098 logical qubits for RSA-2048", 1, False),
            (3, "Q_physical <- Q_logical * 4880                  // ~20 Million physical qubits with surface code", 1, False),
            (4, "Effective_Security <- 0 bits                    // Shor's Polynomial Time Factorization: O(b^3)", 1, False),
            (5, "Runway_Years <- max( 3.0, round( 2035.0 - ( b / 400.0 ), 1 ) )", 1, False),
            (6, "Vulnerability <- CRITICAL_SHOR_VULNERABLE ( Immediate Harvest-Now-Decrypt-Later Threat )", 1, False),
            (7, "else if Algo_Type is 'ECC' or 'ECDSA' then", 0, True),
            (8, "Q_logical <- 6 * b                              // ~1536 logical qubits for P-256 elliptic curves", 1, False),
            (9, "Q_physical <- Q_logical * 3500                  // ~5.3 Million physical qubits", 1, False),
            (10, "Effective_Security <- 0 bits                    // Shor's Discrete Logarithm Algorithm", 1, False),
            (11, "Runway_Years <- max( 2.5, round( 2033.0 - ( b / 100.0 ), 1 ) )", 1, False),
            (12, "Vulnerability <- CRITICAL_SHOR_VULNERABLE", 1, False),
            (13, "else if Algo_Type is 'AES' or 'Symmetric' then", 0, True),
            (14, "Q_logical <- 0;  Q_physical <- 0               // Immune to Shor's Factorization", 1, False),
            (15, "Effective_Security <- b / 2                    // Grover's Quadratic Speedup: O(sqrt(2^b))", 1, False),
            (16, "if Effective_Security < 128 then", 1, True),
            (17, "Vulnerability <- VULNERABLE_GROVER_64BIT ( AES-128 Non-Compliant; Upgrade to AES-256 )", 2, False),
            (18, "else", 1, True),
            (19, "Vulnerability <- COMPLIANT_QUANTUM_RESISTANT ( AES-256 Retains 128-bit Post-Quantum Floor )", 2, False),
            (20, "end if", 1, True),
            (21, "end if", 0, True),
            (22, "R <- ( Q_logical, Q_physical, Effective_Security, Runway_Years, Vulnerability )", 0, False),
            (23, "return R", 0, True)
        ],
        complexity_text="Time Complexity: O(1) closed-form calculation | Space Complexity: O(1) static evaluation memory"
    )

    # -------------------------------------------------------------
    # ALGORITHM 4: Automated CBOM Asset Discovery & Agility Engine
    # -------------------------------------------------------------
    draw_algorithm_box(
        filename_base="algorithm_4_pseudocode",
        title_num="Algorithm 4:",
        title_text="Automated CBOM Discovery & Agility Compliance Engine",
        inputs=[
            "Cryptographic Inventory Dataset D = { (Algo_k, KeySize_k, Context_k) } for k = 1, ..., K",
            "PQC Compliance Standards: NIST FIPS 203 (ML-KEM), FIPS 204 (ML-DSA), FIPS 205 (SLH-DSA)",
            "Enterprise Roots of Trust: Server TPM 2.0, Payment HSM (PKCS#11), KMIP Key Vaults"
        ],
        outputs=[
            "Audited CBOM Matrix C_out and Phased Migration Strategy Roadmap S_roadmap"
        ],
        steps=[
            (1, "Initialize audited CBOM repository: C_out <- []", 0, False),
            (2, "for each entry d_k in Inventory Dataset D do", 0, True),
            (3, "Root_Trust <- DetectHardwareRoot( d_k.Context_k, ['TPM 2.0', 'Payment HSM', 'KMIP', 'KEK'] )", 1, False),
            (4, "if d_k.Algo_k in ['ML-KEM-768', 'ML-DSA-65', 'SLH-DSA-128s', 'AES-256-GCM'] then", 1, True),
            (5, "Status_k <- COMPLIANT_QUANTUM_SAFE", 2, False),
            (6, "Action_k <- 'Retain in Enterprise Production; Enforce Dual-Signature Validation'", 2, False),
            (7, "Phase_k <- 'Phase 4: Full Quantum Resistance'", 2, False),
            (8, "else if d_k.Algo_k in ['RSA-2048', 'RSA-4096', 'ECDSA-P256', 'ECDH-X25519'] then", 1, True),
            (9, "Status_k <- CRITICAL_NON_COMPLIANT ( Broken by Shor's Algorithm )", 2, False),
            (10, "Action_k <- 'Migrate to Hybrid ML-KEM-768 (KEM) & ML-DSA-65 (Signature)'", 2, False),
            (11, "Phase_k <- 'Phase 2: Hybrid Ingress & CA Upgrade (2026-2028)'", 2, False),
            (12, "else if d_k.Algo_k in ['AES-128-GCM', 'SHA-256', '3DES'] then", 1, True),
            (13, "Status_k <- VULNERABLE_MARGINAL ( Grover 64-bit / Legacy Deprecation )", 2, False),
            (14, "Action_k <- 'Re-key Database DEKs with AES-256; Migrate Hashing to SHA-384'", 2, False),
            (15, "Phase_k <- 'Phase 1: Discovery & Deprecation (2025-2026)'", 2, False),
            (16, "end if", 1, True),
            (17, "Record_k <- ( d_k.Algo_k, d_k.KeySize_k, Root_Trust, Status_k, Action_k, Phase_k )", 1, False),
            (18, "C_out.append( Record_k )", 1, False),
            (19, "end for", 0, True),
            (20, "S_roadmap <- GroupByPhase( C_out )             // CycloneDX 1.6 Compliant CBOM", 0, False),
            (21, "return ( C_out, S_roadmap )", 0, True)
        ],
        complexity_text="Time Complexity: O(K) linear sweep over K cryptographic records | Space Complexity: O(K) for CBOM output"
    )

if __name__ == "__main__":
    generate_all()
