Prepare Nginx - turning on status-module:

location /status {
        stub_status on;
        access_log off;
        allow 127.0.0.1;
        deny all;
}


# put shell-script in /etc/zabbix/scripts/
# chmod 755 ...

Create file /tmp/status_nginx.tmp with permissions for Zabbix user


In template there macroses were described:

{$NGINX_CON_NUM} - requests
{$NGINX_REQ_NUM} - connection

You should make the same on Nginx-hosts, and define your own threshold.