#!/usr/bin/env python3

input_file = 'day02_input.txt'
#input_file = 'day02_sample.txt'


def find_repeated_x(start, end):
    start_int = int(start)
    start_str = str(start)
    end_int = int(end)
    end_str = str(end)
    invalid_ids = []
    for _id in range(start_int, end_int+1):
        _id_str = str(_id)
        _id_len = len(_id_str)
        if _id_len <= 1:
            continue
        # check if all the ints are the same
        if len(set(list(map(int, _id_str)))) == 1:
            # print('invalid:', _id)
            invalid_ids.append(_id)

        # if not, check all possible repeat sizes
        else:
            for repeat_len in range(2, _id_len):
                if _id_len % repeat_len == 0:
                    # print(' check:', repeat_len)
                    # split _id_str by repeat len
                    _id_split = [_id_str[i:i+repeat_len] for i in range(0, len(_id_str), repeat_len)]
                    if len(set(_id_split)) == 1:
                        invalid_ids.append(_id)
                        # print(' invalid:', _id)

    return invalid_ids


invalid_ids = []
with open(input_file) as f:
    for line in f.readlines():
        for id_range in line.strip().split(','):
            id_start, id_end = id_range.split('-', maxsplit=2)
            _invalid_ids = find_repeated_x(id_start, id_end)
            print(id_range, id_start, id_end)
            print(' ', int(id_end) - int(id_start), _invalid_ids)
            invalid_ids += _invalid_ids
#print(invalid_ids)
print(sum(set(invalid_ids)))
