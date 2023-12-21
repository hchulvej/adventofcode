import sys
from functools import reduce

input = open("2023_06_1.txt", 'r').read().split("\n")
times = [int(x) for x in input[0].split(" ")[1:] if len(x) > 0]
distances = [int(x) for x in input[1].split(" ")[1:] if len(x) > 0]

def dist(hold, time):
    if hold == 0 or hold >= time:
        return 0
    speed = hold
    return speed * (time - hold)


no_ways_to_win = [len([h for h in range(1,times[k]) if dist(h,times[k]) > distances[k]]) for k in range(len(times))]

print("Part 1: " + str(reduce(lambda x, y: x * y, no_ways_to_win)))

def new_number(arr_of_ints):
    return int("".join([str(x) for x in arr_of_ints]))

nT = new_number(times)
nD = new_number(distances)

no_ways_to_win2 = len([h for h in range(1,nT) if dist(h,nT) > nD])

print("Part 2: " + str(no_ways_to_win2))