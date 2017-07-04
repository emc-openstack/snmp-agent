# SNMP Off-Array Agent

## Introduction
SNMP Off-Array Agent is a python-based application running outside of storage system.
The client can communicate with this agent to retrieve the storage information via SNMP protocal.
But SNMP trap is not in the scope of this agent.

Currently, Unity is the first product supported by this agent. Here are the expected functions:
* Multiple storage systems management
* Support SNMP v2c and v3 protocol  
* Platform independent, that is, support both Windows and Linux
* Capability to deploy and install without internet access.
* Encrypt/Decrypt the configure file of the agent

## Command Line Interface
* snmpagent __help__

  Print out the help manual to list all SNMP agent's subcommands.
  
* snmpagent __*CMD* help__

  Print out the help manual of a specific *CMD*.

* snmpagent __start__ [--configure-file *\<snmpagent.conf\>*]

  Start a SNMP agent with the configuration file *snmpagent.conf* once the configure file is specified. 
Otherwise, the agent will use the default configuration file under the agent installation directory. If the agent is running, it will return an error message in both console and log file.

* snmpagent __restart__

  Restart a SNMP agent. It will return an error message in both console and log file if the agent is not running.
  
* snmpagent __stop__

  Stop a SNMP agent. It will return an error message in both console and log file if the agent is not running.

* snmpagent __addUser__ --version *v3* --name *user_name* --auth *auth_protocol* --authPass *auth_password* [--priv *privacy_protocol*] [--privPass *priv_password*]

  Create a SNMPv3 user, including user name, authentication protocol, authentication password, privacy protocol and privacy password.
   
   Authentication Protocol supported by this agent are:
   * MD5
   * SHA
   
   Privacy Protocol supported by this agent are:
   * DES

* snmpagent __updateUser__ --version *v3* --name *user_name* --auth *auth_protocol* --authPass *auth_password* [--new_auth_password *new_auth_password*] [--priv *new_priv_protocol*] [--privPass *new_priv_password*]

  Change authentication password, privacy protocol and privacy password if it is necessary.

* snmpagent __delUser__  --version *v3* --name *user_name*

  Delete a SNMPv3 user.

* snmpagent __createCommunity__ --name *community_name*

  Create a SNMPv2c community.
  
* snmpagent __delCommunity__  --name *community_name*

  Delete a SNMPv2c community.

* snmpagent __listUsers__

  List all SNMP users, including v2c and v3. But for SNMPv3 user, the authentication password and privacy password are masked by *.

  Sample output of the command __listUsers__:
  ```
  Attributes    Auth          SHA
                Auth Pass    ******
                Name         user_A
                Priv          DES
                Priv Pass    ******
                Version       v3
  Attributes    Community    Public
                Version       v2c
  ```
    
* snmpagent __encrypt__  --configure-file *\<path of snmpagent.conf\>*

  Create a new configuration file, but the password login to the storage is encrypted if it is pain text.
  
* snmpagent __decrypt__  --configure-file *\<path of snmpagent.conf\>*

  Create a new configuration file, but the password login to the storage is decrypted if it is encrypted.
