#!/usr/bin/env python3

input_file = 'day04_input.txt'
#input_file = 'day04_sample.txt'

debug = False

paper_map = []
with open(input_file) as f:
    for line in f.readlines():
        paper_map.append(line.strip())

if debug:
    from pprint import pprint
    pprint(paper_map)
can_move = []
y_len = len(paper_map)
for y, row in enumerate(paper_map):
    print(y, row)
    for x, item in enumerate(row):
        x_len = len(row)
        # print('> ', x, y, item)
        if paper_map[y][x] == '.':
            # print('>> skipping')
            continue

        #
        #             y
        #      _____
        #     |. @ .|-1
        #     |@ * @| y
        #     |@ . .| 1
        #      -----
        #  x  -1 x 1
        #
        neighbors = []
        for x_offset in (-1,0,1):
            for y_offset in (-1,0,1):
                if x_offset == 0 and y_offset == 0:
                    continue
                x_new = x + x_offset
                y_new = y + y_offset
                if 0 <= x_new < x_len and 0 <= y_new < y_len:
                    if paper_map[y_new][x_new] == '@':
                        neighbors.append((x_new, y_new))
        if len(neighbors) < 4:
            can_move.append((x,y))
        if debug:
            can_move_debug = len(neighbors) < 4
            print('>> (' + str(x) + ',' + str(y) + ') neighbors', neighbors)
            print('>> (' + str(x) + ',' + str(y) + ') can_move', can_move_debug)

print('----------------')
print(len(can_move))
print('----------------')
if debug:
    for y, row in enumerate(paper_map):
        row_update = ''
        for x, item in enumerate(row):
            if (x, y) in can_move:
                row_update += 'x'
            else:
                row_update += paper_map[y][x]
        print(row_update)

