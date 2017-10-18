based on https://github.com/PushOk/tarantool_zabbix
In /etc/zabbix/zabbix_agentd.conf follows:
UnsafeUserParameters=1
This allows special symbols in UserParameters: \ ' " ` * ? [ ] { } ~ $ ! & ; ( ) < > | # @


and set in Zabbix GUI macros to your server:
{$TARANTOOLCTL} like so user:password@localhost:3301