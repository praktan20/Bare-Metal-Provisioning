#!/usr/bin/env python3
import sys, os, requests

NB_URL = os.environ['NETBOX_URL']
NB_TOKEN = os.environ['NETBOX_TOKEN']

def get_device(nb_id):
    r = requests.get(f"{NB_URL}/api/dcim/devices/{nb_id}/", headers={"Authorization": f"Token {NB_TOKEN}"}, timeout=10)
    r.raise_for_status()
    return r.json()

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: netbox_validate.py <device_id>")
        sys.exit(2)
    node_id = sys.argv[1]
    dev = get_device(node_id)
    status = dev.get('status') or dev.get('device_role')
    # Minimal validation; expand per site policy
    if not dev:
        print("Device not found")
        sys.exit(2)
    # example checks:
    if not dev.get('primary_ip4') and not dev.get('primary_ip'):
        print("No management IP found")
        sys.exit(3)
    if 'interfaces' in dev and len(dev['interfaces']) == 0:
        print("No interfaces configured")
        sys.exit(4)
    print("OK")
