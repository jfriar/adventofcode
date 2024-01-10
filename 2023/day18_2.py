#!/usr/bin/env python3
import re
import time

input_file = 'day18_input.txt'
#input_file = 'day18_test.txt'

with open(input_file) as f:
    data = [x.strip() for x in f.readlines()]


def get_y_edges(y, dig_edges):
    y_edges = {}
    for edge_name, dig_edge in dig_edges.items():
        a, b = dig_edge['value']
        if a[1] < y < b[1] or y == a[1] == b[1]:
            y_edges[edge_name] = dig_edges[edge_name]
    return y_edges


def ray_edge_count(x, y, dig_edges):
    # print('ray_edge_count')

    # check rays going in the +x direction
    # they must hit a "vertical" y edge, or an x edge that is connect to edges
    # that go in opposite directions (up and down)
    edge_count = 0
    for dig_edge in dig_edges.values():
        a, b = dig_edge['value']
        if a[1] < y < b[1]:
            if x < b[0]:
                # print(a, b)
                edge_count += 1
        elif y == a[1] == b[1]:
            # this is hitting an x edge
            if x < b[0]:
                # print('  check x border', (x, y), (a, b))
                a_change = None
                b_change = None
                # if len(dig_edge['neighbors']) != 2:
                #     raise ValueError('neighbors isnt 2')
                for start, end in dig_edge['neighbors']:
                    # start, end = dig_edge['value']
                    if (a, b) == (start, end):
                        continue
                    elif a in [start, end]:
                        n = start if a == end else end
                        # print('found a', a, 'next', n)
                        a_change = a[1] - n[1]
                    elif b in [start, end]:
                        n = start if b == end else end
                        # print('found b', b, 'next', n)
                        b_change = b[1] - n[1]
                if a_change and b_change and a_change*b_change < 0:
                    # print('include as edge')
                    edge_count += 1
    return edge_count


def find_row_gaps(row_segments, row_min, row_max, debug=False):
    gaps = []
    cursor = row_min
    for segment in row_segments:
        if debug:
            print('cursor:', cursor, 'segment:', segment)
        if cursor > row_max:
            break
        # if cursor is before segment's start
        if cursor < segment[0]:
            # create new gap
            gaps.append((cursor, segment[0]-1))
            if debug:
                print('gap:', (cursor, segment[0]-1))
        cursor = segment[1] + 1

    if debug:
        if cursor < row_max:
            print('final gap:', (cursor, row_max))

    return gaps


def merge_segment_overlaps(dig_map):
    for y, row_a in dig_map.items():
        row_b = []
        for start, end in sorted(row_a):
            # if y in (0, 1077):
            #     print('debug', row_a, start, end)
            if row_b and row_b[-1][1] >= start-1:
                # if y in (0, 1077):
                #     print('debug', row_b[-1][1], '>=', start)
                row_b[-1][1] = max(row_b[-1][1], end)
            else:
                row_b.append([start, end])
        if row_a != row_b:
            # if y in (0, 1077):
            #     print('old:', row_a)
            #     print('new:', row_b)
            #     print()
            dig_map[y] = row_b
    return dig_map


def fill_dig_map(dig_map, dig_edges, debug=False):
    print('fill_dig_map')
    # dig_map = {0: {0: '#', 1: '#'...}
    y_min = min(dig_map.keys())
    y_max = max(dig_map.keys()) + 1
    x_min = min([min(a, b) for row in dig_map.values() for a, b in row])
    x_max = max([max(a, b) for row in dig_map.values() for a, b in row]) + 1
    print('y', y_min, '-', y_max, ' : x', x_min, '-', x_max)
    print('len edges', len(dig_edges))
    _s = time.time()
    for y in range(y_min, y_max):
        if debug:
            if y % 100000 == 0:
                print(y, 'time:', time.time() - _s)
                _s = time.time()
        row = dig_map[y]
        # debug = True if  y == -256 else False
        # gaps = find_row_gaps(row, x_min, x_max, debug)
        #_sg = time.time()
        gaps = find_row_gaps(row, x_min, x_max)
        #print('gap time:', time.time() - _sg)

        #new_row = row
        #_ssg = time.time()
        y_dig_edges = get_y_edges(y, dig_edges)
        for segment in gaps:
            edge_count = 0
            x = segment[0]
            edge_count = ray_edge_count(x, y, y_dig_edges)
            # print(x, y, 'count:', edge_count)

            # a point is in the polygon if the ray hits an odd number of edges
            if edge_count != 0 and edge_count % 2 == 1:
                row.append(list(segment))
        #print('segment time:', time.time() - _ssg)
        #print()
        #row.sort()
        # print('row:', row)
    return merge_segment_overlaps(dig_map)


def dig_border(dig_plan):
    print('dig_border')
    directions = {'R': 1,
                  'L': -1,
                  'U': -1,
                  'D': 1}
    dir_map = {0: 'R',
               1: 'D',
               2: 'L',
               3: 'U'}
    dig_map = {}
    dig_edges = []
    dig_edges_new = {}
    first_edge = None
    prev_edge = None
    dig_map[0] = [(0,0)]
    cursor = (0, 0)
    for step in dig_plan:
        direction, distance, hex_code = step.split(' ', 3)
        # distance = int(distance)
        distance = int(hex_code[2:7], 16)
        direction = dir_map[int(hex_code[7], 16)]

        dig_edge = [cursor]
        x = cursor[0]
        y = cursor[1]
        if direction in ['R', 'L']:
            _step  = directions[direction]
            _start = x
            _end   = _start + distance*_step
            cursor = (_end, y)

            _start, _end = (_start, _end) if _start < _end else (_end, _start)

            # we're going left/right, so stay in this row
            row = dig_map.setdefault(y, [])
            row.append((_start, _end))

        elif direction in ['U', 'D']:
            _step  = directions[direction]
            _start = y
            _end   = y + distance*_step
            cursor = (x, _end)

            # going up/down, so use the same x
            for r in range(_start, _end, _step):
                row = dig_map.setdefault(r, [])
                row.append((x, x))

        dig_edge.append(cursor)
        dig_edge.sort()
        if first_edge is None:
            first_edge = dig_edge
        if prev_edge is not None:
            dig_edges_new[str(prev_edge)]['neighbors'].append(dig_edge)
            dig_edges_new[str(dig_edge)] = {'value': dig_edge,
                                            'neighbors': [prev_edge]}
        else:
            dig_edges_new[str(dig_edge)] = {'value': dig_edge,
                                            'neighbors': []}
        prev_edge = dig_edge
        dig_edges.append(dig_edge)

    if len(dig_edges_new[str(first_edge)]['neighbors']) != 1:
        print(first_edge, dig_edge)
        raise ValueError('testing')
    else:
        dig_edges_new[str(first_edge)]['neighbors'].append(dig_edge)
    # compact the dig_map rows
    # for each row, get a union of the ranges
    dig_map = merge_segment_overlaps(dig_map)

    return dig_map, dig_edges_new


st = time.time()
dig_map, dig_edges = dig_border(data)
# x_min = min([min(a, b) for row in dig_map.values() for a, b in row])
# x_max = max([max(a, b) for row in dig_map.values() for a, b in row]) + 1
# for y, row in dig_map.items():
#     debug = True if y == -256 else False
#     print(find_row_gaps(row, x_min, x_max, debug))
# print()
dig_map = fill_dig_map(dig_map, dig_edges)
count = 0
for y in sorted(dig_map.keys()):
    #print(y, dig_map[y])
    for segment in dig_map[y]:
        count += segment[1] - segment[0] + 1

print('count:', count)
print('correct:', 54662804037719)
print()

print('run time:', time.time() - st)
