#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import urllib2
import sys

item = sys.argv[2] # moniroted item
service = sys.argv[1] # users, authorizations etc.
ip = '172.16.20.135' # = sys.argv[3]
port = '8000' # = sys.argv[4]
resfile = '/tmp/api.looch.status.' + service + '.tmp'

# Make URL
url = 'http://' + ip + ':' + port + '/monitoring/' + service

def search_in_data(data, item, level_counter=0):
                if level_counter > 4:
                                return
                if search(data, item):
                                print data[item]
                                return
                for key in data.keys():
                                search_in_data(data[key], item, level_counter + 1)

def search(data, item):
                if item in data.keys():
                                return True
                return False


with open(resfile) as f:
                data = json.load(f)

search_in_data(data, item)