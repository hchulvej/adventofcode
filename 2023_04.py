input = []

with open('2023_04_1.txt', 'r') as f:
    for l in f.readlines():
        input.append(l.replace('\n', ''))


cards = []
winning_no = []

for line in input:
    left, right = line.split('|')
    left = left.split(":")[1].strip()
    right = right.strip()
    left = [int(n) for n in left.split(" ") if len(n) > 0]
    right = [int(n) for n in right.split(" ") if len(n) > 0]
    cards.append(right)
    winning_no.append(left)
    

def score(card, list_of_winning_numbers, part=1):
    winner = False
    if part == 1:
        res = 0.5
    else:
        res = 0
    for n in card:
        if n in list_of_winning_numbers:
            winner = True
            if part == 1:
                res *= 2
            else:
                res += 1
    if winner:
        return int(res)
    else:
        return 0    

part1 = 0

winning_cards = dict()

for i, win_no in enumerate(winning_no):
    sc1 = score(win_no, cards[i])
    sc2 = score(win_no, cards[i], 2)
    part1 += sc1
    if sc2 > 0:
        winning_cards[i] = sc2

print("Part 1: " + str(part1) + "\n")

scratchcards = [1]*len(cards)

for c in range(len(cards)):
    if c in winning_cards:
        for n in range(scratchcards[c]):
            for m in range(winning_cards[c]):
                scratchcards[c + m + 1] += 1

print("Part 2: " + str(sum(scratchcards)))
    
