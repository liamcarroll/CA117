#!/usr/bin/env python3

import sys

words_dict = {}


def main():
    words = [w.strip() for w in sys.stdin if 5 <= len(w.strip())]
    for word in words:
        words_dict[word.casefold()] = True
    print([w for w in words if w[::-1].casefold() in words_dict])


if __name__ == '__main__':
    main()
