# Ansible playbook to install a Bitcoin Lightning Network node
1. Replace `REPLACE_RPCUSER`, `REPLACE_RPCPASSWORD` and `REPLACE_PRUNE` strings in bitcoin_core/vars/`main.yml` file for your choice, for example:
  ```bash
  download_destination: '/var/tmp'
  bitcoin_core_version: '0.17.1'
  bitcoin_core_file: 'bitcoin-{{bitcoin_core_version}}-arm-linux-gnueabihf.tar.gz'
  bitcoin_core_sha256: 'sha256: aab3c1fb92e47734fadded1d3f9ccf0ac5a59e3cdc28c43a52fcab9f0cb395bc'
  bitcoin_core_path: '/opt/bitcoin'
  bitcoin_core_config_path: '~/.bitcoin'
  bitcoin_core_rpcuser: johndoe
  bitcoin_core_rpcpassword: abcd1234
  bitcoin_core_prune: 50000
  bitcoin_core_data_file: 'bitcoin_datadir.tar.gz'
  ```

2. Replace `REPLACE_EXTERNAL_IP`, `REPLACE_ALIAS`, `REPLACE_RPCUSER` and `REPLACE_RPCPASSWORD` strings in lightning_network_daemon/vars/`main.yml` file for your choice, for example:
  ```bash
  download_destination: '/var/tmp'
  lnd_version: 'v0.5.2-beta'
  lnd_file: 'lnd-linux-armv7-{{lnd_version}}.tar.gz'
  lnd_sha256: 'sha256: 9adf9f3d0b8a62942f68d75ffe043f9255319209f751dee4eac82375ec0a86cd'
  lnd_path: '/opt/lnd'
  lnd_config_path: '~/.bitcoin'
  lnd_externalip: 86.53.156.171
  lnd_alias: my_lightning_network_node
  lnd_rpcuser: johndoe
  lnd_rpcpassword: abcd1234
  ```
2. Write your own `inventory.ini` file wit all your hosts and IP addresses, for example:
  ```bash
  [all]
  raspberryPi_000 ansible_host=192.168.1.101
  raspberryPi_001 ansible_host=192.168.1.102
  raspberryPi_002 ansible_host=192.168.1.103
  ...

  [LightningNetworkNodes]
  raspberryPi_000
  raspberryPi_001
  raspberryPi_002
  ...
  ```

3. Download [complete blockchain data](https://bitcoineando.es/btc_datadir/bitcoin_datadir.tar) from any regular computer. Once downloaded compress the data in a file called `bitcoin_datadir.tar.gz`.
  ```bash
  tar zcvf bitcoin_datadir.tar.gz blocks chainstate
  ```

4. Store it in bitcoin_core/`files` directory.

5. Launch this Ansible playbook to automatically install and configure a Bitcoin Lighting Network node on one or more hosts.
  ```bash
  ansible-playbook -i inventory.ini -u pi --ask-pass main.yaml
  ```
