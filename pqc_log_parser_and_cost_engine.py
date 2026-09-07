"""
PQC Banking Migration Profiler: Log Parser & Capacity Analysis Engine
Master's Capstone Artifact: Internal Banking Settlement REST/TLS Workloads (Platform-Agnostic / On-Premise)
"""

import json
import math
from typing import List, Dict, Any

# NIST FIPS 203 / 204 Parameter Constants (in Bytes) and Relative CPU Costs
CRYPTO_SPECS = {
    # Legacy Asymmetric (Vulnerable to Shor's Algorithm)
    "RSA-2048": {
        "type": "asymmetric",
        "pubkey_bytes": 256,
        "sig_enc_bytes": 256,
        "cpu_cost_multiplier": 1.0,  # Baseline
        "shor_vulnerable": True
    },
    "ECDSA-P256": {
        "type": "asymmetric",
        "pubkey_bytes": 64,
        "sig_enc_bytes": 64,
        "cpu_cost_multiplier": 0.45,
        "shor_vulnerable": True
    },
    # NIST PQC Standards
    "ML-KEM-768": {
        "type": "kem",
        "pubkey_bytes": 1184,
        "sig_enc_bytes": 1088,
        "cpu_cost_multiplier": 0.20, # Very fast lattice vector matrix operations
        "shor_vulnerable": False
    },
    "ML-DSA-65": {
        "type": "signature",
        "pubkey_bytes": 1952,
        "sig_enc_bytes": 3300,
        "cpu_cost_multiplier": 1.35, # Heavier verification & polynomial operations
        "shor_vulnerable": False
    },
    # Symmetric (Evaluated against Grover's algorithm: security halved)
    "AES-128-GCM": {
        "type": "symmetric",
        "key_bits": 128,
        "post_quantum_security_bits": 64, # INSECURE under Grover
        "shor_vulnerable": False,
        "grover_vulnerable": True
    },
    "AES-256-GCM": {
        "type": "symmetric",
        "key_bits": 256,
        "post_quantum_security_bits": 128, # SECURE under Grover
        "shor_vulnerable": False,
        "grover_vulnerable": False
    }
}

# Enterprise On-Premise / Datacenter Hardware Baseline (FIPS 140-3 PCIe/Network Payment HSMs & Server Infrastructure)
ENTERPRISE_HARDWARE_CONSTANTS = {
    "bandwidth_cost_per_gb": 0.05,            # Datacenter interconnect / transit bandwidth cost per GB
    "server_core_monthly_amortized": 45.0,    # Server compute core monthly amortized CapEx/OpEx
    "hsm_appliance_monthly_amortized": 1200.0,# Monthly amortized cost per high-assurance Payment HSM unit (hardware + maintenance)
    "hsm_baseline_rsa_ops_sec": 1200,         # Max RSA-2048 operations per second per HSM appliance core/unit
    "hsm_estimated_pqc_ops_sec": 180          # PQC throughput due to lattice rejection sampling & polynomial complexity (~85% deficit)
}


class PQCLogParserAndAnalyzer:
    """
    Parses structured JSON/REST log outputs from enterprise API gateways
    (e.g., Kong, Nginx, HAProxy, Envoy, F5 BIG-IP) and computes quantum vulnerability,
    MTU packet fragmentation risks, and hardware appliance scaling deltas.
    """

    def __init__(self, target_kem: str = "ML-KEM-768", target_sig: str = "ML-DSA-65"):
        self.target_kem = target_kem
        self.target_sig = target_sig

    def parse_log_entry(self, log_dict: Dict[str, Any]) -> Dict[str, Any]:
        """
        Parses a single JSON API gateway log entry.
        Expected keys: endpoint, tls_cipher, client_cert_type, request_size_bytes,
        response_size_bytes, latency_ms, tps
        """
        endpoint = log_dict.get("endpoint", "/api/v1/unknown")
        tls_cipher = log_dict.get("tls_cipher", "TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256")
        payload_bytes = log_dict.get("request_size_bytes", 500) + log_dict.get("response_size_bytes", 500)
        tps = log_dict.get("tps", 1000)
        base_latency_ms = log_dict.get("latency_ms", 12.0)

        # 1. Identify Asymmetric and Symmetric Components
        legacy_asym = "RSA-2048" if "RSA" in tls_cipher else "ECDSA-P256"
        symmetric_algo = "AES-128-GCM" if "AES_128" in tls_cipher else "AES-256-GCM"

        # 2. Cryptographic Sizing Computations
        legacy_key_bytes = CRYPTO_SPECS[legacy_asym]["pubkey_bytes"]
        legacy_sig_bytes = CRYPTO_SPECS[legacy_asym]["sig_enc_bytes"]
        legacy_handshake_bytes = legacy_key_bytes + legacy_sig_bytes

        pqc_key_bytes = CRYPTO_SPECS[self.target_kem]["pubkey_bytes"]
        pqc_sig_bytes = CRYPTO_SPECS[self.target_sig]["sig_enc_bytes"]
        pqc_handshake_bytes = pqc_key_bytes + pqc_sig_bytes

        # 3. Ethernet MTU Packet Fragmentation Analysis (Standard MTU = 1500 bytes)
        legacy_packets = math.ceil(legacy_handshake_bytes / 1500)
        pqc_packets = math.ceil(pqc_handshake_bytes / 1500)
        fragmentation_risk = pqc_packets > 1

        # Estimated network latency inflation from multi-packet reassembly & TCP window traversals
        additional_latency_ms = max(0.0, (pqc_packets - legacy_packets) * 2.2)
        projected_latency_ms = round(base_latency_ms + additional_latency_ms, 2)

        # 4. Data Transfer Volume Calculations (Monthly at 24/7 sustained TPS)
        seconds_per_month = 30 * 24 * 3600
        monthly_requests = tps * seconds_per_month

        monthly_legacy_traffic_gb = (monthly_requests * legacy_handshake_bytes) / (1024 ** 3)
        monthly_pqc_traffic_gb = (monthly_requests * pqc_handshake_bytes) / (1024 ** 3)
        monthly_traffic_delta_gb = monthly_pqc_traffic_gb - monthly_legacy_traffic_gb

        # 5. Infrastructure Capacity & Hardware Cost Model
        bandwidth_cost_delta = monthly_traffic_delta_gb * ENTERPRISE_HARDWARE_CONSTANTS["bandwidth_cost_per_gb"]

        # Enterprise Payment HSM cluster sizing calculation
        hsm_legacy_needed = max(2, math.ceil(tps / ENTERPRISE_HARDWARE_CONSTANTS["hsm_baseline_rsa_ops_sec"]))
        hsm_pqc_needed = max(2, math.ceil(tps / ENTERPRISE_HARDWARE_CONSTANTS["hsm_estimated_pqc_ops_sec"]))
        monthly_hsm_legacy_cost = hsm_legacy_needed * ENTERPRISE_HARDWARE_CONSTANTS["hsm_appliance_monthly_amortized"]
        monthly_hsm_pqc_cost = hsm_pqc_needed * ENTERPRISE_HARDWARE_CONSTANTS["hsm_appliance_monthly_amortized"]
        monthly_hsm_delta_cost = monthly_hsm_pqc_cost - monthly_hsm_legacy_cost

        total_monthly_infrastructure_delta_usd = round(bandwidth_cost_delta + monthly_hsm_delta_cost, 2)
        hsm_capacity_shortfall_pct = round(((hsm_pqc_needed - hsm_legacy_needed) / hsm_legacy_needed) * 100, 1)

        return {
            "endpoint": endpoint,
            "tps": tps,
            "detected_legacy_asym": legacy_asym,
            "detected_symmetric": symmetric_algo,
            "grover_warning": CRYPTO_SPECS[symmetric_algo]["grover_vulnerable"],
            "shor_vulnerable": CRYPTO_SPECS[legacy_asym]["shor_vulnerable"],
            "legacy_handshake_bytes": legacy_handshake_bytes,
            "pqc_handshake_bytes": pqc_handshake_bytes,
            "packet_fragmentation_factor": f"{legacy_packets} pkt -> {pqc_packets} pkts",
            "base_latency_ms": base_latency_ms,
            "projected_pqc_latency_ms": projected_latency_ms,
            "sla_breached_50ms": projected_latency_ms > 50.0,
            "monthly_traffic_increase_gb": round(monthly_traffic_delta_gb, 2),
            "monthly_infrastructure_cost_delta_usd": total_monthly_infrastructure_delta_usd,
            "hsm_hardware_cluster_scaling": f"{hsm_legacy_needed} units -> {hsm_pqc_needed} units (+{hsm_capacity_shortfall_pct}%)"
        }


# Demonstration Execution with Typical Banking REST JSON Log Samples
if __name__ == "__main__":
    raw_json_logs = [
        {
            "timestamp": "2026-09-03T10:14:22Z",
            "endpoint": "/v1/settlement/credit-transfer",
            "tls_cipher": "TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256",
            "request_size_bytes": 620,
            "response_size_bytes": 410,
            "latency_ms": 14.5,
            "tps": 4500
        },
        {
            "timestamp": "2026-09-03T10:14:23Z",
            "endpoint": "/v1/clearing/rtgs-instant",
            "tls_cipher": "TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384",
            "request_size_bytes": 890,
            "response_size_bytes": 520,
            "latency_ms": 8.2,
            "tps": 8000
        },
        {
            "timestamp": "2026-09-03T10:14:24Z",
            "endpoint": "/v1/ledger/batch-reconciliation",
            "tls_cipher": "TLS_RSA_WITH_AES_128_CBC_SHA",
            "request_size_bytes": 4500,
            "response_size_bytes": 12000,
            "latency_ms": 46.0,
            "tps": 1200
        }
    ]

    analyzer = PQCLogParserAndAnalyzer()
    print("=== PQC BANKING LOG ANALYSIS & CAPACITY RESULTS (ON-PREMISE / ENTERPRISE) ===")
    for log in raw_json_logs:
        result = analyzer.parse_log_entry(log)
        print(json.dumps(result, indent=2))
