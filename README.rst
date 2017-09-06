Dell EMC Unity SNMP Off-Array Agent
===================================


Introduction
------------
Dell EMC Unity SNMP Off-Array Agent is a python-based application running outside of storage system.
Any SNMP client can communicate with this agent to retrieve the storage information via SNMP protocol.
But SNMP trap is not in the scope of this agent.

Currently, Unity is the first product supported by this agent. Here are the expected functions:

- Multiple storage systems management
- Support SNMP v2c and v3 protocol  
- Platform independent, that is, support both Windows and Linux
- Capability to deploy and install without internet access.
- Encrypt/Decrypt the configure file of the agent

Command Line Interface
----------------------

*snmpagent-unity --help*
  Print out the help manual to list all subcommands of Unity SNMP agent .
  
*snmpagent-unity CMD --help*
  Print out the help manual of a specific ``CMD``. ``CMD`` supports ``add-user``, ``update-user``, ``delete-user``, ``create-community``, ``delete-community``, ``list-users``, ``encrypt``, ``decrypt``, ``start``, ``stop``, ``restart``.
  
*snmpagent-unity start --conf_file <file_path>*
  Start a SNMP agent with the specified configuration file ``<file_path>``.
  If the agent is already running, an error message will be returned in both console and log file.

*snmpagent-unity restart*
  Restart a SNMP agent. It returns an error if the agent fails to start the agent.
  
*snmpagent-unity stop*
  Stop the running SNMP agent. It returns an error in both console and log file if the agent is not running.

*snmpagent-unity add-user --name <user_name> --auth <auth_protocol> --auth_key <auth_password> [--priv <privacy_protocol>] [--priv_key <priv_password>]*
  Create a SNMPv3 user, including user name, authentication protocol, authentication password, privacy protocol and privacy password.
  Authentication Protocols supported by this agent are:
  
  - MD5
  - SHA
    
  Privacy Protocols supported by this agent are:
  
  - DES
  - AES

*snmpagent-unity update-user --name <user_name> --auth <new_auth_protocol> --auth_key <new_auth_password> [--priv <new_priv_protocol>] [--priv_key <new_priv_password>]*
  Change authentication protocol, authentication password, privacy protocol and privacy password if it is necessary.

*snmpagent-unity delete-user --name <user_name>*
  Delete a SNMPv3 user.

*snmpagent-unity create-community --name <community_name>*
  Create a SNMPv2c community.
  
*snmpagent-unity delete-community --name <community_name>*
  Delete a SNMPv2c community.

*snmpagent-unity list-users*
  List all SNMP users, including v2c and v3. But for SNMPv3 user, the authentication password and privacy password are encrypted.
  Sample output of the command ``list-users``:

.. code-block:: console

    SNMP Version 2 Community Access:
    public
        Version:    SNMP Version 2c
        Community:  public

    SNMP Version 3 Users:
    for_update
        Version:            SNMP Version 3
        Security Level:     Authentication
        Auth Protocol:      MD5
        Auth Key:           ******
        Privacy Protocol:   -
        Privacy Key:        -



*snmpagent-unity encrypt --conf_file <file_path>*
  Encrpts the specified configuration file. The password login to the storage is encrypted if it is pain text.
  It returns a "Permission denied" message in case the directory is not allowed to write.
  
*snmpagent-unity decrypt --conf_file <file_path>*
  Decryps the specified configuration file. but the password login to the storage is decrypted if it is encrypted.
  It returns a "Permission denied" message in case the directory is not allowed to write.


Agent configuration file
------------------------
In an agent configuration file, a fixed section ``[DEFAULT]`` is required for global settings.

Following options can be configured under ``[DEFAULT]``:

.. code-block:: ini

    # Host IP address for listening by the agent
    agent_ip=0.0.0.0
    # Logging level of the agent
    log_level=debug
    # Log file, can be relative or absolute file path
    log_file=snmpagent-unity.log
    # Max size in bytes before log rotation
    log_file_maxbytes=104857600
    # Max log file count
    log_file_count=10



The agent also supports varying amount of Unity systems in one agent file, here is the configuration for one unity system:

.. code-block:: ini

    [unity-1]
    # Port for servicing the SNMP requests
    agent_port=11161
    # System model, unity is the only supported model for now
    model=unity
    # Unity Managemnt IP address
    mgmt_ip=10.245.101.39
    # Unity User login
    user=admin
    # Unity User password
    password=Password123!
    # Cache interval before fetching new stats From Unity system.
    # Consider setting it to a appropriate value in second for aspects of
    # performance and timeliness
    cache_interval=30



User can configure multiple sections for different system, be aware that each section should have
a unique section name(``unity-1`` in above example).

Restart is required for any change in configration file to take effect.


For a complete example, please check out the agent configuration file: `agent.conf <templates\agent.conf>`_

Authentication data
-------------------

The Unity SNMP agent stores the encrypted access data under the home of user running the agent. Usually it's ``%USERPROFILE%\.snmpagent-unity\`` on Windows, ``$HOME/.snmpagent-unity/`` on *nux.


