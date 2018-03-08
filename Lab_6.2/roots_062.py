#!/usr/bin/env python3

import sys
from math import sqrt

def quadratic_roots(a, b, c):
    return (-b + sqrt(b ** 2 - 4 * a * c)) / (2 * a), (-b - sqrt(b ** 2 - 4 * a * c)) / (2 * a)

def main():
    for line in sys.stdin:
        a, b, c = line.strip().split()

        if quadratic_roots(int(a),int(b),int(c)):
            print('r1 = {}, r2 = {}'.format())


    

if __name__ == '__main__':
    main()
