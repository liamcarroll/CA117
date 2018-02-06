#!/usr/bin/env python3

import sys


def is_palindrome(s):
    if s == s[::-1]:
        return True
    else:
        return False


def main():
    for line in sys.stdin:
        line = line.strip().casefold()
        for c in line:
            if not c.isalnum():
                line = line.replace(c, '')
        print(is_palindrome(line))

if __name__ == '__main__':
    main()
