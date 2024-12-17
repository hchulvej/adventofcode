import numpy as np
from functools import lru_cache
from math import log10

def read_input(input_file):
    with open(input_file) as f:
        lines = [list(map(int, line.split(" "))) for line in f.readlines()]
    return lines

raw_input = np.array(read_input("2024_11_1.txt")[0])

arrangement = [0, 7, 6618216, 26481, 885, 42, 202642, 8791]

def blink(n):
    res = []
    if n == 0:
        res.append(1)
    elif len(str(n)) % 2 == 0:
        left, right = int(str(n)[:len(str(n)) // 2]), int(str(n)[len(str(n)) // 2:])
        res.append(left)
        res.append(right)
    else:
        res.append(n * 2024)
    return res
                
memo_five = dict()

def blink_five_times(arr):
    res = []
    for n in arr:
        if n in memo_five:
            res.extend(memo_five[n])
        else:
            t_aar = [n]
            for _ in range(5):
                tmp = []
                for i in t_aar:
                    tmp.extend(blink(i))
                t_aar = tmp
            memo_five[n] = t_aar
            res.extend(t_aar)
    return res


# Not my idea, but it works

@lru_cache(None)
def calc(n, blinks=25):
	if blinks == 0:
		return 1

	if n == 0:
		return calc(1, blinks - 1)

	n_digits = int(log10(n)) + 1
	if n_digits % 2 == 0:
		power = 10**(n_digits // 2)
		return calc(n // power, blinks - 1) + calc(n % power, blinks - 1)

	return calc(n * 2024, blinks - 1)

print(sum(calc(n) for n in arrangement))
print(sum(calc(n, blinks=75) for n in arrangement))