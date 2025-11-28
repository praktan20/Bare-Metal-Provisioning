#!/usr/bin/env python3
import argparse, time, requests
parser = argparse.ArgumentParser()
parser.add_argument("--hostname", required=True)
parser.add_argument("--timeout", type=int, default=1800)
args = parser.parse_args()

start = time.time()
while time.time() - start < args.timeout:
    try:
        r = requests.get(f"http://provision-collector.internal/api/hosts/{args.hostname}/status", timeout=5)
        if r.status_code == 200 and r.json().get("status") == "installed":
            print("Provision complete")
            exit(0)
    except Exception:
        pass
    time.sleep(10)
print("Timeout waiting for provision")
exit(1)
