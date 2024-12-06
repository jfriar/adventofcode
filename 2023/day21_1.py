#!/usr/bin/env python3

input_file = 'day21_input.txt'
# input_file = 'day21_test.txt'

with open(input_file) as f:
    data = [x.strip() for x in f.readlines()]


start = (None, None)
for y, row in enumerate(data):
    x = row.find('S')
    if x != -1:
        start = (x, y)
        break

print('start:', start)
count = 0
cursors = set([start])
x_max = len(data[0])
y_max = len(data)
while count < 64:
    count += 1
    new_cursors = set()
    for cursor in cursors:
        offsets = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for offset_x, offset_y in offsets:
            new_x = cursor[0] + offset_x
            new_y = cursor[1] + offset_y
            if new_x < 0 or new_x >= x_max or new_y < 0 or new_y >= y_max:
                continue
            if data[new_y][new_x] in ['.', 'S']:
                # print('can move', (offset_x, offset_y), 'to:', (new_x, new_y))
                new_cursors.add((new_x, new_y))
    cursors = new_cursors

print(len(set(cursors)))
# print()
# for y, row in enumerate(data):
#     _row = list(row)
#     for x, char in enumerate(_row):
#         for _x, _y in cursors:
#             if x == _x and y == _y:
#                 _row[x] = 'O'
#     print(''.join(_row))
