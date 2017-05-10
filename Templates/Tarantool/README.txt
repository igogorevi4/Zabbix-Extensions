based on https://github.com/PushOk/tarantool_zabbix
In /etc/zabbix/zabbix_agentd.conf follows:
UnsafeUserParameters=1
This allows special symbols in UserParameters: \ ' " ` * ? [ ] { } ~ $ ! & ; ( ) < > | # @
