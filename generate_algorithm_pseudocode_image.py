"""
Generates an IEEE/ACM Dissertation-Style Algorithm Box Image (Algorithm 1)
with EXTRA LARGE, HIGH-IMPACT typography (24pt Title, 18pt Headers, 16.5pt Body Code).
"""

import os
import matplotlib
matplotlib.rcParams['svg.fonttype'] = 'none'
import matplotlib.pyplot as plt

TNR = 'Times New Roman'

def render_algorithm_image():
    # 20 x 25 inches canvas at 300 DPI (High Resolution & Extra Large Text)
    fig, ax = plt.subplots(figsize=(20, 25), dpi=300)
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

    # 1. Outer Frame & Header Bar
    # Top heavy double rules
    ax.plot([3, 97], [99.0, 99.0], color='#002060', lw=4.5)
    ax.plot([3, 97], [98.0, 98.0], color='#002060', lw=2.0)
    
    # Title with Extra Large fonts
    txt(3.5, 94.8, "Algorithm 1:", fs=24.0, bold=True, color='#002060')
    txt(21.0, 94.8, "PQC Network Bandwidth & Latency Overhead Sizing Engine", fs=21.0, bold=True, color='#0F172A')
    
    # Mid rule below title
    ax.plot([3, 97], [91.8, 91.8], color='#002060', lw=2.5)
    
    # 2. Input / Output Block
    curr_y = 88.2
    txt(4.5, curr_y, "Input:", fs=18.5, bold=True, color='#002060')
    txt(14.0, curr_y, "API Traces T = { (e_i, C_i, tps_i, L_base,i) } for i = 1, ..., N", fs=17.5, italic=True)
    
    curr_y -= 3.5
    txt(14.0, curr_y, "Target PQC Primitives: KEM K (e.g., ML-KEM-768), Signature S (e.g., ML-DSA-65)", fs=17.0)
    
    curr_y -= 3.5
    txt(14.0, curr_y, "Hardware Specs: PubKeySize(c), SigSize(c), Ethernet MTU = 1500 bytes", fs=17.0)
    
    curr_y -= 3.5
    txt(14.0, curr_y, "Operational Constraints: Bank SLA Limit = 50.0 ms, Expansion Threshold = 3.0x", fs=17.0)
    
    curr_y -= 3.8
    txt(4.5, curr_y, "Output:", fs=18.5, bold=True, color='#002060')
    txt(14.0, curr_y, "Sizing Assessment Matrix M = { (e_i, tps_i, BW_leg, BW_pqc, Gamma_i, Phi_i, L_pqc, Risk_i) }", fs=17.5, italic=True)
    
    # Separator rule between headers and algorithm body
    curr_y -= 2.8
    ax.plot([3, 97], [curr_y, curr_y], color='#94A3B8', lw=1.8)
    
    # 3. Algorithm Body (Step by Step with Line Numbers)
    steps = [
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
    ]
    
    curr_y -= 3.5
    for num, code, indent, is_keyword in steps:
        # Line number (bold slate)
        txt(4.5, curr_y, f"{num:2d}:", fs=16.0, bold=True, color='#475569')
        
        # Indentation offset
        x_indent = 10.5 + (indent * 4.2)
        
        if code.startswith("//"):
            txt(x_indent, curr_y, code, fs=16.0, bold=False, color='#059669', italic=True)
        elif "CRITICAL_RISK" in code:
            txt(x_indent, curr_y, code, fs=16.5, bold=True, color='#DC2626')
        elif "COMPLIANT_MANAGED" in code:
            txt(x_indent, curr_y, code, fs=16.5, bold=True, color='#16A34A')
        elif is_keyword:
            txt(x_indent, curr_y, code, fs=16.8, bold=True, color='#002060')
        else:
            txt(x_indent, curr_y, code, fs=16.5, bold=False, color='#0F172A')
            
        curr_y -= 2.45

    # Bottom Heavy Rule
    curr_y += 0.5
    ax.plot([3, 97], [curr_y, curr_y], color='#002060', lw=3.5)

    # Complexity Badge at Bottom
    curr_y -= 2.8
    txt(4.5, curr_y, "Complexity Analysis:", fs=16.0, bold=True, color='#002060')
    txt(23.0, curr_y, "Time Complexity: O(N) linear scan over API endpoints | Space Complexity: O(N) for assessment matrix M", fs=15.5, italic=True, color='#334155')

    plt.tight_layout()
    
    base_dir = os.path.dirname(os.path.abspath(__file__))
    png_path = os.path.join(base_dir, "algorithm_1_pseudocode.png")
    svg_path = os.path.join(base_dir, "algorithm_1_pseudocode.svg")
    
    plt.savefig(png_path, dpi=300, bbox_inches='tight', facecolor='#FFFFFF')
    plt.savefig(svg_path, bbox_inches='tight', facecolor='#FFFFFF')
    plt.close('all')
    
    print(f"Generated successfully with EXTRA LARGE font sizes:\n1. PNG: {png_path}\n2. SVG: {svg_path}")

if __name__ == "__main__":
    render_algorithm_image()
