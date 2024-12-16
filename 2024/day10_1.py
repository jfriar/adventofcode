#!/usr/bin/env python3

input_file = 'day10_input.txt'
# input_file = 'day10_sample.txt'


check_positions = [(1, 0),
                   (-1, 0),
                   (0, 1),
                   (0, -1)]


def get_next_moves(x, y):
    next_moves = []
    # topographic_map
    len_x = len(topographic_map[0])
    len_y = len(topographic_map)
    height = topographic_map[y][x]
    for dx, dy in check_positions:
        next_x = x + dx
        next_y = y + dy
        if next_x < 0 or next_x >= len_x or next_y < 0 or next_y >= len_y:
            # out of bounds
            continue
        next_height = topographic_map[next_y][next_x]
        if next_height - height != 1:
            # not a valid move
            continue
        # print(len_x, len_y, ':', dx, dy, ':', next_x, next_y, ':', height, next_height)
        next_moves.append((next_x, next_y))

    return next_moves


def find_trails(trailhead):
    trails = set()
    # check positions
    potential_trails = set([trailhead])
    # print('potential_trails', potential_trails)
    while potential_trails:
        trail = potential_trails.pop()
        _x = trail[-2]
        _y = trail[-1]
        if topographic_map[_y][_x] == 9:
            trails.add(trail)
            continue
        next_moves = get_next_moves(_x, _y)
        for next_move in next_moves:
            # print('next_move:', next_move)
            # print('  ', (*trail, *next_move))
            potential_trails.add((*trail, *next_move))
        # print()
    return trails


def score_trailhead(trails):
    height_9s = set()
    for trail in trails:
        height_9s.add((trail[-2], trail[-1]))

    return len(height_9s)


with open(input_file) as f:
    topographic_map = [[int(l) for l in line.rstrip()] for line in f.readlines()]

sum_scores = 0
for y, line in enumerate(topographic_map):
    for x, height in enumerate(line):
        if height == 0:
            # found a trailhead
            score = score_trailhead(find_trails((x, y)))
            print((x, y), 'score:', score)
            sum_scores += score

print('\nsum of scores:', sum_scores)
print('done')
            
