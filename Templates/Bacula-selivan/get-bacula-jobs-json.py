#!/usr/bin/env python

import subprocess
from conf import conf

command="echo quit | timeout %d bconsole -c '%s'" % (conf['bconsole_wait'], conf['bconsole_conf_file'])
exit_code=subprocess.Popen(command,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE).wait()
if exit_code != 0:
	print file(conf['jobs_cache_file']).read()
	quit(1)

out=open(conf['jobs_cache_file'],'w')
out.write('{ "data": [ \n')

command="echo show jobs | timeout %d bconsole -c %s | awk '/^Job/ {sub(\"name=\",\"\",$2); print $2}'" % (conf['bconsole_wait'], conf['bconsole_conf_file'])
proc=subprocess.Popen(command, shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
jobs_raw=proc.communicate()[0]
firstrun=1
for job in jobs_raw.split('\n'):
	if job == '': continue
	if firstrun != 1:
		out.write(',\n')
	else:
		firstrun=0
	out.write("{ \"{#JOBNAME}\":\"%s\"}" % job)

out.write(' ] }')
out.close()

print file(conf['jobs_cache_file']).read()

