# put it in /etc/zabbix/scripts/
# chmod 755 ...
#!/bin/bash

FILESTATUS=/tmp/status_nginx.tmp # chmod 777 ...
NOWTIME=$(date +%s)
if [ ! -f $FILESTATUS ]
then wget http://localhost/nginx_status -O $FILESTATUS -o /dev/null
fi
FILETIME=$(stat -c %Y $FILESTATUS)
#let "TIME = $NOWTIME - $FILETIME"
TIME=$(($NOWTIME-$FILETIME))
if [ "$TIME" -ge "20" ]
then
wget http://localhost/nginx_status -O $FILESTATUS -o /dev/null
fi
case "$1" in
active)
awk 'NR==1 {print $3}' $FILESTATUS
exit 0
;;
accepts)
awk 'NR==3 {print $1}' $FILESTATUS
;;
handled)
awk 'NR==3 {print $2}' $FILESTATUS
;;
requests)
awk 'NR==3 {print $3}' $FILESTATUS
;;
reading)
awk 'NR==4 {print $2}' $FILESTATUS
;;
writing)
awk 'NR==4 {print $4}' $FILESTATUS
;;
waiting)
awk 'NR==4 {print $6}' $FILESTATUS
;;
*)
echo "ZBX_UNSUPPORTED"
exit 1
;;
esac

exit 0
