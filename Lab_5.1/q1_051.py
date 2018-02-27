#!/usr/bin/env python3

import sys


def main():
    s = sys.argv[1]
    chars = [c for c in s]
    for i in range(0, len(chars), 2):
        try:
            tmp = chars[i]
            chars[i] = chars[i + 1]
            chars[i + 1] = tmp
        except IndexError:
            pass
    print(''.join(chars))


if __name__ == '__main__':
    main()
