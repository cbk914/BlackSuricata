#!/bin/bash
# Network Interfaces tunning for Suricata
# Licensed under GPLv2
# Copyright cbk914@riseup.net 2018
echo "[*] Network Interfaces Status:"
NETSTATUS="ip -o link show|awk '{print $2,$9}'"
echo $NETSTATUS
INTERFACE=`nmcli --terse --fields DEVICE dev status| awk '{print $1}'`
# Number of packets to process simultaneously
# 1024 x core is OK
# If Suricata is compiled with CUDA, set this value to 60000 or higher
echo "max-pending-packets = 4096" >> /etc/suricata/suricata.yaml
# Disable Offloading (not compatible with all net interfaces)
ethtool -K $INTERFACE lro off
ethtool -K $INTERFACE gro off
