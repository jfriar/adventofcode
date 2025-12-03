#!/usr/bin/env python3

input_file = 'day01_input.txt'
#input_file = 'day01_sample.txt'

pos = 50
count_zeros = 0
debug = False

with open(input_file) as f:
    for line in f.readlines():
        direction = line[0].upper()
        rotation = int(line[1:]) % 100
        if direction == 'L':
            pos -= rotation
        else:
            pos += rotation
        if pos < 0:
            pos += 100
        elif pos >= 100:
            pos -= 100
        if pos == 0:
            count_zeros += 1
            # print(line, direction, pos)
        if debug:
            print(line, direction, pos)

print('password:', count_zeros)
