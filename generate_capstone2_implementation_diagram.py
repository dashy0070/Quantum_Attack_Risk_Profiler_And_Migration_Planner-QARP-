"""
Generates the exact visual End-to-End Implementation Architecture Diagram
for Capstone 2: Quantum Attack Risk Profiler and Migration Planner (QARP).
Matches the style, layout, color-coded multi-box pipelines, and institutional branding
of the Capstone 1 slide format, with perfect vertical spacing and no overlapping labels.
"""

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Rectangle

def generate_implementation_diagram():
    # 16:9 widescreen presentation canvas at 300 DPI
    fig, ax = plt.subplots(figsize=(18, 10.5), dpi=300)
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    ax.axis('off')

    fig.patch.set_facecolor('#FFFFFF')
    ax.set_facecolor('#FFFFFF')

    font_family = 'DejaVu Sans'

    # =========================================================================
    # TOP MAIN HEADER (Institutional Presentation Banner)
    # =========================================================================
    ax.text(2.0, 96.5, "Implementation", fontsize=28, fontweight='bold', color='#333333', fontfamily=font_family, va='center')
    
    # REVA UNIVERSITY Logo / Text
    ax.text(98.0, 96.5, "REVA UNIVERSITY", fontsize=15, fontweight='bold', color='#D9531E', fontfamily=font_family, va='center', ha='right')
    ax.text(98.0, 93.8, "M.Tech Capstone-2 Project", fontsize=10, color='#666666', fontfamily=font_family, va='center', ha='right')

    # Accent decorative timeline dot & line
    ax.plot([2.0, 98.0], [92.0, 92.0], color='#CBD5E1', lw=1.2)
    ax.plot([47.5, 52.5], [92.0, 92.0], color='#0B3C9B', lw=3.0)
    circle = plt.Circle((50.0, 92.0), 0.7, facecolor='#0B3C9B', edgecolor='#FFFFFF', lw=1.5, zorder=5)
    ax.add_patch(circle)

    # =========================================================================
    # MAIN SLIDE BANNER (Deep Royal Blue)
    # =========================================================================
    main_banner = FancyBboxPatch(
        (1.5, 84.5), 97.0, 5.8,
        boxstyle="round,pad=0.3,rounding_size=0.8",
        facecolor='#0B3C9B',
        edgecolor='#072A6F',
        linewidth=1.5
    )
    ax.add_patch(main_banner)

    ax.text(3.5, 87.4, "END-TO-END QARP TELEMETRY PROFILING & CAPACITY SIZING PIPELINE", fontsize=15.0, fontweight='bold', color='#FFFFFF', fontfamily=font_family, va='center')
    ax.text(96.5, 87.4, "Passive Stream Ingestion → Quantum Cryptanalysis → Dynamic Capacity Sizing → 2033 Roadmap", fontsize=9.2, color='#93C5FD', fontfamily=font_family, va='center', ha='right')

    # =========================================================================
    # SECTION 1: FORWARD STREAMING & QUANTUM CRYPTANALYSIS PIPELINE (Top Half)
    # =========================================================================
    sec1_hdr = FancyBboxPatch(
        (1.5, 78.5), 97.0, 3.2,
        boxstyle="round,pad=0.2,rounding_size=0.5",
        facecolor='#EBF3FC',
        edgecolor='#BDD7EE',
        linewidth=1.2
    )
    ax.add_patch(sec1_hdr)

    # Blue square bullet
    ax.add_patch(Rectangle((2.8, 79.6), 1.0, 1.0, facecolor='#1F4E79', edgecolor='none'))
    ax.text(4.5, 80.1, "1. FORWARD TELEMETRY INGESTION, QUANTUM RISK PROFILING & CBOM GENERATION", fontsize=10.5, fontweight='bold', color='#1F4E79', fontfamily=font_family, va='center')

    # Helper function to draw component cards with perfect vertical separation
    def draw_card(x, y, w, h, title, subtitle, badge_color, border_color, bullets):
        # Card Body
        card = FancyBboxPatch(
            (x, y), w, h,
            boxstyle="round,pad=0.4,rounding_size=0.8",
            facecolor='#FFFFFF',
            edgecolor=border_color,
            linewidth=1.8
        )
        ax.add_patch(card)

        # Title at the very top of the card
        ax.text(x + 1.2, y + h - 2.4, title, fontsize=11.2, fontweight='bold', color=border_color, fontfamily=font_family, va='center')
        
        # Subtitle Pill placed cleanly below title (with 1.8 units gap)
        badge_w = len(subtitle) * 0.42 + 2.4
        badge = FancyBboxPatch(
            (x + 1.2, y + h - 5.8), min(badge_w, w - 2.4), 2.1,
            boxstyle="round,pad=0.2,rounding_size=0.4",
            facecolor='#FFFFFF',
            edgecolor=badge_color,
            linewidth=1.2
        )
        ax.add_patch(badge)
        ax.text(x + 2.0, y + h - 4.75, subtitle, fontsize=8.0, fontweight='bold', color=badge_color, fontfamily=font_family, va='center')

        # Bullets start safely below badge
        curr_y = y + h - 7.6
        for b_title, b_desc in bullets:
            ax.text(x + 1.2, curr_y, f"• {b_title}", fontsize=8.6, fontweight='bold', color='#0F172A', fontfamily=font_family, va='top')
            curr_y -= 1.8
            ax.text(x + 2.2, curr_y, b_desc, fontsize=7.8, color='#334155', fontfamily=font_family, va='top')
            curr_y -= 2.7

    # --- TOP 4 CARDS ---
    top_w = 22.8
    top_h = 32.8
    top_y = 44.5

    # 1. Telemetry Emitters (Blue)
    draw_card(
        1.5, top_y, top_w, top_h,
        "1. Live Telemetry Ingress", "Mixed Banking Feeds (:8080)",
        '#0B3C9B', '#0B3C9B',
        [
            ("Traffic Sources Ingested:", "REST/JSON, Zeek TLS 1.3 PCAP,\nISO 20022 (pacs.008 & pain.001)"),
            ("High-Velocity Buffering:", "Asynchronous queue supporting\n1,000 to 10,000 simulated TPS"),
            ("Passive Inspection:", "Non-intrusive network tap with\n0 ms impact on live bank core"),
            ("Endpoint Profiling:", "Maps caller IPs, cipher IDs,\nand raw payload byte lengths")
        ]
    )

    # 2. Async Parser Engine (Red/Orange)
    draw_card(
        26.2, top_y, top_w, top_h,
        "2. Async Streaming Parser", "pqc_log_parser_and_cost_engine.py",
        '#C00000', '#C00000',
        [
            ("Token & Schema Extraction:", "defusedxml & regex tokenizer\nsafely extracts XML/JSON fields"),
            ("Cryptographic Audit:", "Identifies active ciphers (RSA-2048,\nECDSA P-256, AES-128, 3DES, SHA-1)"),
            ("Harvest Vulnerability Triage:", "Flags long-term confidential\nassets exposed to HNDL threats"),
            ("Throughput Velocity:", "Calculates dynamic burst rate\nand transaction rate (TPS)")
        ]
    )

    # 3. Quantum Cryptanalysis (Purple)
    draw_card(
        50.9, top_y, top_w, top_h,
        "3. Cryptanalysis Engine", "Algorithm 3: FTQ-CREA",
        '#7030A0', '#7030A0',
        [
            ("Gidney–Ekerå Shor's Model:", "RSA-2048 factored in 8 hrs via\n20M physical noisy qubits"),
            ("Grover's Key Reduction:", "AES-128 reduced to ~64-bit strength\nMandates AES-256 upgrade"),
            ("Mosca Inequality Evaluator:", "Computes X + Y > Z to establish\nhard cryptographic deadline"),
            ("Target PQC Primitives:", "Selects NIST FIPS 203 (ML-KEM)\nand FIPS 204 (ML-DSA-65)")
        ]
    )

    # 4. CycloneDX 1.6 CBOM (Green)
    draw_card(
        75.6, top_y, top_w, top_h,
        "4. Automated CBOM Engine", "Algorithm 4: CBOM-DAGA",
        '#1E7E34', '#1E7E34',
        [
            ("OWASP Standard Generation:", "Outputs formal CycloneDX 1.6\nCryptography Bill of Materials"),
            ("Asset Vulnerability Graph:", "Classifies algorithms: Classical,\nTransitional, and Quantum-Safe"),
            ("Machine-Readable Export:", "Produces compliant JSON/XML\nready for enterprise audit vaults"),
            ("Continuous Discovery:", "Updates cryptographic posture\nin real time across all gateways")
        ]
    )

    # Connecting Arrows
    def draw_arrow(x1, y1, x2, y2, color):
        ax.annotate(
            '', xy=(x2, y2), xytext=(x1, y1),
            arrowprops=dict(arrowstyle="-|>,head_width=0.45,head_length=0.7", color=color, lw=2.4)
        )

    draw_arrow(24.5, 61.0, 26.0, 61.0, '#0B3C9B')
    draw_arrow(49.2, 61.0, 50.7, 61.0, '#C00000')
    draw_arrow(73.9, 61.0, 75.4, 61.0, '#7030A0')

    # =========================================================================
    # SECTION 2: NETWORK PACKET PHYSICS, HSM SIZING & GOVERNANCE (Bottom Half)
    # =========================================================================
    sec2_hdr = FancyBboxPatch(
        (1.5, 39.5), 97.0, 3.2,
        boxstyle="round,pad=0.2,rounding_size=0.5",
        facecolor='#E8F8F0',
        edgecolor='#A9DFBF',
        linewidth=1.2
    )
    ax.add_patch(sec2_hdr)

    # Green circle bullet
    circle_sec2 = plt.Circle((3.3, 41.1), 0.55, facecolor='#196F3D', edgecolor='none')
    ax.add_patch(circle_sec2)
    ax.text(4.5, 41.1, "2. TRANSPORT PACKET PHYSICS, PAYMENT HSM CAPACITY SIZING & 2025–2033 ROADMAP", fontsize=10.5, fontweight='bold', color='#196F3D', fontfamily=font_family, va='center')

    # --- BOTTOM 3 CARDS ---
    bot_w = 30.8
    bot_h = 34.0
    bot_y = 3.5

    # Card A: Network MTU (Teal/Green)
    draw_card(
        1.5, bot_y, bot_w, bot_h,
        "A. MTU Packet Physics Engine", "Algorithm 1: Network Overhead Sizer",
        '#117A65', '#117A65',
        [
            ("1,500-Byte Ethernet MTU Boundary:", "PQC key & signature sizes expand payload beyond 1,500B MTU,\nsplitting single TLS handshake into 3 to 4 fragmented TCP packets"),
            ("Empirical Serialization Latency:", "Fragmentation introduces +6.6 ms network transport penalty,\npushing high-frequency clearing routes toward the 50 ms SLA ceiling"),
            ("Middlebox Resilience Audit:", "Detects enterprise middleboxes, proxies, and firewalls that drop\nfragmented PQC handshake packets on WAN banking backbones")
        ]
    )

    # Card B: Payment HSM Sizing (Amber/Red)
    draw_card(
        34.6, bot_y, bot_w, bot_h,
        "B. Physical Payment HSM Sizer", "Table 10.1: Dynamic Cost & Deficit Modeler",
        '#D9531E', '#D9531E',
        [
            ("Physical liboqs Micro-Benchmarks:", "ML-DSA-65 signing (385.4 μs) runs >9x slower than ECDSA (42.1 μs);\nPhysical HSM signing drops from ~1,111 TPS to ~180 TPS per appliance"),
            ("The 522.2% Hardware Capacity Deficit:", "At 10,000 TPS settlement, traditional linear models budget 9 HSMs;\nPQC reality requires 56 physical HSM units (+522.2% deficit)"),
            ("Enterprise Financial Impact:", "Creates an unbudgeted $56,400.00/month operational variance;\nTotals $2,030,400.00 ($2.03M) Capex/Opex over 3-year refresh cycle")
        ]
    )

    # Card C: Streamlit UI & Roadmap (Navy/Blue)
    draw_card(
        67.7, bot_y, bot_w, bot_h,
        "C. Streamlit Dashboard & Roadmap", "app.py — Interactive Migration Planner",
        '#0B3C9B', '#0B3C9B',
        [
            ("Interactive Multi-Tab Dashboard:", "Streamlit UI features real-time log ingestion, CycloneDX CBOM\nexplorer, interactive qubit sliders, and dynamic HSM cost charts"),
            ("Four-Stage Phased Migration Roadmap:", "Phase 1 (2025–26): Discovery & CBOM; Phase 2 (2026–28): Hybrid TLS;\nPhase 3 (2028–30): PKI & ISO 20022; Phase 4 (2030–33): Full CNSA 2.0"),
            ("Zero-Downtime Governance:", "Eliminates guess-work for banking infrastructure architects,\nenabling verifiable compliance with NIST, ISO, and PCI DSS v4.0.1")
        ]
    )

    # Bottom Connecting Arrows
    draw_arrow(32.5, 20.5, 34.4, 20.5, '#117A65')
    draw_arrow(65.6, 20.5, 67.5, 20.5, '#D9531E')

    # Vertical Pipeline Bridging Arrow (Connecting Top Pipeline to Bottom Pipeline)
    ax.annotate(
        '', xy=(82.0, 39.5), xytext=(82.0, 44.5),
        arrowprops=dict(arrowstyle="-|>,head_width=0.45,head_length=0.7", color='#196F3D', lw=2.4)
    )

    # Save high-resolution PNG
    output_png = "capstone2_implementation_diagram.png"
    plt.tight_layout()
    plt.savefig(output_png, dpi=300, bbox_inches='tight', facecolor=fig.get_facecolor(), edgecolor='none')
    plt.close()
    print(f"Successfully generated updated Capstone 2 implementation diagram: {output_png}")

if __name__ == "__main__":
    generate_implementation_diagram()
