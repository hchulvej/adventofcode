import numpy as np

def read_input(input_file):
    with open(input_file) as f:
        lines = [list(line.strip()) for line in f.readlines()]
    return lines

raw_input = read_input("2024_06_2.txt")
data = np.array(raw_input, dtype=str)

# Part One

def guard_initial_position(data):
    if np.any(data == '^'):
        return (tuple(zip(np.where(data == '^')[0], np.where(data == '^')[1]))[0], "u")
    if np.any(data == 'v'):
        return (tuple(zip(np.where(data == 'v')[0], np.where(data == '^')[1]))[0], "d")
    if np.any(data == '<'):
        return (tuple(zip(np.where(data == '<')[0], np.where(data == '^')[1]))[0], "l")
    if np.any(data == '>'):
        return (tuple(zip(np.where(data == '>')[0], np.where(data == '^')[1]))[0], "r")

guard = [guard_initial_position(data)]

boundaries = (0, 0, data.shape[0] - 1, data.shape[1] - 1)

obstacles = [(x, y) for x, y in zip(np.where(data == '#')[0], np.where(data == '#')[1])]

print(guard, boundaries)