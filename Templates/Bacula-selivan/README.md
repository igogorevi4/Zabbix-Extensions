WARNING: https://www.bareos.org/en/faq/why_fork.html You may be interested in using Bareos instead of original Bacula.

NOTICE: germanodlf created analogous tool based on this, which seems more mature and feature-reach: [germanodlf/bacula-zabbix](https://github.com/germanodlf/bacula-zabbix) You may be interested to check it out.

bacula_zabbix_integration
=========================

Scripts and template to integrate bacula with zabbix.

Abilities
---------
* separate monitoring for each job
* low-level auto-discovery of new jobs

Workflow
---------
For each job it's exit status and parameters are forwarded to Zabbix.

Triggers
--------
* Job exit status indicates error
* Job was not launched for 36 hours
* FD non-fatal errors occured
* SD errors occured
* Verify job failed
 
Installation
------------

* Copy file somewhere. Default is /etc/bacula/bacula-to-zabbix
* Make sure that zabbix user can launch bconsole and get output of 'show jobs' command.
* Tweak conf.py:
	* path to zabbix_sender
	* bconsole config file
	* jobs list cache file. (!) This file should be avaliable for write to zabbix user.
	* timeout for bconsole command in seconds (default 5 seconds)
	* hostname for sending messages to zabbix
* Add UserParameter from to zabbix_agentd.conf. Example in file conf-zabbix_agentd-userparam. Restart zabbix_agentd
* Config Messages resuorce in bacula-director.conf. Example in file conf-bacula-dir-messages. You can directly include this file with @/etc/bacula/bacula-to-zabbix/conf-bacula-dir-messages. Reload config for bacula-director
* Add template tmpl bacula-director.xml to zabbix. Assign it to host with bacula-director.
* Disable auto-generated triggers for jobs that are not backup type(restore jobs, ...)

Feedback
--------

Feel free to send bug reports and feature requests [here](https://github.com/selivan/bacula_zabbix_integration/issues).

**P.S.** If this code is useful for you - don't forget to put a star on it's [github repo](https://github.com/selivan/ansible_ipmi_lan_manage).
