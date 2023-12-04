#!/usr/bin/env python3
import re

#input_file = 'day3_test.txt'
input_file = 'day3_input.txt'

def search_for_symbol():
    return


with open(input_file) as f:
    schematic = [x.strip() for x in f.readlines()]
    part_numbers = []
    for i, row in enumerate(schematic):
        row_numbers = re.findall(r"(?<!\d)\d+(?!\d)", row)

        #print(row, row_numbers)
        #print(row_numbers, schematic[i])
        #print(row_numbers)
        if i > 0:
            print(schematic[i-1])
        print(schematic[i])
        if i < len(schematic)-1:
            print(schematic[i+1])


        # for rn in row_numbers:
        for rm in re.finditer(r"(?<!\d)\d+(?!\d)", row):
            rn = rm[0]
            # rn_x1 = re.search(r"(?<!\d){0}(?!\d)".format(rn), schematic[i]).start()
            rn_x1 = rm.start()
            rn_x2 = rn_x1 + len(rn)
            #print(schematic[i][rn_x1:rn_x2])

            # check previous
            if rn_x1 > 0:
                # check this row
                if re.match(r"[^0-9.]", schematic[i][rn_x1-1]):
                    print('previous')
                    print(schematic[i][rn_x1-1], schematic[i][rn_x1:rn_x2])
                    part_numbers.append(rn)
                    continue
                # check previous row
                if i > 0:
                    if re.match(r"[^0-9.]", schematic[i-1][rn_x1-1]):
                        print('previous above')
                        print(schematic[i-1][rn_x1-1], schematic[i-1][rn_x1:rn_x2])
                        print(schematic[i][rn_x1-1], schematic[i][rn_x1:rn_x2])
                        part_numbers.append(rn)
                        continue
                # check the next row
                if i < len(schematic)-1:
                    if re.match(r"[^0-9.]", schematic[i+1][rn_x1-1]):
                        print('previous below')
                        print(schematic[i][rn_x1-1], schematic[i][rn_x1:rn_x2])
                        print(schematic[i+1][rn_x1-1], schematic[i+1][rn_x1:rn_x2])
                        part_numbers.append(rn)
                        continue

            # check next
            if rn_x2 < len(row):
                # check this row
                if re.match(r"[^0-9.]", schematic[i][rn_x2]):
                    print('next')
                    print(schematic[i][rn_x1:rn_x2], schematic[i][rn_x2])
                    part_numbers.append(rn)
                    continue
                # check previous row
                if i > 0:
                    if re.match(r"[^0-9.]", schematic[i-1][rn_x2]):
                        print('next above')
                        print(schematic[i-1][rn_x1:rn_x2], schematic[i-1][rn_x2])
                        print(schematic[i][rn_x1:rn_x2], schematic[i][rn_x2])
                        part_numbers.append(rn)
                        continue
                # check next row
                if i < len(schematic)-1:
                    if re.match(r"[^0-9.]", schematic[i+1][rn_x2]):
                        print('next below')
                        print(schematic[i][rn_x1:rn_x2], schematic[i][rn_x2])
                        print(schematic[i+1][rn_x1:rn_x2], schematic[i+1][rn_x2])
                        part_numbers.append(rn)
                        continue

            # check previous row
            if i > 0:
                for _x in range(len(rn)):
                    x = rn_x1 + _x
                    #print(schematic[i][rn_x1:rn_x2], 'x:', x, 'val:', schematic[i-1][x])
                    if re.match(r"[^0-9.]", schematic[i-1][x]):
                        print('above')
                        print(schematic[i-1][rn_x1:rn_x2])
                        print(schematic[i][rn_x1:rn_x2])
                        part_numbers.append(rn)
                        continue

            # check next row
            if i < len(schematic)-1:
                for _x in range(len(rn)):
                    x = rn_x1 + _x
                    #print(schematic[i][rn_x1:rn_x2], 'x:', x, 'val:', schematic[i+1][x])
                    if re.match(r"[^0-9.]", schematic[i+1][x]):
                        print('below')
                        print(schematic[i][rn_x1:rn_x2])
                        print(schematic[i+1][rn_x1:rn_x2])
                        part_numbers.append(rn)
                        continue

    print()
    part_numbers = [int(p) for p in part_numbers]
    print(sum(part_numbers))

