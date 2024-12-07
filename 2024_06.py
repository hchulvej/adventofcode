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
        return list(zip(np.where(data == '^')[0], np.where(data == '^')[1]))[0]
    if np.any(data == 'v'):
        return list(zip(np.where(data == 'v')[0], np.where(data == '^')[1]))[0]
    if np.any(data == '<'):
        return list(zip(np.where(data == '<')[0], np.where(data == '^')[1]))[0]
    if np.any(data == '>'):
        return list(zip(np.where(data == '>')[0], np.where(data == '^')[1]))[0]

guard = []

obstacles = [(x, y) for x, y in zip(np.where(data == '#')[0], np.where(data == '#')[1])]



print(list(zip(np.where(data == '^')[0], np.where(data == '^')[1]))[0])