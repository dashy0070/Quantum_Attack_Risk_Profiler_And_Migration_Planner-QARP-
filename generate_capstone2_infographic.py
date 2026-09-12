import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
import os

def create_capstone2_infographic():
    # Figure size: 16 x 8 inches (2:1 aspect ratio, exact match to user's supplied infographic layout)
    fig, ax = plt.subplots(figsize=(16, 8), dpi=300)
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 50)
    ax.axis('off')
    fig.patch.set_facecolor('#FFFFFF')

    font_family = 'sans-serif'

    # Card layout coordinates
    card_y = 12.0
    card_w = 31.6
    card_h = 36.8

    # Helper function to draw each card
    def draw_card(x, y, w, h, border_color, bg_color, header_color, title, badge_text, badge_bg):
        # Outer Card Box
        card_box = FancyBboxPatch(
            (x, y), w, h,
            boxstyle="round,pad=0.3,rounding_size=0.8",
            facecolor=bg_color,
            edgecolor=border_color,
            linewidth=1.8
        )
        ax.add_patch(card_box)

        # Title
        ax.text(x + 1.2, y + h - 2.5, title, fontsize=12.2, fontweight='bold', color=header_color, fontfamily=font_family, va='center')

        # Badge
        badge_w = 8.8
        badge_h = 2.2
        badge_x = x + w - badge_w - 1.2
        badge_y = y + h - 3.6
        badge_box = FancyBboxPatch(
            (badge_x, badge_y), badge_w, badge_h,
            boxstyle="round,pad=0.2,rounding_size=0.4",
            facecolor=badge_bg,
            edgecolor='none'
        )
        ax.add_patch(badge_box)
        ax.text(badge_x + badge_w / 2.0, badge_y + badge_h / 2.0, badge_text, fontsize=7.8, fontweight='bold', color='#FFFFFF', fontfamily=font_family, va='center', ha='center')

    # =========================================================================
    # 1. CARD 1: Cryptographic Benchmarking (Blue Theme)
    # =========================================================================
    draw_card(1.2, card_y, card_w, card_h, '#3B82F6', '#EFF6FF', '#1D4ED8', "1. Cryptographic Benchmarking", "LIBOQS FIPS", '#1D4ED8')
    
    c1_x = 2.4
    # Section 1
    ax.text(c1_x, card_y + 32.5, "• Physical Hardware Testbed:", fontsize=9.0, fontweight='bold', color='#111827', fontfamily=font_family, va='top')
    ax.text(c1_x + 1.0, card_y + 30.7, "Workstation host running compiled liboqs C library", fontsize=8.2, color='#374151', fontfamily=font_family, va='top')
    ax.text(c1_x + 1.0, card_y + 29.1, "Benchmarked NIST FIPS 203 (KEM) & FIPS 204 (DSA).", fontsize=8.2, fontweight='bold', color='#111827', fontfamily=font_family, va='top')

    # Section 2
    ax.text(c1_x, card_y + 26.6, "• Key Encapsulation (ML-KEM-768):", fontsize=9.0, fontweight='bold', color='#111827', fontfamily=font_family, va='top')
    ax.text(c1_x + 1.0, card_y + 24.8, "KeyGen: 28.4 μs | Encap: 37.2 μs | Decap: 32.1 μs", fontsize=8.2, fontweight='bold', color='#2563EB', fontfamily='monospace', va='top')
    ax.text(c1_x + 1.0, card_y + 23.2, "Lightweight overhead; near-parity with classical ECDHE.", fontsize=8.2, color='#374151', fontfamily=font_family, va='top')

    # Section 3
    ax.text(c1_x, card_y + 20.7, "• Digital Signatures Bottleneck (ML-DSA-65):", fontsize=9.0, fontweight='bold', color='#111827', fontfamily=font_family, va='top')
    ax.text(c1_x + 1.0, card_y + 18.9, "• Signing takes 385.4 μs (>9x slower than ECDSA at 42.1 μs)", fontsize=8.0, fontweight='bold', color='#DC2626', fontfamily=font_family, va='top')
    ax.text(c1_x + 1.0, card_y + 17.4, "• Verification takes 162.3 μs (matrix polynomial math)", fontsize=8.0, color='#374151', fontfamily=font_family, va='top')
    ax.text(c1_x + 1.0, card_y + 15.9, "• Signature size: 3,300 B (44x larger than ECDSA)", fontsize=8.0, color='#374151', fontfamily=font_family, va='top')

    # Section 4
    ax.text(c1_x, card_y + 13.4, "• Baseline Comparison (RSA-2048):", fontsize=9.0, fontweight='bold', color='#111827', fontfamily=font_family, va='top')
    ax.text(c1_x + 1.0, card_y + 11.6, "RSA-2048 signing: 1,111 ops/sec per physical appliance", fontsize=8.2, color='#374151', fontfamily=font_family, va='top')
    ax.text(c1_x + 1.0, card_y + 10.0, "ML-DSA-65 signing drops to only ~180 ops/sec per unit.", fontsize=8.2, fontweight='bold', color='#111827', fontfamily=font_family, va='top')

    # Callout Box 1
    callout1 = FancyBboxPatch((2.2, card_y + 1.0), card_w - 2.0, 4.4, boxstyle="round,pad=0.2,rounding_size=0.4", facecolor='#FFFFFF', edgecolor='#BFDBFE', linewidth=1.2)
    ax.add_patch(callout1)
    ax.text(3.2, card_y + 3.9, "✓ Benchmark Ground Truth:", fontsize=8.6, fontweight='bold', color='#1D4ED8', fontfamily=font_family, va='center')
    ax.text(3.2, card_y + 2.2, "Signing—not key exchange—is the primary bottleneck.", fontsize=8.0, color='#374151', fontfamily=font_family, va='center')

    # =========================================================================
    # 2. CARD 2: Transport & MTU Physics (Green Theme)
    # =========================================================================
    draw_card(34.2, card_y, card_w, card_h, '#22C55E', '#F0FDF4', '#15803D', "2. Transport & MTU Physics", "PACKET DYNAMICS", '#15803D')
    
    c2_x = 35.4
    # Section 1
    ax.text(c2_x, card_y + 32.5, "• 1,500-Byte Ethernet MTU Boundary:", fontsize=9.0, fontweight='bold', color='#111827', fontfamily=font_family, va='top')
    ax.text(c2_x + 1.0, card_y + 30.7, "Standard Ethernet Maximum Transmission Unit = 1,500B", fontsize=8.2, color='#374151', fontfamily=font_family, va='top')
    ax.text(c2_x + 1.0, card_y + 29.1, "Classical RSA/ECC handshakes easily fit in a single packet.", fontsize=8.2, color='#374151', fontfamily=font_family, va='top')

    # Section 2
    ax.text(c2_x, card_y + 26.6, "• TCP Packet Fragmentation:", fontsize=9.0, fontweight='bold', color='#111827', fontfamily=font_family, va='top')
    ax.text(c2_x + 1.0, card_y + 24.8, "ML-DSA-65 & ML-KEM-768 expand handshake > 4,484 B", fontsize=8.2, fontweight='bold', color='#15803D', fontfamily='monospace', va='top')
    ax.text(c2_x + 1.0, card_y + 23.2, "Forces TCP stack to split handshake into 3 to 4 fragments.", fontsize=8.2, color='#374151', fontfamily=font_family, va='top')

    # Section 3
    ax.text(c2_x, card_y + 20.7, "• Induced Latency Overhead:", fontsize=9.0, fontweight='bold', color='#111827', fontfamily=font_family, va='top')
    ax.text(c2_x + 1.0, card_y + 18.9, "Packet fragmentation introduces an empirical +6.6 ms penalty", fontsize=8.2, fontweight='bold', color='#111827', fontfamily=font_family, va='top')
    ax.text(c2_x + 1.0, card_y + 17.3, "Under WAN jitter, latency pushes toward the 50 ms SLA ceiling.", fontsize=8.2, color='#374151', fontfamily=font_family, va='top')

    # Section 4
    ax.text(c2_x, card_y + 14.8, "• Middlebox Drop Simulation:", fontsize=9.0, fontweight='bold', color='#111827', fontfamily=font_family, va='top')
    ax.text(c2_x + 1.0, card_y + 13.0, "Tested legacy enterprise middleboxes, proxies, and firewalls.", fontsize=8.2, color='#374151', fontfamily=font_family, va='top')
    ax.text(c2_x + 1.0, card_y + 11.4, "Proved that stateful firewalls drop fragmented PQC packets.", fontsize=8.2, fontweight='bold', color='#DC2626', fontfamily=font_family, va='top')

    # Callout Box 2
    callout2 = FancyBboxPatch((35.2, card_y + 1.0), card_w - 2.0, 4.4, boxstyle="round,pad=0.2,rounding_size=0.4", facecolor='#FFFFFF', edgecolor='#BBF7D0', linewidth=1.2)
    ax.add_patch(callout2)
    ax.text(36.2, card_y + 3.9, "✓ SLA Boundary Verified:", fontsize=8.6, fontweight='bold', color='#15803D', fontfamily=font_family, va='center')
    ax.text(36.2, card_y + 2.2, "Models packet inflation risks before deploying on live WAN.", fontsize=8.0, color='#374151', fontfamily=font_family, va='center')

    # =========================================================================
    # 3. CARD 3: Capacity & Deficit Validation (Red Theme)
    # =========================================================================
    draw_card(67.2, card_y, card_w, card_h, '#EF4444', '#FEF2F2', '#B91C1C', "3. Capacity & Deficit Validation", "ENTERPRISE SIZING", '#B91C1C')
    
    c3_x = 68.4
    # Section 1
    ax.text(c3_x, card_y + 32.5, "• Simulated Settlement Loads:", fontsize=9.0, fontweight='bold', color='#111827', fontfamily=font_family, va='top')
    ax.text(c3_x + 1.0, card_y + 30.7, "Workload stress tests from 1,000 to 10,000 TPS", fontsize=8.2, color='#374151', fontfamily=font_family, va='top')
    ax.text(c3_x + 1.0, card_y + 29.1, "Evaluated core banking payment switches & ISO 20022.", fontsize=8.2, color='#374151', fontfamily=font_family, va='top')

    # Section 2
    ax.text(c3_x, card_y + 26.6, "• Failure of Traditional IT Models:", fontsize=9.0, fontweight='bold', color='#111827', fontfamily=font_family, va='top')
    ax.text(c3_x + 1.0, card_y + 24.8, "Static linear worksheets assume 1:1 hardware scaling", fontsize=8.2, color='#374151', fontfamily=font_family, va='top')
    ax.text(c3_x + 1.0, card_y + 23.2, "Traditional models budget only 9 HSMs for 10,000 TPS.", fontsize=8.2, fontweight='bold', color='#DC2626', fontfamily=font_family, va='top')

    # Section 3
    ax.text(c3_x, card_y + 20.7, "• The 522.2% Hardware Capacity Deficit:", fontsize=9.0, fontweight='bold', color='#111827', fontfamily=font_family, va='top')
    ax.text(c3_x + 1.0, card_y + 18.9, "ML-DSA-65 hardware limits require 56 physical HSM units", fontsize=8.2, color='#374151', fontfamily=font_family, va='top')
    ax.text(c3_x + 1.0, card_y + 17.3, "Reveals an unbudgeted +522.2% capacity shortfall (56 vs 9).", fontsize=8.2, fontweight='bold', color='#DC2626', fontfamily=font_family, va='top')

    # Section 4
    ax.text(c3_x, card_y + 14.8, "• Financial Budget Variance:", fontsize=9.0, fontweight='bold', color='#111827', fontfamily=font_family, va='top')
    ax.text(c3_x + 1.0, card_y + 13.0, r"Creates an unbudgeted \$56,400.00/month operational variance", fontsize=8.2, color='#374151', fontfamily=font_family, va='top')
    ax.text(c3_x + 1.0, card_y + 11.4, r"Totals \$2,030,400.00 (\$2.03M) unbudgeted 3-year refresh gap.", fontsize=8.2, fontweight='bold', color='#111827', fontfamily=font_family, va='top')

    # Callout Box 3
    callout3 = FancyBboxPatch((68.2, card_y + 1.0), card_w - 2.0, 4.4, boxstyle="round,pad=0.2,rounding_size=0.4", facecolor='#FFFFFF', edgecolor='#FECACA', linewidth=1.2)
    ax.add_patch(callout3)
    ax.text(69.2, card_y + 3.9, "✓ Capacity Validated:", fontsize=8.6, fontweight='bold', color='#B91C1C', fontfamily=font_family, va='center')
    ax.text(69.2, card_y + 2.2, "Replaces flawed linear sizing with workload-tested budgets.", fontsize=8.0, color='#374151', fontfamily=font_family, va='center')

    # =========================================================================
    # 4. BOTTOM METRIC BAR (4 Columns)
    # =========================================================================
    bar_y = 1.2
    bar_h = 9.8
    metric_bar = FancyBboxPatch(
        (1.2, bar_y), 97.6, bar_h,
        boxstyle="round,pad=0.3,rounding_size=0.6",
        facecolor='#F8FAFC',
        edgecolor='#CBD5E1',
        linewidth=1.4
    )
    ax.add_patch(metric_bar)

    kpis = [
        ("385.4 μs", "ML-DSA-65 Signing Latency", ">9x slower than ECDSA P-256", '#059669'),
        ("3–4 Packets", "TCP MTU Fragmentation", "Splits across 1,500B Ethernet MTU", '#059669'),
        ("+522.2%", "Payment HSM Deficit", "56 vs. 9 units at 10,000 TPS", '#059669'),
        (r"\$2.03 Million", "Unbudgeted 3-Year Gap", r"\$56,400/mo operational variance", '#059669')
    ]

    col_w = 97.6 / 4.0
    for idx, (metric, title, subtitle, col) in enumerate(kpis):
        cx = 1.2 + (idx * col_w) + (col_w / 2.0)
        
        # Metric value (large bold green)
        ax.text(cx, bar_y + 7.0, metric, fontsize=15.5, fontweight='bold', color=col, fontfamily=font_family, va='center', ha='center')
        # Title (dark bold)
        ax.text(cx, bar_y + 4.2, title, fontsize=9.2, fontweight='bold', color='#111827', fontfamily=font_family, va='center', ha='center')
        # Subtitle
        ax.text(cx, bar_y + 2.0, subtitle, fontsize=8.0, color='#475569', fontfamily=font_family, va='center', ha='center')

        # Vertical Divider Line
        if idx < 3:
            div_x = 1.2 + ((idx + 1) * col_w)
            ax.plot([div_x, div_x], [bar_y + 1.2, bar_y + bar_h - 1.2], color='#E2E8F0', lw=1.2)

    # Save PNG and SVG
    output_png = "capstone2_testing_validation_infographic.png"
    output_svg = "capstone2_testing_validation_infographic.svg"
    plt.tight_layout(pad=0.4)
    plt.savefig(output_png, dpi=300, bbox_inches='tight', facecolor=fig.get_facecolor(), edgecolor='none')
    plt.savefig(output_svg, format='svg', bbox_inches='tight', facecolor=fig.get_facecolor(), edgecolor='none')
    plt.close()
    print(f"Successfully generated: {output_png} and {output_svg}")

if __name__ == "__main__":
    create_capstone2_infographic()
