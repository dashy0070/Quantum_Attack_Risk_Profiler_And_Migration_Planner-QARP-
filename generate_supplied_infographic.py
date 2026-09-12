import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Rectangle
import os

def create_supplied_infographic():
    # Figure size: 16 x 8 inches (matching the 2:1 aspect ratio of the user image)
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
        badge_w = 7.8
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
        ax.text(badge_x + badge_w / 2.0, badge_y + badge_h / 2.0, badge_text, fontsize=8.0, fontweight='bold', color='#FFFFFF', fontfamily=font_family, va='center', ha='center')

    # =========================================================================
    # 1. CARD 1: Client Architecture (Blue)
    # =========================================================================
    draw_card(1.2, card_y, card_w, card_h, '#3B82F6', '#EFF6FF', '#1D4ED8', "1. Client Architecture", "CHROME MV3", '#1D4ED8')
    
    # Card 1 Text Content
    c1_x = 2.4
    
    # Section 1
    ax.text(c1_x, card_y + 32.5, "• Browser Environment:", fontsize=9.0, fontweight='bold', color='#111827', fontfamily=font_family, va='top')
    ax.text(c1_x + 1.0, card_y + 30.7, "Google Chrome (v115+) hosting the", fontsize=8.2, color='#374151', fontfamily=font_family, va='top')
    ax.text(c1_x + 1.0, card_y + 29.1, "PQC Upgrade Broker extension.", fontsize=8.2, fontweight='bold', color='#111827', fontfamily=font_family, va='top')

    # Section 2
    ax.text(c1_x, card_y + 26.6, "• DOM Hooking & Interception:", fontsize=9.0, fontweight='bold', color='#111827', fontfamily=font_family, va='top')
    ax.text(c1_x + 1.0, card_y + 24.8, "inject.js / content.js", fontsize=8.4, fontweight='bold', color='#2563EB', fontfamily='monospace', va='top')
    ax.text(c1_x + 1.0, card_y + 23.2, "Transparently overrides window.fetch()", fontsize=8.2, color='#374151', fontfamily=font_family, va='top')
    ax.text(c1_x + 1.0, card_y + 21.6, "capturing outbound banking payloads.", fontsize=8.2, color='#374151', fontfamily=font_family, va='top')

    # Section 3
    ax.text(c1_x, card_y + 19.1, "• Client-Side Hybrid Encryption:", fontsize=9.0, fontweight='bold', color='#111827', fontfamily=font_family, va='top')
    ax.text(c1_x + 1.0, card_y + 17.3, "• Generates ephemeral keypair", fontsize=8.0, color='#374151', fontfamily=font_family, va='top')
    ax.text(c1_x + 1.0, card_y + 15.8, "• ML-KEM-768 (Kyber) encapsulation", fontsize=8.0, fontweight='bold', color='#111827', fontfamily=font_family, va='top')
    ax.text(c1_x + 1.0, card_y + 14.3, "• X25519 ECDHE classical key exchange", fontsize=8.0, fontweight='bold', color='#111827', fontfamily=font_family, va='top')
    ax.text(c1_x + 1.0, card_y + 12.8, "• AES-256-GCM payload cipher", fontsize=8.0, fontweight='bold', color='#111827', fontfamily=font_family, va='top')

    # Section 4
    ax.text(c1_x, card_y + 10.3, "• In-Browser Response Decrypt:", fontsize=9.0, fontweight='bold', color='#111827', fontfamily=font_family, va='top')
    ax.text(c1_x + 1.0, card_y + 8.5, "Decrypts bank confirmation in browser", fontsize=8.2, color='#374151', fontfamily=font_family, va='top')
    ax.text(c1_x + 1.0, card_y + 6.9, "before DOM render (Zero plain wire exposure).", fontsize=8.2, color='#374151', fontfamily=font_family, va='top')

    # Callout Box 1
    callout1 = FancyBboxPatch((2.2, card_y + 1.0), card_w - 2.0, 4.4, boxstyle="round,pad=0.2,rounding_size=0.4", facecolor='#FFFFFF', edgecolor='#BFDBFE', linewidth=1.2)
    ax.add_patch(callout1)
    ax.text(3.2, card_y + 3.9, "✓ Zero User Disruption:", fontsize=8.6, fontweight='bold', color='#1D4ED8', fontfamily=font_family, va='center')
    ax.text(3.2, card_y + 2.2, "100% transparent browser proxying.", fontsize=8.0, color='#374151', fontfamily=font_family, va='center')

    # =========================================================================
    # 2. CARD 2: Server Architecture (Green)
    # =========================================================================
    draw_card(34.2, card_y, card_w, card_h, '#22C55E', '#F0FDF4', '#15803D', "2. Server Architecture", "REVERSE PROXY", '#15803D')
    
    # Card 2 Text Content
    c2_x = 35.4

    # Section 1
    ax.text(c2_x, card_y + 32.5, "• PQC Gateway Server:", fontsize=9.0, fontweight='bold', color='#111827', fontfamily=font_family, va='top')
    ax.text(c2_x + 1.0, card_y + 30.7, "server_gateway.py (Port 8443 / 8080)", fontsize=8.4, fontweight='bold', color='#15803D', fontfamily='monospace', va='top')
    ax.text(c2_x + 1.0, card_y + 29.1, "Powered by liboqs-python (NIST FIPS 203).", fontsize=8.2, color='#374151', fontfamily=font_family, va='top')

    # Section 2
    ax.text(c2_x, card_y + 26.6, "• Key Decapsulation & Decrypt:", fontsize=9.0, fontweight='bold', color='#111827', fontfamily=font_family, va='top')
    ax.text(c2_x + 1.0, card_y + 24.8, "• Decapsulates ML-KEM-768 secret", fontsize=8.0, fontweight='bold', color='#111827', fontfamily=font_family, va='top')
    ax.text(c2_x + 1.0, card_y + 23.3, "• Computes X25519 shared secret", fontsize=8.0, fontweight='bold', color='#111827', fontfamily=font_family, va='top')
    ax.text(c2_x + 1.0, card_y + 21.8, "• Reconstructs key via HKDF-SHA256", fontsize=8.0, fontweight='bold', color='#111827', fontfamily=font_family, va='top')
    ax.text(c2_x + 1.0, card_y + 20.3, "• Authenticates & decrypts AES-256 payload", fontsize=8.0, color='#374151', fontfamily=font_family, va='top')

    # Section 3
    ax.text(c2_x, card_y + 17.8, "• Legacy Banking Core API:", fontsize=9.0, fontweight='bold', color='#111827', fontfamily=font_family, va='top')
    ax.text(c2_x + 1.0, card_y + 16.0, "legacy_bank_api.py (Port 5000)", fontsize=8.4, fontweight='bold', color='#15803D', fontfamily='monospace', va='top')
    ax.text(c2_x + 1.0, card_y + 14.4, "Receives clean JSON over local IPC;", fontsize=8.2, color='#374151', fontfamily=font_family, va='top')
    ax.text(c2_x + 1.0, card_y + 12.8, "executes transaction balance update.", fontsize=8.2, color='#374151', fontfamily=font_family, va='top')

    # Section 4
    ax.text(c2_x, card_y + 10.3, "• Zero Code Modification:", fontsize=9.0, fontweight='bold', color='#111827', fontfamily=font_family, va='top')
    ax.text(c2_x + 1.0, card_y + 8.5, "Drop-in proxy requires 0 code changes", fontsize=8.2, fontweight='bold', color='#15803D', fontfamily=font_family, va='top')
    ax.text(c2_x + 1.0, card_y + 6.9, "to existing core banking systems.", fontsize=8.2, color='#374151', fontfamily=font_family, va='top')

    # Callout Box 2
    callout2 = FancyBboxPatch((35.2, card_y + 1.0), card_w - 2.0, 4.4, boxstyle="round,pad=0.2,rounding_size=0.4", facecolor='#FFFFFF', edgecolor='#BBF7D0', linewidth=1.2)
    ax.add_patch(callout2)
    ax.text(36.2, card_y + 3.9, "✓ Enterprise Drop-in:", fontsize=8.6, fontweight='bold', color='#15803D', fontfamily=font_family, va='center')
    ax.text(36.2, card_y + 2.2, "Retrofits legacy APIs without refactoring.", fontsize=8.0, color='#374151', fontfamily=font_family, va='center')

    # =========================================================================
    # 3. CARD 3: Quantum Attack Scenario (Red)
    # =========================================================================
    draw_card(67.2, card_y, card_w, card_h, '#EF4444', '#FEF2F2', '#B91C1C', "3. Quantum Attack Scenario", "THREAT MODEL", '#B91C1C')
    
    # Card 3 Text Content
    c3_x = 68.4

    # Section 1
    ax.text(c3_x, card_y + 32.5, "• Threat Model (HNDL):", fontsize=9.0, fontweight='bold', color='#111827', fontfamily=font_family, va='top')
    ax.text(c3_x + 1.0, card_y + 30.7, '"Harvest Now, Decrypt Later"', fontsize=8.4, fontweight='bold', color='#111827', fontfamily=font_family, va='top')
    ax.text(c3_x + 1.0, card_y + 29.1, "Adversary archives encrypted wire traffic.", fontsize=8.2, color='#374151', fontfamily=font_family, va='top')

    # Section 2
    ax.text(c3_x, card_y + 26.6, "• Attack Simulation Tool:", fontsize=9.0, fontweight='bold', color='#111827', fontfamily=font_family, va='top')
    ax.text(c3_x + 1.0, card_y + 24.8, "Scapy PCAP Wire Sniffer", fontsize=8.4, fontweight='bold', color='#DC2626', fontfamily='monospace', va='top')
    ax.text(c3_x + 1.0, card_y + 23.2, "Captures raw frames on 127.0.0.1 loopback.", fontsize=8.2, color='#374151', fontfamily=font_family, va='top')

    # Section 3
    ax.text(c3_x, card_y + 20.7, "• Baseline vs. Shor's Algorithm:", fontsize=9.0, fontweight='bold', color='#111827', fontfamily=font_family, va='top')
    ax.text(c3_x + 1.0, card_y + 18.9, "• Classical TLS (Disabled): RSA/ECC keys", fontsize=8.0, fontweight='bold', color='#DC2626', fontfamily=font_family, va='top')
    ax.text(c3_x + 2.2, card_y + 17.4, "are cracked by quantum polynomial factoring.", fontsize=8.0, color='#374151', fontfamily=font_family, va='top')
    ax.text(c3_x + 1.0, card_y + 15.9, "• Hybrid PQC (Enabled): ML-KEM lattice", fontsize=8.0, fontweight='bold', color='#15803D', fontfamily=font_family, va='top')
    ax.text(c3_x + 2.2, card_y + 14.4, "math is immune to Shor's algorithm.", fontsize=8.0, color='#374151', fontfamily=font_family, va='top')

    # Section 4
    ax.text(c3_x, card_y + 11.9, "• Empirical Test Finding (Ch. 9):", fontsize=9.0, fontweight='bold', color='#111827', fontfamily=font_family, va='top')
    ax.text(c3_x + 1.0, card_y + 10.1, "0% Plaintext Decryptability achieved", fontsize=8.4, fontweight='bold', color='#15803D', fontfamily=font_family, va='top')
    ax.text(c3_x + 1.0, card_y + 8.5, "against active adversarial wire harvesting.", fontsize=8.2, color='#374151', fontfamily=font_family, va='top')

    # Callout Box 3
    callout3 = FancyBboxPatch((68.2, card_y + 1.0), card_w - 2.0, 4.4, boxstyle="round,pad=0.2,rounding_size=0.4", facecolor='#FFFFFF', edgecolor='#FECACA', linewidth=1.2)
    ax.add_patch(callout3)
    ax.text(69.2, card_y + 3.9, "✓ Quantum Resilient:", fontsize=8.6, fontweight='bold', color='#B91C1C', fontfamily=font_family, va='center')
    ax.text(69.2, card_y + 2.2, "Full immunity against future CRQCs.", fontsize=8.0, color='#374151', fontfamily=font_family, va='center')

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
        ("4.8 ms", "Handshake Latency", "Meets < 5.0 ms SLA target"),
        ("< 1.5%", "CPU Utilization", "At 1,000 concurrent users"),
        ("0% Leakage", "PCAP Decryptability", "Harvest-Now-Decrypt-Later Immune"),
        ("0 Changes", "Legacy Backend Impact", "100% plug-and-play proxy")
    ]

    col_w = 97.6 / 4.0
    for idx, (metric, title, subtitle) in enumerate(kpis):
        cx = 1.2 + (idx * col_w) + (col_w / 2.0)
        
        # Metric value (green)
        ax.text(cx, bar_y + 7.0, metric, fontsize=15.5, fontweight='bold', color='#059669', fontfamily=font_family, va='center', ha='center')
        # Title (dark bold)
        ax.text(cx, bar_y + 4.2, title, fontsize=9.2, fontweight='bold', color='#111827', fontfamily=font_family, va='center', ha='center')
        # Subtitle
        ax.text(cx, bar_y + 2.0, subtitle, fontsize=8.0, color='#475569', fontfamily=font_family, va='center', ha='center')

        # Vertical Divider Line
        if idx < 3:
            div_x = 1.2 + ((idx + 1) * col_w)
            ax.plot([div_x, div_x], [bar_y + 1.2, bar_y + bar_h - 1.2], color='#E2E8F0', lw=1.2)

    # Save PNG and SVG
    output_png = "capstone1_testing_validation_infographic.png"
    output_svg = "capstone1_testing_validation_infographic.svg"
    plt.tight_layout(pad=0.4)
    plt.savefig(output_png, dpi=300, bbox_inches='tight', facecolor=fig.get_facecolor(), edgecolor='none')
    plt.savefig(output_svg, format='svg', bbox_inches='tight', facecolor=fig.get_facecolor(), edgecolor='none')
    plt.close()
    print(f"Successfully generated: {output_png} and {output_svg}")

if __name__ == "__main__":
    create_supplied_infographic()
