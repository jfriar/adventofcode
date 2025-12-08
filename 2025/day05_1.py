#!/usr/bin/env python3

input_file = 'day05_input.txt'
#input_file = 'day05_sample.txt'

fresh_ingredient_id_ranges = []
collect_ranges = True
ingredient_ids = []

with open(input_file) as f:
    for line in f.readlines():
        line = line.strip()
        if line == '':
            collect_ranges = False
            continue

        if collect_ranges:
            start, end = list(map(int, line.split('-')))
            fresh_ingredient_id_ranges.append((start, end))
        else:
            ingredient_ids.append(int(line))

# from pprint import pprint
# pprint(fresh_ingredient_id_ranges)
# print('')
# pprint(ingredient_ids)

fresh_ids = []
for ingredient_id in ingredient_ids:
    for start, end in fresh_ingredient_id_ranges:
        if start <= ingredient_id <= end:
            fresh_ids.append(ingredient_id)
            break
        
print(len(fresh_ids))

