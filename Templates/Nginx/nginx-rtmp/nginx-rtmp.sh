# put it in /etc/zabbix/scripts/
# chmod 755 ...
#!/bin/bash

FILESTATUS=/tmp/rtmp_nginx.tmp # chmod 777 ...
#NOWTIME=$(date +%s)
#if [ ! -f $FILESTATUS ]
#then wget http://91.109.202.182/stat -O $FILESTATUS -o /dev/null
#fi
#FILETIME=$(stat -c %Y $FILESTATUS)
#TIME=$(($NOWTIME-$FILETIME))
#if [ "$TIME" -ge "20" ]
#then
wget http://127.0.1.1/stat -O $FILESTATUS -o /dev/null
#fi
case "$1" in
bytes_in)
grep $1 $FILESTATUS | cut -f2 -d '>' | cut -f1 -d '<' | head -n1
exit 0
;;
bytes_out)
grep $1 $FILESTATUS | cut -f2 -d '>' | cut -f1 -d '<' | head -n1
exit 0
;;
accepted)
grep $1 $FILESTATUS | cut -f2 -d '>' | cut -f1 -d '<'
exit 0
;;
*)
echo "ZBX_UNSUPPORTED"
exit 1
;;
esac

exit 0