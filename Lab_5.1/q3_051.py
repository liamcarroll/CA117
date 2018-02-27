#!/usr/bin/env python3

import sys


def sorter(t):
    return t[1]


def main():
    for line in sys.stdin:
        s = line.strip()
        runs = {}
        for i, c in enumerate(s):
            if c.isupper() and (not s[i - 1].isupper() or i == 0):
                start = i
                runs['start_{}'.format(start)] = 1
            elif c.isupper():
                runs['start_{}'.format(start)] += 1
            else:
                continue
        longest_run = max(runs.items(), key=sorter)
        print(s[int(longest_run[0][-1]):int(longest_run[0][-1]) + longest_run[1]])

if __name__ == '__main__':
    main()
