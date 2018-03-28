#!/usr/bin/env python3

import sys

board_file = sys.argv[1]
dict_file = sys.argv[2]

with open(dict_file, 'r') as f:
    valid_words = [line.strip() for line in f]


def row_words(index, board):
    words = []
    rel_pos = index % 4
    end_bound = 4 - rel_pos
    start_bound = rel_pos + 1
    for i in range(1, end_bound):
        print(board[index:index + i + 1])
        if board[index:index + i + 1] in valid_words and len(set(board[index:index + i + 1])) == len(board[index:index + i + 1]):
            words.append(board[index:index + i + 1])
    for i in range(1, start_bound):
        print(board[index:index - i - 1:-1])
        if board[index:index - i - 1:-1] in valid_words and len(set(board[index:index - i - 1:-1])) == len(board[index:index - i - 1:-1]):
            words.append(board[index:index - i - 1:-1])
    return words


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
