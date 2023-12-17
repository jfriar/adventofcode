#!/usr/bin/env python3

input_file = 'day13_input.txt'
# input_file = 'day13_test.txt'


def find_mirror_axis(pattern, skip=0, debug=False):
    # this only looks for "x" axis at the "y" position (height)
    pattern_len = len(pattern)
    midpoint = int(pattern_len / 2)
    for y in range(0, pattern_len):
        if y == skip-1:
            #print(' > skipping:', skip, 'y:', y, 'length:', pattern_len)
            continue
        elif y == 0:
            # top = [pattern[0]]
            # bottom = [pattern[1]]
            if pattern[0] and pattern[0] == pattern[1]:
                return y+1
        elif y < midpoint:
            top = pattern[:y+1]
            # bottom = pattern[y+1:y+1+len(top)]
            if top and top == list(reversed(pattern[y+1:y+1+len(top)])):
                return y+1
        else:
            bottom = pattern[y+1:]
            # top = pattern[y+1-len(bottom):y+1]
            if bottom and pattern[y+1-len(bottom):y+1] == list(reversed(bottom)):
                return y+1

    return 0


def find_x_y_axis(pattern, orig=None, debug=False):
    if orig is not None:
        x_skip, y_skip = orig
    else:
        x_skip, y_skip = [0, 0]

    # x axis
    x_axis = find_mirror_axis(pattern, x_skip, debug)
    # y axis
    transposed = [''.join(z) for z in zip(*pattern)]
    y_axis = find_mirror_axis(transposed, y_skip, debug)
    return (x_axis, y_axis)


def clean_smudges(pattern, index):
    # get the original x/y axis
    x_orig, y_orig = find_x_y_axis(pattern)
    print('orig axis:', x_orig, y_orig)

    # now find a new x/y axis
    x_new = 0
    y_new = 0
    _x = 0
    _y = 0
    new_pattern = [list(row) for row in pattern]
    while x_new == 0 and y_new == 0:
        # new_pattern = []
        # for y in range(len(pattern)):
        old_char = new_pattern[_y][_x]
        new_char = '.' if old_char == '#' else '#'
        new_pattern[_y][_x] = new_char

        x_new, y_new = find_x_y_axis(new_pattern, [x_orig, y_orig])

        if x_new != 0 or y_new != 0:
            print(' new axis:', x_new, y_new, '_x _y:', _x, _y)
            break

        if x_new == x_orig and x_new != 0:
            print(' no axis found! _x, _y:', _x, _y, 'pattern index:', index)
        elif y_new == y_orig and y_new != 0:
            print(' no axis found! _x, _y:', _x, _y, 'pattern index:', index)

        if _y > len(pattern)-1:
            print(' no axis found! _x, _y:', _x, _y, 'pattern index:', index)
            raise

        # reset new_pattern for next iteration
        new_pattern[_y][_x] = old_char
        if _x == len(pattern[0])-1:
            _x = 0
            _y += 1
        else:
            _x += 1
    return (x_new, y_new)


with open(input_file) as f:
    data = [x.strip() for x in f.readlines()]

patterns = []
_tmp = []
for row in data:
    if row != '':
        _tmp.append(row)
    else:
        patterns.append(_tmp)
        _tmp = []

if _tmp:
    patterns.append(_tmp)

total = 0
for i, p in enumerate(patterns):
    # x_axis, y_axis = find_x_y_axis(p)
    x_axis, y_axis = clean_smudges(p, i)
    # print('y_axis:', y_axis, 'x_axis:', x_axis)
    total += (x_axis*100) + y_axis

print('total:', total)
print('correct:', 25450)
