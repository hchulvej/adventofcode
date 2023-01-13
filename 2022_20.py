

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

def move_pos(ind: int, mvs: int, l: list[tuple]) -> list[tuple]:
    
    def move_left(from_ind: int, lst: list[tuple]) -> list[tuple]:
        if from_ind > 1:
            lst = lst.insert(from_ind - 1, lst.pop(from_ind))
        if from_ind == 1:
            lst = lst.append(lst.pop(1))
        if from_ind == 0:
            lst = lst.insert(FL-1, lst.pop(0))
        return lst
    
    def move_right(from_ind: int, lst: list[tuple]) -> list[tuple]:
        if from_ind < FL - 2:
            lst = lst.insert(from_ind + 1, lst.pop(from_ind))
        if from_ind == FL - 2:
            lst = lst.insert(0, lst.pop(1))
        if from_ind == FL - 1:
            lst = lst.insert(1, lst.pop(FL - 1))
        return lst
    
    if mvs > 0:
        for i in range(mvs):
            l = move_right((ind + i) % FL, l)
        return l
    if mvs < 0:
        for i in range(mvs):
            l = move_left((ind - i) % FL, l)
        return l
    return l
        

def move(orig_index: int, l: list[tuple]) -> list[tuple]:
    val = data[orig_index]
    
    if val == 0:
        return l
    
    curr_index = l.index((orig_index, val))
    new_index = (curr_index + val) % (FL - 1)
    
    if curr_index == new_index:
        return l
    if curr_index < new_index:
        e = l.pop(curr_index)
        l.insert(new_index, e)
        return l
    if curr_index > new_index:
        e = l.pop(curr_index)
        l.insert(new_index + 1, e)
        return l
    
    
l = elements.copy()
print(l)
for i in range(FL):
    l = move(i, l)
    print(l)
    