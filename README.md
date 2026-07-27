# Remote Sunrise Helper for Windows 2026.14 - Unauthenticated Directory Creation
Remote Sunrise Helper for Windows 2026.14 - Unauthenticated Directory Creation
```
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
# for the new versions is: 
# ssl-cert: Subject: commonName=SecureHTTPServer/organizationName=Remote Sunrise LTD/countryName=US
# Issuer: commonName=SecureHTTPServer/organizationName=Remote Sunrise LTD/countryName=US

```

## Syntax
```
Usage: poc.py <target_ip> <api_port> <path>
Example: poc.py 192.168.1.103 49737 'C:/Users/Public/backdoor'
Example: poc.py 192.168.1.103 49737 '%USERPROFILE%/Desktop/newfolder'

```
<img width="900" height="90" alt="image" src="https://github.com/user-attachments/assets/408cd07f-f540-4117-b921-364b68292408" />
