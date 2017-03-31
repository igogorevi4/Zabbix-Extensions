bareos/bacula zabbix_integration
=========================

Scripts and template to integrate bareos/bacula with zabbix.

Abilities
---------
* separate monitoring for each job
* low-level auto-discovery of new jobs
* send emails about jobs

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

* install zbxsend python module
	* `pip install zbxsend` or `pypi-install zbxsend` or `any command related to your distro`
* `cd /etc/bareos` or `cd /etc/bacula`
* `git clone https://github.com/paleg/bareos_zabbix_integration.git`
* Make sure that zabbix user can launch bconsole and get output of 'show jobs' command (add 'zabbix' user to 'bareos/bacula' group)
* Tweak conf.py:
    * server type (`bareos` or `bacula`)
    * path to zabbix agent conf
    * bconsole config file
    * timeout for bconsole command in seconds (default 5 seconds)
    * log dir
    * email settings ('From' header and smtp server)
* Add UserParameter to zabbix_agentd.conf ( `UserParameter=bareos.jobs,/etc/bareos/bareos_zabbix_integration/get-jobs.py` or `UserParameter=bacula.jobs,/etc/bacula/bareos_zabbix_integration/get-jobs.py`)
* Config Messages resource in bareos-dir.conf/bacula-dir.conf. ( Samples can be found with `./notify.py --help` and `./notify_operator.py --help` )
* Add template MyTemplate_Bareos.xml/MyTemplate_Bacula.xml to zabbix. Assign it to host with bareos/bacula director.
* Disable auto-generated triggers for jobs that are not backup type(restore jobs, ...)
