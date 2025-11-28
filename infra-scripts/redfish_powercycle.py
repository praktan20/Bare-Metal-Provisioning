#!/usr/bin/env python3
import argparse, requests, urllib3
urllib3.disable_warnings()

def power_cycle(host, user, passwd):
    base = f"https://{host}/redfish/v1/Systems/1/Actions/ComputerSystem.Reset"
    payload = {"ResetType":"ForceRestart"}
    r = requests.post(base, json=payload, auth=(user, passwd), verify=False, timeout=10)
    r.raise_for_status()
    print("Power cycle triggered")

if __name__ == "__main__":
    p=argparse.ArgumentParser()
    p.add_argument("--host", required=True)
    p.add_argument("--user", required=True)
    p.add_argument("--pass", dest="passwd", required=True)
    args = p.parse_args()
    power_cycle(args.host, args.user, args.passwd)
