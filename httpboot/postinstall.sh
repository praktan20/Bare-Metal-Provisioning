#!/bin/bash
# postinstall.sh <node_name>
NODE_NAME=$1
# basic sysctl + kube deps (example)
modprobe br_netfilter
echo br_netfilter > /etc/modules-load.d/k8s.conf
cat > /etc/sysctl.d/k8s.conf <<EOF
net.bridge.bridge-nf-call-ip6tables = 1
net.bridge.bridge-nf-call-iptables = 1
EOF
sysctl --system

# signal collector that postinstall finished (collector must accept this)
curl -sS http://provision-collector.internal/api/hosts/${NODE_NAME}/postinstall -d '{"status":"postinstalled"}' -H "Content-Type: application/json"
