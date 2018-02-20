#!/usr/bin/env python3

import sys
import string

def main():
    words = []
    count = {}
    for line in sys.stdin:
        line = line.strip().casefold().split()
        for w in line:
            word = w.strip(string.punctuation)
            if word not in count:
                count[word] = 1
                words.append(word)
            else:
                count[word] += 1
    words = sorted(words)
    for w in words:
        print('{} : {}'.format(w, count[w]))

if __name__ == '__main__':
    main()