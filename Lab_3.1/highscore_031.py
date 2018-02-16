#!/usr/bin/env python3

import sys


def score(a, b, c):
    return a * a + b * b + c * c + 7 * min(a, b, c)


def main():
    for line in sys.stdin:
        nums = line.strip().split()
        [a, b, c, d] = [int(nums[0]), int(nums[1]), int(nums[2]), int(nums[3])]
    

if __name__ == '__main__':
    main()
