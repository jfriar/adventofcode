#!/usr/bin/env python3
import functools

input_file = 'day05_input.txt'
# input_file = 'day05_sample.txt'


def sort_by_rules(a, b):
    if b in page_ordering_rules.get(a, []):
        # a < b
        return -1
    elif a in page_ordering_rules.get(b, []):
        # a > b
        return 1
    # a == b
    return 0


with open(input_file) as f:
    is_rule = True
    page_ordering_rules = {}
    updates = []
    for line in f.readlines():
        line = line.rstrip()
        if line == '':
            is_rule = False
            continue
        if is_rule:
            before, after = line.split('|')
            before = int(before)
            after = int(after)
            page_ordering_rules.setdefault(before, []).append(after)
        else:
            updates.append([int(page) for page in line.split(',')])

# print(page_ordering_rules)
# print(updates)
# print()

solution = 0
for update in updates:
    _update = update.copy()
    _update.sort(key=functools.cmp_to_key(sort_by_rules))
    if update == _update:
        middle = int(len(update)/2)
        print('correct:', update, update[middle])
        solution += update[middle]
    # else:
    #     print('incorrect:', update, _update)
    # print(update, _update)

print('\nsolution:', solution)

