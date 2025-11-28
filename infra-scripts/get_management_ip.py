#!/usr/bin/env python3
import sys, os, requests
NB_URL = os.environ['NETBOX_URL']; NB_TOKEN = os.environ['NETBOX_TOKEN']
if len(sys.argv) < 2:
    print("0.0.0.0"); exit(1)
node_id = sys.argv[1]
r = requests.get(f"{NB_URL}/api/dcim/devices/{node_id}/", headers={"Authorization": f"Token {NB_TOKEN}"}, timeout=10)
r.raise_for_status()
dev = r.json()
mgmt = dev.get('primary_ip4') or dev.get('primary_ip')
if mgmt:
    print(mgmt.get('address').split('/')[0])
else:
    print("0.0.0.0")
