#!/usr/bin/env python3

input_file = 'day09_input.txt'
# input_file = 'day09_sample.txt'


def compact_back_to_front(expanded_map):
    # if expanded_map.find('.') == -1:
    #     return expanded_map

    compacted_map = expanded_map.copy()
    length = len(compacted_map)
    end = length - 1
    start = compacted_map.index('.')
    count = 0
    loop_id = 0
    while start < end:
        file_id = compacted_map[end]
        if file_id != '.':
            # expanded_map = list(expanded_map)
            compacted_map[start] = file_id
            compacted_map[end] = '.'
            # expanded_map = ''.join(expanded_map)
        # print(expanded_map)
        # print('start',start,'end',end,'file_id',file_id)
        start = compacted_map.index('.')
        end -= 1
        if (10000 * count) == loop_id:
            print(loop_id, ':', start, end)
            count += 1
        loop_id += 1
    return compacted_map


with open(input_file) as f:
    disk_maps = [line.rstrip() for line in f.readlines()]

expanded_maps = []
for disk_map in disk_maps:
    file_id = 0
    expanded_map = []
    for i, d in enumerate(disk_map):
        # if i is odd
        if i % 2:
            # free_space
            expanded_map += ['.'] * int(d)
        else:
            # file_size
            expanded_map += [file_id] * int(d)
            file_id += 1
    compacted_map = compact_back_to_front(expanded_map)
    checksum = 0
    for i, d in enumerate(compacted_map):
        if d == '.':
            break
        checksum += (int(d) * i)

    # print(expanded_map, compacted_map, checksum)
    dot_index = compacted_map.index('.')
    print(compacted_map[dot_index-10:dot_index-1], checksum)
    # expanded_maps.append(compact_back_to_front(expanded_map))

# print(expanded_maps)
