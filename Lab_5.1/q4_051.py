#!/usr/bin/env python3

import sys


def mean(l):
    return sum(l) / len(l)


def median(l):
    sorted_nums = sorted(l)
    if len(sorted_nums) % 2:
        pos_median = (len(sorted_nums) + 1) // 2
        return sorted_nums[pos_median - 1]
    else:
        pos1, pos2 = (len(sorted_nums) + 1) // 2, ((len(sorted_nums) + 1) // 2) + 1
        return (sorted_nums[pos1 - 1] + sorted_nums[pos2 - 1]) / 2


def mode(l):
    return max(l, key=l.count)


def main():
    nums = []
    for line in sys.stdin:
        n = int(line.strip())
        nums.append(n)

    print('Mean: {:.1f}'.format(mean(nums)))
    print('Mode: {:.1f}'.format(mode(nums)))
    print('Median: {:.1f}'.format(median(nums)))

if __name__ == '__main__':
    main()
