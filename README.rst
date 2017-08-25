SNMP Off-Array Agent
====================


Introduction
------------
SNMP Off-Array Agent is a python-based application running outside of storage system.
The client can communicate with this agent to retrieve the storage information via SNMP protocal.
But SNMP trap is not in the scope of this agent.

Currently, Unity is the first product supported by this agent. Here are the expected functions:

- Multiple storage systems management
- Support SNMP v2c and v3 protocol  
- Platform independent, that is, support both Windows and Linux
- Capability to deploy and install without internet access.
- Encrypt/Decrypt the configure file of the agent

Command Line Interface
----------------------

*snmpagent --help*
  Print out the help manual to list all SNMP agent's subcommands.
  
*snmpagent CMD --help*
  Print out the help manual of a specific ``CMD``. ``CMD`` supports ``add-user``, ``update-user``, ``delete-user``, ``create-community``, ``delete-community``, ``list-users``, ``encrypt``, ``decrypt``, ``start``, ``stop``, ``restart``.
  
*snmpagent start [--conf_file <file_path>]*
  Start a SNMP agent with the configuration file ``<file_path>`` once the configure file is specified. 
  Otherwise, the agent will use the default configuration file under the agent installation directory. If the agent is running, it will return an error message in both console and log file.

*snmpagent restart*
  Restart a SNMP agent. It will return an error message in both console and log file if the agent is not running.
  
*snmpagent stop*
  Stop a SNMP agent. It will return an error message in both console and log file if the agent is not running.

*snmpagent add-user --name <user_name> --auth <auth_protocol> --auth_key <auth_password> [--priv <privacy_protocol>] [--priv_key <priv_password>]*
  Create a SNMPv3 user, including user name, authentication protocol, authentication password, privacy protocol and privacy password.
  Authentication Protocol supported by this agent are:
  
  - MD5
  - SHA
    
  Privacy Protocol supported by this agent are:
  
  - DES
  - AES

*snmpagent update-user --name <user_name> --auth <new_auth_protocol> --auth_key <new_auth_password> [--priv <new_priv_protocol>] [--priv_key <new_priv_password>]*
  Change authentication protocol, authentication password, privacy protocol and privacy password if it is necessary.

*snmpagent delete-user --name <user_name>*
  Delete a SNMPv3 user.

*snmpagent create-community --name <community_name>*
  Create a SNMPv2c community.
  
*snmpagent delete-community --name <community_name>*
  Delete a SNMPv2c community.

*snmpagent list-users*
  List all SNMP users, including v2c and v3. But for SNMPv3 user, the authentication password and privacy password are encrypted.
  Sample output of the command ``list-users``:
  ::
    SNMP Version 2 Community Access:
    user_1
      Version:    SNMPv2c
      Community:  Public
    SNMP Version 3 Users:
    user_2
      Version:            SNMPv3
      Security Level:     authPriv
      Auth Protocol:      MD5
      Auth Key:           34a0323fa11e5432ebe681b103de1fa5\x06
      Privacy Protocol:   AES
      Privacy Key:        040591c13f4a9d3b470f108493d26b0f\x06
    
*snmpagent encrypt --conf_file <file_path>*
  Create a new configuration file in the same direcotry of unencrypted configuration file, but the password login to the storage is encrypted if it is pain text. It will reutrn a "Permission deny" message in case that the directory is not allowed to write.
  
*snmpagent decrypt --conf_file <file_path>*
  Create a new configuration file in the same directory of the encrypted configuration file, but the password login to the storage is decrypted if it is encrypted. It will reutrn a "Permission deny" message in case that the directory is not allowed to write.

Configurations
--------------



Authentication data
-------------------
