#!/usr/bin/env python3

input_file = 'day04_input.txt'
# input_file = 'day04_sample.txt'

print_board = False
print_word = False

def find_word(word, x, y, delta_x, delta_y):
    len_word = len(word)
    len_rows = len(board)
    len_cols = len(board[0])

    found = False

    next_x = x
    next_y = y
    for i in range(0, len_word):
        if (next_x < 0 or next_x >= len_cols) or \
                (next_y < 0 or next_y >= len_rows):
            # next_x or next_y is out of bounds
            found = False
            break

        if word[i] == board[next_y][next_x]:
            # next_x, next_y is a match
            next_x += delta_x
            next_y += delta_y
            found = True
        else:
            # next_x, next_y is incorrect
            found = False
            break

    return found


with open(input_file) as f:
    board = []
    board = [line.rstrip() for line in f.readlines()]


if print_board:
    for row in board:
        print(row)
    print()

words = ['MAS', 'SAM']
word_count = 0

# for each coord on the board, check if there is a word match
for y, row in enumerate(board):
    for x, column in enumerate(row):
        potential = False
        # check down-right first
        for word in words:
            if find_word(word, x, y, 1, 1):
                # down-right found
                potential = True
                break
        if potential:
            for word in words:
                if find_word(word, x+2, y, -1, 1):
                    # down-left offset by 2 found
                    word_count += 1
                    if print_word:
                        print('found word[%s] at x[%s], y[%s] : delta_x[%s], delta_y[%s]' % (word, x, y, 1, 1))
                        print('found word[%s] at x[%s], y[%s] : delta_x[%s], delta_y[%s]' % (word, x+2, y, -1, 1))
                    break

print('\nfound word[%s] %s times' % (word, word_count))
