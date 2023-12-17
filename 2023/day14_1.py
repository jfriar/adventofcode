#!/usr/bin/env python3
import collections

input_file = 'day14_input.txt'
# input_file = 'day14_test.txt'


DIRECTIONS = {'n': (0, -1),
              's': (0, 1),
              'e': (1, 0),
              'w': (-1, 0)}


def print_board(board):
    for row in board:
        if isinstance(row, list):
            print(''.join(row))
        else:
            print(row)


def tilt_board(board, direction):
    d = DIRECTIONS[direction]
    while True:
        moves = 0
        for y in range(0, len(board)):
            for x in range(0, len(board[y])):
                char = board[y][x]
                next_y = y + d[1]
                next_x = x + d[0]
                if next_y < 0 or next_y > len(board)-1:
                    continue
                if next_x < 0 or next_x > len(board[y])-1:
                    continue
                if char in ['.', '#']:
                    continue
                if char == 'O' and board[y+d[1]][x+d[0]] == '.':
                    board[y+d[1]][x+d[0]] = board[y][x]
                    board[y][x] = '.'
                    moves += 1
        print(moves)
        if moves == 0:
            break
    return board


def calculate_board_load(board, direction):
    board_len = len(board)
    load_list = []
    for y in range(0, board_len):
        c = collections.Counter(board[y])
        _load = c['O'] * (board_len - y)
        load_list.append(_load)
    return sum(load_list)


with open(input_file) as f:
    data = [x.strip() for x in f.readlines()]

print_board(data)
print()
new_board = tilt_board([list(d) for d in data], 'n')
print()
print_board(new_board)
print(calculate_board_load(new_board, 'n'))
# correct: 107142
