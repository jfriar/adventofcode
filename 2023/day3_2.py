#!/usr/bin/env python3
import re

#input_file = 'day3_test2.txt'
input_file = 'day3_input.txt'

def search_for_symbol():
    return


with open(input_file) as f:
    schematic = [x.strip() for x in f.readlines()]

    num_map = {}
    for i, row in enumerate(schematic):
        num_map[i] = {}
        for rm in re.finditer(r"(?<!\d)\d+(?!\d)", row):
            rn_x1 = rm.start()
            rn_x2 = rm.end()
            rn = {rm[0]: (rn_x1, rn_x2)}
            num_map[i].update({r: rn  for r in range(rn_x1, rn_x2)})

    gears = []
    for i, row in enumerate(schematic):
        # if i > 0:
        #     print(schematic[i-1])
        # print(schematic[i])
        # if i < len(schematic)-1:
        #     print(schematic[i+1])

        # for rn in row_numbers:
        for rm in re.finditer(r"\*", row):
            rn = rm[0]
            rn_x1 = rm.start()
            rn_x2 = rm.end()
            #print(schematic[i][rn_x1:rn_x2])

            row_gears = set()
            # check previous
            if rn_x1 > 0:
                # check this row
                x = rn_x1 - 1
                if schematic[i][x].isdigit():
                    print('previous')
                    print(schematic[i][x], schematic[i][rn_x1:rn_x2])
                    if num_map.get(x):
                        row_gears.add(tuple(num_map[i][x].items()))
                # check previous row
                if i > 0:
                    if schematic[i-1][x].isdigit():
                        print('previous above')
                        print(schematic[i-1][x], schematic[i-1][rn_x1:rn_x2])
                        print(schematic[i][x], schematic[i][rn_x1:rn_x2])
                        if num_map.get(x):
                            row_gears.add(tuple(num_map[i-1][x].items()))
                # check the next row
                if i < len(schematic)-1:
                    if schematic[i+1][x].isdigit():
                        print('previous below')
                        print(schematic[i][x], schematic[i][rn_x1:rn_x2])
                        print(schematic[i+1][x], schematic[i+1][rn_x1:rn_x2])
                        if num_map.get(x):
                            row_gears.add(tuple(num_map[i+1][x].items()))

            # check next
            if rn_x2 < len(row):
                x = rn_x2
                # check this row
                if schematic[i][x].isdigit():
                    print('next')
                    print(schematic[i][rn_x1:rn_x2], schematic[i][x])
                    row_gears.add(tuple(num_map[i][x].items()))
                # check previous row
                if i > 0:
                    if schematic[i-1][x].isdigit():
                        print('next above')
                        print(schematic[i-1][rn_x1:rn_x2], schematic[i-1][x])
                        print(schematic[i][rn_x1:rn_x2], schematic[i][x])
                        row_gears.add(tuple(num_map[i-1][x].items()))
                # check next row
                if i < len(schematic)-1:
                    if schematic[i+1][x].isdigit():
                        print('next below')
                        print(schematic[i][rn_x1:rn_x2], schematic[i][x])
                        print(schematic[i+1][rn_x1:rn_x2], schematic[i+1][x])
                        row_gears.add(tuple(num_map[i+1][x].items()))

            # check previous row
            if i > 0:
                for _x in range(len(rn)):
                    x = rn_x1 + _x
                    #print(schematic[i][rn_x1:rn_x2], 'x:', x, 'val:', schematic[i-1][x])
                    if schematic[i-1][x].isdigit():
                        print('above')
                        print(schematic[i-1][rn_x1:rn_x2])
                        print(schematic[i][rn_x1:rn_x2])
                        row_gears.add(tuple(num_map[i-1][x].items()))

            # check next row
            if i < len(schematic)-1:
                for _x in range(len(rn)):
                    x = rn_x1 + _x
                    #print(schematic[i][rn_x1:rn_x2], 'x:', x, 'val:', schematic[i+1][x])
                    if schematic[i+1][x].isdigit():
                        print('below')
                        print(schematic[i][rn_x1:rn_x2])
                        print(schematic[i+1][rn_x1:rn_x2])
                        row_gears.add(tuple(num_map[i+1][x].items()))

            if len(row_gears) >= 2:
                gears.append(row_gears)

    print()
    from pprint import pprint
    pprint(num_map)
    print()
    pprint(gears)
    gear_ratios = []
    for gear in gears:
        gear_ratio = 1
        print(gear)
        for num in gear:
            print('num:', num[0][0])
            try:
                gear_ratio *= int(num[0][0])
            except:
                print(num)
                raise
        gear_ratios.append(gear_ratio)
    print(sum(gear_ratios))

