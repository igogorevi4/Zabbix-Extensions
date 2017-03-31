#!/usr/bin/env python
'''
Simple script to send Bacula reports to Zabbix
Made by Pavel Selivanov <selivan5@yandex.ru>
Forked by Valen Tau <wavilen@gmail.com>
Should be used in Bacula-dir config instead of mail command:
mail = <> = all, !skipped
mailcommand = "/etc/zabbix/bacula_notify.py %n %t %l %e %r"
operatorcommand = "/etc/zabbix/bacula_notify.py %r <bacula-sd server name>"
Hostnames in Zabbix and Bacula must correspond
'''
import sys
import re
import subprocess
import datetime
import os
# Logging
import logging
logging.basicConfig(
    format=u'%(levelname)-8s [%(asctime)s] %(message)s',
    level=logging.DEBUG,
    filename=u'/var/log/bacula/{0}.log'.format(os.path.basename(__file__))
)
logging.info('sys.argv: ' + repr(sys.argv))

# Handle incorrect call
if sys.version_info >= (3,):
    logging.warn("Need python version 2 to run. Tested with python 2.6")
    quit(1)

if len(sys.argv) < 6:
    logging.warn(
        (
            "Usage: %s "
            "JOB_NAME JOB_TYPE JOB_LEVEL JOB_EXIT_CODE ZABBIX_SERVER"
        ) % sys.argv[0]
    )
    quit(5)

# Settings
from conf import conf

# Get values from arguments
job_name = sys.argv[1]
result = {}
result['bacula.job_type'] = sys.argv[2]
result['bacula.job_level'] = sys.argv[3]
result['bacula.job_exit_code'] = sys.argv[4]
zabbix_server = sys.argv[5]

# Define how to get values from input
tests = (

    ("\s*FD Files Written:\s+([0-9]+)\s*",
        "bacula.fd_fileswritten",
        lambda x: x.group(1)),

    ("\s*SD Files Written:\s+([0-9]+)\s*",
        "bacula.sd_fileswritten",
        lambda x: x.group(1)),

    ("\s*FD Bytes Written:\s+([0-9][,0-9]*)\s+\(.*\)\s*",
        "bacula.fd_byteswritten",
        lambda x: x.group(1).translate(None, ",")),

    ("\s*SD Bytes Written:\s+([0-9][,0-9]*)\.*",
        "bacula.sd_byteswritten",
        lambda x: x.group(1).translate(None, ",")),

    ("\s*Last Volume Bytes:\s+([0-9][,0-9]*).*",
        "bacula.lastvolumebytes",
        lambda x: x.group(1).translate(None, ",")),

    ("\s*Files Examined:\s+([0-9][,0-9]*)\s*",
        "bacula.verify_filesexamined",
        lambda x: x.group(1).translate(None, ",")),

    ("\s*Non-fatal FD errors:\s+([0-9]+)\s*",
        "bacula.fd_errors_non_fatal",
        lambda x: x.group(1)),

    ("\s*SD Errors:\s+([0-9]+)\s*",
        "bacula.sd_errors",
        lambda x: x.group(1))

)

# Get values from input
for line in sys.stdin.readlines():
    for regexp, key, value in tests:
        match = re.match(regexp, line)
        if match:
            # DEBUG
            logging.debug(line)
            result[key] = value(match)

# DEBUG
logging.debug(repr(result))

# Send result to zabbix
for key, value in result.iteritems():
    command = "{0} -z {1} -s {2} -k '{3}[{4}]' -o '{5}'".format(
        conf['zabbix_sender'],
        zabbix_server,
        conf['hostname'],
        key,
        job_name,
        value)
    logging.info(command)
    subprocess.call(command, shell=True)
