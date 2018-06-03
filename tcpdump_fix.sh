#!/bin/bash
# CopyLeft 2018 by cbk
setcap cap_net_raw,cap_net_admin=eip /usr/sbin/tcpdump
getcap /usr/sbin/tcpdump
echo "User can now run tcpdump"

