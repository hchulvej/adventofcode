import sys
from collections import Counter
input = open("2023_07_1.in").read().splitlines()
values = list("23456789TJQKA")

def base_value(hand):
    return -sum([values.index(hand[i]) * 13**(4 - i) for i in range(5)])

def hand_type(hand):
    signature = sorted(Counter(hand).values(), reverse=True)
    # 5 of a kind
    if signature[0] == 5:
        return 1
    # 4 of a kind
    if signature[0] == 4:
        return 2
    # Full house
    if len(signature) > 1 and signature[0] == 3 and signature[1] == 2:
        return 3
    # 3 of a kind
    if len(signature) > 1 and signature[0] == 3 and signature[1] == 1:
        return 4
    # 2 pairs
    if len(signature) > 1 and signature[0] == 2 and signature[1] == 2:
        return 5
    # 1 pair
    if len(signature) > 1 and signature[0] == 2 and signature[1] == 1:
        return 6
    else:
        return 7

hands = dict()

for line in input:
    pair = line.split(" ")
    hands[pair[0]] = int(pair[1])

s_hands = sorted(hands.keys(), key=base_value)
s_hands = sorted(s_hands, key=hand_type)

no_hands = len(s_hands)
print("Part 1: " + str(sum([(no_hands - i) * hands[s_hands[i]] for i in range(no_hands)])))


# Part 2
values = list("J23456789TQKA")

def hand_type_p2(hand: str):
    possible_hands = set([hand])
    for c in [hand[i] for i in range(5) if hand[i] != "J"]:
        possible_hands.add(hand.replace("J", c, -1))
    return min([hand_type(h) for h in possible_hands])


s_hands = sorted(hands.keys(), key=base_value)
s_hands = sorted(s_hands, key=hand_type_p2)

no_hands = len(s_hands)
print("Part 2: " + str(sum([(no_hands - i) * hands[s_hands[i]] for i in range(no_hands)])))