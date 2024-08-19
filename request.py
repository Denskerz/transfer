https://github.com/dsuch/pymqi/tree/main/code

If you use optional Oracle configuration files such as tnsnames.ora, sqlnet.ora or oraaccess.xml with Instant Client, then put the files in an accessible directory, for example in /opt/oracle/your_config_dir. Then use:

import cx_Oracle
cx_Oracle.init_oracle_client(config_dir="/opt/oracle/your_config_dir")
Or set the environment variable TNS_ADMIN to that directory name.

Alternatively, put the files in the network/admin subdirectory of Instant Client, for example in /usr/lib/oracle/21/client64/lib/network/admin. This is the default Oracle configuration directory for executables linked with this Instant Client.
