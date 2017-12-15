Requirements:
    *   bareos veriosion >= 15.2
    *   python 2.7
    *   active zabbix-agent
    *   Find the password for bconsole connection needs - usually it's in this file /etc/bareos/bconsole.conf
    *   python-bareos module

Intallation zabbix module to monitor Bareos

Run installation.script.sh as root 

Then upload xml-template to your own zabbix and link it to bareos-server

#http://wiki.bacula.org/doku.php?id=faq#what_do_all_those_job_status_codes_mean
Bareos Job Status Code	Meaning
A	Canceled by user
B	Blocked
C	Created, but not running
c	Waiting for client resource
D	Verify differences
d	Waiting for maximum jobs
E	Terminated in error
e	Non-fatal error
f	fatal error
F	Waiting on File Daemon
j	Waiting for job resource
M	Waiting for mount
m	Waiting for new media
p	Waiting for higher priority jobs to finish
R	Running
S	Scan
s	Waiting for storage resource
T	Terminated normally
t	Waiting for start time
