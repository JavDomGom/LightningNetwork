#!/usr/bin/env python3

from util import *

def main():
    """Main method"""

    createDirIfNotExist()

    # A while loop for the user input interface
    while True:
        printMenuHeader('Installing Lightning Network Nodes')
        print('Please choose\n')
        print('1: Configure nodes')
        print('2: Install')
        print('q: Quit')
        userChoice = getUserChoice()
        if userChoice == '1':
            configureNodes()
        elif userChoice == '2':
            install()
        elif userChoice == 'q':
            break
        else:
            print('Input was invalid, please pick a value from the list!')
    else:
        print('User left!')


if __name__ == "__main__":
    main()
