#!/usr/bin/env python3

import sys

score_to_par = {-7: 9,
                -6: 8,
                -5: 7,
                -4: 6,
                -3: 5,
                -2: 4,
                -1: 3,
                0: 2,
                1: 1}


def main():
    for line in sys.stdin:
