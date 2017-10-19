NOTICE!!!
zabbix user in psql must be superuser
after changing configuring psql sometimes it has to restart postgresql service (not reload)

PostgreSQL monitoring with Zabbix.
This configurations was tested on postgres 9.6 and zabbix-server 3.0

based on pgCayenne 

There are 2 templates:
	* Common: common metrics and discovery databases
	* DATABASENAME: tables autodiscovery
	  So you need to copy database-template for each DB. Use template.preparing.sh script: 
	  	./template.preparing.sh mydatabase 
	  then upload to Zabbix gui

#### INSTALLATIONs

```
git clone https://github.com/igogorevi4/Zabbix-Extensions.git

mkdir /etc/zabbix/zabbix_agentd.d/

cp files/postgresql/postgresql.conf /etc/zabbix/zabbix_agentd.d/

nano /etc/zabbix/zabbix_agentd.conf

Include=/etc/zabbix/zabbix_agentd.d/

systemctl restart zabbix-agent.service
```
```
- create zabbix user in postgres:

	CREATE USER zabbix WITH PASSWORD 'qwerty12345' SUPERUSER;
	
- edit access rules in postgres [pg_hba.conf](http://www.postgresql.org/docs/9.6/static/auth-pg-hba-conf.html)
	host    all             zabbix             127.0.0.1/32            trust
- or add file .pgpass to zabbix homedir with content like so: 
	
	host IP:port:database:postges user:password
	127.0.0.1:5432:*:zabbix:qwerty12345 # for all DBs

```
- import XML template into web monitoring and link template with target host;

- edit template macros, go to the template page and open "Macros" tab:

- if you want to monitor buffers' and SQL statements executed by a server statistic, you need to add some extensions for all DBs you want observe:

	CREATE EXTENSION pg_stat_statements;
	CREATE EXTENSION pg_buffercache;

PG_CONNINFO - connection settings for zabbix agent connections to the postgres service;

PG_CONNINFO_STANDBY - connection settings for zabbix agent connections to the postgres service on standby servers, required for streaming replication lag monitoring;

PG_CACHE_HIT_RATIO - shared buffers cache ratio;

PG_CHECKPOINTS_REQ_THRESHOLD - threshold for checkpoints which occured by demand;

PG_CONFLICTS_THRESHOLD - threshold for recovery conflicts trigger;

PG_CONN_IDLE_IN_TRANSACTION - threshold for connections which is idle in transaction state;

PG_CONN_TOTAL_PCT - the percentage of the total number of connections to the maximum allowed (max_connections);

PG_CONN_WAITING - threshold for connections which is in waiting state;

PG_DATABASE_SIZE_THRESHOLD - threshold for database size;

PG_DEADLOCKS_THRESHOLD - threshold for deadlock conflicts trigger;

PG_LONG_QUERY_THRESHOLD - threshold for long transactions trigger;

PG_PING_THRESHOLD_MS - threshold for postgres service response;

PG_SR_LAG_BYTE - threshold in bytes for streaming replication lag between server and discovered standby servers;

PG_SR_LAG_SEC - threshold in seconds for streaming replication lag between server and discovered standby servers;

PG_UPTIME_THRESHOLD - threshold for service uptime.

- add additional items into template if required.

#### Graphs description
- PostgreSQL bgwriter - information about buffers, how much allocated and written.
- PostgreSQL buffers - general information about shared buffers; how much cleaned, dirtied, used and total.
- PostgreSQL checkpoints - checkpoints and write/sync time during chckpoints.
- PostgreSQL connections - connection info (idle, active, waiting, idle in transaction).
- PostgreSQL service response - service response, average query time (pg_stat_statements required).
- PostgreSQL summary db stats: block hit/read - information about how much blocks read from disk or cache.
- PostgreSQL summary db stats: events - commits and rollbacks, recovery conflicts and deadlocks.
- PostgreSQL summary db stats: temp files - information about allocated temporary files.
- PostgreSQL summary db stats: tuples - how much tuples inserted/deleted/updated/fetched/returned.
- PostgreSQL transactions - max execution time for active/idle/waiting/prepared transactions.
- PostgreSQL uptime - cache hit ratio and uptime.
- PostgerSQL write-ahead log - information about amount of WAL write and WAL segments count.
- PostgreSQL database size - per-database graph with database size.
- PostgreSQL table read stat - information about how much block of table or index readden from disk or cache (per-table).
- PostgreSQL table rows - how much tuples inserted/updated/deleted per second (per-table).
- PostgreSQL table scans - sequential/index scans andhow much rows returned by this scans (per-table).
- PostgreSQL table size - table and table's indexes size (per-table).
- PostgreSQL streaming replication lag with standby - streaming replication between master and standby in bytes and seconds (per-standby).

#### Known issues:
- Supported PostgreSQL version is 9.6
- Strongly recommended install pg_buffercache and pg_stat_statements extensions into monitored database.
- Table low-level discovery require manual specifies a list of tables to find, otherwise LLD generate many items (21 item per table).