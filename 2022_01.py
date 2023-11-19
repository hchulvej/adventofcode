import heapq
from functools import reduce

input = []

with open('2022_01.txt', 'r') as f:
    for l in f.readlines():
        input.append((l.replace('\n', '')))

pq = []
sum = 0

for i in range(len(input)):
    if len(input[i]) > 0:
        sum = sum + int(input[i])
    else:
        pq.append(sum)
        sum = 0

heapq.heapify(pq)
top_three = heapq.nlargest(3, pq)
print(top_three[0])
print(reduce(lambda x, y: x + y, top_three, 0))