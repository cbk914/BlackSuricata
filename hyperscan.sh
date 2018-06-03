#!/bin/bash
# Hyperscan installation
echo "[+] Installing dependencies..."
apt update
apt install libboost-dev make ragel 
cd /tmp
echo "[+] Downloading Hyperscan..."
git clone https://github.com/01org/hyperscan
cd hyperscan
mkdir build
cd build
cmake -DBUILD_STATIC_AND_SHARED=1 ../
echo "[+] Compilling..."
make 
make install
echo "/usr/local/lib" | sudo tee --append /etc/ld.so.conf.d/usrlocal.conf
ldconfig
echo "[*] All done"
exit 0
