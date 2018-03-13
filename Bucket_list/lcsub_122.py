#!/usr/bin/env python3

import sys


def get_all_substrings(input_string):
    length = len(input_string)
    return [input_string[i:j + 1] for i in range(length) for j in range(i, length)]


def main():
    lines = []
    for line in sys.stdin:
        lines.append(line.strip())
    s1, s2 = lines
    substrings_s1 = set(get_all_substrings(s1))
    substrings_s2 = set(get_all_substrings(s2))
    common_substrings = substrings_s1.intersection(substrings_s2)
    lcsub = max(common_substrings, key=len)
    index_lcsub = s2.find(lcsub)
    print('{} {} {}'.format(lcsub, len(lcsub), index_lcsub))


if __name__ == '__main__':
    main()
