#!/usr/bin/env python3

input_file = 'day06_input.txt'
#input_file = 'day06_sample.txt'


ROTATE_MAP = '^>v<'
ROTATE_MAP_LEN = len(ROTATE_MAP)
MOVE_MAP = {'^': (0, -1),
            'v': (0, 1),
            '>': (1, 0),
            '<': (-1, 0)}


def guard_move(direction, position, obstacles, x_len, y_len):
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
        resp, next_direction, (next_x, next_y) = guard_move(next_direction, position, obstacles, x_len, y_len)
    else:
        # continue in same direction
        next_direction = direction

    return (resp, next_direction, (next_x, next_y))


def find_guard_vectors(guard_direction, guard_position, guard_map_obstacles, guard_map_x_len, guard_map_y_len):
    move_resp = 0
    current_direction = guard_direction
    current_position = guard_position
    vectors = set()
    while move_resp == 0:
        prev_vectors = vectors.copy()
        vectors.add((current_direction, current_position))
        move_resp, current_direction, current_position = guard_move(current_direction,
                                                                    current_position,
                                                                    guard_map_obstacles,
                                                                    guard_map_x_len,
                                                                    guard_map_y_len)
        if vectors == prev_vectors:
            print('>>>loop found<<<')
            move_resp = 2

    return move_resp, vectors


with open(input_file) as f:
    guard_map = [line.rstrip() for line in f.readlines()]

guard_map_x_len = len(guard_map[0])
guard_map_y_len = len(guard_map)

guard_map_obstacles = set()
guard_current_start_direction = None
guard_current_start_position = None

for y, line in enumerate(guard_map):
    for x, val in enumerate(line):
        if val == '#':
            guard_map_obstacles.add((x, y))
        elif val == '.':
            continue
        elif guard_current_start_position is None and guard_current_start_direction is None:
            guard_current_start_direction = val
            guard_current_start_position = (x, y)
        else:
            raise ValueError('What the crap is this')

print('current position:', guard_current_start_position)

guard_map_obstacles_orig = guard_map_obstacles.copy()

move_resp, guard_vectors = find_guard_vectors(guard_current_start_direction,
                                              guard_current_start_position,
                                              guard_map_obstacles,
                                              guard_map_x_len,
                                              guard_map_y_len)
guard_vectors_orig = guard_vectors.copy()
guard_positions_orig = set([pos for d, pos in guard_vectors_orig])


print('number of vectors:', len(set([pos for d, pos in guard_vectors])))

choices = 0
for y in range(0, guard_map_y_len):
    for x in range(0, guard_map_x_len):
        if (x, y) in guard_map_obstacles_orig:
            continue
        valid_pos = False
        for x_delta in range(-1,2):
            for y_delta in range(-1,2):
                if (x+x_delta,y+y_delta) in guard_positions_orig:
                    valid_pos = True
                    break
            if valid_pos:
                break
        if valid_pos is False:
            # print('false')
            continue
        map_obstacles = guard_map_obstacles_orig.copy()
        map_obstacles.add((x, y))
        move_resp, guard_vectors = find_guard_vectors(guard_current_start_direction,
                                                      guard_current_start_position,
                                                      map_obstacles,
                                                      guard_map_x_len,
                                                      guard_map_y_len)
        if move_resp == 2:
            choices += 1
            print((x,y), 'number of vectors:', len(set([pos for d, pos in guard_vectors])))

print('\nnumber of choices:', choices)
