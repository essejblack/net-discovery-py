# Python Network Discovery Tool (Scapy + ipaddress)

This project is a simple network discovery scanner written in Python.  
It checks which IP addresses are **up (alive)** and **down (no response)** on a given subnet.

## How it Works

- Uses `ipaddress` to generate all IPs in a subnet.
- Sends ICMP Echo Requests (ping) using Scapy.
- Detects which hosts respond and which do not.

## Requirements

- Python 3
- scapy library
- ipaddress library

Install scapy:

```bash
pip install scapy
```

Install ipaddress:

```bash
pip install ipaddress
```
Run Script

```bash
python discover.py
```

## Notes

- Run the script as administrator or root to avoid ICMP permission errors.
- Scanning large networks (like `/16` or `/8`) will take more time.
- Adjust the timeout if needed for slower networks.
- Only scan networks you have permission to test.