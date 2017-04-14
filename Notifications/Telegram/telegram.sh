#!/bin/bash

#	1.	create you own bot 
#	2.	put bot key to this script
#	3.	add this bot to your contact list
#	4.	wgite any message to it
#	5.	find out you chat_id using https://api.telegram.org/bot$BOTKEY/getUpdates
#https://core.telegram.org/bots/api

CHATID="$1"
THEME="$2"
BODY="$3"

BOTKEY="12345:sdsadsa-dfdsf" #like this
TIMEOUT="10"

TEXT="<b>$THEME </b> $BODY " #<a href="https://zabbix.vispamedia.com">inline URL</a> "

#PARSEMODE="markdown"
PARSEMODE="html"

curl  -s --max-time $TIMEOUT  "https://api.telegram.org/bot$BOTKEY/sendMessage?chat_id=$CHATID&disable_web_page_preview=1&parse_mode=$PARSEMODE&text=$TEXT" > /dev/null