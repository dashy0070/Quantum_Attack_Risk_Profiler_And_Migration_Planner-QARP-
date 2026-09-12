"""
Sample Banking PCAP Generator
Creates genuine binary PCAP files containing TLS Handshakes and HTTP access traffic
for testing QARP Live Packet Capture Ingestion & Quantum Profiling.
"""

import struct
import time

def create_tls_client_hello_packet(src_ip, dst_ip, src_port, dst_port, server_name, cipher_suite_code):
    # 1. TLS ClientHello Payload
    sni_bytes = server_name.encode('utf-8')
    # Server Name Extension
    sni_ext = struct.pack(
        ">HHHB",
        0x0000, # Extension: server_name (0)
        len(sni_bytes) + 5, # Ext length
        len(sni_bytes) + 3, # Server Name list length
        0x00 # Server Name Type: host_name (0)
    ) + struct.pack(">H", len(sni_bytes)) + sni_bytes

    # Supported Groups (Elliptic Curves) Extension (X25519, secp256r1)
    curves_ext = struct.pack(">HHH2H", 0x000a, 6, 4, 0x001d, 0x0017) # X25519, secp256r1

    extensions = sni_ext + curves_ext
    ext_length = len(extensions)

    # ClientHello body
    client_version = 0x0303 # TLS 1.2 / TLS 1.3
    random_bytes = b"\x5a\x2b\x8c\x11" * 8 # 32 bytes random
    session_id = b"\x00" # 0 length session id
    cipher_suites = struct.pack(">HH", 2, cipher_suite_code)
    compression_methods = b"\x01\x00" # 1 method: null (0)

    ch_body = struct.pack(">H", client_version) + random_bytes + session_id + cipher_suites + compression_methods + struct.pack(">H", ext_length) + extensions
    
    # Handshake Header (Type 1 = ClientHello, 3-byte length)
    hs_header = struct.pack(">B", 0x01) + struct.pack(">I", len(ch_body))[1:] # 1 byte type + 3 bytes len
    tls_handshake = hs_header + ch_body

    # TLS Record Layer (Type 0x16 = Handshake, Version 0x0301, 2-byte length)
    tls_record = struct.pack(">BHH", 0x16, 0x0301, len(tls_handshake)) + tls_handshake

    # 2. TCP Header (20 bytes)
    tcp_hdr = struct.pack(
        ">HHIIBBHHH",
        src_port, dst_port,
        100000, 0,
        (5 << 4), 0x18, # 20 bytes hdr (5*4), ACK + PSH flags
        65535, 0, 0
    )

    # 3. IPv4 Header (20 bytes)
    ip_src_parts = [int(p) for p in src_ip.split('.')]
    ip_dst_parts = [int(p) for p in dst_ip.split('.')]
    ip_total_len = 20 + len(tcp_hdr) + len(tls_record)
    ip_hdr = struct.pack(
        ">BBHHHBBH4B4B",
        0x45, 0x00, ip_total_len,
        54321, 0x4000,
        64, 6, 0, # TTL 64, Proto 6 (TCP), checksum 0
        *ip_src_parts, *ip_dst_parts
    )

    # 4. Ethernet Header (14 bytes)
    eth_hdr = bytes.fromhex("005056c00001") + bytes.fromhex("005056c00008") + struct.pack(">H", 0x0800)

    return eth_hdr + ip_hdr + tcp_hdr + tls_record


def generate_banking_pcap(filepath="sample_banking_traffic.pcap"):
    """
    Generates a full binary PCAP file with simulated live TLS banking ingress traffic.
    """
    packets = []
    
    # Banking Flows
    flows = [
        {"src_ip": "10.0.1.50", "dst_ip": "192.168.10.100", "sport": 49152, "dport": 443, "sni": "settlement.core-bank.internal/v1/credit-transfer", "cipher": 0xC02F}, # TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256
        {"src_ip": "10.0.2.75", "dst_ip": "192.168.10.101", "sport": 49153, "dport": 443, "sni": "rtgs.instant-clearing.fed/v1/clearing", "cipher": 0xC02C}, # TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384
        {"src_ip": "10.0.3.88", "dst_ip": "192.168.10.102", "sport": 49154, "dport": 443, "sni": "openbanking.fapi-auth.bank/v1/consent", "cipher": 0xC02F}, # TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256
        {"src_ip": "10.0.4.92", "dst_ip": "192.168.10.103", "sport": 49155, "dport": 443, "sni": "swift-gateway.iso20022.net/v1/mt103", "cipher": 0x002F}, # TLS_RSA_WITH_AES_128_CBC_SHA
        {"src_ip": "10.0.5.12", "dst_ip": "192.168.10.104", "sport": 49156, "dport": 443, "sni": "identity.fapi2.auth/v1/token", "cipher": 0xC02B}, # TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256
        {"src_ip": "10.0.6.44", "dst_ip": "192.168.10.105", "sport": 49157, "dport": 443, "sni": "pos-switch.iso8583.switch/v1/cards", "cipher": 0x009D}  # TLS_RSA_WITH_AES_256_GCM_SHA384
    ]

    base_time = int(time.time())

    for idx, f in enumerate(flows):
        pkt_bytes = create_tls_client_hello_packet(f["src_ip"], f["dst_ip"], f["sport"], f["dport"], f["sni"], f["cipher"])
        packets.append((base_time + idx, idx * 150000, pkt_bytes))

    # PCAP Global Header (24 bytes)
    # Magic 0xa1b2c3d4, Major 2, Minor 4, Zone 0, Sigfigs 0, Snaplen 65535, Linktype 1 (Ethernet)
    global_hdr = struct.pack("<IHHiIII", 0xa1b2c3d4, 2, 4, 0, 0, 65535, 1)

    with open(filepath, "wb") as f:
        f.write(global_hdr)
        for ts_sec, ts_usec, pkt in packets:
            # Packet Header (16 bytes): ts_sec, ts_usec, incl_len, orig_len
            pkt_hdr = struct.pack("<IIII", ts_sec, ts_usec, len(pkt), len(pkt))
            f.write(pkt_hdr)
            f.write(pkt)

    print(f"[SUCCESS] Generated valid binary PCAP at: {filepath} ({len(packets)} TLS Handshake packets)")

if __name__ == "__main__":
    generate_banking_pcap("sample_banking_traffic.pcap")
    generate_banking_pcap("demo/sample_banking_traffic.pcap")
