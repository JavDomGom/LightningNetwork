# Ansible playbook to install Bitcoin Core and Lightning Network Node

## Getting Started
With this playbook you can install the Bitcoin Core client and a Node Lightning Network in "N" computers from a single point of execution.

## Requirements

### Control Machine
- GNU/Linux, Unix or OS X operative system. Windows isn’t supported.
- [Ansible 2.7](https://docs.ansible.com/ansible/latest/installation_guide/intro_installation.html#latest-releases-via-pip)
- Python 2 (versions [2.6](https://www.python.org/download/releases/2.6/) or [2.7](https://www.python.org/downloads/release/python-2715/)) or Python 3 (versions [3.5](https://www.python.org/downloads/release/python-350/) and higher).
- SSH protocol to manage machines.

### Managed Node
You can use a regular computer or RaspberryPi to run Bitcoin Core and Lightning Network node.
- GNU/Linux, Unix or OS X operative system. Windows isn’t supported.
- Python [2.6](https://www.python.org/download/releases/2.6/) or higher.
- Internet connection to download software.

![alt text](img/ansible_playbook_bitcoin_lightning_network.png)

## How it works
This Ansible Playbook can be executed in two possible ways:
* Automatic mode with an interactive menu.
* Manual execution.

### Automatic mode with an interactive menu.
1. Execute this command:
  ```bash
  ~$ python3 start.py
  ```
2. The following interactive menu will be displayed on the screen.
  ```
  ==================================
  Installing Lightning Network Nodes
  ==================================
  Please choose

  1: Configure nodes
  2: Install
  q: Quit

  Your choice:
  ```
3. First you have to configure the nodes that you want to install, for this you have to select the first option of the menu. You will have to answer some common questions, such as the value for prune and the name of the nodes in the Ansible inventory (not hostname), and finally you will have to answer a question set for each node you want to build, for example:
  ```
  Your choice: 1

  Prune (Default: 50000):
  Number of nodes: 2
  Name for nodes: raspberryPi
  Node raspberryPi_000 IP: 192.168.1.100
  Node raspberryPi_000 alias (Default: lnd_000):
  Node raspberryPi_000 user: JavDomGom
  Node raspberryPi_000 password: abcd1234
  Node raspberryPi_001 IP: 192.168.1.101
  Node raspberryPi_001 alias (Default: lnd_001):
  Node raspberryPi_001 user: JavDomGom
  Node raspberryPi_001 password: abcd1234
  ```
In questions that suggest a default value you can press Enter without entering any data if you agree with the suggested value.

4. Finally just install.
  ```
  Your choice: 2

  SSH password: HERE_ENTER_YOUR_HOSTS_COMMON_PASSWORD

  PLAY [Bitcoin core and Lightning Network node installation] ********************************************

  TASK [Gathering Facts] *********************************************************************************
  ok: [raspberryPi_001]
  ok: [raspberryPi_000]

  TASK [init_conf : Modify static ip_address in /etc/dhcpcd.conf file] ***********************************
  changed: [raspberryPi_001]
  changed: [raspberryPi_000]

  TASK [init_conf : Modify static routers in /etc/dhcpcd.conf file] **************************************
  changed: [raspberryPi_001]
  changed: [raspberryPi_000]

  .
  .
  .

  TASK [lightning_network_daemon : Add Lightning Network Daemon directory to PATH in pi .profile file] ***
  changed: [raspberryPi_001]
  changed: [raspberryPi_000]

  TASK [lightning_network_daemon : Configuring Lightning Network Daemon] *********************************
  changed: [raspberryPi_001]
  changed: [raspberryPi_000]

  PLAY RECAP *********************************************************************************************
  raspberryPi_000            : ok=24   changed=22   unreachable=0    failed=0
  raspberryPi_001            : ok=24   changed=22   unreachable=0    failed=0
  ```

### Manual execution
In case you choose a manual execution before you must perform the following steps.

1. Replace `REPLACE_PRUNE` string in bitcoin_core/vars/`main.yml` file for your choice, for example:
  ```bash
  download_destination: '/var/tmp'
  bitcoin_core_version: '0.17.1'
  bitcoin_core_file: 'bitcoin-{{bitcoin_core_version}}-arm-linux-gnueabihf.tar.gz'
  bitcoin_core_sha256: 'sha256: aab3c1fb92e47734fadded1d3f9ccf0ac5a59e3cdc28c43a52fcab9f0cb395bc'
  bitcoin_core_path: '/opt/bitcoin'
  bitcoin_core_config_path: '~/.bitcoin'
  bitcoin_core_prune: 50000
  ```

2. Replace `REPLACE_EXTERNAL_IP` string in lightning_network_daemon/vars/`main.yml` file for your choice, for example:
  ```bash
  download_destination: '/var/tmp'
  lnd_version: 'v0.5.2-beta'
  lnd_file: 'lnd-linux-armv7-{{lnd_version}}.tar.gz'
  lnd_sha256: 'sha256: 9adf9f3d0b8a62942f68d75ffe043f9255319209f751dee4eac82375ec0a86cd'
  lnd_path: '/opt/lnd'
  lnd_config_path: '~/.bitcoin'
  lnd_externalip: 86.53.156.171
  ```
3. Write your own `inventory.ini` file with your hosts, IP addresses and other custom variables like `alias`, `rpcuser` and `rpcpassword`, for example:
  ```bash
  [all]
  myNode_000 ansible_host=192.168.1.100 alias=lnd_000 rpcuser=Bob rpcpassword=abcd1234
  myNode_001 ansible_host=192.168.1.101 alias=lnd_001 rpcuser=Alice rpcpassword=1234abcd
  myNode_002 ansible_host=192.168.1.102 alias=lnd_002 rpcuser=JohnDoe rpcpassword=qazwsxed
  ...

  [LightningNetworkNodes]
  myNode_000
  myNode_001
  myNode_002
  ...
  ```

4. Launch this Ansible playbook to automatically install and configure a Bitcoin Lighting Network node on one or more hosts.
  ```bash
  ~$ ansible-playbook -i inventory.ini -u pi --ask-pass main.yaml
  ```

5. The Ansible installation starts in the same way as in point 4 of the automatic installation.

## Testing
To ensure that it works correctly, we must access any node via SSH, for example:
  ```bash
  ~$ ssh -o StrictHostKeyChecking=no pi@192.168.1.100
  ```
Check your Bitcoin Core configuration file.
  ```bash
  ~$ cat ~/.bitcoin/bitcoin.conf
  ```
Make sure that the values of the `rpcuser`, `rpcpassword` and `prune` variables have been correctly set.
  ```
  daemon=1
  server=1
  rpcuser=JavDomGom
  rpcpassword=abcd1234
  prune=50000
  zmqpubrawblock=tcp://127.0.0.1:18501
  zmqpubrawtx=tcp://127.0.0.1:18502
  ```
Check your Lightning Network Node configuration file.
  ```bash
  ~$ cat ~/.lnd/lnd.conf
  ```
Make sure that the values of the `externalip`, `alias`, `bitcoind.rpcuser` and `bitcoind.rpcpass` variables have been correctly set.
  ```
  bitcoin.active=1
  bitcoin.mainnet=1
  bitcoin.node=bitcoind
  externalip=86.53.156.171
  alias=lnd_000
  bitcoind.rpcuser=JavDomGom
  bitcoind.rpcpass=abcd1234
  bitcoind.zmqpubrawblock=tcp://127.0.0.1:18501
  bitcoind.zmqpubrawtx=tcp://127.0.0.1:18502
  rpclisten=0.0.0.0:10009
  ```
Finally, execute the following command to make sure that the blocks of the Bitcoin blockchain are completely synchronized:
  ```bash
  ~$ bitcoin-cli getblockchaininfo
  ```
It will return a result similar to this:
  ```
  {
    "chain": "main",
    "blocks": 565515,
    "headers": 565515,
    "bestblockhash": "000000000000000000240c6851b130e577a62e47a54d637db24bcba4f5a18638",
    "difficulty": 6071846049920.752,
    "mediantime": 1551632167,
    "verificationprogress": 0.9999956283626329,
    ...
  ```
If the values of the `blocks` and `headers` attributes are equal it means that the blockchain is correctly synchronized.
