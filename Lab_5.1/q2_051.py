#!/usr/bin/env python3

import sys


def main():
    evil_chars = ['e', 'v', 'i', 'l']
    matched_chars = []
    for line in sys.stdin:
        word = line.strip().casefold()
        matched_chars = [c for c in word if c in evil_chars]
        if matched_chars == evil_chars:
            print(line.strip())

if __name__ == '__main__':
    main()
