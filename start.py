#!/usr/bin/env python3

from util import *

def main():
    """Main method"""

    createDirIfNotExist()

    # A while loop for the user input interface
    while True:
        printMenuHeader('Installing Lightning Network Nodes')
        print('\nPlease choose:\n')
        print(' 1: Configure Ansible inventory.ini file')
        print(' 2: Install')
        print(' q: Quit')

        userChoice = getUserChoice()

        if userChoice == '1':
            configureAnsibleInventory()
        if userChoice == '2':
            install()
        elif userChoice == 'q':
            break
        else:
            print('Input was invalid, please pick a value from the list!')
            pressIntro()
            continue
    else:
        print('Exiting ...')


if __name__ == "__main__":
    main()
