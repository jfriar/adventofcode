#!/usr/bin/env python3
import copy

input_file = 'day19_input.txt'
#input_file = 'day19_test.txt'

with open(input_file) as f:
    data = [x.strip() for x in f.readlines()]
    workflows = {}
    parts = []
    is_part = False
    for line in data:
        if line == '':
            is_part = True
            continue

        if is_part:
            # {x=787,m=2655,a=1222,s=2876}
            part = {}
            # strip '{' and '}'
            for l in line[1:-1].split(','):
                category, value = l.split('=')
                part[category] = int(value)
            parts.append(part)
        else:
            # qkq{x<1416:A,crn}
            workflow = []
            name, rest = line.split('{')
            # strip the remaining '}'
            for r in rest[:-1].split(','):
                if r.count(':') > 0:
                    comparison = '>' if r.count('>') == 1 else '<'
                    category, _rest = r.split(comparison)
                    value, dest = _rest.split(':')
                    workflow.append((category, comparison, int(value), dest))
                else:
                    workflow.append((None, None, None, r))
            workflows[name] = workflow


def process_workflows(name, workflows, part, lvl=0):
    # print('workflow name:', name, 'lvl:', lvl)
    # part[x] = [1, 4000]
    # workflow[name] = qkq{x<1416:A,crn}
    parts = []

    while name not in ['A', 'R']:
        for rule in workflows[name]:
            category, comparison, value, dest = rule
            if all(x is None for x in [category, comparison, value]):
                name = dest
                break
            else:
                if comparison == '>' and part[category][1] > value:
                    # if part[category][0] >= value:
                    #     # no splitting
                    # else:
                    if part[category][0] <= value:
                        # splitting - new_part is the "lower half"/non-match
                        new_part = copy.deepcopy(part)
                        new_part[category][1] = value
                        parts.extend(process_workflows(name, workflows, new_part, lvl+1))

                        # the matching range of category values
                        part[category][0] = value + 1

                    name = dest
                    break

                elif comparison == '<' and part[category][0] < value:
                    if part[category][1] >= value:
                        # splitting - new_part is the "upper" half/non-match
                        new_part = copy.deepcopy(part)
                        new_part[category][0] = value
                        parts.extend(process_workflows(name, workflows, new_part, lvl+1))

                        part[category][1] = value - 1

                    name = dest
                    break

    if name != 'R':
        # print('lvl:', lvl, 'accepted:', part)
        parts.append(part)
    # else:
    #     print('lvl:', lvl, 'rejected:', part)

    return parts
        

part = {'x': [1, 4000],
        'm': [1, 4000],
        'a': [1, 4000],
        's': [1, 4000]}

processed_workflows = process_workflows('in', workflows, part)
# print(len(processed_workflows))
# print()
# from pprint import pprint
# pprint(processed_workflows)
# print()

count = []
for i in processed_workflows:
  _count = 1
  for v in i.values():
    _count *= v[1] - v[0] + 1
  count.append(_count)

print('count:  ', sum(count))
print('correct:', 116138474394508)

