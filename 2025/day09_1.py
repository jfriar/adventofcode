#!/usr/bin/env python3

input_file = 'day09_input.txt'
#input_file = 'day09_sample.txt'

red_tiles = []
with open(input_file) as f:
    for line in f.readlines():
        x, y = map(int,line.strip().split(','))
        red_tiles.append((x,y))

print(red_tiles)

pos = red_tiles.pop(0)
max_area = 0

while pos:
    x, y = pos
    for _x, _y in red_tiles:
        area = abs(x - _x + 1) * abs(y - _y + 1)
        if area > max_area:
            max_area = area
    if red_tiles:
        pos = red_tiles.pop(0)
    else:
        pos = False

print(max_area)
