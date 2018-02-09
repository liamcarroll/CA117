#!/usr/bin/env python3

import sys


def main():
    for line in sys.stdin:
        try:
            n = int(line.strip())
            break
        except ValueError:
            print('{} is not a number'.format(line.strip()))
    print('Thank you for {}'.format(n))

if __name__ == '__main__':
    main()
