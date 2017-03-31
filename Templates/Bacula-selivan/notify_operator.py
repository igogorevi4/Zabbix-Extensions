#!/usr/bin/env python
'''
Simple script to send Bacula reports to Zabbix
Made by Pavel Selivanov <selivan5@yandex.ru>
Forked by Valen Tau <wavilen@gmail.com>
Should be used in Bacula-dir config instead of mail command:
mail = <> = all, !skipped
mailcommand = "/etc/zabbix/bacula_notify.py %r %c"
operatorcommand = "/etc/zabbix/bacula_notify_operator.py %r <bacula-sd server name>"
Hostnames in Zabbix and Bacula must correspond
'''
import sys
import re
import os
import datetime
import subprocess
# Logging
import logging
logging.basicConfig(
    format=u'%(levelname)-8s [%(asctime)s] %(message)s',
    level=logging.DEBUG,
    filename=u'/var/log/bacula/{0}.log'.format(os.path.basename(__file__))
)
logging.info('sys.argv: ')
for _str in sys.argv:
    logging.info(_str)

# Handle incorrect call
if sys.version_info >= (3,):
    logging.warn("Need python version 2 to run. Tested with python 2.6")
    quit(1)

if len(sys.argv) < 3:
    logging.warn(
        "Usage: {0} ZABBIX_SERVER HOSTNAME CUSTOM_MESSAGE".format(sys.argv[0]))
    quit(5)

# Settings
from conf import conf

command = "{0} -z {1} -s {2} -k 'bacula.custommessage' -o '{3}'".format(
    conf['zabbix_sender'],
    sys.argv[1],
    conf['hostname'],
    sys.stdin.read()
)
logging.info(command)
subprocess.call(command, shell=True)
