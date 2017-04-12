#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import urllib2
import sys

service = sys.argv[1] # users, authorizations etc.
ip = sys.argv[2]
port = sys.argv[3]
resfile = '/tmp/api.looch.status.' + service + '.' + ip + '.tmp'

# Make URL
url = 'http://' + ip + ':' + port + '/monitoring/' + service

# Read to file
response = urllib2.urlopen(url)
myfile = response.readline()

with open(resfile, 'w') as f:
                f.write(myfile)