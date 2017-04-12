#!/usr/bin/python

import os
import sys
import json

logdir = sys.argv[1]

data = []

for (logdir, _, files) in os.walk(logdir):
        for f in files:
                if f.endswith(".log"):
                        path = os.path.join(logdir, f)
                        data.append({'#LOGFILEPATH':path})
                        jsondata = json.dumps(data)

print json.dumps({"data": data})