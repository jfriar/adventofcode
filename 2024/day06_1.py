#!/usr/bin/env python3
import functools

input_file = 'day06_input.txt'
# input_file = 'day06_sample.txt'


ROTATE_MAP = '^>v<'
ROTATE_MAP_LEN = len(ROTATE_MAP)
MOVE_MAP = {'^': (0, -1),
            'v': (0, 1),
            '>': (1, 0),
            '<': (-1, 0)}


def guard_move(direction, position, x_len, y_len):
    resp = 0
    x = position[0]
    y = position[1]
    next_x = x + MOVE_MAP[direction][0]
    next_y = y + MOVE_MAP[direction][1]

    if next_x < 0 or next_x >= x_len or next_y < 0 or next_y >= y_len:
        # out of bounds
        resp = 1
        next_direction = direction
        next_x, next_y = position
    elif (next_x, next_y) in obstacles:
        # obstacle hit, change direction
        next_direction = ROTATE_MAP[(ROTATE_MAP.index(direction)+1) % ROTATE_MAP_LEN]
        resp, next_direction, (next_x, next_y) = guard_move(next_direction, position, x_len, y_len)
    else:
        # continue in same direction
        next_direction = direction

    return (resp, next_direction, (next_x, next_y))


with open(input_file) as f:
    guard_map = [line.rstrip() for line in f.readlines()]

guard_map_x_len = len(guard_map[0])
guard_map_y_len = len(guard_map)
obstacles = set()
guard_positions = set()
guard_current_direction = None
guard_current_position = None

for y, line in enumerate(guard_map):
    for x, val in enumerate(line):
        if val == '#':
            obstacles.add((x, y))
        elif val == '.':
            continue
        elif guard_current_position is None and guard_current_direction is None:
            guard_current_direction = val
            guard_current_position = (x, y)
        else:
            raise ValueError('What the crap is this')

# print(obstacles)
print('current position:', guard_current_position)

move_resp = 0
while move_resp != 1:
    guard_positions.add(guard_current_position)
    move_resp, guard_current_direction, guard_current_position = guard_move(guard_current_direction,
                                                                            guard_current_position,
                                                                            guard_map_x_len,
                                                                            guard_map_y_len)

print('number of positions:', len(guard_positions))

