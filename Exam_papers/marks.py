#!/usr/bin/env python3

import sys


def main():
    try:
        with open(sys.argv[1], 'r') as f:
            for l in f:
                l = l.strip()
                name, mark = ' '.join(l.split()[1:-1]), l.split()[-1]
                if int(mark) >= 40:
                    print('{:s} passed with a mark of {:d}'.format(
                        name, int(mark)))
                else:
                    print('{:s} failed with a mark of {:d}'.format(
                        name, int(mark)))

    except ValueError:
        print('Invalid mark encountered: {:s}. Exiting.'.format(mark))

if __name__ == '__main__':
    main()
