from scapy.all import ARP, Ether, srp

def scan_networks(network):
    print("Active hosts :")
    packet = Ether(dst="ff:ff:ff:ff:ff:ff") / ARP(pdst=network)
    ans, _ = srp(packet, timeout=2, iface="en0", verbose=0)

    for _, received in ans:
        if received.haslayer(ARP):  
            print(f"IP: {received[ARP].psrc}, MAC: {received[ARP].hwsrc}")
scan_networks("172.16.0.0/16")