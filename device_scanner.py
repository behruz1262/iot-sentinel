import subprocess
import re

def scan_network(subnet="192.168.0.0/24"):
    print(f"🔍 Scanning network: {subnet}")
    result = subprocess.run(["nmap", "-sn", subnet], capture_output=True, text=True)
    devices = re.findall(r"Nmap scan report for (.*?)\n", result.stdout)
    print("📡 Devices found:")
    for d in devices:
        print(f" - {d}")
    return devices