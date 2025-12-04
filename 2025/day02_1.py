#!/usr/bin/env python3

input_file = 'day02_input.txt'
#input_file = 'day02_sample.txt'


def find_repeated_twice(start, end):
    start_int = int(start)
    start_str = str(start)
    end_int = int(end)
    end_str = str(end)
    invalid_ids = []
    for _id in range(start_int, end_int+1):
        _id_str = str(_id)
        _id_len = len(_id_str)
        # only check if the id is an even length
        if _id_len % 2 == 0:
            half_way = int(_id_len / 2)
            _id_left = _id_str[:half_way]
            _id_right = _id_str[half_way:]
            if _id_left == _id_right:
                invalid_ids.append(_id)
                print('  ', _id_left, _id_right)
    return invalid_ids


invalid_ids = []
with open(input_file) as f:
    for line in f.readlines():
        for id_range in line.strip().split(','):
            id_start, id_end = id_range.split('-', maxsplit=2)
            print(id_range, id_start, id_end)
            print(' ', int(id_end) - int(id_start))
            invalid_ids += find_repeated_twice(id_start, id_end)
print(sum(invalid_ids))
