#!/usr/bin/env python3

import os

outDir          = 'out'
inventoryFile   = 'inventory.ini'


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


def configureAnsibleInventory():
    """Configure Ansible inventory.ini file."""

    # Set local variables.
    nodeList    = []
    n_nodes     = int(input('\nNumber of nodes: '))

    # Ask to user data about nodes.
    for node in range(n_nodes):
        nodeName    = input('Node {} name: '.format(node))
        nodeIp      = input('Node {} IP: '.format(node))
        nodeAlias   = input('Node {} alias: '.format(node))
        nodeDict    = {
            'name': nodeName,
            'ip': nodeIp,
            'alias': nodeAlias
        }
        nodeList.append(nodeDict)

    # Write data inventory.ini file.
    try:
        with open(inventoryFile, 'w') as f:
            f.write('[all]\n')
            for host in nodeList:
                f.write('{} ansible_host={} alias={}\n'.format(
                    host['name'],
                    host['ip'],
                    host['alias'])
                )
            f.write('\n[LightningNetworkNodes]\n')
            for host in nodeList:
                f.write('{}\n'.format(host['name']))
    except IOError:
        print('Saving failed!')


def install():
    pass
