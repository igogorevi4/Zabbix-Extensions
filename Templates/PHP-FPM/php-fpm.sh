# put it in /etc/zabbix/scripts/
# chmod 755 ...
#!/bin/bash

FILESTATUS=/tmp/status_php.tmp # chmod 777 ...
FILEPING=/tmp/php_fpm_ping.tmp # chmod 777 ...

NOWTIME=$(date +%s)
if [ ! -f $FILESTATUS ]
then wget http://localhost/php-status -O $FILESTATUS -o /dev/null
fi
FILETIME=$(stat -c %Y $FILESTATUS)
let "TIME = $NOWTIME - $FILETIME"
if [ "$TIME" -ge "20" ]
then
wget http://localhost/php-status -O $FILESTATUS -o /dev/null
fi

case "$1" in
active_processes)
grep "^active processes" $FILESTATUS | awk '{print $NF}'
;;
accepted_conn)
grep "^accepted conn" $FILESTATUS | awk '{print $NF}'
;;
idle_processes)
grep "^idle processes:" $FILESTATUS | awk '{print $NF}'
;;
listen_queue_len)
grep "^listen queue len" $FILESTATUS | awk '{print $NF}'
;;
listen_queue)
grep "^listen queue:" $FILESTATUS | awk '{print $NF}'
;;
max_active_processes)
grep "^max active processes" $FILESTATUS | awk '{print $NF}'
;;
max_children_reached)
grep "^max children reached" $FILESTATUS | awk '{print $NF}'
;;
max_listen_queue)
grep "^max listen queue" $FILESTATUS | awk '{print $NF}'
;;
total_processes)
grep "^total processes" $FILESTATUS | awk '{print $NF}'
;;
ping)
wget http://localhost/ping -O $FILEPING -o /dev/null
grep "^1" $FILEPING
;;

*)
echo "ZBX_UNSUPPORTED"
exit 1
;;
esac

exit 0