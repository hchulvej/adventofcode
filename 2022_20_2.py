

"""
    Load and parse data
"""

with open('./2022_20.txt', "r", encoding="utf-8") as file:
    data = list()
    for line in file:
        data.append(int(line.strip()))

FL = len(data)

indices = list(range(FL))
   
"""
    Part One: Mixing
"""

def elements(ind: list[int]) -> list[int]:
    return [data[i] for i in ind]

def move(orig_ind: int, l: list[int]) -> list[int]:
    steps = data[orig_ind] % (FL - 1)
    
    from_pos = l.index(orig_ind)
    l.pop(from_pos)
    to_pos = (from_pos + steps) % len(l)
    #print(orig_ind, data[orig_ind], l, to_pos)
    if to_pos == FL - 1:
        to_pos = 0
    if to_pos == 0:
        to_pos = FL - 1
    l.insert(to_pos, orig_ind)
    
    return l


ex0 = [2, 1, -3, 3, -2, 0, 4]
ex1 = [1, -3, 2, 3, -2, 0, 4]
ex2 = [1, 2, 3, -2, -3, 0, 4]
ex3 = [1, 2, -2, -3, 0, 3, 4]
ex4 = [1, 2, -3, 0, 3, 4, -2]
ex5 = [1, 2, -3, 0, 3, 4, -2]
ex6 = [1, 2, -3, 4, 0, 3, -2]

if False:
    indices = move(0, indices)
    assert elements(indices) == ex0
    indices = move(1, indices)
    assert elements(indices) == ex1
    indices = move(2, indices)
    assert elements(indices) == ex2
    indices = move(3, indices)
    assert elements(indices) == ex3
    indices = move(4, indices)
    assert elements(indices) == ex4
    indices = move(5, indices)
    assert elements(indices) == ex5
    indices = move(6, indices)
    assert elements(indices) == ex6


if False: #part 1
# Mix
    for i in range(FL):
        indices = move(i, indices)
        

    elems = elements(indices)


    z_index = elems.index(0)
    sum_val = 0
    for _ in range(3):
        z_index += 1000
        z_index = z_index % FL
        
        sum_val += elems[z_index]

    print(sum_val)
    
if True: #part 2
    
    data = [811589153 * d for d in data]
    
    for _ in range(10):
        for i in range(FL):
            indices = move(i, indices)
    
    elems = elements(indices)


    z_index = elems.index(0)
    sum_val = 0
    for _ in range(3):
        z_index += 1000
        z_index = z_index % FL
        
        sum_val += elems[z_index]

    print(sum_val)