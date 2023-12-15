#!/usr/bin/env python3
import re
import itertools

input_file = 'day12_input.txt'
# input_file = 'day12_test.txt'

# '.' == operational
# '#' == damaged
# '?' == unknown
# ???.### 1,1,3


def generate_rx(backup):
    rx = ''
    for i, x in enumerate(backup):
        if i == 0:
            _rx = '^[^#]*'
        else:
            _rx = '[^#]+'
        rx += _rx + '#{' + str(x) + '}'
    rx += '[^#]*$'
    return rx


def findall_filter(item):
    found = re.findall(r"{0}".format(rx), item)
    if found:
        return True
    return False


def permutations(string):

    if len(string) == 1:
        if string == '?':
            return ['#', '.']
        else:
            return string

    cur = string[0]
    if cur == '?':
        cur = ['#', '.']

    rest = permutations(string[1:])

    return set([''.join(p) for p in itertools.product(cur, rest)])


with open(input_file) as f:
    data = [x.strip() for x in f.readlines()]

total_arrangements = []
for row in data:
    condition, backup = row.split(' ', 1)
    backup = [int(b) for b in backup.split(',')]
    rx = generate_rx(backup)
    # print(set(filter(findall_filter, permutations(condition))))
    arrangements = len(set(filter(findall_filter, permutations(condition))))
    total_arrangements.append(arrangements)
    #print(condition, rx, ' - ', arrangements)

print()
print('total:', sum(total_arrangements))
# correct answer: 8193
