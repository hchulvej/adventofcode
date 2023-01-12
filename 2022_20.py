import math

"""
    Load and parse data
"""

with open('./2022_20.txt', "r", encoding="utf-8") as file:
    data = list()
    for line in file:
        data.append(int(line.strip()))

FILE_LENGTH = len(data)

"""
    Part One: Mixing
"""

def move(element: int, l: list[int]) -> list[str]:
    if element == 0:
        return l
       
    if element > 0:
        ind_e = l.index(element)
        ind_n = (ind_e + abs(element)) % (FILE_LENGTH - 1)
        l.remove(element)
        l.insert(ind_n, element)
    if element < 0:
        l.reverse()
        ind_e = l.index(element)
        ind_n = (ind_e - element) % (FILE_LENGTH - 1)
        l.remove(element)
        l.insert(ind_n, element)
        l.reverse()
        
    return l

l = data.copy()
for element in data:
    l = move(element, l)
    
ind_0 = l.index(0)
ind_1 = (ind_0 + 1000) % (FILE_LENGTH)
ind_2 = (ind_0 + 2000) % (FILE_LENGTH)
ind_3 = (ind_0 + 3000) % (FILE_LENGTH)
print(l[ind_1] + l[ind_2] + l[ind_3])