#!/usr/bin/env python3

input_file = 'day12_input.txt'
# input_file = 'day12_sample1.txt'
# input_file = 'day12_sample2.txt'
# input_file = 'day12_sample3_pt2.txt'
# input_file = 'day12_sample4_pt2.txt'
# input_file = 'day12_sample3.txt'

moves = ((1, 0), (-1, 0), (0, 1), (0, -1))


def find_neighbors(x, y, plant_type):
    neighbors = set()
    for dx, dy in moves:
        nx = x + dx
        ny = y + dy
        if nx < 0 or nx >= len_x or ny < 0 or ny >= len_y:
            continue
        if garden_plots[ny][nx] == plant_type:
            neighbors.add((nx, ny))
    return neighbors


def num_neighbors(x, y, plant_type):
    neighbors = 0
    for dx, dy in moves:
        nx = x + dx
        ny = y + dy
        if nx < 0 or nx >= len_x or ny < 0 or ny >= len_y:
            continue
        if garden_plots[ny][nx] == plant_type:
            neighbors += 1
    return neighbors


with open(input_file) as f:
    garden_plots = [line.rstrip() for line in f.readlines()]

len_y = len(garden_plots)
len_x = len(garden_plots[0])
seen = set()
neighbors = set()

plots_by_type = {}
for y, row in enumerate(garden_plots):
    for x in range(len_x):
        if (x, y) in seen:
            continue
        plant_type = garden_plots[y][x]
        neighbors.update(find_neighbors(x, y, plant_type))
        seen.add((x,y))
        add_points = set([(x, y)])
        # add_points.add((x,y))
        while neighbors:
            (_x, _y) = neighbors.pop()
            if (_x, _y) in seen:
                continue
            neighbors.update(find_neighbors(_x, _y, plant_type))
            seen.add((_x, _y))
            add_points.add((_x, _y))
        plots_by_type.setdefault(plant_type, []).append(add_points)


def group_continuous_edges(elements):
    edges = []
    _edge = set()
    # print('> elements:', elements)
    for row in elements.values():
        _row = sorted(row)
        # print('>> _row:', _row)
        for i, v in enumerate(_row):
            _edge.add(v)
            if i >= len(_row) - 1:
                # if we have reached the end
                edges.append(_edge)
                _edge = set()
                break

            if _row[i+1] == v + 1:
                # continuous edge
                continue
            # next edge
            edges.append(_edge)
            _edge = set()

    return edges


def find_edges(plot, plant_type):
    edges = {'top': {},
             'bottom': {},
             'left': {},
             'right': {}}

    for x, y in plot:
        neighbors = find_neighbors(x, y, plant_type)
        if (x+1, y) not in neighbors:
            # edges['right'].add((x, y))
            edges['right'].setdefault(x, set()).add(y)
        if (x-1, y) not in neighbors:
            # edges['left'].add((x, y))
            edges['left'].setdefault(x, set()).add(y)
        if (x, y-1) not in neighbors:
            # edges['top'].add((x, y))
            edges['top'].setdefault(y, set()).add(x)
        if (x, y+1) not in neighbors:
            # edges['bottom'].add((x, y))
            edges['bottom'].setdefault(y, set()).add(x)

    return edges


from pprint import pprint

def count_sides(edge, plant_type, direction):
    dx, dy = direction
    num_sides = 1
    edge_sorted = sorted(edge)
    edge_len = len(edge_sorted)
    sides = []
    _side = set()
    for (x, y) in edge_sorted:
        _side.add((x,y))
        if edge_len == 1:
            break
        same_side = False
        # n_x, n_y = edges_sorted[i+1]
        if (x+dx, y+dy) in edge:
            same_side = True
            continue
            # if x+dx == n_x and y+dy == n_y:
            #     same_edge = True
            #     break
        if same_side is False:
            num_sides += 1
            _side.add((x, y))
            sides.append(_side)
            _side = set()
            _side.add((x, y))

    # print('sides', sides)
    print('sides:')
    pprint(sides)
    return num_sides


# print(find_neighbors(0,0,'A'))
# find area and perimeter
total_price = 0
for plant_type, plots in plots_by_type.items():
    for i, plot in enumerate(plots):
        edges = set()
        area = len(plot)
        perimeter = sum([4 - num_neighbors(x, y, plant_type) for x, y in plot])
        edges = find_edges(plot, plant_type)
        # print(' edges:', edges)
        # print(' edges:')
        # pprint(edges)

        # num_sides = 0
        # for edge, vals in edges.items():
        #     _edges = group_continuous_edges(vals)
        #     # print('  edge: ', edge)
        #     # print('  vals:')
        #     # pprint(vals)
        #     # print('  _edges:')
        #     # pprint(_edges)
        #     # print()
        #     num_sides += len(_edges)
        num_sides = sum([len(group_continuous_edges(vals)) for edge, vals in edges.items()])
        # num_sides = sum([count_edges(edge, plant_type) for edge in edges.values()])
        # num_sides = 1
        # num_sides = 0
        # for edge_type, edge in edges.items():
        #     num_sides += count_sides(edge, plant_type)
        #     print(' edge_type:', edge_type, ' num_sides:', num_sides)
        # price = area * perimeter
        price = area * num_sides
        total_price += price
        print(plant_type, i, 'price:', price, plot)
        print(' area:', area)
        print(' num_sides:', num_sides)


print('total price:', total_price)
