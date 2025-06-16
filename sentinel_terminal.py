from device_scanner import scan_network
from packet_sniffer import sniff_packets
from analyzer import is_encrypted
from report_generator import generate_report
from threat_checker import check_ip_threat

def run_terminal():
    print("💀 Smart But Not Silent: The Sentinel Terminal 💀\n")
    devices = scan_network("192.168.0.0/24")

    sniff_choice = input("Sniff packets now? (y/n): ").lower()
    if sniff_choice == 'y':
        sniff_packets()

    print("\n⚠️ Generating Report...")
    sample_data = {
        "devices": devices,
        "suspicious_ips": ["203.0.113.5", "198.51.100.10"]
    }

    generate_report(sample_data)

if __name__ == "__main__":
    run_terminal()