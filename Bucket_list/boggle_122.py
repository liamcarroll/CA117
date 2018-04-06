#!/usr/bin/env python3

import sys

board_file = sys.argv[1]
dict_file = sys.argv[2]

with open(dict_file, 'r') as f:
    valid_words = [line.strip() for line in f]

class BoggleBoard(object):

    def __init__(self, board):
        self.board = board

    def row_words(self, e):
        

def main():
    with open(board_file, 'r') as f:
        boards = [line.strip() for line in f]

    boards_words = {}

    for board in boards:
        board_count = 1
        words = []
        for i in range(len(board)):
            words + row_words(i, board)
        boards_words[board_count] = words

    print(boards_words)


if __name__ == '__main__':
    main()
