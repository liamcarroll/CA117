#!/usr/bin/env python3

import sys


def highest_student(file):
    highest = 0
    with open(file, 'r') as f:
        for line in f:
            if highest < int(line[:2]):
                highest = int(line[:2])
                highest_line = line.strip()
        return highest_line


def main():
    try:
        filename = sys.argv[1]
        best_student_line = highest_student(filename)
        best_mark = best_student_line[:2]
        best_student = best_student_line[3:]
        print('Best student: {}'.format(best_student))
        print('Best mark: {}'.format(best_mark))
    except FileNotFoundError:
        print('The file {} could not be opened.'.format(filename))

if __name__ == '__main__':
    main()
