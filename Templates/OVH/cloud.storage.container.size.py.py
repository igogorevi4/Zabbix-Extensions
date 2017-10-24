# -*- encoding: utf-8 -*-

import json
import ovh
import sys

# pass as parameter container ID you want to see 
containerid = sys.argv[1]

client = ovh.Client(
    endpoint='ovh-eu',               # Endpoint of API OVH Europe (List of available endpoints)
    application_key='application_key',    # Application Key
    application_secret='application_secret', # Application Secret
    consumer_key='consumer_key',       # Consumer Key
)

result = client.get('/cloud/project/11463cd19d7e4bf7be1c5a64991f37fd/storage/' + containerid)

data = json.dumps(result, indent=4)
resp = json.loads(data)

print (resp['storedBytes'])