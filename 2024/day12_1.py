#!/usr/bin/env python3

input_file = 'day12_input.txt'
# input_file = 'day12_sample1.txt'
# input_file = 'day12_sample2.txt'
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

# find area and perimeter
total_price = 0
for plant_type, plots in plots_by_type.items():
    for i, plot in enumerate(plots):
        area = len(plot)
        perimeter = sum([4 - num_neighbors(x, y, plant_type) for x, y in plot])
        price = area * perimeter
        total_price += price
        # print(plant_type, i, 'area:', area, 'perimeter:', perimeter, plot)
        print(plant_type, i, 'price:', price, plot)

print('total price:', total_price)
