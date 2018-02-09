#!/usr/bin/env python3

import sys


def main():
    try:
        filename = sys.argv[1]
        highest = 0
        with open(filename, 'r') as f:
            for line in f:
                try:
                    if highest < int(line[:2]):
                        highest = int(line[:2])
                        highest_line = line.strip()
                except ValueError:
                    print('Invalid mark {} encountered. Skipping.'.format(line[:2]))
        best_mark = highest_line[:2]
        best_student = highest_line[3:]
        print('Best student: {}'.format(best_student))
        print('Best mark: {}'.format(best_mark))
    except FileNotFoundError:
        print('The file {} could not be opened.'.format(filename))

if __name__ == '__main__':
    main()
