#!/usr/bin/env python3

import sys


def score(a, b, c):
    return a * a + b * b + c * c + 7 * min(a, b, c)


def highscore(a, b, c, d):
    for i in range(1, d + 1):
        a_incremented = score(a + 1, b, c)
        b_incremented = score(a, b + 1, c)
        c_incremented = score(a, b, c + 1)

        if max(a_incremented, b_incremented, c_incremented) == a_incremented:
            a += 1
        elif max(a_incremented, b_incremented, c_incremented) == b_incremented:
            b += 1
        else:
            c += 1
    return score(a, b, c)


def main():
    for line in sys.stdin:
        nums = line.strip().split()
        print(highscore(int(nums[0]), int(
            nums[1]), int(nums[2]), int(nums[3])))

if __name__ == '__main__':
    main()
