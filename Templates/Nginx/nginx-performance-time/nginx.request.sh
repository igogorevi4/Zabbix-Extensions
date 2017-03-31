#!/bin/bash

#Preparing
#put to /etc/zabbix/scripts/nginx.request.time.sh
#add task to cron: * * * * * bash /etc/zabbix/scripts/nginx.request.time.sh
#chmod 744 $RESFILE #for reading by Zabbix-agent

LOGFILE='/home/log/nginx/access.log'
RESFILE='/tmp/nginx.request.time.tmp'

CURRENT_TIME=:$(date +"%H:%M" --date 'now - 1 minutes'): # timestamp - 1  muniute = previous

#min
a=$(grep $CURRENT_TIME $LOGFILE | awk '{print $(NF-3)}' | grep request_time | grep "\." | cut -f2 -d= | sort | head -n 1)
echo "min="${a::6} > $RESFILE #rewrite this file

#max
a=$(grep $CURRENT_TIME $LOGFILE | awk '{print $(NF-3)}' | grep request_time | grep "\." | cut -f2 -d= | sort | tail -n 1)
echo "max="${a::6} >> $RESFILE

#percentile


#mean
NUMBER=$(grep $CURRENT_TIME $LOGFILE | awk '{print $(NF-3)}' | grep request_time | grep "\." | cut -f2 -d= | sort | wc -l)
SUM=$(grep $CURRENT_TIME $LOGFILE | awk '{print $(NF-3)}' | grep request_time | grep "\." | cut -f2 -d= | awk '{s+=$1} END {print s}' | cut -f1 -d.)
MEAN=$(echo - | awk -v n=$NUMBER -v s=$SUM '{ print s / n }')
echo "mean="${MEAN::6} >> $RESFILE