#!/usr/bin/env python3

import sys

def highest_student(file):
    try:
        highest = 0
        with open(file, 'r') as f:
            for line in f:
                tokens = line.strip().split()
                if highest < int(tokens[0]):
                    highest = int(tokens[0])
                    highest_line = tokens
        return tokens
    except FileNotFoundError:
        print('The file {} could not be opened.'.format(file))


def main():
    filename = sys.argv[1]
    best_mark = highest_student(filename)[0]
    best_student = highest_student(filename)[1]
    print('Best student: {}'.format(best_student))
    print('Best mark: {}'.format(best_mark))


if __name__ == '__main__':
    main()