#!/usr/bin/env python3

import sys

from priority_queue_112 import PQ


def main():
    M = int(sys.argv[1])
    pq = PQ()

    for n in sys.stdin:
        pq.insert(int(n.strip()))
        if pq.size() > M:
            pq.delMax()

    while not pq.is_empty():
        print(pq.delMax())

if __name__ == '__main__':
    main()
