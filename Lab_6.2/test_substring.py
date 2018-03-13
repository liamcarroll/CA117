#!/usr/bin/env python3

import sys


def get_all_substrings(input_string):
    length = len(input_string)
    return [input_string[i:j+1], i for i in range(length) for j in range(i,length)]

def main():
    lines = []
    for line in sys.stdin:
        lines.append(line.strip())
    s1, s2 = lines
    print(s1)
    print(s2)