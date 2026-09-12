"""
Generates the Testing & Validation Presentation Slide for Capstone 2:
'TESTING, VALIDATION & EMPIRICAL BENCHMARKING'
Matches the 3-pillar card layout + bottom 4-column KPI metric bar format.
Outputs both:
1. capstone2_testing_validation.svg (Fully editable vector SVG)
2. capstone2_testing_validation.png (300 DPI high-res presentation image)
"""

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Rectangle

def generate_testing_validation_slide():
    # 16:9 widescreen presentation canvas at 300 DPI
    fig, ax = plt.subplots(figsize=(18, 10.5), dpi=300)
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    ax.axis('off')

    fig.patch.set_facecolor('#FFFFFF')
    ax.set_facecolor('#FFFFFF')

    font_family = 'DejaVu Sans'

    # =========================================================================
    # 1. TOP HEADER BANNER (Institutional Branding & Slide Title)
    # =========================================================================
    ax.text(2.0, 96.5, "Testing & Validation", fontsize=28, fontweight='bold', color='#1E293B', fontfamily=font_family, va='center')
    
    # REVA University Logo Text
    ax.text(98.0, 96.5, "REVA UNIVERSITY", fontsize=15, fontweight='bold', color='#D9531E', fontfamily=font_family, va='center', ha='right')
    ax.text(98.0, 93.8, "M.Tech Capstone-2 Project", fontsize=10, color='#64748B', fontfamily=font_family, va='center', ha='right')

    # Accent timeline line
    ax.plot([2.0, 98.0], [92.0, 92.0], color='#CBD5E1', lw=1.2)
    ax.plot([47.5, 52.5], [92.0, 92.0], color='#7030A0', lw=3.0)
    circle = plt.Circle((50.0, 92.0), 0.7, facecolor='#7030A0', edgecolor='#FFFFFF', lw=1.5, zorder=5)
    ax.add_patch(circle)

    # Main Royal Blue Banner
    main_banner = FancyBboxPatch(
        (1.5, 84.5), 97.0, 5.8,
        boxstyle="round,pad=0.3,rounding_size=0.8",
        facecolor='#0B3C9B',
        edgecolor='#072A6F',
        linewidth=1.5
    )
    ax.add_patch(main_banner)
    ax.text(3.5, 87.4, "EMPIRICAL BENCHMARKING, MTU NETWORK PHYSICS & CAPACITY VALIDATION", fontsize=14.5, fontweight='bold', color='#FFFFFF', fontfamily=font_family, va='center')
    ax.text(96.5, 87.4, "Physical liboqs Timings → MTU Packet Fragmentation → 10,000 TPS HSM Deficit Modeling", fontsize=9.2, color='#93C5FD', fontfamily=font_family, va='center', ha='right')

    # =========================================================================
    # 2. THREE PILLAR COLUMNS (Cards 1, 2, 3)
    # =========================================================================
    card_w = 31.0
    card_h = 63.5
    card_y = 18.5

    def draw_testing_card(x, y, w, h, title, badge_txt, border_col, badge_col, bg_tint, sections, bottom_check):
        # Card Background
        card = FancyBboxPatch(
            (x, y), w, h,
            boxstyle="round,pad=0.4,rounding_size=0.8",
            facecolor='#FFFFFF',
            edgecolor=border_col,
            linewidth=2.0
        )
        ax.add_patch(card)

        # Header Title (Purple)
        ax.text(x + 1.8, y + h - 2.8, title, fontsize=13.0, fontweight='bold', color='#7030A0', fontfamily=font_family, va='center')

        # Badge on Right
        badge_w = len(badge_txt) * 0.46 + 2.4
        badge_box = FancyBboxPatch(
            (x + w - badge_w - 1.8, y + h - 3.9), badge_w, 2.2,
            boxstyle="round,pad=0.2,rounding_size=0.4",
            facecolor=badge_col,
            edgecolor='none'
        )
        ax.add_patch(badge_box)
        ax.text(x + w - badge_w/2 - 1.8, y + h - 2.8, badge_txt, fontsize=8.2, fontweight='bold', color='#FFFFFF', fontfamily=font_family, va='center', ha='center')

        # Header Divider
        ax.plot([x + 1.5, x + w - 1.5], [y + h - 5.2, y + h - 5.2], color='#E2E8F0', lw=1.2)

        # Sections & Bullets
        curr_y = y + h - 7.5
        for sec_title, lines in sections:
            ax.text(x + 1.8, curr_y, f"• {sec_title}", fontsize=9.6, fontweight='bold', color='#0F172A', fontfamily=font_family, va='top')
            curr_y -= 2.2
            for line in lines:
                ax.text(x + 3.2, curr_y, line, fontsize=8.6, color='#334155', fontfamily=font_family, va='top')
                curr_y -= 2.1
            curr_y -= 1.6

        # Bottom Checkmark Callout Box
        callout_h = 7.5
        callout_box = FancyBboxPatch(
            (x + 1.8, y + 2.0), w - 3.6, callout_h,
            boxstyle="round,pad=0.3,rounding_size=0.6",
            facecolor=bg_tint,
            edgecolor=border_col,
            linewidth=1.3
        )
        ax.add_patch(callout_box)
        
        c_title, c_desc = bottom_check
        ax.text(x + 3.2, y + 2.0 + callout_h - 2.2, f"✓ {c_title}", fontsize=9.2, fontweight='bold', color='#0F172A', fontfamily=font_family, va='center')
        ax.text(x + 3.2, y + 2.0 + 2.4, c_desc, fontsize=8.4, color='#334155', fontfamily=font_family, va='center')

    # --- CARD 1: Physical liboqs Benchmarking (Blue/Purple Theme) ---
    draw_testing_card(
        1.5, card_y, card_w, card_h,
        "1. Cryptographic Benchmarking", "LIBOQS FIPS",
        '#0B3C9B', '#0B3C9B', '#EFF6FF',
        [
            ("Physical Hardware Testbed:", [
                "Workstation host running compiled liboqs C library",
                "Benchmarked NIST FIPS 203 (KEM) & FIPS 204 (DSA)"
            ]),
            ("Key Encapsulation (ML-KEM-768):", [
                "KeyGen: 28.4 μs | Encapsulation: 37.2 μs | Decap: 32.1 μs",
                "Lightweight overhead; near-parity with classical ECDHE"
            ]),
            ("Digital Signatures Bottleneck (ML-DSA-65):", [
                "Signing takes 385.4 μs (>9x slower than ECDSA at 42.1 μs)",
                "Verification takes 162.3 μs (matrix polynomial overhead)",
                "Signature size: 3,300 B (44x larger than classical ECDSA)"
            ]),
            ("Baseline Comparison (RSA-2048):", [
                "RSA-2048 signing: 1,111 ops/sec per physical appliance",
                "ML-DSA-65 signing drops to only ~180 ops/sec per unit"
            ])
        ],
        ("Benchmark Ground Truth:", "Proves transaction signing—not key exchange—is the primary bottleneck.")
    )

    # --- CARD 2: Network MTU & Latency Simulation (Teal/Green Theme) ---
    draw_testing_card(
        34.5, card_y, card_w, card_h,
        "2. Transport & MTU Physics", "PACKET DYNAMICS",
        '#117A65', '#117A65', '#F0FDFA',
        [
            ("1,500-Byte Ethernet MTU Boundary:", [
                "Standard Ethernet Maximum Transmission Unit = 1,500B",
                "Classical RSA/ECC handshakes easily fit in a single packet"
            ]),
            ("TCP Packet Fragmentation:", [
                "ML-DSA-65 & ML-KEM-768 expand handshake > 4,484 bytes",
                "Forces TCP stack to split handshake into 3 to 4 fragments"
            ]),
            ("Induced Latency Overhead:", [
                "Packet fragmentation introduces an empirical +6.6 ms penalty",
                "Under WAN jitter, latency pushes toward the 50 ms SLA ceiling"
            ]),
            ("Middlebox Drop Simulation:", [
                "Tested legacy enterprise middleboxes, proxies, and firewalls",
                "Proved that stateful firewalls drop fragmented PQC packets"
            ])
        ],
        ("SLA Boundary Verified:", "Models packet inflation risks before deploying on live banking WAN rails.")
    )

    # --- CARD 3: Hardware Capacity & Deficit (Red/Amber Theme) ---
    draw_testing_card(
        67.5, card_y, card_w, card_h,
        "3. Capacity & Deficit Validation", "ENTERPRISE SIZING",
        '#C00000', '#C00000', '#FEF2F2',
        [
            ("Simulated Settlement Loads:", [
                "Workload stress tests from 1,000 to 10,000 TPS",
                "Evaluated core banking payment switches & ISO 20022"
            ]),
            ("Failure of Traditional IT Models:", [
                "Static linear worksheets assume 1:1 hardware scaling",
                "Traditional models budget only 9 HSMs for 10,000 TPS"
            ]),
            ("The 522.2% Hardware Capacity Deficit:", [
                "ML-DSA-65 hardware limits require 56 physical HSM units",
                "Reveals an unbudgeted +522.2% capacity shortfall (56 vs 9)"
            ]),
            ("Financial Budget Variance:", [
                r"Creates an unbudgeted \$56,400.00/month operational variance",
                r"Totals \$2,030,400.00 (\$2.03M) unbudgeted 3-year refresh gap"
            ])
        ],
        ("Capacity Validated:", "Replaces flawed linear sizing with workload-tested hardware budgets.")
    )

    # =========================================================================
    # 3. BOTTOM KPI METRIC SUMMARY BAR (4 Columns)
    # =========================================================================
    kpi_bar = FancyBboxPatch(
        (1.5, 2.0), 97.0, 14.5,
        boxstyle="round,pad=0.3,rounding_size=0.8",
        facecolor='#F8FAFC',
        edgecolor='#CBD5E1',
        linewidth=1.5
    )
    ax.add_patch(kpi_bar)

    kpis = [
        ("385.4 μs", "ML-DSA-65 Signing Latency", ">9x slower than ECDSA P-256", '#7030A0'),
        ("3–4 Packets", "TCP MTU Fragmentation", "Splits across 1,500B Ethernet MTU", '#117A65'),
        ("+522.2%", "Payment HSM Deficit", "56 vs. 9 units at 10,000 TPS", '#C00000'),
        (r"\$2.03 Million", "Unbudgeted 3-Year Gap", r"\$56,400/month operational variance", '#0B3C9B')
    ]

    col_w = 97.0 / 4.0
    for idx, (metric, lbl, sub, col) in enumerate(kpis):
        cx = 1.5 + (idx * col_w) + (col_w / 2.0)
        
        # Metric Number (Large Bold)
        ax.text(cx, 11.5, metric, fontsize=17.0, fontweight='bold', color=col, fontfamily=font_family, va='center', ha='center')
        # Metric Label
        ax.text(cx, 7.5, lbl, fontsize=9.8, fontweight='bold', color='#0F172A', fontfamily=font_family, va='center', ha='center')
        # Sub-caption
        ax.text(cx, 4.5, sub, fontsize=8.4, color='#64748B', fontfamily=font_family, va='center', ha='center')

        # Vertical Divider
        if idx < 3:
            div_x = 1.5 + ((idx + 1) * col_w)
            ax.plot([div_x, div_x], [3.5, 15.0], color='#E2E8F0', lw=1.2)

    # Save PNG and SVG
    output_png = "capstone2_testing_validation.png"
    output_svg = "capstone2_testing_validation.svg"
    plt.tight_layout()
    plt.savefig(output_png, dpi=300, bbox_inches='tight', facecolor=fig.get_facecolor(), edgecolor='none')
    plt.savefig(output_svg, format='svg', bbox_inches='tight', facecolor=fig.get_facecolor(), edgecolor='none')
    plt.close()
    print(f"Successfully generated: {output_png} and {output_svg}")

if __name__ == "__main__":
    generate_testing_validation_slide()
