from scapy.all import sniff, IP, TCP, UDP
from datetime import datetime

def process_packet(packet):
    if IP in packet:
        ip_layer = packet[IP]
        print(f"[{datetime.now().strftime('%H:%M:%S')}] {ip_layer.src} → {ip_layer.dst} | Proto: {packet.proto}")

def sniff_packets(interface="wlan0"):
    print(f"🛰️ Starting packet capture on {interface}...")
    sniff(prn=process_packet, store=0)