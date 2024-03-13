import scapy.all as scapy

def process_packet(packet):
    """
    Process captured packets and display relevant information.
    :param packet: Captured packet.
    """
    if packet.haslayer(scapy.IP):
        src_ip = packet[scapy.IP].src
        dst_ip = packet[scapy.IP].dst
        protocol = packet[scapy.IP].proto
        print(f"Source IP: {src_ip} | Destination IP: {dst_ip} | Protocol: {protocol}")

        if packet.haslayer(scapy.Raw):
            payload = packet[scapy.Raw].load
            print(f"Payload: {payload.decode(errors='ignore')}")  # Decode payload to string

def main():
    try:
        interface = input("Enter the network interface (e.g., eth0, wlan0): ")
        print("Sniffing packets... Press Ctrl+C to stop.")
        scapy.sniff(iface=interface, store=False, prn=process_packet)
    except KeyboardInterrupt:
        print("\nPacket sniffing stopped by user.")

if __name__ == "__main__":
    main()
