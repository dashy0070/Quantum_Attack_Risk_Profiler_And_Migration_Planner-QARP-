"""
Generates the exact infographic-style coloured image for:
'PROJECT DELIVERABLES & OBJECTIVE ACHIEVEMENT MATRIX' (Capstone 2)
with EXTRA LARGE, HIGH-CONTRAST TYPOGRAPHY for presentation slides / projector view.
"""

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Rectangle

def generate_matrix_infographic_large():
    # 16:9 widescreen presentation canvas at 300 DPI
    fig, ax = plt.subplots(figsize=(16, 9), dpi=300)
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    ax.axis('off')

    fig.patch.set_facecolor('#F8FAFC')
    ax.set_facecolor('#F8FAFC')

    font_family = 'DejaVu Sans'

    # =========================================================================
    # 1. TOP HEADER BANNER (Royal Blue)
    # =========================================================================
    banner_box = FancyBboxPatch(
        (1.5, 90.5), 97, 8.0,
        boxstyle="round,pad=0.5,rounding_size=1.2",
        facecolor='#0B3C9B',
        edgecolor='#072A6F',
        linewidth=1.8
    )
    ax.add_patch(banner_box)

    ax.text(
        4.5, 94.5,
        "PROJECT DELIVERABLES & OBJECTIVE ACHIEVEMENT MATRIX",
        fontsize=20.5,
        fontweight='bold',
        color='#FFFFFF',
        fontfamily=font_family,
        va='center',
        ha='left'
    )

    ax.text(
        96.5, 94.5,
        "M.Tech Capstone-2",
        fontsize=13.5,
        fontweight='bold',
        color='#93C5FD',
        fontfamily=font_family,
        va='center',
        ha='right'
    )

    # =========================================================================
    # 2. COLUMN HEADERS (Dark Navy Bar)
    # =========================================================================
    hdr_box = Rectangle((1.5, 85.0), 97, 5.0, facecolor='#091A36', edgecolor='none')
    ax.add_patch(hdr_box)

    ax.text(8.0, 87.5, "Phase & Objective", fontsize=13.5, fontweight='bold', color='#FFFFFF', fontfamily=font_family, va='center', ha='center')
    ax.text(45.5, 87.5, "Implementation & Deliverable Evidence", fontsize=13.5, fontweight='bold', color='#FFFFFF', fontfamily=font_family, va='center', ha='center')
    ax.text(82.5, 87.5, "Chapter", fontsize=13.5, fontweight='bold', color='#FFFFFF', fontfamily=font_family, va='center', ha='center')
    ax.text(92.8, 87.5, "Status", fontsize=13.5, fontweight='bold', color='#FFFFFF', fontfamily=font_family, va='center', ha='center')

    # =========================================================================
    # 3. ROWS DATA WITH LARGE FONTS & CRISP WRAPPING
    # =========================================================================
    rows = [
        {
            "obj_num": "Objective 1",
            "phase": "(Design Phase)",
            "evidence": [
                "• Formulated comprehensive STRIDE-Quantum Threat Model across four trust boundaries (TB-1 to TB-4).",
                "• Integrated Gidney–Ekerå math: factoring 2048-bit RSA requires 20M physical qubits in 8 hours.",
                "• Established automated cryptographic triage rules for symmetric ciphers under Grover's algorithm."
            ],
            "chapter": "Ch. 7",
            "status": "Fully Met"
        },
        {
            "obj_num": "Objective 2",
            "phase": "(Build Phase)",
            "evidence": [
                "• Constructed high-throughput streaming parser & CycloneDX 1.6 CBOM generator for live traffic.",
                "• Successfully ingests mixed banking payloads: REST/JSON logs, passive Zeek TLS 1.3 telemetry,",
                "  and structured ISO 20022 financial clearing messages (pacs.008 & pain.001) in real time."
            ],
            "chapter": "Ch. 8",
            "status": "Fully Met"
        },
        {
            "obj_num": "Objective 3",
            "phase": "(Test Phase)",
            "evidence": [
                "• Executed physical cryptographic benchmarks using Open Quantum Safe (liboqs) on local hardware.",
                "• Proved NIST FIPS 203 ML-KEM-768 key encapsulation is fast (37.2 μs) for data-in-transit.",
                "• Discovered NIST FIPS 204 ML-DSA-65 signing (385.4 μs) is >9x slower than ECDSA P-256 (42.1 μs)."
            ],
            "chapter": "Ch. 9",
            "status": "Fully Met"
        },
        {
            "obj_num": "Objective 4",
            "phase": "(Validate Phase)",
            "evidence": [
                "• Modelled 1,500B Ethernet MTU: PQC handshakes split into 3–4 TCP packet fragments (+6.6 ms latency).",
                "• Validated hardware throughput bottlenecks under simulated banking settlement loads up to 10,000 TPS.",
                "• Proved traditional linear IT sizing underestimates physical Payment HSM cluster capacity by 522.2% (56 vs 9)."
            ],
            "chapter": "Ch. 9 & 10",
            "status": "Fully Met"
        },
        {
            "obj_num": "Objective 5",
            "phase": "(Deploy Phase)",
            "evidence": [
                "• Packaged end-to-end framework into an interactive, open-source Streamlit dashboard (app.py).",
                "• Integrated automated CBOM generation, STRIDE scoring, and dynamic enterprise HSM cost engine.",
                "• Published fully documented codebase, synthetic test generators, and test suites on public GitHub."
            ],
            "chapter": "Ch. 6 & 8",
            "status": "Fully Met"
        }
    ]

    # Row positioning
    row_height = 16.0
    y_start = 85.0

    for idx, r in enumerate(rows):
        y_top = y_start - (idx * row_height)
        y_bottom = y_top - row_height
        y_center = (y_top + y_bottom) / 2.0

        # Alternating row background
        bg_color = '#FFFFFF' if idx % 2 == 0 else '#F3F6FA'
        row_rect = Rectangle((1.5, y_bottom), 97, row_height, facecolor=bg_color, edgecolor='none')
        ax.add_patch(row_rect)

        # Bottom row border
        ax.plot([1.5, 98.5], [y_bottom, y_bottom], color='#CBD5E1', lw=1.2)

        # Col 1: Objective & Phase (Large Fonts)
        ax.text(8.0, y_center + 2.6, r["obj_num"], fontsize=15.0, fontweight='bold', color='#0B3C9B', fontfamily=font_family, va='center', ha='center')
        ax.text(8.0, y_center - 2.6, r["phase"], fontsize=12.0, fontweight='bold', color='#475569', fontfamily=font_family, va='center', ha='center')

        # Col 2: Evidence Lines (Much Larger Text: 12.0pt)
        ev_y = y_center + 3.8
        for line in r["evidence"]:
            ax.text(16.5, ev_y, line, fontsize=11.6, color='#0F172A', fontfamily=font_family, va='center', ha='left')
            ev_y -= 3.8

        # Col 3: Chapter (Large Font: 13.5pt)
        ax.text(82.5, y_center, r["chapter"], fontsize=13.5, fontweight='bold', color='#0F172A', fontfamily=font_family, va='center', ha='center')

        # Col 4: Status Badge (Larger Green Rounded Pill Badge)
        badge_w, badge_h = 8.8, 5.2
        badge_box = FancyBboxPatch(
            (92.8 - badge_w/2, y_center - badge_h/2),
            badge_w, badge_h,
            boxstyle="round,pad=0.3,rounding_size=1.4",
            facecolor='#E8F8F0',
            edgecolor='#27AE60',
            linewidth=1.8
        )
        ax.add_patch(badge_box)
        ax.text(92.8, y_center, r["status"], fontsize=12.2, fontweight='bold', color='#1E824C', fontfamily=font_family, va='center', ha='center')

    # Outer border around entire table
    table_bottom = y_start - (len(rows) * row_height)
    outer_box = Rectangle((1.5, table_bottom), 97, (len(rows) * row_height) + 5.0, facecolor='none', edgecolor='#0A2540', linewidth=1.8)
    ax.add_patch(outer_box)

    # Vertical column dividers
    for x_div in [15.0, 77.5, 87.5]:
        ax.plot([x_div, x_div], [table_bottom, 85.0], color='#E2E8F0', lw=1.2)

    # Save outputs
    output_png = "project_deliverables_matrix.png"
    plt.tight_layout()
    plt.savefig(output_png, dpi=300, bbox_inches='tight', facecolor=fig.get_facecolor(), edgecolor='none')
    plt.close()
    print(f"Successfully generated updated LARGE-FONT matrix infographic: {output_png}")

if __name__ == "__main__":
    generate_matrix_infographic_large()
