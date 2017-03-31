#!/usr/bin/env python

import sys
import os
import subprocess
import argparse
from argparse import RawTextHelpFormatter
import smtplib
import logging
from email.mime.text import MIMEText
from zbxsend import Metric, send_to_zabbix

# Settings
from conf import conf

def sendmail(msg, recipients):
    subject = "{0}: message for operator".format(conf['type'].title())
    logging.debug( "sending email ({0}) to '{1}'".format(subject, recipients) )

    msg = MIMEText(msg)
    msg['Subject'] = subject
    msg['From'] = conf['email_from']
    msg['To'] = ', '.join(recipients)

    s = smtplib.SMTP( conf['email_server'] )
    s.sendmail( conf['email_from'], recipients, msg.as_string() )
    s.quit()

logging.basicConfig(
    format=u'%(levelname)-8s [%(asctime)s] %(message)s',
    level=logging.DEBUG,
    filename=u'{0}/{1}.log'.format(conf['log_dir'], os.path.basename(__file__))
                   )
logging.info('sys.argv: ' + repr(sys.argv))

# Handle incorrect call
# zbxsend is broken in 3.x (https://github.com/alledm/zbxsend/commit/a485c97a4f0c2fa46fe3192da9979cbeade752b4)
if sys.version_info >= (3,):
    logging.warn("Need python version 2.x to run")
    quit(1)

parser = argparse.ArgumentParser(
            formatter_class=RawTextHelpFormatter,
            description=
"""Simple script to send {1} operator reports to Zabbix.
Should be used in {1}-dir config instead of mail command:
    mail = root@localhost,admin@domain = all, !skipped
    operatorcommand = "{0} [--recipients '%r']"
Hostnames in Zabbix and {1} must correspond
""".format(os.path.realpath(__file__), conf['type'].title())
                                )

parser.add_argument('--recipients',
                    action='store',
                    type=lambda x: x.split(),
                    default=[],
                    help='space-separated list of report recipients (%%r)')

args = parser.parse_args()

msg = sys.stdin.read()

metrics = [ Metric(conf['hostname'], "{0}.custommessage".format(conf['type']), msg) ]
logging.info( "sending custom message to '{0}': '{1}'".format(conf['zabbix_server'], metrics) )
send_to_zabbix(metrics, conf['zabbix_server'], 10051, 20)

if args.recipients:
    sendmail(msg, args.recipients)
