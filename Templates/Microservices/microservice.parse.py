#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import sys

service = sys.argv[1]
resfile = '/tmp/microservice.' + service + '.status.tmp'

with open(resfile) as f:
                data = json.load(f)

state = []

for key, value in data["dependencies"].items():
    if value == 1:
        state.append(key)

if state:
    print (str(state))
else:
    print ('OK')