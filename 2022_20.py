

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
    steps = data[orig_ind]

    if steps == 0:
        return l

    right = True
    if steps < 0:
        steps = -steps
        right = False
    
    steps = steps % (FL - 1)
        
    if right:
        to_overtake = (l.index(orig_ind) + steps) % FL
        if to_overtake == FL - 1:
            l.remove(orig_ind)
            l.insert(0, orig_ind)
        else:
            left_part = l[:to_overtake + 1]
            right_part = l[to_overtake + 1:]
            #print(left_part, right_part)
            if orig_ind in left_part:
                left_part.remove(orig_ind)
                left_part.append(orig_ind)
                #print(left_part, right_part)
            else:
                right_part.remove(orig_ind)
                left_part.append(orig_ind)
            left_part.extend(right_part)
            l = left_part
        return l
    else:
        l.reverse()
        to_overtake = (l.index(orig_ind) + steps) % FL
        if to_overtake == FL - 1:
            l.remove(orig_ind)
            l.insert(0, orig_ind)
        else:
            left_part = l[:to_overtake + 1]
            right_part = l[to_overtake + 1:]
            if orig_ind in left_part:
                left_part.remove(orig_ind)
                left_part.append(orig_ind)
            else:
                right_part.remove(orig_ind)
                left_part.append(orig_ind)
                left_part.extend(right_part)
                l = left_part
        l.reverse()
        return l


# Mix
for i in range(FL):
    indices = move(i, indices)

elems = elements(indices)
print(elems)


z_index = elems.index(0)
sum_val = 0
for _ in range(3):
    z_index += 1000
    z_index = z_index % FL
    print(elems[z_index])
    sum_val += elems[z_index]

print(sum_val)