mkdir /etc/zabbix/scripts/; chown root:root -R /etc/zabbix/scripts/; chmod 755 /etc/zabbix/scripts/; nano /etc/zabbix/scripts/memcache-stats.sh

chown root:root /etc/zabbix/scripts/memcache-stats.sh; chmod 755 /etc/zabbix/scripts/memcache-stats.sh; sudo -u zabbix /etc/zabbix/scripts/memcache-stats.sh "none" uptime

Основа взята здесь: http://wiki.enchtex.info/howto/zabbix/zabbix_memcache_monitoring