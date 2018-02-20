#!/usr/bin/env python3

import sys

contacts = {}


def main():
    with open(sys.argv[1], 'r') as f:
        for line in f:
            [name, number] = line.strip().split()
            contacts[name] = number

    for line in sys.stdin:
        name = line.strip()
        print('Name: {}'.format(name))
        try:
            print('Phone: {}'.format(contacts[name]))
        except KeyError:
            print('No such contact')

if __name__ == '__main__':
    main()