#!/bin/bash
# Licensed under GPLv2
# Copyright cbk914@riseup.net 2018

read -p "Network interface? " interface
cd /tmp/
echo "[*] Downloading Suricata Stable version..."
wget https://www.openinfosecfoundation.org/download/suricata-current.tar.gz
echo "[*] Uncompressing..."
tar zvxf suricata-current.tar.gz
echo "[*] Installing dependencies..."
apt update
apt-get install build-essential pkg-config libpcre++-dev libyaml-dev libpcap0.8-dev zlib1g-dev libpcre3 libpcre3-dbg libpcre3-dev build-essential libpcap-dev   libnet1-dev libyaml-0-2 libyaml-dev pkg-config zlib1g zlib1g-dev libcap-ng-dev libcap-ng0 make libmagic-dev libjansson-dev libnss3-dev libgeoip-dev liblua5.1-dev libhiredis-dev libevent-dev libnetfilter-queue-dev libnetfilter-queue1 libnetfilter-log-dev libnetfilter-log1 libnfnetlink-dev libnfnetlink0
echo "[*] Installing Suricata..."
cd suricata-current
./configure --enable-geoip
make
make install-full
ldconfig
echo "[*] Latest adjustments..."
# Disable LRO/GRO
ethtool -K $interface gro off lro off

/usr/local/bin/suricata -c /usr/local/etc/suricata/suricata.yaml -i $interface --
