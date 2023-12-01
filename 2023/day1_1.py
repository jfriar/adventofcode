#!/usr/bin/env python3

input_file = 'day1_input.txt'

with open(input_file) as f:
    coords = []
    for line in f.readlines():
        line_ints = [x for x in line if x.isdigit()]
        coords.append(int(line_ints[0] + line_ints[-1]))
    print(sum(coords))
