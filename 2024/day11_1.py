#!/usr/bin/env python3

input_file = 'day11_input.txt'
# input_file = 'day11_sample.txt'


def change_stone(stone):
    if stone == '0':
        new_stone = ['1']
    elif len(stone) % 2 == 0:
        mid = int(len(stone) / 2)
        left_stone = int(stone[:mid])
        right_stone = int(stone[mid:])
        new_stone = [str(left_stone), str(right_stone)]
    else:
        new_stone = [str(int(stone) * 2024)]
    return new_stone


def blink(stone_line):
    # print('old:', stone_line)
    new_line = []
    for stone in stone_line:
        new_line += change_stone(stone)
    # print('new:', new_line, '\n')
    return new_line


with open(input_file) as f:
    stone_lines = [line.rstrip().split(' ') for line in f.readlines()]

# print(stone_lines[0])

new_line = blink(stone_lines[0])

num_blinks = 25
# stone_line = stone_lines[1]
stone_line = stone_lines[0]
for i in range(num_blinks):
    stone_line = blink(stone_line)
    print('i =', i, 'num_stones =', len(stone_line))

