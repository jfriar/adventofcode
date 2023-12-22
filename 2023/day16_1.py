#!/usr/bin/env python3

input_file = 'day16_input.txt'
# input_file = 'day16_test.txt'

with open(input_file) as f:
    data = [x.strip() for x in f.readlines()]

direction_map = {'e': (1, 0),
                 'w': (-1, 0),
                 'n': (0, -1),
                 's': (0, 1)}


def next_direction(char, current_direction):
    if char == '-' and current_direction in ['n', 's']:
        return ['e', 'w']
    elif char == '|' and current_direction in ['e', 'w']:
        return ['n', 's']
    elif char == '/':
        if current_direction == 'e':
            return 'n'
        elif current_direction == 'n':
            return 'e'
        elif current_direction == 'w':
            return 's'
        elif current_direction == 's':
            return 'w'
    elif char == '\\':
        if current_direction == 'e':
            return 's'
        elif current_direction == 'n':
            return 'w'
        elif current_direction == 'w':
            return 'n'
        elif current_direction == 's':
            return 'e'

    return current_direction


def find_next_coords(coords):
    # next_coords = [(x, y, direction), ...]
    next_coords = []
    new_direction = next_direction(data[coords[1]][coords[0]], coords[2])
    if isinstance(new_direction, list):
        for d in new_direction:
            new_coords = (coords[0] + direction_map[d][0], coords[1] + direction_map[d][1])
            next_coords.append(new_coords + (d,))
    else:
        new_coords = (coords[0] + direction_map[new_direction][0], coords[1] + direction_map[new_direction][1])
        next_coords.append(new_coords + (new_direction,))
    return next_coords


map_len = len(data)
row_len = len(data[0])

# start at 0,0
path_coords = [(0, 0, 'e')]
energized = set()
energized.add(path_coords[0])
count = 0
while True:
    new_path_coords = []
    for path_coord in path_coords:
        #print('finding path for', path_coord)
        next_coords = find_next_coords(path_coord)
        for next_coord in next_coords:
            if next_coord[0] < 0 or next_coord[0] > row_len-1:
                #print('no more for', next_coord)
                continue
            elif next_coord[1] < 0 or next_coord[1] > map_len-1:
                #print('no more for', next_coord)
                continue
            else:
                #print('next path', next_coord)
                if next_coord in energized:
                    continue
                energized.add(next_coord)
                new_path_coords.append(next_coord)

    if not new_path_coords:
        print('no more new path coords')
        break
    path_coords = new_path_coords

    # count += 1
    # if count > 32:
    #     print('early exit')
    #     print(new_path_coords)
    #     break

# print('energized', sorted(energized))

# data = [list(d) for d in data]
# for e in energized:
#     data[e[1]][e[0]] = '#'
# data = [''.join(d) for d in data]
# 
# for row in data:
#     print(row)

energized_coords = set()
for e in energized:
    energized_coords.add((e[0], e[1]))
print()
print('energized count:', len(energized_coords))
