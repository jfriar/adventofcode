#!/usr/bin/env python3

input_file = 'day19_input.txt'
# input_file = 'day19_test.txt'

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


def process_part(part, workflows):
    workflow_name = 'in'
    while workflow_name not in ['A', 'R']:
        workflow = workflows[workflow_name]
        # print(' workflow:', workflow_name)
        for rule in workflow:
            category, comparison, value, dest = rule
            if all(x is None for x in [category, comparison, value]):
                # print(' >last one reached')
                workflow_name = dest
                break
            else:
                if comparison == '>' and part[category] > value:
                    workflow_name = dest
                    break
                elif comparison == '<' and part[category] < value:
                    workflow_name = dest
                    break

    return workflow_name


# from pprint import pprint
# print(parts)
# print()
# pprint(workflows)

count = 0
for part in parts:
    result = process_part(part, workflows)
    # print(part, result)
    if result == 'A':
        count += sum(part.values())

print('count:', count)
