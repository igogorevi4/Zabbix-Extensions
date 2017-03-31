#!/bin/bash
##### OPTIONS VERIFICATION #####
if [[ -z "$1" || -z "$2" ]]; then
  exit 1
fi
##### PARAMETERS #####
RESERVED="$1"
METRIC="$2"
NC="/bin/nc" # or /usr/bin/nc
CACHE_TTL="55"
CACHE_FILE="/tmp/zabbix.memcache.cache"
EXEC_TIMEOUT="1"
NOW_TIME=`date '+%s'`
##### RUN ##### 
if [ -s "${CACHE_FILE}" ]; then
  CACHE_TIME=`stat -c"%Y" "${CACHE_FILE}"`
else
  CACHE_TIME=0
fi
DELTA_TIME=$((${NOW_TIME} - ${CACHE_TIME}))
#
if [ ${DELTA_TIME} -lt ${EXEC_TIMEOUT} ]; then
  sleep $((${EXEC_TIMEOUT} - ${DELTA_TIME}))
elif [ ${DELTA_TIME} -gt ${CACHE_TTL} ]; then
  echo "" >> "${CACHE_FILE}" # !!!
  DATACACHE=`echo -e "stats\nquit" | ${NC} -q2 127.0.0.1 11211`
  echo "${DATACACHE}" > "${CACHE_FILE}" # !!!
  chmod 640 "${CACHE_FILE}"
fi
#
cat "${CACHE_FILE}" | grep -i "STAT ${METRIC} " | awk '{print $3}' | head -n1
#
exit 0