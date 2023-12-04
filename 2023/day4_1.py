#!/usr/bin/env python3
import re

input_file = 'day4_input.txt'

with open(input_file) as f:
    cards = [x.strip() for x in f.readlines()]

def solve(data):
    points = 0
    for card in cards:
        card_split = card.split(': ', 1)
        card_meta = card_split[0]
        card_data = card_split[1].split(' | ')
        winners = re.findall(r"\d+", card_data[0])
        my_cards = re.findall(r"\d+", card_data[1])
        my_winners = [int(c) for c in my_cards if c in winners]
        # print(winners, my_cards, my_winners)
        points += 2**(len(my_winners)-1) if len(my_winners) > 0 else 0
        #print(' ', len(my_winners), ' | ', points)
    return points


print(solve(cards))
