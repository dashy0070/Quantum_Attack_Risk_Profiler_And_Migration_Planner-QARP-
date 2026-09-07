"""
Script to generate high-resolution, publication-grade Algorithm Flowchart
with LARGE, easily readable fonts, prominent boxes, and clear arrows.
"""

import matplotlib
matplotlib.rcParams['svg.fonttype'] = 'none'
import matplotlib.pyplot as plt
import matplotlib.patches as patches

TNR = 'Times New Roman'

def create_flowchart():
    # Large 16 x 22 inch canvas at 300 DPI
    fig, ax = plt.subplots(figsize=(16, 22), dpi=300)
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 130)
    ax.axis('off')
    
    # Background
    fig.patch.set_facecolor('#F8FAFC')
    ax.set_facecolor('#F8FAFC')

    def txt(x, y, s, fs=13.0, bold=False, color='#0F172A', ha='center', va='center', italic=False):
        ax.text(x, y, s, fontsize=fs, color=color, ha=ha, va=va,
                fontweight='bold' if bold else 'normal',
                fontstyle='italic' if italic else 'normal',
                fontfamily=TNR)

    def draw_box(x, y, w, h, title, lines, header_bg, body_bg='#FFFFFF', border_col='#1E293B', is_diamond=False):
        if is_diamond:
            diamond = patches.Polygon([
                [x + w/2, y + h],
                [x + w, y + h/2],
                [x + w/2, y],
                [x, y + h/2]
            ], closed=True, facecolor=body_bg, edgecolor=border_col, linewidth=2.5, zorder=3)
            ax.add_patch(diamond)
            txt(x + w/2, y + h/2 + 2.0, title, fs=14.5, bold=True, color='#0F172A')
            for i, line in enumerate(lines):
                txt(x + w/2, y + h/2 - 1.8 - (i * 2.8), line, fs=13.0, bold=True if "Bank SLA" in line else False, color='#334155')
        else:
            card = patches.FancyBboxPatch(
                (x, y), w, h, boxstyle='round,pad=0.6,rounding_size=1.5',
                facecolor=body_bg, edgecolor=border_col, linewidth=2.2, zorder=2)
            ax.add_patch(card)
            
            header_h = 4.8
            banner = patches.FancyBboxPatch(
                (x, y + h - header_h), w, header_h, boxstyle='round,pad=0.2,rounding_size=1.2',
                facecolor=header_bg, edgecolor=border_col, linewidth=1.2, zorder=3)
            ax.add_patch(banner)
            txt(x + w/2, y + h - header_h/2, title, fs=14.5, bold=True, color='white')
            
            start_y = y + h - header_h - 3.2
            for i, line in enumerate(lines):
                txt(x + w/2, start_y - (i * 2.9), line, fs=12.5, bold=False, color='#0F172A')

    def draw_arrow(x1, y1, x2, y2, label=None, label_side='right', col='#334155'):
        ax.annotate('', xy=(x2, y2), xytext=(x1, y1),
                    arrowprops=dict(arrowstyle="-|>", color=col, lw=2.6, mutation_scale=20),
                    zorder=4)
        if label:
            lx = (x1 + x2) / 2 + (3.2 if label_side=='right' else -3.2)
            ly = (y1 + y2) / 2
            txt(lx, ly, label, fs=13.0, bold=True, color=col)

    # -------------------------------------------------------------
    # 0. MAIN TITLE & SUBTITLE
    # -------------------------------------------------------------
    outer_frame = patches.FancyBboxPatch(
        (2, 2), 96, 126, boxstyle='round,pad=0.8,rounding_size=1.8',
        facecolor='#FFFFFF', edgecolor='#CBD5E1', linewidth=2.0, zorder=1)
    ax.add_patch(outer_frame)

    title_banner = patches.FancyBboxPatch(
        (4, 117), 92, 9.5, boxstyle='round,pad=0.4,rounding_size=1.2',
        facecolor='#002060', edgecolor='#002060', linewidth=1.2, zorder=2)
    ax.add_patch(title_banner)
    txt(50, 123.5, "Algorithm 1: PQC Sizing & Network Overhead Profiler for Banking APIs", fs=17.5, bold=True, color='white')
    txt(50, 119.8, "Mathematical & Network Performance Modeling Pipeline (REST / TLS 1.3 / ISO 20022)", fs=13.0, italic=True, color='#E2E8F0')

    # -------------------------------------------------------------
    # STAGE 1: INPUT / TELEMETRY INGESTION
    # -------------------------------------------------------------
    draw_box(
        x=16, y=101, w=68, h=13.5,
        title="Step 1: Telemetry & Migration Parameter Ingestion",
        lines=[
            "• Ingest API Trace: { Endpoint, Legacy Algorithm (RSA/ECDSA), TPS, Payload Size }",
            "• Ingest Target NIST PQC Parameters: { Target KEM = ML-KEM-768, Target Signature = ML-DSA-65 }",
            "• Query PQC Benchmark Specification Matrix (liboqs / NIST FIPS 203 & 204)"
        ],
        header_bg='#1E3A8A'
    )

    draw_arrow(50, 101, 50, 93)

    # -------------------------------------------------------------
    # STAGE 2: CRYPTOGRAPHIC SIZING EXTRACTION
    # -------------------------------------------------------------
    draw_box(
        x=16, y=79.5, w=68, h=13.5,
        title="Step 2: Cryptographic Key & Signature Size Lookup",
        lines=[
            "• Classical Size:   S_legacy = PubKey_size(C_leg) + Sig_size(C_leg)     [e.g., 256B + 256B = 512 B]",
            "• PQC Target Size:  S_pqc = PubKey_size(ML-KEM) + Sig_size(ML-DSA)   [e.g., 1184B + 3300B = 4484 B]",
            "• Handshake Overhead Delta:  Delta_S = S_pqc - S_legacy  (+775.8% payload expansion)"
        ],
        header_bg='#0284C7'
    )

    draw_arrow(50, 79.5, 50, 71.5)

    # -------------------------------------------------------------
    # STAGE 3: THROUGHPUT & BANDWIDTH EXPANSION COMPUTATION
    # -------------------------------------------------------------
    draw_box(
        x=16, y=58, w=68, h=13.5,
        title="Step 3: Throughput & Network Bandwidth Expansion Computation",
        lines=[
            "• Legacy Bandwidth:   BW_legacy = [ TPS * S_legacy ] / (1024 * 1024)   [MB/s]",
            "• Post-Quantum Bandwidth: BW_pqc = [ TPS * S_pqc ] / (1024 * 1024)      [MB/s]",
            "• Bandwidth Expansion Factor:  Gamma = BW_pqc / max(1.0, BW_legacy)"
        ],
        header_bg='#0D9488'
    )

    draw_arrow(50, 58, 50, 50)

    # -------------------------------------------------------------
    # STAGE 4: PACKET FRAGMENTATION & LATENCY ESTIMATION
    # -------------------------------------------------------------
    draw_box(
        x=16, y=36.5, w=68, h=13.5,
        title="Step 4: TCP MTU Packet Fragmentation & Latency Overhead Modeling",
        lines=[
            "• Compute MTU Packet Count:   Phi_pkts = ceil( S_pqc / 1500 bytes )   (1 packet -> 3 packets)",
            "• Model Latency Inflation:    Delta_T_lat = ( S_pqc / 1500 ) * 1.5 ms   [+4.48 ms overhead]",
            "• Projected Endpoint Latency: T_total = T_base + Delta_T_lat"
        ],
        header_bg='#D97706'
    )

    draw_arrow(50, 36.5, 50, 29)

    # -------------------------------------------------------------
    # STAGE 5: CONDITIONAL SLA & RISK DECISION DIAMOND
    # -------------------------------------------------------------
    draw_box(
        x=23, y=16.5, w=54, h=12.5,
        title="SLA Breach & Risk Evaluation",
        lines=[
            "Is Gamma > 3.0x  OR",
            "T_total > Bank SLA (50.0 ms)?"
        ],
        header_bg='',
        body_bg='#FEF3C7',
        border_col='#B45309',
        is_diamond=True
    )

    # Branches from Diamond
    # YES Branch (Left to Alert)
    draw_arrow(23, 22.8, 14, 22.8, label="YES", label_side='left', col='#DC2626')
    draw_arrow(14, 22.8, 14, 15.5, col='#DC2626')

    # NO Branch (Right to Compliant)
    draw_arrow(77, 22.8, 86, 22.8, label="NO", label_side='right', col='#16A34A')
    draw_arrow(86, 22.8, 86, 15.5, col='#16A34A')

    # Alert Box (Left)
    draw_box(
        x=4, y=4.5, w=26, h=11,
        title="[!] CRITICAL RISK ALERT",
        lines=[
            "• Multi-Packet TLS Latency Spike",
            "• Sizing Deficit: Expand HSMs (+525%)",
            "• Priority PQC Migration Track"
        ],
        header_bg='#DC2626',
        body_bg='#FEF2F2',
        border_col='#DC2626'
    )

    # Compliant Box (Right)
    draw_box(
        x=70, y=4.5, w=26, h=11,
        title="[OK] MANAGED COMPLIANCE",
        lines=[
            "• Handshake Within SLA (<50ms)",
            "• Standard Buffer Allocation",
            "• Low/Moderate Migration Urgency"
        ],
        header_bg='#16A34A',
        body_bg='#F0FDF4',
        border_col='#16A34A'
    )

    # Center Down Arrow to Output
    draw_arrow(50, 16.5, 50, 15.5)

    # Output Aggregator Box (Center)
    draw_box(
        x=33, y=4.5, w=34, h=11,
        title="Step 5: Output Report Record",
        lines=[
            "• Output Vector: { Endpoint, TPS, BW_leg,",
            "   BW_pqc, Gamma_scale, Delta_T, Status }",
            "• Stream to Streamlit UI & Capstone Engine"
        ],
        header_bg='#475569',
        body_bg='#F8FAFC',
        border_col='#334155'
    )

    plt.tight_layout()
    
    png_path = "pqc_overhead_algorithm_flowchart.png"
    svg_path = "pqc_overhead_algorithm_flowchart.svg"
    
    plt.savefig(png_path, dpi=300, bbox_inches='tight')
    plt.savefig(svg_path, bbox_inches='tight')
    plt.close()
    
    print(f"Generated flowchart successfully with enlarged font sizes:\n1. PNG: {png_path}\n2. SVG: {svg_path}")

if __name__ == "__main__":
    create_flowchart()
