#!/usr/bin/env python3

import sys


def unique_words(l):
    unique_words = []
    for word in l:
        if word not in unique_words:
            unique_words.append(word)
    return len(unique_words)

def main():
    text = sys.stdin.read().strip().casefold()
    for c in text:
        if not c.isalnum() and not c.isspace():
            text = text.replace(c, '')
    words = text.split()
    print(unique_words(words))

if __name__ == '__main__':
    main()
