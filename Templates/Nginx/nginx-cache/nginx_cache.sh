# put it in /etc/zabbix/scripts/
# chmod 755 ...
#!/bin/bash

LOGFILE=/var/log/nginx/cache.log
awk '{print $3}' $LOGFILE | sort | uniq -c | sort -r | grep "S1" -i | awk '{print $1}'

#9 MISS
#6 STALE
#19 BYPASS
#156 –
#127 HIT

exit 0

