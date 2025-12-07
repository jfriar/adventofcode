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

def check_neighbors(paper_map):
    paper_map_new = paper_map.copy()
    can_move = []
    y_len = len(paper_map)
    for y, row in enumerate(paper_map):
        # print(y, row)
        new_row = paper_map_new[y]
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
                paper_map_new[y] = paper_map[y][:x] + '.' + paper_map[y][x+1:] 
                new_row = new_row[:x] + '.' + new_row[x+1:]
            if debug:
                can_move_debug = len(neighbors) < 4
                print('>> (' + str(x) + ',' + str(y) + ') neighbors', neighbors)
                print('>> (' + str(x) + ',' + str(y) + ') can_move', can_move_debug)

        paper_map_new[y] = new_row

    print('----------------')
    print(len(can_move))
    print('----------------')
    if debug:
        for y, row in enumerate(paper_map):
            row_update = ''
            _new_row = ''
            for x, item in enumerate(row):
                if (x, y) in can_move:
                    row_update += 'x'
                    _new_row += '.'
                else:
                    row_update += paper_map[y][x]
            print(row_update)

    return paper_map_new, len(can_move)

paper_map_new = paper_map.copy()
moved = 1
total_moved = 0
while moved != 0:
    paper_map_new, moved = check_neighbors(paper_map_new)
    if moved == 0:
        break

    total_moved += moved
    if debug:
        print('|--------------|')
        print('--- moved', moved, '---')
        for row in paper_map_new:
            print(row)
        print('|--------------|')

print("\n", 'total moved:', total_moved)
