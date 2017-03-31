from socket import gethostname
from ConfigParser import ConfigParser
from StringIO import StringIO

server_type = "bacula"

conf = {
            'type' : server_type,
            'log_dir': "/var/log/{0}/".format(server_type),
            'zabbix_agent_conf': "/etc/zabbix/zabbix_agentd.conf",
            'bconsole_conf_file': "/etc/{0}/bconsole.conf".format(server_type),
            'bconsole_wait': 5,
            'email_from': "{0} <{1}@localhost>".format(server_type, server_type.title()),
            'email_server': "127.0.0.1"
       }

zcfg = ConfigParser()
with open(conf['zabbix_agent_conf']) as stream:
    fakefile = StringIO("[global]\n" + stream.read())
    zcfg.readfp(fakefile)
zserver = zcfg.get('global', 'server').split(',')[0]

conf['hostname'] = gethostname()
conf['zabbix_server'] = zserver
