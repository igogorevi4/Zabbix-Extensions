from socket import gethostname

conf={
	'zabbix_sender':"/usr/bin/zabbix_sender",
	'jobs_cache_file':"/etc/bacula/bacula-to-zabbix/bacula-jobs-json.cache",
	'bconsole_conf_file':"/etc/bacula/bconsole.conf",
	'bconsole_wait':5
	}
conf['hostname']=gethostname()

