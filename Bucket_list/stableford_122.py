#!/usr/bin/env python3

import sys

lines = []
par = {}
index = {}

score_to_par = {-7: 9,
                -6: 8,
                -5: 7,
                -4: 6,
                -3: 5,
                -2: 4,
                -1: 3,
                0: 2,
                1: 1}

def score(line):
    shots = {}
    handicap = int(line.split()[-19])
    i = 0
    while i < handicap:
        if 18 < i:
            i = i -18
            shots[index[i]] += 1
            print(shots)
        else:
            shots[index[i]] += 1
            print(shots)
        i += 1
    return shots


def main():
    for line in sys.stdin:
        lines.append(line.strip())
    for i in range(18):
        par[i] = int(lines[0].split()[i])
        index[int(lines[1].split()[i])] = i
    print(index)
    print(score(lines[2]))
    

if __name__ == '__main__':
    main()
