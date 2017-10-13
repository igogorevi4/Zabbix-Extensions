# put it in /etc/zabbix/scripts/
# chmod 755 ...
#!/bin/bash

case "$1" in
active)
curl -s http://127.0.0.1/nginx_status | grep Active | awk ' {print $NF} '
exit 0
;;
accepts)
curl -s http://127.0.0.1/nginx_status | grep accepts -A 1 | tail -n 1 | awk ' {print $1} '
;;
handled)
curl -s http://127.0.0.1/nginx_status | grep handled -A 1 | tail -n 1 | awk ' {print $2} '
;;
requests)
curl -s http://127.0.0.1/nginx_status | grep requests -A 1 | tail -n 1 | awk ' {print $3} '
;;
reading)
curl -s http://127.0.0.1/nginx_status | grep Reading | awk ' {print $2} '
;;
writing)
curl -s http://127.0.0.1/nginx_status | grep Writing | awk ' {print $4} '
;;
waiting)
curl -s http://127.0.0.1/nginx_status | grep Waiting | awk ' {print $6} '
;;
*)
echo "ZBX_UNSUPPORTED"
exit 1
;;
esac

exit 0

