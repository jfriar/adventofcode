#!/usr/bin/env python3
import collections
import functools

input_file = 'day7_input.txt'
#input_file = 'day7_test.txt'

card_values = {str(c): c-2 for c in range(2, 10)}
card_values.update({'T': 8, 'J': 9, 'Q': 10, 'K': 11, 'A': 12})


def camel_card_hand_compare(item1, item2):
    # hand = [cards, bid]
    for i, val1 in enumerate(item1[0]):
        val2 = item2[0][i]
        if card_values[val1] > card_values[val2]:
            return 1
        elif card_values[val1] < card_values[val2]:
            return -1
    return 0


def group_by_hand_type(hands):
    # python 3.7+ dicts preserve order.
    # hand_types = {1: [], 2:{} ... 6: []}
    hand_types = {r: [] for r in range(0, 7)}
    for hand in data:
        cards, bid = hand.split(' ', 1)
        c = collections.Counter(cards)
        strength = max(c.values())
        # 5 and 4 of a kind can't have multiple pairs
        # 1 of a kind can't have multiple pairs
        # print(cards)
        msg = cards
        if strength == 5:
            t = 6
            msg += ' five of a kind'
        elif strength == 4:
            t = 5
            msg += ' four of a kind'
        elif strength == 3:
            if 2 in c.values():
                t = 4
                msg += ' full house'
            else:
                t = 3
                msg += ' three of a kind'
        elif strength == 2:
            _c = collections.Counter(c.values())
            if _c[2] >= 2:
                t = 2
                msg += ' two pair'
            else:
                t = 1
                msg += ' one pair'
        else:
            t = 0
        # print(msg)

        hand_types[t].append([cards, bid])
    return hand_types


with open(input_file) as f:
    data = [x.strip() for x in f.readlines()]

rank = 1
winnings = []
hand_types = group_by_hand_type(data)
for hand_type, hands in hand_types.items():
    for hand in sorted(hands, key=functools.cmp_to_key(camel_card_hand_compare)):
        _winnings = int(hand[1]) * rank
        # print(' ', rank, hand, '_winnings:', _winnings)
        rank += 1
        winnings.append(_winnings)

print('total winnings:', sum(winnings))
print('total winnings:', 249390788)
