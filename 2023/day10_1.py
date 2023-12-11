#!/usr/bin/env python3

input_file = 'day10_input.txt'
#input_file = 'day10_test.txt'
#input_file = 'day10_test2.txt'

PIPES = '|-LJ7FS'

# | => up, down
# - => left, right
# L => up, right
# J => up, left
# 7 => down, left
# F => down, right
#
# up    = (0, -1)
# down  = (0, 1)
# left  = (-1, 0)
# right = (1, 0)
PIPE_CONNECTIONS = {'|': {(0, -1): '|7FS',
                          (0, 1):  '|LJS',
                          (-1, 0): None,
                          (1, 0):  None},
                    '-': {(0, -1): None,
                          (0, 1):  None,
                          (-1, 0): '-LFS',
                          (1, 0):  '-J7S'},
                    'L': {(0, -1): '|7FS',
                          (0, 1):  None,
                          (-1, 0): None,
                          (1, 0):  '-J7S'},
                    'J': {(0, -1): '|7FS',
                          (0, 1):  None,
                          (-1, 0): '-LFS',
                          (1, 0):  None},
                    '7': {(0, -1): None,
                          (0, 1):  '|LJS',
                          (-1, 0): '-LFS',
                          (1, 0):  None},
                    'F': {(0, -1): None,
                          (0, 1):  '|LJS',
                          (-1, 0): None,
                          (1, 0):  '-J7S'},
                    'S': {(0, -1): '|7F',
                          (0, 1):  '|LJ',
                          (-1, 0): '-LF',
                          (1, 0):  '-J7'}}


def next_relative_pipes(char):
    next_pipes = []
    for _y in [-1, 0, 1]:
        for _x in [-1, 0, 1]:
            pc = PIPE_CONNECTIONS.get(char, {}).get((_x, _y))
            if pc is not None:
                next_pipes.append((pc, _x, _y))
    if char != 'S' and len(next_pipes) != 2:
        raise ValueError('PROBLEM, incorrect number of PIPES')
    return next_pipes


def next_pipes(x, y, data, seen):
    # returns a list of pipes [(next_pipe_char, next_x, next_y)]
    _next_relative_pipes = next_relative_pipes(data[y][x])
    pipes = []
    # print('S:', _next_relative_pipes)
    for pc, _x, _y in _next_relative_pipes:
        next_x = x + _x
        next_y = y + _y
        next_char = data[next_y][next_x]
        next_pipe = (next_char, next_x, next_y)
        if next_char in pc and next_pipe not in seen:
            # print('found next:', next_pipe)
            pipes.append(next_pipe)
    return pipes


with open(input_file) as f:
    data = [x.strip() for x in f.readlines()]


# find the starting point
for y, row in enumerate(data):
    if 'S' in row:
        start = [row.index('S'), y]

x, y = start
seen = set()
seen.add(('S', x, y,))

_next_pipes = next_pipes(x, y, data, seen)

# find two pipes adjacent to the start to create the two paths
if len(_next_pipes) == 2:
    print('starting! S: {0}, {1}'.format(x, y))
    path = {0: [_next_pipes[0]],
            1: [_next_pipes[1]]}
    seen.add(_next_pipes[0])
    seen.add(_next_pipes[1])

# find each path's adjacent pipes
counter = 1
while True:
    path0 = next_pipes(path[0][-1][1], path[0][-1][2], data, seen)
    path1 = next_pipes(path[1][-1][1], path[1][-1][2], data, seen)
    for p in path0:
        seen.add(p)
    for p in path1:
        seen.add(p)
    counter += 1
    if path0 == path1:
        # print('seen:', seen)
        print('final path:', path0, 'count:', counter)
        break
    else:
        # print('next path0: {0}, path1: {1}'.format(path0, path1))
        path[0].append(path0[0])
        path[1].append(path1[0])

