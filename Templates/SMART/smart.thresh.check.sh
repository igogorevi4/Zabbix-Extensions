#!/bin/bash
# add zabbix-user to /etc/sudoers to execute this scpirt without sudo
# zabbix ALL= (ALL) NOPASSWD: /usr/sbin/smartctl, /etc/zabbix/scripts/smart.thresh.check.sh

DISK=$1
ATTRIBUTE=$2
DIFF=0

# Current value
VALUE=$((10#$(sudo smartctl -A $DISK | grep -i "$ATTRIBUTE" | tail -1 | awk '{ print $4 }'))) # $((10#...)) - this is needed to correctly decimal calculation
# THRESH
THRESH=$((10#$(sudo smartctl -A $DISK | grep -i "$ATTRIBUTE" | tail -1 | awk '{ print $6 }'))) # $((10#...)) - this is needed to correctly decimal calculation

let "DIFF = $VALUE - $THRESH"

echo $DIFF