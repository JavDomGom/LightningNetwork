#!/usr/bin/env python3

import os
import fileinput
import subprocess
import yaml

outDir          = 'out'
inventoryFile   = 'inventory.ini'
mainYaml        = 'main.yaml'
nodesConfigured = False

def printMenuHeader(title):
    """Prints menu headers with format.

    Attributes:
        :title: Title to show in header.
    """

    # Line for pretty print menu headers.
    line = '=' * len(title)

    # Clear screen.
    # os.system('clear')

    print('%s\n%s\n%s' % (line, title, line))


def pressIntro():
    """Wait for a user to press Enter and back to the main menu."""

    input('\nPress [Enter] to continue ...')


def getUserChoice():
    """Prompts the user for it's choice and return it."""

    user_input = input('\nYour choice: ')
    return user_input


def createDirIfNotExist(dir=outDir):
    """If dir not exist creat it.
    Attributes:
        :dir: Directory to check.
    """

    if not os.path.exists(dir):
        os.makedirs(dir)


def replaceData(file, oldString, newString):
    """Replace string in a template file.

    Attributes:
        :file:      Template in which the replacement will be made.
        :oldString: Old string that will be replaced.
        :newString: New replacement string.
    """

    try:
        for line in fileinput.input([file], inplace=True):
            print(line.replace(oldString, newString), end='')
    except IOError:
        print('ERROR: Saving data failed!')


def configureNodes():
    """Configure Ansible inventory.ini file."""

    # Set local variables.
    nodesList       = []
    defaultPrune    = '50000'
    globalUser      = str(input('\nGlobal access user: '))
    prune           = input('Prune (Default: {}): '.format(defaultPrune)) or defaultPrune
    n_nodes         = int(input('Number of nodes: '))
    nodesName       = input('Name for nodes: ')
    externalIP      = os.popen('curl -s ifconfig.me').readline()
    bcVarsFile      = 'bitcoin_core/vars/main.yml'
    lndVarsFile     = 'lightning_network_daemon/vars/main.yml'

    # Ask to user data about nodes.
    for n in range(n_nodes):
        number          = str(n).zfill(3)
        name            = nodesName+'_'+number
        defaultAlias    = 'lnd_'+number
        ip              = input('Node {} IP: '.format(name))
        alias           = input('Node {} alias (Default: {}): '
                          .format(name, defaultAlias)) or defaultAlias
        rpcuser         = input('Node {} user: '.format(name))
        rpcpassword     = input('Node {} password: '.format(name))
        nodeDict        = {
            'name': name,
            'ip': ip,
            'alias': alias,
            'rpcuser': rpcuser,
            'rpcpassword': rpcpassword
        }
        nodesList.append(nodeDict)

    # Write data inventory.ini file.
    try:
        with open(inventoryFile, 'w') as f:
            f.write('[all]\n')
            for host in nodesList:
                f.write('{} ansible_host={} alias={} rpcuser={} rpcpassword={}\n'
                    .format(
                        host['name'],
                        host['ip'],
                        host['alias'],
                        host['rpcuser'],
                        host['rpcpassword']
                    )
                )
            f.write('\n[LightningNetworkNodes]\n')
            for host in nodesList:
                f.write('{}\n'.format(host['name']))
    except IOError:
        print('Saving failed!')

    replaceData(mainYaml, 'REPLACE_GLOBAL_USER', globalUser)
    replaceData(bcVarsFile, 'REPLACE_PRUNE', prune)
    replaceData(lndVarsFile, 'REPLACE_EXTERNAL_IP', externalIP)

    nodesConfigured = True

def install():
    """This method launch Ansible playbook to install Bitcoin Core and Lightning Network."""
    with open(mainYaml, 'r') as f:
        try:
            remote_user = yaml.load(f)[0]['remote_user']
            subprocess.run(['ansible-playbook -i '+inventoryFile+' -u '+remote_user+' --ask-pass '+mainYaml], shell=True)
        except yaml.YAMLError as e:
            print(e)
    pressIntro()
