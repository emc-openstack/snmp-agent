Dell EMC Unity SNMP Off-Array Agent
===================================

**Table of contents**

- `Introduction`_
- `License`_
- `Requirements`_
- `Installation`_
    * `From Pypi`_
    * `From source`_
- `User guide`_
    * `Get help`_
    * `Daemon and service control`_
    * `SNMP user management`_
    * `Configuration file encryption and decryption`_
- `Agent configuration file`_
- `Agent authentication data`_
- `Contributions`_
- `Release note`_

Introduction
------------
Dell EMC Unity SNMP Off-Array Agent is a python-based application running outside of Unity system.
It provides a easy-to-use CLI tool for management purpose and a daemon to handle the incoming SNMP
queries.

Any SNMP client can communicate with this agent to retrieve the storage information via SNMP protocol.
Currently the SNMP trap is not supported by this agent.

The Unity is the first product supported by this agent.
Here are the features:

- Support SNMPv2c and SNMPv3 protocol.
- Support multiple storage systems management.
- Platform independent, both Windows and Linux are supported.
- Capability to deploy and install without internet access.
- Encrypt/Decrypt the configure file of the agent.

License
-------

`Apache License 2.0 <LICENSE>`_

Requirements
------------

- Python 2.7 or Python 3.4 and above.
- Linux/Windows.

Installation
------------

From Pypi
^^^^^^^^^
Install via ``pip`` is recommended way to deploy the ``snmpagent-unity``.

.. code-block:: console

    pip install snmpagent-unity

From source
^^^^^^^^^^^

If latest code is preferred, User can clone this repository and install from source.

.. code-block:: console

    git clone http://github.com/emc-openstack/snmpagent-unity
    cd snmpagent-unity
    python setup.py install

After installation, a command line tool ``snmpagent-unity`` will be installed under ``/usr/local/bin/`` (Linux) or
``<python installation path>\Scripts\`` (Windows)

User guide
----------

Get help
^^^^^^^^

- Get general help

.. code-block:: console

    snmpagent-unity --help

Print out the help manual to list all subcommands.

- Get help for specific command

.. code-block:: console

    snmpagent-unity <CMD> --help

Print out the help manual of a specific ``<CMD>``.
``<CMD>`` supports ``add-user``, ``update-user``, ``delete-user``, ``create-community``,
``delete-community``, ``list-users``, ``encrypt``, ``decrypt``, ``start``, ``stop``, ``restart``.

Daemon and service control
^^^^^^^^^^^^^^^^^^^^^^^^^^

- Start a daemon

.. code-block:: console

    snmpagent-unity start --conf_file <file_path>

Start a SNMP agent with the specified configuration file ``<file_path>``.
This command will return error if the daemon is already running.
For the configuration file, you can refer to `Agent configuration file`_

- Restart a running daemon

.. code-block:: console

    snmpagent-unity restart

Restart a SNMP agent. An error will occur if not running daemon found.

- Stop a running daemon

.. code-block:: console

    snmpagent-unity stop

SNMP user management
^^^^^^^^^^^^^^^^^^^^
- Create a SNMP v2 community

.. code-block:: console

    snmpagent-unity create-community --name <community_name>


- Delete a SNMP v2 community

.. code-block:: console

    snmpagent-unity delete-community --name <community_name>

- Create a SNMP v3 user

.. code-block:: console

    snmpagent-unity add-user --name <user_name> --auth <auth_protocol> --auth_key <auth_password> [--priv <privacy_protocol>] [--priv_key <priv_password>]


Create a SNMPv3 user with user name, authentication protocol, authentication password, privacy protocol and privacy password.

Authentication Protocols supported are:
  
  - MD5
  - SHA
    
Privacy Protocols supported are:
  
  - DES
  - AES

- Update a SNMP v3 user

.. code-block:: console

    snmpagent-unity update-user --name <user_name> --auth <new_auth_protocol> --auth_key <new_auth_password> [--priv <new_priv_protocol>] [--priv_key <new_priv_password>]


Change privacy protocol and privacy password if provided.

- Delete a SNMP v3 user

.. code-block:: console

    snmpagent-unity delete-user --name <user_name>


- List all users

.. code-block:: console

    snmpagent-unity list-users

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


Configuration file encryption and decryption
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. note::
    The encrypted/decrypted file will replace the original file immediately after
    the command, so make sure the daemon is stopped before performing these operations.

- Encrypt a configuration file

.. code-block:: console

    snmpagent-unity encrypt --conf_file <file_path>

Encrypt the specified configuration file.
The password of the Unity system is encrypted if it is pain text.

- Decrypt a configuration file

.. code-block:: console

    snmpagent-unity decrypt --conf_file <file_path>

Decrypt the specified configuration file.
The password of the Unity system is decrypted if it is encrypted.


Agent configuration file
------------------------

In an agent configuration file, a fixed section ``[DEFAULT]`` is required for global settings.

Following options can be configured under ``[DEFAULT]``:

.. code-block:: ini

    # Host IP address for listening by the agent
    agent_ip=0.0.0.0
    # Logging level of the agent
    # Supported log level: debug, info, warning, error, critical
    log_level=info
    # Log file, can be relative or absolute file path
    log_file=snmpagent-unity.log
    # Max size in bytes before log rotation
    log_file_maxbytes=104857600
    # Max log file count
    log_file_count=10



The agent also supports varying amount of Unity systems in one agent file, here is the configuration for two unity systems:

.. code-block:: ini

    [unity-1]
    # Port for servicing the SNMP requests
    agent_port=11161
    # System model, unity is the only supported model for now
    model=unity
    # Unity Management IP address
    mgmt_ip=10.10.10.1
    # Unity User login
    user=admin
    # Unity User password
    password=password
    # Cache interval before fetching new stats From Unity system.
    # Consider setting it to a appropriate value in second for aspects of
    # performance and timeliness
    # Please set a smaller value than metric query interval (60s)
    # so the metric info can be calculated correctly
    cache_interval=30

    [unity-2]
    agent_port=11162
    model=unity
    mgmt_ip=10.10.10.2
    user=admin
    password=password
    cache_interval=30


User can configure multiple sections for different system, be aware that each section should have
a unique section name(like ``unity-1`` and ``unity-2`` in above example).

Restart is required for any change in configration file to take effect.

For a complete example, please check out the agent configuration file `agent.conf <templates/agent.conf>`_

Agent authentication data
-------------------------

The Unity SNMP agent stores the encrypted access data under the home of user running the agent.
Usually it's ``%USERPROFILE%\.snmpagent-unity\`` on Windows, ``$HOME/.snmpagent-unity/`` on Linux.

Contributions
-------------
Simply fork this repo and send PR for your code change(also tests to cover your change),
remember to give a title and description of your PR. We are willing to enhance this project with you :).


Release note
------------

v0.1.0: First release of snmpagent-unity
