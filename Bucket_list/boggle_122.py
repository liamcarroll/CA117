#!/usr/bin/env python3

import sys

board_file = sys.argv[1]
dict_file = sys.argv[2]

def 


def main():
    with open(board_file, 'r') as f:
        boards = [line.strip() for line in f]

    with open(dict_file, 'r') as f:
        valid_words = [line.strip() for line in f]

    for board in boards:
        for i, e in enumerate(board):
            

if __name__ == '__main__':
    main()
