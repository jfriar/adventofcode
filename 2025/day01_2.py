#!/usr/bin/env python3

input_file = 'day01_input.txt'
#input_file = 'day01_sample.txt'

pos = 50
count_zeros = 0
debug = True

with open(input_file) as f:
    for line in f.readlines():
        direction = line[0].upper()
        rotation = int(line[1:]) % 100
        count_zeros += int(line[1:]) // 100
        prev_pos = pos
        if direction == 'L':
            pos -= rotation
        else:
            pos += rotation
        if pos == 0:
            count_zeros += 1
        if pos < 0:
            pos += 100
            if prev_pos != 0:
                count_zeros += 1
        elif pos >= 100:
            pos -= 100
            if prev_pos != 0:
                count_zeros += 1
        #if pos == 0:
        #    count_zeros += 1
            # print(line, direction, pos)
        if debug:
            print(line, direction, pos, count_zeros)

print('password:', count_zeros)
