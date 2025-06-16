from scapy.all import TCP

def is_encrypted(packet):
    try:
        if TCP in packet and (packet[TCP].dport == 443 or packet[TCP].sport == 443):
            return True
        return False
    except:
        return False