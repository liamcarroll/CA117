#!/usr/bin/env python3

import sys


def score(a, b, c):
    return (a * a) + (b * b) + (c * c) + 7 * min(a, b, c)

# Put all the tokens on largest number
def all_on_largest(a, b, c, d):
    if max(a, b, c) == a:
        a += d
        return score(a, b, c)
    elif max(a, b, c) == b:
        b += d
        return score(a, b, c)
    else:
        c += d
        return score(a, b, c)

# All on zero if there is a zero present
def all_on_zero(a, b, c, d):
    if not a:
        a = d
        return score(a, b, c)
    elif not b:
        b = d
        return score(a, b, c)
    elif not c:
        c = d
        return score(a, b, c)
    return 0


#Add one to a,b,c for each token and see which produces largest value and continue
def one_by_one_approach(a, b, c, d):
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
        print(max(all_on_largest(int(nums[0]), int(nums[1]), int(nums[2]), int(nums[3])), all_on_zero(int(nums[0]), int(
            nums[1]), int(nums[2]), int(nums[3])), one_by_one_approach(int(nums[0]), int(nums[1]), int(nums[2]), int(nums[3]))))

if __name__ == '__main__':
    main()
