#!/usr/bin/env python3

input_file = 'day11_input.txt'
# input_file = 'day11_sample.txt'


def change_stone(stone, stone_val):
    new_stone = {}
    if stone == 0:
        new_stone[1] = stone_val
    elif len(str(stone)) % 2 == 0:
        # even len
        stone = str(stone)
        mid = int(len(stone) / 2)
        left_stone = int(stone[:mid])
        right_stone = int(stone[mid:])
        new_stone[left_stone] = stone_val
        # in case right_stone == left_stone
        new_stone[right_stone] = new_stone.get(right_stone, 0) + stone_val
    else:
        new_stone[stone * 2024] = stone_val
    return new_stone


def blink(stones, debug=False):
    if debug:
        print('old:', stones)
    new_stones = {}
    for stone, stone_val in stones.items():
        change_stones = change_stone(stone, stone_val)
        for new_stone, new_stone_val in change_stones.items():
            new_stones[new_stone] = new_stones.get(new_stone, 0) + new_stone_val

    # new_line = [s for stone in stone_line for s in change_stone(stone)]
    if debug:
        print('new:', new_stones, '\n')
    return new_stones


with open(input_file) as f:
    stone_lines = [[int(l) for l in line.rstrip().split(' ')] for line in f.readlines()]

num_blinks = 75
stone_line = stone_lines[0]
# stone_line = stone_lines[1]
print(stone_line)

stones = {}
for stone in stone_line:
    stones[stone] = stones.get(stone, 0) + 1

for i in range(num_blinks):
    stones = blink(stones)
print('i =', i, 'num_stones =', sum([s for s in stones.values()]))
# print(stones)
