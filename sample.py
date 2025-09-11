from scapy.all import ARP, Ether, srp
import socket

def scan_networks(network):
    packet = Ether(dst="ff:ff:ff:ff:ff:ff") / ARP(pdst=network)
    answered, _ = srp(packet, timeout=2, iface="en0", verbose=0)

    print("IP           MAC              Hostname")
    for _, r in answered:
        ip = r[ARP].psrc
        mac = r[Ether].src
        try:
            hostname = socket.gethostbyaddr(ip)[0]
        except socket.herror:
            hostname = "Unknown"
        print(f"{ip:15} {mac:17} {hostname}")

scan_networks("172.16.0.0/16")
