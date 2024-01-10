#!/usr/bin/env python3
import re

input_file = 'day18_input.txt'
# input_file = 'day18_test.txt'

with open(input_file) as f:
    data = [x.strip() for x in f.readlines()]


def ray_edge_count(x, y, dig_edges):
    # check rays going in the +x direction
    # they must hit a "vertical" y edge, or an x edge that is connect to edges
    # that go in opposite directions (up and down)
    edge_count = 0
    for a, b in dig_edges:
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
                for start, end in dig_edges:
                    if a in [start, end] and (a, b) != (start, end):
                        n = start if a == end else end
                        # print('found a', a, 'next', n)
                        a_change = a[1] - n[1]
                    if b in [start, end] and (a, b) != (start, end):
                        n = start if b == end else end
                        # print('found b', b, 'next', n)
                        b_change = b[1] - n[1]
                if a_change and b_change and a_change*b_change < 0:
                    # print('include as edge')
                    edge_count += 1
    return edge_count


def fill_dig_map(dig_map, dig_edges):
    # dig_map = {0: {0: '#', 1: '#'...}
    new_map = []
    y_min = min(dig_map.keys())
    y_max = max(dig_map.keys()) + 1
    x_min = min([min(row.keys()) for row in dig_map.values()])
    x_max = max([max(row.keys()) for row in dig_map.values()]) + 1
    # print(y_min, '-', y_max, ' : ', x_min, '-', x_max)
    for y in range(y_min, y_max):
        row = ''
        fill_in = False
        for x in range(x_min, x_max):
            char = dig_map.get(y, {}).get(x, '.')

            # this is super slow:
            # if char == '.':
            #     edge_count = ray_edge_count(x, y, dig_edges)
            #     if edge_count != 0 and edge_count % 2 == 1:
            #         # this point is internal to the borders
            #         char = '#'

            row += char
        # new_map.append(row)
        # print(row)

        # for the row, find all the '.' segments, and figure out if they should
        # be '#' instead (to fill within the borders).  This approach only
        # requires the first point of the edge segment to be checked.
        new_row = row
        for segment in re.finditer(r'[^#]+', row):
            edge_count = 0
            x = segment.span(0)[0]
            # x+x_min to handle negative x grids
            edge_count = ray_edge_count(x+x_min, y, dig_edges)
            # print(x, y, 'count:', edge_count)

            # a point is in the polygon if the ray hits an odd number of edges
            if edge_count != 0 and edge_count % 2 == 1:
                # print('> found internal segment', segment)
                span = segment.span(0)
                start = span[0]
                end = span[1]
                span_len = end - start
                if start == 0:
                    new_row = '#' * span_len + new_row[end:]
                else:
                    new_row = new_row[0:start] + '#' * span_len + new_row[end:]
        new_map.append(new_row)
        # print(new_row)
        # print()
    return new_map


def dig_border(dig_plan):
    directions = {'R': 1,
                  'L': -1,
                  'U': -1,
                  'D': 1}
    dig_map = {}
    dig_edges = []
    cursor = (0, 0)
    dig_map[0] = {0: '#'}
    for step in dig_plan:
        dig_edge = [cursor]
        direction, distance, color = step.split(' ', 3)
        distance = int(distance)
        x = cursor[0]
        y = cursor[1]
        if direction in ['R', 'L']:
            #print(direction, distance)
            # 0   6    1
            # 6-1 0-1 -1
            # we're going right - so stay in this row
            row = dig_map.setdefault(y, {})
            _step  = directions[direction]
            _start = x + _step
            _end   = x + distance*_step + _step
            for r in range(_start, _end, _step):
                row[r] = '#'
            new_x = _end - _step
            cursor = (new_x, y)
            # print('y', y)
            # print('row', row)
            # print('new_row', new_row)
        elif direction in ['U', 'D']:
            _step  = directions[direction]
            _start = y + _step
            _end   = y + distance*_step + _step

            for r in range(_start, _end, _step):
                row = dig_map.setdefault(r, {})
                row[x] = '#'

            new_y = _end - _step
            cursor = (x, new_y)
        dig_edge.append(cursor)
        dig_edge.sort()
        dig_edges.append(dig_edge)
    return dig_map, dig_edges


dig_map, dig_edges = dig_border(data)
dig_map = fill_dig_map(dig_map, dig_edges)
count = 0
for row in dig_map:
    count += row.count('#')

print('count:', count)
# print('correct:', 62573)
