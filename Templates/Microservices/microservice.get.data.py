#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import urllib2
import sys

service = sys.argv[1]
port = sys.argv[2]
ip = sys.argv[3]
resfile = '/tmp/microservice.' + service + '.status.tmp'

# Make URL
url = 'http://' + ip + ':' + port + '/status'

# Read to file
response = urllib2.urlopen(url)
myfile = response.readline()

with open(resfile, 'w') as f:
                f.write(myfile)
