import numpy as np

def read_input(input_file):
    with open(input_file) as f:
        lines = [list(map(int, line.split(" "))) for line in f.readlines()]
    return lines

raw_input = np.array(read_input("2024_11_1.txt")[0])

arrangement = [0, 7, 6618216, 26481, 885, 42, 202642, 8791]

def blink(arr):
    res = []
    for val in arr:
        if val == 0:
            res.append(1)
        elif len(str(val)) % 2 == 0:
            s_val = str(val)
            s_left = s_val[:len(s_val)//2]
            s_right = s_val[(len(s_val) // 2):]
            left = int(s_left)
            right = int(s_right)
            if left < 0 or right < 0:
                print(s_val)
            res += [left, right]
        else:
            res.append(val * 2024)
    return res
                

t_aar = [0]
for _ in range(75):
    t_aar = blink(t_aar)
    #print(len(arrangement))
print(len(t_aar))
