#!/usr/bin/env python3

import sys
import time


def get_all_substrings(input_string):
    length = len(input_string)
    return [input_string[i:j + 1] for i in range(length) for j in range(i, length)]


def main():
    s1 = sys.stdin.readline().strip()
    s2 = sys.stdin.readline().strip()
    #Find all common substrings
    common_substrings = set([s1[i:j + 1] for i in range(len(s1)) for j in range(i, len(s1)) if s1[i:j + 1] in s2])
    #lcsub = max(common_substrings, key=len)
    #index_lcsub = s2.find(lcsub)
    #print('{} {} {}'.format(lcsub, len(lcsub), index_lcsub))


if __name__ == '__main__':
    main()
