import re

"""
    Load and parse data
"""

with open('./2022_20_small.txt', "r", encoding="utf-8") as file:
    data = list()
    for line in file:
        data.append(int(line.strip()))

FILE_LENGTH = len(data)

"""
    Part One: Mixing
"""

positions = dict(zip(range(FILE_LENGTH), [[data[i]] for i in range(FILE_LENGTH)]))

print(positions)