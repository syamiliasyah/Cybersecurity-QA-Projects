import ipaddress

def analyze_ip(ip_with_subnet):
    print(f"--- Network Analysis for: {ip_with_subnet} ---")
    try:
        network = ipaddress.ip_network(ip_with_subnet, strict=False)
        print(f"Network Address: {network.network_address}")
        print(f"Broadcast Address: {network.broadcast_address}")
        print(f"Subnet Mask: {network.netmask}")
        print(f"Total Usable Hosts: {network.num_addresses - 2}")
    except ValueError as e:
        print(f"Invalid IP/Subnet format: {e}")

if __name__ == "__main__":
    # Test CCNA network logic
    sample_cidr = "192.168.1.50/24"
    analyze_ip(sample_cidr)
