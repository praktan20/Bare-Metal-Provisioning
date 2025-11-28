#!/usr/bin/env python3
import argparse, os
TFTP_ROOT = os.environ.get("TFTP_HTTP_ROOT","/var/www/html/ipxe")
parser = argparse.ArgumentParser()
parser.add_argument("--mac", required=True)
parser.add_argument("--image-url", required=True)
args = parser.parse_args()
macfile = args.mac.replace(":", "-").lower()
content = f"""#!ipxe
dhcp
set base-url {args.image_url}
kernel ${'{'}base-url{'}'}/vmlinuz ip=dhcp autoinstall ds=nocloud-net;s=${'{'}base-url{'}'}/kickstarts/{macfile}/
initrd ${'{'}base-url{'}'}/initrd
boot
"""
os.makedirs(TFTP_ROOT, exist_ok=True)
with open(os.path.join(TFTP_ROOT, macfile+".ipxe"), "w") as f:
    f.write(content)
print("Wrote iPXE config for", args.mac)
