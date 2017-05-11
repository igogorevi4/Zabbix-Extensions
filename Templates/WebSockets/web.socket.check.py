#!/usr/bin/python
# Checking possibility of socket connection

import sys
from websocket import create_connection

host = sys.argv[1]

#open connection, try to send message, recieve and close
try:
        ws = create_connection("wss://%s" % (host))
        ws.send("ping")
        result =  ws.recv()
        ws.close()
        connectionState = 1
except Exception:
        connectionState = 0

print connectionState