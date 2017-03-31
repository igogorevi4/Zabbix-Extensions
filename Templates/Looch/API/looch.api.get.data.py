#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import urllib2
import sys

service = sys.argv[1] # users, authorizations etc.
ip = '172.16.20.135' # = sys.argv[3]
port = '8000' # = sys.argv[4]
resfile = '/tmp/api.looch.status.' + service + '.tmp'

# Make URL
url = 'http://' + ip + ':' + port + '/monitoring/' + service

# Read to file
response = urllib2.urlopen(url)
myfile = response.readline()

with open(resfile, 'w') as f:
				f.write(myfile)