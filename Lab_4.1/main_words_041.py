#!/usr/bin/env python3

import sys
import string

def main():
    words = []
    count = {}
    longest_w = 0
    for line in sys.stdin:
        line = line.strip().casefold().split()
        for w in line:
            word = w.strip(string.punctuation)
            if 3 < len(word) and word not in count:
                count[word] = 1
                words.append(word)
            elif 3 < len(word):
                count[word] += 1
    words = sorted(words)
    longest_key = len(str(max(count.values())))
    for w in words:
        if 3 <= count[w]:
            print('{:>{:d}s} : {:>{:d}d}'.format(w, longest_w, count[w], longest_key))

if __name__ == '__main__':
    main()