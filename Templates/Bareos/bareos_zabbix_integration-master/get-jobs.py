#!/usr/bin/env python

import subprocess
import locale
import json

from conf import conf

encoding = locale.getdefaultlocale()[1]

if conf['type'] == 'bareos':
    command="echo show jobs | timeout %d bconsole -c %s | grep -i name | cut -d \'\"\' -f 2" % (conf['bconsole_wait'], conf['bconsole_conf_file'])
elif conf['type'] == 'bacula':
    command="echo show jobs | timeout %d bconsole -c %s | awk '/^Job/ {sub(\"name=\",\"\",$2); print $2}'" % (conf['bconsole_wait'], conf['bconsole_conf_file'])
else:
    command="echo"
proc=subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
jobs_raw=proc.communicate()[0]

result = dict( {'data': [ { "{#JOBNAME}": job } for job in jobs_raw.decode(encoding).split('\n') if job ]} )

print(json.JSONEncoder(sort_keys=True, indent=3).encode(result))
