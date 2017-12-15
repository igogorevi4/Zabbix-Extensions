#!/bin/bash
#run as root

#Installation bareos-python module

git clone https://github.com/bareos/python-bareos
cd python-bareos
python setup.py install
cd ../

#preparation zabbix config
mkdir /etc/zabbix/scripts/
mkdir /etc/zabbix/scripts/bareos/
touch /etc/zabbix/scripts/bareos/config
cp bareos.monitoring.py /etc/zabbix/scripts/bareos/bareos.monitoring.py
echo password=$(grep Password /etc/bareos/bconsole.conf | cut -f2 -d\") >> /etc/zabbix/scripts/bareos/config
chown -R zabbix:zabbix /etc/zabbix/scripts/bareos/
chmod -R 700 /etc/zabbix/scripts/bareos/
cp bareos.conf /etc/zabbix/zabbix_agentd.d/

systemctl restart zabbix-agent

sudo -u zabbix zabbix_agentd -t bareos.jobs.discovery