#!/usr/bin/env python3
import re

input_file = 'day11_input.txt'
#input_file = 'day11_test.txt'


def expand_rows(rows):
    expanded = []
    for row in rows:
        if row.find('#') != -1:
            expanded.append(row)
        else:
            expanded.append(row)
            expanded.append(row)
    return expanded


def get_distance(a, b):
    # a = (x_1, y_1), b = (x_2, y_2)
    x1, x2 = (a[0], b[0]) if b[0] > a[0] else (b[0], a[0])
    y1, y2 = (a[1], b[1]) if b[1] > a[1] else (b[1], a[1])
    return (x2-x1) + (y2-y1)


with open(input_file) as f:
    data = [x.strip() for x in f.readlines()]

expanded_x = expand_rows(data)
_expanded_x = [list(row) for row in expanded_x]

_transpose_x_to_y = [''.join(r) for r in list(zip(*_expanded_x))]

expanded_y = expand_rows(_transpose_x_to_y)
_expanded_y = [list(row) for row in expanded_y]

expanded = [''.join(r) for r in list(zip(*_expanded_y))]

galaxies = []
for y, row in enumerate(expanded):
    for m in re.finditer('#', row):
        galaxies.append((m.start(), y))
    # print(row)

print()
print(galaxies)
print()

distances = []
while True:
    if not galaxies:
        break
    cur_galaxy = galaxies.pop()
    for galaxy in galaxies:
        distance = get_distance(cur_galaxy, galaxy)
        distances.append(distance)
        # print(cur_galaxy, galaxy, distance)

print('distance:', sum(distances))
