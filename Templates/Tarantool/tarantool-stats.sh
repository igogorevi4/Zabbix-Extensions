#!/bin/bash

echo "box.stat()" |  tarantoolctl connect $1 2>/dev/null |grep $2 -A 2 |grep $3|  awk -F':' '{print $2}' |sed -e"s/ //g"
