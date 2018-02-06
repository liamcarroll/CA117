#!/usr/bin/env python3

import sys


def main():
    tokens = []
    for line in sys.stdin:
        tokens += line.strip().split()
    print(len(tokens))

if __name__ == '__main__':
    main()
