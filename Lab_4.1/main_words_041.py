#!/usr/bin/env python3

import sys
import string

words = []
count = {}


def main():
    for line in sys.stdin:
        line = line.strip().casefold().split()
        for w in line:
            word = w.strip(string.punctuation)

            if 3 < len(word) and word not in count:
                count[word] = 1
                words.append(word)
            elif 3 < len(word):
                count[word] += 1

    words_3_freq_plus = sorted([key for key in count if 3 <= count[key]])

    longest_w = len(max(words_3_freq_plus, key=len))
    longest_key = len(str(max(count.values())))

    for w in words_3_freq_plus:
        print('{:>{:d}s} : {:>{:d}d}'.format(
            w, longest_w, count[w], longest_key))

if __name__ == '__main__':
    main()
