#!/usr/bin/env python
import bareos.bsock
import sys
import re
from configobj import ConfigObj
import json

command = sys.argv[1]

try:
    config = ConfigObj('/etc/zabbix/scripts/bareos/config')
    secretspassword = config.get('password')
except Exception as E:
    print E
    sys.exit(1)

password=bareos.bsock.Password(secretspassword)

#conneting to bconsole
directorconsole=bareos.bsock.DirectorConsoleJson(address="localhost", port=9101, password=password)

#Discovery Bareos' jobs
def discovery():
    jobs=directorconsole.call(".jobs")
    data = []
    for i in jobs['jobs']:
        data.append({'{#BAREOSJOBNAME}': i['name']})

    return json.dumps({"data": data}, indent=4, sort_keys=True)

#Bareos' jobs status explanation
#http://wiki.bacula.org/doku.php?id=faq#what_do_all_those_job_status_codes_mean
#"type": "B", - only if backup
#bad job status
#e, f, E, B,

#Get status of job
def status():
    jobs=directorconsole.call("llist jobs")
    data = []
    for i in jobs['jobs']:
        data.append({'jobname': i['name'], 'status': i['jobstatus'], 'timestamp': i['jobtdate'], 'starttime': i['starttime']})

    return json.dumps(data, indent=4, sort_keys=True)

function_dict = {'status':status, 'discovery':discovery }
func = function_dict[command]

print func()
