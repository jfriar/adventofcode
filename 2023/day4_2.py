#!/usr/bin/env python3
import collections
import re

input_file = 'day4_input.txt'

def get_card_wins(card):
    card_split = card.split(': ', 1)
    card_meta = card_split[0]
    card_data = card_split[1].split(' | ')
    winners = re.findall(r"\d+", card_data[0])
    my_cards = re.findall(r"\d+", card_data[1])
    my_winners = [int(c) for c in my_cards if c in winners]
    return len(my_winners)


with open(input_file) as f:
    cards = [x.strip() for x in f.readlines()]

    total_cards = collections.Counter()
    for i, card in enumerate(cards):
        total_cards.update([card])
        card_wins = get_card_wins(card)
        # print('card_points:', card_points)
        if card_wins > 0:
            for next_card in range(i+1, i+1+card_wins):
                total_cards.update([cards[next_card]]*total_cards[card])

    print(sum(total_cards.values()))
    #print(sum([num for card, num in total_cards.items()]))

