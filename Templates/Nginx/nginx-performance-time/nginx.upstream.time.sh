#!/bin/bash

#Preparing
#put to /etc/zabbix/scripts/nginx.request.time.sh
#add task to cron: * * * * * bash /etc/zabbix/scripts/nginx.upstream.time.sh
#chmod 744 $RESFILE #for reading by Zabbix-agent

LOGFILE='/var/log/nginx/access.log'
RESFILE='/tmp/nginx.upstream.response.time.tmp'

CURRENT_TIME=:$(date +"%H:%M" --date 'now - 1 minutes'): # timestamp - 1  muniute = previous

if grep $CURRENT_TIME $LOGFILE | awk '{print $(NF-1),$NF}' | grep upstream_response_time; then

        #min
        a=$(grep $CURRENT_TIME $LOGFILE | awk '{print $(NF-1),$NF}' | grep upstream_response_time | awk '{print $NF}' | grep "\." | sort | head -n 1)
        echo "min="${a::6} > $RESFILE #rewrite this file

        #max
        a=$(grep $CURRENT_TIME $LOGFILE | awk '{print $(NF-1),$NF}' | grep upstream_response_time | awk '{print $NF}' | grep "\." | sort | tail -n 1)
        echo "max="${a::6} >> $RESFILE

        #mean
        NUMBER=$(grep $CURRENT_TIME $LOGFILE | awk '{print $(NF-1),$NF}' | grep upstream_response_time | awk '{print $NF}' | grep "\." | sort | wc -l)
        SUM=$(grep $CURRENT_TIME $LOGFILE | awk '{print $(NF-1),$NF}' | grep upstream_response_time | awk '{print $NF}' | grep "\." | awk '{s+=$1} END {print s}' )
        MEAN=$(echo - | awk -v n=$NUMBER -v s=$SUM '{ print s / n }')
        echo "mean="${MEAN::6} >> $RESFILE

else

        echo -e 'min=0.00\nmax=0.00\nmean=0.00' > $RESFILE #rewrite this file

fi