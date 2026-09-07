import matplotlib
matplotlib.rcParams['svg.fonttype'] = 'none'
import matplotlib.pyplot as plt
import matplotlib.patches as patches

TNR = 'Times New Roman'

def txt(ax, x, y, s, fs=11.0, bold=False, color='#0F172A', ha='center', va='center'):
    ax.text(x, y, s, fontsize=fs, color=color, ha=ha, va=va,
            fontweight='bold' if bold else 'normal', fontfamily=TNR)

def draw_phase_column(ax, x, y, w, h, phase_num, phase_title, layer_tag, bullets, bottom_title, bottom_desc, theme_col, light_bg):
    # 1. Main Column Outer Box
    card = patches.FancyBboxPatch(
        (x, y), w, h, boxstyle='round,pad=0.008,rounding_size=0.015',
        facecolor='#FFFFFF', edgecolor=theme_col, linewidth=2.2, zorder=2)
    ax.add_patch(card)

    # 2. Top Header Banner
    banner_h = 0.120
    banner = patches.FancyBboxPatch(
        (x, y + h - banner_h), w, banner_h, boxstyle='round,pad=0.004,rounding_size=0.012',
        facecolor=theme_col, edgecolor=theme_col, linewidth=0, zorder=3)
    ax.add_patch(banner)
    
    txt(ax, x + w/2, y + h - 0.038, phase_num, fs=11.5, bold=True, color='white')
    txt(ax, x + w/2, y + h - 0.078, phase_title, fs=13.0, bold=True, color='white')

    # 3. Sub-layer Pill Badge
    badge_w = 0.145
    badge_h = 0.040
    badge_y = y + h - banner_h - 0.060
    badge = patches.FancyBboxPatch(
        (x + (w - badge_w)/2, badge_y), badge_w, badge_h, boxstyle='round,pad=0.004,rounding_size=0.015',
        facecolor=light_bg, edgecolor='none', zorder=3)
    ax.add_patch(badge)
    txt(ax, x + w/2, badge_y + badge_h/2, layer_tag, fs=10.0, bold=True, color=theme_col)

    # 4. Bullet Points Section
    bullet_start_y = badge_y - 0.065
    row_step = 0.115
    for i, (head, sub) in enumerate(bullets):
        by = bullet_start_y - i * row_step
        # Bullet title
        txt(ax, x + 0.020, by, f"•  {head}", fs=11.5, bold=True, color='#0F172A', ha='left')
        # Bullet subtitle
        txt(ax, x + 0.038, by - 0.035, sub, fs=9.5, bold=False, color='#475569', ha='left')

    # 5. Bottom Callout Box
    bot_h = 0.120
    bot_y = y + 0.022
    bot_box = patches.FancyBboxPatch(
        (x + 0.012, bot_y), w - 0.024, bot_h, boxstyle='round,pad=0.006,rounding_size=0.012',
        facecolor=light_bg, edgecolor=theme_col, linewidth=1.5, zorder=3)
    ax.add_patch(bot_box)
    
    txt(ax, x + w/2, bot_y + bot_h*0.68, bottom_title, fs=10.0, bold=True, color=theme_col)
    txt(ax, x + w/2, bot_y + bot_h*0.32, bottom_desc, fs=11.0, bold=True, color='#0F172A')

def generate_pipeline_figure():
    fig, ax = plt.subplots(figsize=(20, 9.5), dpi=300)
    fig.patch.set_facecolor('#FFFFFF')
    ax.set_facecolor('#FFFFFF')
    
    ax.set_xlim(-0.01, 1.01)
    ax.set_ylim(-0.01, 1.01)
    ax.axis('off')

    # Column Width and Gap Geometry
    CW = 0.224
    GAP = 0.024
    START_X = 0.018
    Y_POS = 0.045
    CH = 0.900

    # Colors
    C1 = '#0284C7'; BG1 = '#F0F9FF'  # Phase 1: Cyan-Blue
    C2 = '#D97706'; BG2 = '#FFFBEB'  # Phase 2: Amber-Gold
    C3 = '#DC2626'; BG3 = '#FEF2F2'  # Phase 3: Crimson-Red
    C4 = '#059669'; BG4 = '#F0FDF4'  # Phase 4: Emerald-Green

    # -------------------------------------------------------------
    # PHASE 1: LOCAL DATA INGESTION
    # -------------------------------------------------------------
    p1_x = START_X
    p1_bullets = [
        ("JSON Gateway Logs", "Envoy / NGINX / Local REST"),
        ("Banking API Metadata", "Target Endpoints & Ciphers"),
        ("Mock ISO 20022 Traces", "pacs.008 & pain.001 Schemas")
    ]
    draw_phase_column(ax, p1_x, Y_POS, CW, CH,
                      "PHASE 1", "LOCAL DATA INGESTION", "[ INPUT LAYER ]",
                      p1_bullets, "TELEMETRY EXTRACTED", "TPS, Payload & Ciphers",
                      C1, BG1)

    # -------------------------------------------------------------
    # PHASE 2: EMPIRICAL BENCHMARK
    # -------------------------------------------------------------
    p2_x = p1_x + CW + GAP
    p2_bullets = [
        ("Open Quantum Safe", "liboqs C & Python wrapper"),
        ("Local Host CPU Timing", "ML-KEM-768 & ML-DSA-65"),
        ("Hardware Profiling", "Throughput Slump vs. RSA/ECDSA")
    ]
    draw_phase_column(ax, p2_x, Y_POS, CW, CH,
                      "PHASE 2", "EMPIRICAL BENCHMARK", "[ CRYPTO ENGINE ]",
                      p2_bullets, "EMPIRICAL BENCHMARKS", "Host CPU Latency & Cycles",
                      C2, BG2)

    # -------------------------------------------------------------
    # PHASE 3: NETWORK & SLA PROFILER
    # -------------------------------------------------------------
    p3_x = p2_x + CW + GAP
    p3_bullets = [
        ("MTU Boundary Model", "1,500 Byte Ethernet limit"),
        ("Packet Fragmentation", "Handshake splits across packets"),
        ("Banking SLA Analyzer", "Flags Latency > 50ms Breaches")
    ]
    draw_phase_column(ax, p3_x, Y_POS, CW, CH,
                      "PHASE 3", "NETWORK & SLA PROFILER", "[ NETWORKING LAYER ]",
                      p3_bullets, "NETWORK BOTTLENECK", "MTU Packets & SLA Breaches",
                      C3, BG3)

    # -------------------------------------------------------------
    # PHASE 4: LOCAL RISK DASHBOARD
    # -------------------------------------------------------------
    p4_x = p3_x + CW + GAP
    p4_bullets = [
        ("Gidney-Ekerå Matrix", "Logical & Physical Qubits"),
        ("Grover Triage", "Forces AES-128 → AES-256"),
        ("Physical HSM Sizing", "Dedicated Core Scaling Model")
    ]
    draw_phase_column(ax, p4_x, Y_POS, CW, CH,
                      "PHASE 4", "LOCAL RISK DASHBOARD", "[ EXECUTIVE COCKPIT ]",
                      p4_bullets, "DEMO DELIVERABLE", "localhost:8501 Dashboard",
                      C4, BG4)

    # -------------------------------------------------------------
    # HORIZONTAL DASHED CONNECTORS BETWEEN COLUMNS
    # -------------------------------------------------------------
    def draw_connector(x_start, x_end, y_val):
        ax.plot([x_start, x_end], [y_val, y_val],
                color='#94A3B8', linestyle='--', linewidth=2.2, zorder=1)
        ax.plot([x_end - 0.005], [y_val], marker='o', markersize=4, color='#64748B', zorder=2)

    conn_y = Y_POS + CH * 0.55
    draw_connector(p1_x + CW, p2_x, conn_y)
    draw_connector(p2_x + CW, p3_x, conn_y)
    draw_connector(p3_x + CW, p4_x, conn_y)

    # Save outputs
    png_out = r'D:\Anirban\000000_Mtech Reva\CapStone_2\qarp_methodology_pipeline.png'
    svg_out = r'D:\Anirban\000000_Mtech Reva\CapStone_2\qarp_methodology_pipeline.svg'

    plt.savefig(png_out, format='png', dpi=300, facecolor='white', bbox_inches='tight', pad_inches=0.08)
    plt.savefig(svg_out, format='svg', facecolor='white', bbox_inches='tight', pad_inches=0.08)
    print(f"Success:\n1. PNG: {png_out}\n2. SVG: {svg_out}")

if __name__ == '__main__':
    generate_pipeline_figure()