import numpy as np

def read_input(input_file):
    with open(input_file) as f:
        lines = [list(map(int, line.split(" "))) for line in f.readlines()]
    return lines

raw_input = np.array(read_input("2024_11_2.txt")[0])

arrangement = raw_input

def split_stone(arr, index):
    val = str(arr[index])
    left, right = int(val[:len(val)//2 + 1]), int(val[(len(val) // 2 + 1):])
    return [left, right]

def blink(arr):
    # Todo: Make new result array and return it
    pass
                

print(arrangement)
arrangement = blink(arrangement)
print(arrangement)