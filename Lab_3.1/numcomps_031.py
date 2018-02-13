#!/usr/bin/env python3

import sys


def test_replace(n):
    if not n % 3:
        return 'X'
    else:
        return n


def is_prime(n):
    if n < 2:
        return False
    else:
        for i in range(2, n):
            if not n % i:
                return False
        return True


def main():
    l = [i for i in range(1, int(sys.argv[1]) + 1)]
    print('Multiples of 3: {}'.format([n for n in l if not n % 3]))
    print('Multiples of 3 squared: {}'.format([n * n for n in l if not n % 3]))
    print('Multiples of 4 doubled: {}'.format([2 * n for n in l if not n % 4]))
    print('Multiples of 3 or 4: {}'.format(
        [n for n in l if not n % 3 or not n % 4]))
    print('Multiples of 3 and 4: {}'.format(
        [n for n in l if not n % 3 and not n % 4]))
    print('Multiples of 3 replaced: {}'.format([test_replace(n) for n in l]))
    print('Primes: {}'.format([n for n in l if is_prime(n)]))

if __name__ == '__main__':
    main()
