

"""
    Load and parse data
"""

with open('./2022_20_small.txt', "r", encoding="utf-8") as file:
    data = list()
    for line in file:
        data.append(int(line.strip()))

FL = len(data)

elements = list(zip(range(FL), data))
   
"""
    Part One: Mixing
"""

def move(orig_index: int, l: list[tuple]) -> list[tuple]:
    val = data[orig_index]
    
    if val == 0:
        return l
    
    curr_index = l.index((orig_index, val))
    new_index = (curr_index + val) % (FL - 1)
    
    if val > 0:
        if new_index < FL - 2:
            l.insert(new_index + 1, (orig_index, val))
            if new_index <= curr_index:
                l.pop(curr_index + 1)
            else:
                l.pop(curr_index)
        if new_index == FL - 2:
            l.pop(curr_index)
            l.insert(0, (orig_index, val))
        if new_index == FL - 1:
            l.pop(curr_index)
            l.insert(1, (orig_index, val))
    
    if val < 0:
        if new_index > 1:
            l.insert(new_index - 1, (orig_index, val))
            l.pop(curr_index)
        if new_index == 1:
            l.pop(curr_index)
            l.append((orig_index, val))
        if new_index == 0:
            l.pop(curr_index)
            l.insert(FL - 2, (orig_index, val))
    
    return l

l = elements.copy()
print(l)
for i in range(FL):
    l = move(i, l)
    print(l)
    