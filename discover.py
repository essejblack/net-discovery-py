from scapy.all import ICMP,sr1,IP
from ipaddress import IPv4Network
import threading

rangeIP = "192.168.1.0/24"
hosts = list(IPv4Network(rangeIP).hosts())
upHosts = []
        
def scan_host(host):
    resp = sr1(IP(dst=str(host))/ICMP(),timeout=2,verbose=0)
    if resp is not None:
        upHosts.append(host)
        print(f"Host {host} is up")

    
def main():
    threads = []
    print(f"Scanning network: {rangeIP}")
    hostsCount = len(hosts)
    
    for i in range(hostsCount):
        t = threading.Thread(target=scan_host, args=(hosts[i],))
        t.start()
        threads.append(t)

    for t in threads:
        t.join()
            
if __name__ == "__main__":
    main()