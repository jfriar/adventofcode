#!/usr/bin/env python3

input_file = 'day03_input.txt'
#input_file = 'day03_sample.txt'

joltages = []
with open(input_file) as f:
    for line in f.readlines():
        line = line.strip()
        joltage_list = sorted(list(map(int, line)), reverse=True)
        max1 = joltage_list[0]
        #max2 = joltage_list[1]
        if line.index(str(max1)) < len(line)-1:
            use_max = max1
            #use_max = joltage_list[0]
        else:
            #use_max = max2
            use_max = joltage_list[1]
        max_index = line.index(str(use_max))
        max_remainder = max(list(map(int, line[max_index+1:])))
        max_joltage = str(use_max) + str(max_remainder)
        joltages.append(int(max_joltage))
        #print(line, max_joltage)

#print(joltages)
print(sum(joltages))
