put the script into /usr/lib/zabbix/alertscripts/ - it's described in zabbix-server configeuration file, parameter "AlertScriptsPath"
chmod 755

you can check how it does work:
bash /usr/lib/zabbix/alertscripts/slack.sh '@SLACKUSERNAME' PROBLEM 'Oh no! Something is wrong!' - set your own slack-username

In zabbix GUI set slack.sh as script in Administration > Media Types
Then create Action, choose notification via Slack
