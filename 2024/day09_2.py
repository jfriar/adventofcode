#!/usr/bin/env python3

input_file = 'day09_input.txt'
# input_file = 'day09_sample.txt'


def find_free_range(size, compacted_map):
    _size = 0
    _free_start = None
    _free_end = None
    for i, block in enumerate(compacted_map):
        if block == '.':
            if _free_start is None:
                _free_start = i
            _free_end = i
            _size += 1
        else:
            _free_start = None
            _free_end = None
            _size = 0
        if _size == size:
            # print('found _size', _size, ' == size', size)
            break

    if (_free_end - _free_start + 1) < size:
        return None, None

    return _free_start, _free_end


def compact_back_to_front(expanded_map):
    compacted_map = expanded_map.copy()
    end = len(compacted_map) - 1
    count = 0
    loop_id = 0
    while True:
        file_id = compacted_map[end]
        if file_id != '.':
            file_id_start = compacted_map.index(file_id)
            num_file_id = compacted_map.count(file_id)
            free_start, free_end = find_free_range(num_file_id, compacted_map)

            if free_start and free_end and free_end < file_id_start:
                # print('found range:', free_start, free_end, 'for:', file_id)
                # print(' free_start', free_start, 'num_file_id', num_file_id)
                for i in range(free_start, free_start+num_file_id):
                    # print(' >', compacted_map[i], ' =>', file_id)
                    compacted_map[i] = file_id
                for i in range(file_id_start, file_id_start+num_file_id):
                    compacted_map[i] = '.'
            end = file_id_start
            # print('file_id', file_id, 'end', end, compacted_map[end+1])
            if int(file_id) == 0:
                break
        # print(expanded_map)
        # print('start',start,'end',end,'file_id',file_id)
        end -= 1
        if (10000 * count) == loop_id:
            print(loop_id, ':', end)
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
            continue
        checksum += (int(d) * i)

    # print(expanded_map, '\n', ''.join([str(c) for c in compacted_map]), '\n', checksum)
    dot_index = compacted_map.index('.')
    print(compacted_map[dot_index-10:dot_index-1], checksum)
    # expanded_maps.append(compact_back_to_front(expanded_map))

# print(expanded_maps)
