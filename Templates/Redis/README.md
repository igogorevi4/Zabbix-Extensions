0) change server IP on redis-stats.py

1) Put redis.conf into your zabbix_agentd.conf config subdirectory (like: /etc/zabbix/zabbix_agentd.d/).

2) Change script name in redis.conf to use redis-stats.py . Redis server params can be passed to the python script as arguments e.g.:
redis-stats.py localhost -p 6379 -a mypassword

3) Change your zabbix_agentd.conf config so it will include this file:
Include=/etc/zabbix/zabbix_agentd.d/

4) Put zbx_redis_stats.py into your zabbix_agentd.conf config subdirectory (like: /etc/zabbix/scripts/).
change zabbix_host in the script

5) Change paths in redis.conf if need it.

6) In working dir (/etc/zabbix/scripts) do:

For use python verson script:

pip install redis
chmod +x zbx_redis_stats.py

7) Import zbx_redis_template.xml into zabbix in Tepmplate section web gui.
There is a macros in template: {$REDIS_HOSTNAME} - 'localhost' by default.
Change it in Zabbix GUI for server, if you connect to redis using other hostname.