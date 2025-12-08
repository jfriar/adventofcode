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
            break

        if collect_ranges:
            start, end = list(map(int, line.split('-')))
            fresh_ingredient_id_ranges.append([start, end])

fresh_ingredient_id_ranges = list(sorted(fresh_ingredient_id_ranges))
#print(fresh_ingredient_id_ranges)

# [[1,5], [8,20]]
# get [4,9]
# get all ranges this is in
# 4 in [1, 5]
# 9 in [8, 20]
# for all ranges this pair is in, find the lowest x, highest y to create one new range
merged_id_ranges = []
for start, end in fresh_ingredient_id_ranges:
    find_containing_ranges = []
    for _start, _end in merged_id_ranges:
        if _start <= start <= _end or _start <= end <= _end:
            find_containing_ranges.append([_start, _end])

    if not find_containing_ranges:
        merged_id_ranges.append([start, end])
    else:
        start_lowest = start
        end_highest = end
        for _start, _end in find_containing_ranges:
            merged_id_ranges.remove([_start, _end])
            if _start < start_lowest:
                start_lowest = _start
            if _end > end_highest:
                end_highest = _end
        merged_id_ranges.append([start_lowest, end_highest])
    merged_id_ranges = list(sorted(merged_id_ranges))
    
print(len(merged_id_ranges))
#print(merged_id_ranges)

total_ids = 0
for start, end in merged_id_ranges:
    total_ids += end - start + 1

print('total:', total_ids)
