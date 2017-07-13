Jenkins' job monitoring with LLD by Zabbix

INSTALLATION:

0.  create jenkins-api user for zabbix

1.  copy config & jenkis.job.status.py to directory /etc/zabbix/scripts/jenkins/
    
        mkdir /etc/zabbix/scripts/jenkins/
        cp config /etc/zabbix/scripts/jenkins/
        cp jenkins.job.status.py /etc/zabbix/scripts/jenkins/
        chmod 755 /etc/zabbix/scripts/jenkins/
        chmod 711 /etc/zabbix/scripts/jenkins/*
        chown zabbix:zabbix /etc/zabbix/scripts/jenkins/
        chown zabbix:zabbix /etc/zabbix/scripts/jenkins/*

2.  copy jenkins.conf to /etc/zabbix/zabbix_agentd.d/

        cp jenkins.conf /etc/zabbix/zabbix_agentd.d/

3.  restart zabbix-agent

        systemctl restart zabbix-agent

4.  Upload template to Zabbix GUI
5.  Link 'Jenkins Job' templdate with you host where jenkins works
6.  In 1 hour check discovery and latest data