import matplotlib
matplotlib.rcParams['svg.fonttype'] = 'none'
import matplotlib.pyplot as plt
import matplotlib.patches as patches

TNR = 'Times New Roman'

def txt(ax, x, y, s, fs=11.5, bold=False, color='#0F172A', ha='center', va='center'):
    ax.text(x, y, s, fontsize=fs, color=color, ha=ha, va=va,
            fontweight='bold' if bold else 'normal', fontfamily=TNR)

def draw_component_box(ax, x, y, w, h, title, lines, hdr_color, bg_color):
    ax.add_patch(patches.FancyBboxPatch(
        (x, y), w, h, boxstyle='round,pad=0.006,rounding_size=0.015',
        facecolor=bg_color, edgecolor=hdr_color, linewidth=2.2, zorder=2))
    
    hh = 0.056
    ax.add_patch(patches.FancyBboxPatch(
        (x, y + h - hh), w, hh, boxstyle='round,pad=0.003,rounding_size=0.010',
        facecolor=hdr_color, edgecolor=hdr_color, linewidth=0, zorder=3))
    
    txt(ax, x + w/2, y + h - hh/2, title, fs=12.0, bold=True, color='white')
    
    body_h = h - hh
    step = body_h / (len(lines) + 1)
    for i, line in enumerate(lines):
        txt(ax, x + w/2, y + h - hh - step * (i + 1), line, fs=10.5, color='#1E293B')

def draw_prominent_arrow(ax, x1, y1, x2, y2, tag, desc, color):
    # Heavy, visible arrow shaft with large arrow head
    ax.annotate('', xy=(x2, y2), xytext=(x1, y1),
                arrowprops=dict(arrowstyle='-|>,head_width=0.45,head_length=0.7',
                                color=color, lw=3.2), zorder=4)
    
    # 2-line badge pill placed directly above the arrow midpoint
    mid_x = (x1 + x2) / 2
    mid_y = (y1 + y2) / 2
    
    # Clean pill badge
    label_text = f"{tag}\n{desc}"
    ax.text(mid_x, mid_y + 0.002, label_text,
            fontsize=9.5, color=color, ha='center', va='center',
            fontweight='bold', fontfamily=TNR, zorder=6,
            bbox=dict(boxstyle='round,pad=0.35,rounding_size=0.01',
                      facecolor='#FFFFFF', edgecolor=color, linewidth=1.5))

def draw_boundary(ax, x, y, w, h, label, color):
    ax.add_patch(patches.FancyBboxPatch(
        (x, y), w, h, boxstyle='round,pad=0.010,rounding_size=0.02',
        facecolor='none', edgecolor=color,
        linestyle='--', linewidth=2.5, zorder=1))
    
    ax.text(x + w/2, y + h + 0.016, label,
            fontsize=12.0, color='white', ha='center', va='bottom',
            fontweight='bold', fontfamily=TNR, zorder=6,
            bbox=dict(facecolor=color, edgecolor='none', boxstyle='round,pad=0.40'))

def generate_threat_model():
    fig, ax = plt.subplots(figsize=(24, 13.5), dpi=300)
    fig.patch.set_facecolor('#FFFFFF')
    ax.set_facecolor('#FFFFFF')
    
    ax.set_xlim(-0.01, 1.01)
    ax.set_ylim(-0.01, 1.01)
    ax.axis('off')

    # Main Diagram Header
    txt(ax, 0.50, 0.985,
        'CAPSTONE-2 (QARP) - STRIDE-QUANTUM THREAT MODEL',
        fs=18.0, bold=True, color='#0F172A')
    txt(ax, 0.50, 0.958,
        'Trust Boundaries  |  System Interfaces  |  Quantum Attack Vectors  |  Architectural Mitigations',
        fs=12.0, color='#475569')

    # Balanced Box & Gap Geometry (Arrow span = GAP = 0.065)
    BW  = 0.165   # Box width
    BH  = 0.205   # Box height
    GAP = 0.065   # Wide channel for large arrows and labels
    P   = 0.012   # Boundary padding

    CX = [
        0.035,
        0.035 + BW + P*2 + GAP,
        0.035 + (BW + P*2 + GAP)*2,
        0.035 + (BW + P*2 + GAP)*3,
    ]
    
    RY = [0.600, 0.370, 0.140]

    # Visual Palette
    M_HDR = '#C026D3'; M_BG = '#FDF4FF'; M_BND = '#A21CAF'  # TB-1: Magenta
    P_HDR = '#9333EA'; P_BG = '#FAF5FF'; P_BND = '#7E22CE'  # TB-2: Purple
    B_HDR = '#4F46E5'; B_BG = '#EEF2FF'; B_BND = '#3730A3'  # TB-3: Soft Indigo Blue
    V_HDR = '#6366F1'; V_BG = '#F8FAFC'; V_BND = '#4338CA'  # TB-4: Slate Indigo
    
    R_COL = '#E11D48'; R_BG = '#FFF1F2'                     # Attack red
    L_MIG = '#16A34A'; L_BG = '#F0FDF4'                     # Mitigation green

    # Boundaries
    span_h = (RY[0] + BH) - RY[2] + P*3.0
    draw_boundary(ax, CX[0]-P, RY[2]-P*1.5, BW+P*2, span_h, 'TB-1: Untrusted External Zone', M_BND)
    draw_boundary(ax, CX[1]-P, RY[2]-P*1.5, BW+P*2, span_h, 'TB-2: Ingress and Telemetry', P_BND)
    draw_boundary(ax, CX[2]-P, RY[2]-P*1.5, BW+P*2, span_h, 'TB-3: QARP Core Engine', B_BND)
    draw_boundary(ax, CX[3]-P, RY[2]-P*1.5, BW+P*2, span_h, 'TB-4: Cryptographic Vault', V_BND)

    # TB-1 Boxes
    draw_component_box(ax, CX[0], RY[0], BW, BH, 'Banking Clients and APIs',
                       ['Retail and Mobile Apps', 'Open Banking (FAPI OAuth 2.0)', 'Corporate REST Gateways'], M_HDR, M_BG)
    draw_component_box(ax, CX[0], RY[1], BW, BH, 'Interbank Network Nodes',
                       ['SWIFT Alliance Access', 'SEPA / Fedwire Clearing', 'Counterparty Ingress Tunnels'], M_HDR, M_BG)
    draw_component_box(ax, CX[0], RY[2], BW, BH, 'CRQC Threat Actor',
                       ['Harvest Now Decrypt Later', "Shor's & Grover's Algorithms", 'Fiber-tap Traffic Recorder'], M_HDR, M_BG)

    # TB-2 Boxes (Purple) - Edge WAF & Next-Gen Firewalls
    draw_component_box(ax, CX[1], RY[0], BW, BH, 'Edge WAF & Ingress Proxy',
                       ['F5 BIG-IP Advanced WAF', 'NGINX Plus / Envoy Gateway', 'TLS 1.2/1.3 & Hybrid KEM'], P_HDR, P_BG)
    draw_component_box(ax, CX[1], RY[1], BW, BH, 'Next-Gen Firewall (NGFW)',
                       ['Palo Alto / Check Point Gateways', 'Deep Packet Inspection (DPI)', 'MTU 1500B Middlebox Filter'], P_HDR, P_BG)
    draw_component_box(ax, CX[1], RY[2], BW, BH, 'Packet Sniffer & Message Bus',
                       ['Promiscuous PCAP Sniffer', 'Kafka ISO 20022 Stream', '1,000 to 15,000 TPS Ingress'], P_HDR, P_BG)

    # TB-3 Boxes
    draw_component_box(ax, CX[2], RY[0], BW, BH, 'Streaming & PCAP Dissector',
                       ['Pure-Python PCAP Parser', 'Cipher Suite Classifier', 'MTU Reassembly & Latency Calc'], B_HDR, B_BG)
    draw_component_box(ax, CX[2], RY[1], BW, BH, 'CBOM and Risk Engine',
                       ['CycloneDX 1.6 CBOM Export', 'STRIDE-Q & DREAD Scoring', 'NIST FIPS 203 / 204 / 205'], B_HDR, B_BG)
    draw_component_box(ax, CX[2], RY[2], BW, BH, 'Hardware Sizing & Threat Suite',
                       ['Gidney-Ekera Qubit Calculator', 'Side-Channel NTT/FIA Simulator', '+525% Payment HSM Engine'], B_HDR, B_BG)

    # TB-4 Boxes
    draw_component_box(ax, CX[3], RY[0], BW, BH, 'Enterprise KMS and TPM 2.0',
                       ['Platform Measurement (PCRs)', 'Key Lifecycle Governance', 'FIPS 140-3 Cryptographic Core'], V_HDR, V_BG)
    draw_component_box(ax, CX[3], RY[1], BW, BH, 'Payment HSM Clusters',
                       ['Thales payShield / Utimaco', 'PIN Translation & PEK Handling', 'LMK and ZMK Master Vaults'], V_HDR, V_BG)
    draw_component_box(ax, CX[3], RY[2], BW, BH, 'Settlement Ledger DB',
                       ['Immutable RTGS Ledger Records', 'AES-256 GCM Encrypted Data', 'DEK Wrapped with AES-256 KEK'], V_HDR, V_BG)

    # Prominent Arrows with Full Runway & 2-Line Labels
    def RE(c): return CX[c] + BW
    def LE(c): return CX[c]
    def MY(r): return RY[r] + BH/2

    # Row 0
    draw_prominent_arrow(ax, RE(0)+0.005, MY(0), LE(1)-0.005, MY(0), 'IF-1', 'HTTPS TLS Handshake', M_BND)
    draw_prominent_arrow(ax, RE(1)+0.005, MY(0), LE(2)-0.005, MY(0), 'IF-2', 'JSON & Zeek Telemetry', P_BND)
    draw_prominent_arrow(ax, RE(2)+0.005, MY(0), LE(3)-0.005, MY(0), 'IF-3', 'KMS Key Audit Query', B_BND)

    # Row 1
    draw_prominent_arrow(ax, RE(0)+0.005, MY(1), LE(1)-0.005, MY(1), 'IF-4', 'ISO 20022 pacs.008', M_BND)
    draw_prominent_arrow(ax, RE(1)+0.005, MY(1), LE(2)-0.005, MY(1), 'IF-5', 'CBOM Inventory Feed', P_BND)
    draw_prominent_arrow(ax, RE(2)+0.005, MY(1), LE(3)-0.005, MY(1), 'IF-6', 'PIN Block / PKCS#11', B_BND)

    # Row 2
    draw_prominent_arrow(ax, RE(0)+0.005, MY(2), LE(1)-0.005, MY(2), 'IF-7', 'Encrypted Traffic HNDL', M_BND)
    draw_prominent_arrow(ax, RE(1)+0.005, MY(2), LE(2)-0.005, MY(2), 'IF-8', 'Fragmented PQC Packets', P_BND)
    draw_prominent_arrow(ax, RE(2)+0.005, MY(2), LE(3)-0.005, MY(2), 'IF-9', 'DEK Wrap / KEK Vault', B_BND)

    # Bottom Summary Panels
    PY = 0.006
    PH = 0.115
    LX = 0.015
    RX = 0.515
    HDR_Y = PY + PH - 0.018
    ROW_STEP = 0.022

    # Left Panel: Attack Vectors
    ax.add_patch(patches.FancyBboxPatch(
        (0.005, PY), 0.490, PH, boxstyle='round,pad=0.008,rounding_size=0.012',
        facecolor=R_BG, edgecolor=R_COL, linewidth=2.0, zorder=2))
    ax.text(LX, HDR_Y, 'QUANTUM ATTACK VECTORS (STRIDE-QUANTUM)',
            fontsize=12.0, color=R_COL, fontweight='bold', fontfamily=TNR, va='top', ha='left')
    
    attacks = [
        'IF-1 / IF-7  Information Disclosure: Shor cracks ECDH X25519; enables HNDL session playback.',
        'IF-4         Spoofing & Tampering: Shor factors RSA-2048 to forge pacs.008 settlement XMLs.',
        'IF-8         Denial of Service: Oversized PQC keys (>1500 B) trigger NGFW middlebox buffer drops & HSM stalls.',
        'TB-4 (int.)  Elevation of Privilege: Grover ~2^64 ops cracks 128-bit KEKs, exposing database DEKs.',
    ]
    for i, line in enumerate(attacks):
        ax.text(LX, HDR_Y - ROW_STEP*(i+1), line, fontsize=10.5, color='#881337', fontfamily=TNR, va='top', ha='left')

    # Right Panel: Mitigations
    ax.add_patch(patches.FancyBboxPatch(
        (0.505, PY), 0.490, PH, boxstyle='round,pad=0.008,rounding_size=0.012',
        facecolor=L_BG, edgecolor=L_MIG, linewidth=2.0, zorder=2))
    ax.text(RX, HDR_Y, 'QARP ARCHITECTURAL MITIGATIONS (IMPLEMENTED IN app.py)',
            fontsize=12.0, color=L_MIG, fontweight='bold', fontfamily=TNR, va='top', ha='left')
    
    mitigations = [
        'IF-1 / IF-7  Terminate F5 WAF / NGINX Hybrid TLS 1.3 (ML-KEM-768 + X25519) dual key encapsulation.',
        'IF-4         Dual-sign ISO 20022 schemas with NIST FIPS 204 (ML-DSA-65) and AES-256 GCM tags.',
        'IF-8         Tune Palo Alto NGFW reassembly buffers & scale Payment HSMs (+525%) to prevent dropouts.',
        'TB-4 (int.)  Enforce AES-256 Key Wrap (NIST SP 800-38F), TPM 2.0 PCR attestation, and FIPS 140-3 HSM isolation.',
    ]
    for i, line in enumerate(mitigations):
        ax.text(RX, HDR_Y - ROW_STEP*(i+1), line, fontsize=10.5, color='#14532D', fontfamily=TNR, va='top', ha='left')

    # Save outputs
    svg_path = r'D:\Anirban\000000_Mtech Reva\CapStone_2\Threat Model .svg'
    png_path = r'D:\Anirban\000000_Mtech Reva\CapStone_2\qarp_threat_model_HQ.png'
    
    plt.savefig(svg_path, format='svg', facecolor='white', bbox_inches='tight', pad_inches=0.1)
    plt.savefig(png_path, format='png', dpi=300, facecolor='white', bbox_inches='tight', pad_inches=0.1)
    print(f"Success:\n1. SVG: {svg_path}\n2. PNG: {png_path}")

if __name__ == '__main__':
    generate_threat_model()