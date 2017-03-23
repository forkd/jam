#!/bin/bash
#knock-knock.sh
#
# This code should be used with a firewall using
# multiport port knocking.  In this case, the 
# sequence of ports configured to allow access is:
# 19846, 20113, and 19701.
#
# AUTHOR: José Lopes Oliveira Jr. <indiecode.com.br>
#
## 

PORTS="19846 20113 19701"

USER="$(echo $1 | cut -d@ -f1)"
TARGET="$(echo $1 | cut -d@ -f2)"

for port in $PORTS; do
    nc -w 1 "$TARGET" "$port"
done

ssh "$USER"@"$TARGET"

