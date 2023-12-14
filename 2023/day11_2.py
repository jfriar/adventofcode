#!/usr/bin/env python3
import re

input_file = 'day11_input.txt'
#input_file = 'day11_test.txt'


def empty_space(rows):
    return [i for i, row in enumerate(rows) if row.find('#') == -1]


def get_distance(a, b, x_empty_space, y_empty_space):
    # a = (x_1, y_1), b = (x_2, y_2)
    multiplier = 1000000
    x1, x2 = (a[0], b[0]) if b[0] > a[0] else (b[0], a[0])
    y1, y2 = (a[1], b[1]) if b[1] > a[1] else (b[1], a[1])

    x_offsets = [i for i in range(x1+1, x2) if i in x_empty_space]
    _x_offset = len(x_offsets) * multiplier
    x_offset = _x_offset - len(x_offsets) if _x_offset > 0 else 0

    y_offsets = [i for i in range(y1+1, y2) if i in y_empty_space]
    _y_offset = len(y_offsets) * multiplier
    y_offset = _y_offset - len(y_offsets) if _y_offset > 0 else 0
    return (x2-x1 + x_offset) + (y2-y1 + y_offset)


with open(input_file) as f:
    data = [x.strip() for x in f.readlines()]

y_empty_space = empty_space(data)

_data = [list(row) for row in data]
_transpose_x_to_y = [''.join(r) for r in list(zip(*_data))]

x_empty_space = empty_space(_transpose_x_to_y)

galaxies = []
for y, row in enumerate(data):
    for m in re.finditer('#', row):
        galaxies.append((m.start(), y))
    # print(row)

print()
print('galaxies:', galaxies)
print('x_empty_space:', x_empty_space)
print('y_empty_space:', y_empty_space)
print()

distances = []
while True:
    if not galaxies:
        break
    cur_galaxy = galaxies.pop()
    for galaxy in galaxies:
        distance = get_distance(cur_galaxy, galaxy, x_empty_space, y_empty_space)
        distances.append(distance)
        # print(cur_galaxy, galaxy, distance)

print('distance:', sum(distances))
