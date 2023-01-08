import re

"""
    Load and parse data
"""

with open('./2022_19_small.txt', "r", encoding="utf-8") as file:
    data = list()
    for line in file:
        data.append(tuple([int(x) for x in re.findall(r'\d+', line)]))

print(data)