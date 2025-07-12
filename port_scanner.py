import socket

def scan_ports(target):
    print(f"\n[+] Scanning ports on {target}...")
    open_ports = []
    for port in range(1, 1025):  # Scan 1-1024
        try:
            sock = socket.socket()
            sock.settimeout(0.5)
            result = sock.connect_ex((target, port))
            if result == 0:
                open_ports.append(port)
            sock.close()
        except:
            pass
    print("[+] Open Ports:")
    for port in open_ports:
        print(f" - Port {port}")
