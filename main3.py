from modules import port_scanner, brute_forcer, vuln_scanner

def banner():
    print("\n--- PENTEST TOOLKIT ---")
    print("1. Port Scanner")
    print("2. Brute Forcer (HTTP Basic Auth)")
    print("3. Vulnerability Scanner (SQLi/XSS)")
    print("0. Exit")

if __name__ == "__main__":
    while True:
        banner()
        choice = input("Select a module: ")
        if choice == "1":
            target = input("Enter target IP: ")
            port_scanner.scan_ports(target)
        elif choice == "2":
            url = input("Enter login URL (with Basic Auth): ")
            username = input("Username: ")
            wordlist = input("Path to password wordlist: ")
            brute_forcer.http_brute_force(url, username, wordlist)
        elif choice == "3":
            url = input("Enter target URL: ")
            vuln_scanner.scan(url)
        elif choice == "0":
            print("Exiting...")
            break
        else:
            print("Invalid choice!")
