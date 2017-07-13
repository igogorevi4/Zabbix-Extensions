#!/usr/bin/python
# desc: Jenkins' job monitoring with LLD

import os
import sys
import time
import json
import baker
import requests
import urllib2
import base64
from configobj import ConfigObj
from datetime import datetime as dt

try:
    config = ConfigObj('/etc/zabbix/scripts/jenkins/config')
    HOSTNAME = config.get('hostname')
    USERNAME = config.get('username')
    PASSWORD = config.get('password')
    JENKINS_URL = config.get('jenkins_url')
    PREFIX = config.get('prefix',"")
except Exception as E:
    print E
    sys.exit(1)

if PREFIX == "":
    PREFIX = ["HIGH-DTB","HIGH-BI","DISASTER-DTB","HIGH-SUPPORT"]

# Discoverying jenkins' job by Zabbix
def _discovery(prefix=""):
    jobs = requests.get(JENKINS_URL + '/view/All/api/json', auth=(USERNAME,PASSWORD))
    data = { 'data':[] }
    if prefix.lower() == 'all':
        for job in jobs.json().get('jobs'):
            if job.get('color') != "disabled":
                data['data'].append({'{#JOBNAME}' : job.get('name') })
    elif prefix is not None:
        for job in jobs.json().get('jobs'):
            if job.get('name').upper().startswith(prefix.upper()) and job.get('color') != "disabled" :
                data['data'].append({'{#JOBNAME}' : job.get('name') })
    return json.dumps(data)

# Get result status of job
def _status(name="",maxtime=0):
    request = urllib2.Request(JENKINS_URL + '/job/' + name + '/lastBuild/api/json')
    base64string = base64.b64encode('%s:%s' % (USERNAME, PASSWORD))
    request.add_header("Authorization", "Basic %s" % base64string)
    result = urllib2.urlopen(request)
    data = json.load(result)
    jobStatus = data['result']
    print (jobStatus)

@baker.command
def discovery(prefix=""):
     return _discovery(prefix=prefix)

@baker.command
def status(name="",maxtime=0):
    _status(name=name,maxtime=maxtime)

if __name__ == "__main__":
    baker.run()