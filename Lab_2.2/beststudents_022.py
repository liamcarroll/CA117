#!/usr/bin/env python3

import sys


def main():
    try:
        filename = sys.argv[1]
        highest_lines = []
        lines = []
        with open(filename, 'r') as f:
            for line in f:
                lines.append(line.strip())
            highest = 0

            for line in lines:
                try:
                    if highest < int(line[:2]):
                        highest = int(line[:2])
                except ValueError:
                    print('Invalid mark {} encountered. Skipping.'.format(line[:2]))

            for line in lines:
                if int(line[:2]) == highest:
                    highest_lines.append(line[3:])

        best_mark = highest
        best_students = ', '.join(highest_lines)
        print('Best student(s): {}'.format(best_students))
        print('Best mark: {}'.format(best_mark))
    except FileNotFoundError:
        print('The file {} could not be opened.'.format(filename))

if __name__ == '__main__':
    main()
