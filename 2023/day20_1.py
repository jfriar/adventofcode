#!/usr/bin/env python3
import collections

input_file = 'day20_input.txt'
#input_file = 'day20_test.txt'
#input_file = 'day20_test1.txt'
#input_file = 'day20_test2.txt'

with open(input_file) as f:
    data = [x.strip() for x in f.readlines()]
    modules = {}
    for d in data:
        module_type = None
        if d.startswith('%'):
            module_type = 'flip-flop'
            d = d[1:]
        elif d.startswith('&'):
            module_type = 'conjunction'
            d = d[1:]
        name, dest = d.split(' -> ')
        dest = dest.split(', ')
        modules[name] = {'dest': dest,
                         'type': module_type}
        if module_type == 'flip-flop':
            modules[name]['state'] = 'off'
        elif module_type == 'conjunction':
            modules[name]['memory'] = {}


def flip_flop(state, pulse):
    if pulse == 'HIGH':
        return state, None
    if state == 'off':
        return 'on', 'HIGH'
    return 'off', 'LOW'


def conjunction(memory):
    if 'LOW' in memory.values():
        return 'HIGH'
    return 'LOW'

# def conjunction(memory, pulse, source):
#     memory[source] = pulse
#     if all(m == 'HIGH' for m in memory.values()):
#         return 'LOW'
#         # return memory, 'LOW'
#     return 'HIGH'
#     # return memory, 'HIGH'


def push_button(modules, pulse_count, debug=False):
    # add the "button" pulse
    # pulses = {'LOW': 1,
    #           'HIGH': 0}
    pulse_count['LOW'] += 1
    modules_keys = modules.keys()
    queue = collections.deque([('broadcaster', 'LOW')])
    # rounds = 0
    while len(queue) > 0:
        current, pulse = queue.popleft()
        # rounds += 1
        for dest in modules[current]['dest']:
            pulse_count[pulse] += 1
            # if not modules.get(dest):
            if dest not in modules_keys:
                continue
            elif modules[dest]['type'] == 'flip-flop':
                modules[dest]['state'], dest_pulse = flip_flop(modules[dest]['state'], pulse)
                if dest_pulse:
                    queue.append((dest, dest_pulse))
            elif modules[dest]['type'] == 'conjunction':
                modules[dest]['memory'][current] = pulse
                #dest_pulse = conjunction(modules[dest]['memory'])
                dest_pulse = 'HIGH' if 'LOW' in modules[dest]['memory'].values() else 'LOW'
                queue.append((dest, dest_pulse))
            # print(current, '-'+pulse+'->', dest)
    return modules, pulse_count


# pre-warm conjunction memory
for name in modules.keys():
    for dest in modules[name]['dest']:
        if modules.get(dest) and modules[dest]['type'] == 'conjunction':
            modules[dest]['memory'][name] = 'LOW'

pulse_count = {'LOW': 0,
               'HIGH': 0}

for i in range(0, 1000):
    modules, pulse_count = push_button(modules, pulse_count)

LOW = pulse_count['LOW']
HIGH = pulse_count['HIGH']

print('LOW', LOW, 'HIGH', HIGH)
print(int(LOW*HIGH))
