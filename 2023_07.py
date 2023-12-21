import sys
input = open("2023_07_test.in").read().splitlines()

values = list("AKQJT98765432")

def score(card):
    first_card = card[0]
    print(values.index(first_card))
    scorecard = dict(zip(values, [0]*len(values)))
    for c in list(card):
        scorecard[c] += 1
    
    scores = [scorecard[c] for c in scorecard.keys() if scorecard[c] > 0]
    scores.sort(reverse=True)
    scores = "".join(list(map(str, scores)))
    
    # Five of a kind
    if scores == "5":
        return (7, values.index(first_card))
    # Four of a kind
    if scores == "41":
        return (6, values.index(first_card))
    # Full house
    if scores == "32":
        return (5, values.index(first_card))
    # Three of a kind
    if scores == "311":
        return (4, values.index(first_card))
    # Two pairs
    if scores == "221":
        return (3, values.index(first_card))
    # One pair
    if scores == "2111":
        return (2, values.index(first_card))
    # High card
    if scores == "11111":
        return (1, values.index(first_card))
    

cards = dict()
for line in input:
    pair = line.split(" ")
    cards[pair[0]] = int(pair[1])

print(cards)