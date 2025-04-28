from scapy.all import ICMP,sr1,IP,TCP
from ipaddress import IPv4Network

rangeIP = "192.168.1.0/24"
network = IPv4Network(rangeIP)
print(f"Scanning network: {network.hosts()}")
upHosts = []
for host in network:
    if (host in (network.network_address,network.broadcast_address)):
        continue
    resp = sr1(IP(dst=str(host))/ICMP(),timeout=2,verbose=0)
    if resp is not None:
        upHosts.append(host)
        print(f"Host {host} is up")