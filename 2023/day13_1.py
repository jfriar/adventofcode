#!/usr/bin/env python3

input_file = 'day13_input.txt'
# input_file = 'day13_test.txt'


def find_mirror_axis(pattern):
    midpoint = int(len(pattern) / 2)
    for y in range(0, len(pattern)):
        if y == 0:
            top = [pattern[0]]
            bottom = [pattern[1]]
        elif y < midpoint:
            top = pattern[:y+1]
            bottom = pattern[y+1:y+1+len(top)]
        else:
            bottom = pattern[y+1:]
            top = pattern[y+1-len(bottom):y+1]

        if not top or not bottom:
            continue

        bottom_rev = list(reversed(bottom))

        # print([y, y+1])
        # pprint(bottom_rev, width=2)
        # print()
        # pprint(top, width=2)
        # print('--------------')
        # pprint(bottom, width=2)
        # print()

        if top == bottom_rev:
            # print('found!')
            return y+1
    return 0


with open(input_file) as f:
    data = [x.strip() for x in f.readlines()]

patterns = []
_tmp = []
for row in data:
    if row != '':
        _tmp.append(row)
    else:
        patterns.append(_tmp)
        _tmp = []

if _tmp:
    patterns.append(_tmp)

from pprint import pprint

total = 0
for p in patterns:
    # x axis
    x_axis = find_mirror_axis(p)

    # y axis
    transposed = [''.join(z) for z in zip(*p)]
    y_axis = find_mirror_axis(transposed)

    # print('y_axis:', y_axis, 'x_axis:', x_axis)

    total += (x_axis*100) + y_axis

print('total:', total)
