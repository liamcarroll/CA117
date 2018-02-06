#!/usr/bin/env python3

import sys


def anagram(word, candidate):
    if len(word) != len(candidate):
        return False
    for c in candidate:
        if c not in word:
            return False
    return True


def main():
    for line in sys.stdin:
        words = line.strip().split()
        print(anagram(words[0], words[1]))

if __name__ == '__main__':
    main()