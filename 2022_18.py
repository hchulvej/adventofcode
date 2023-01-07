from collections import deque

"""
    Load and parse data
"""

with open('./2022_18.txt', "r", encoding="utf-8") as file:
    data = set()
    for line in file:
        data.add(tuple([int(x) for x in line.strip("\n").split(",")]))


"""
    Create the bounding box
"""
min_x: int = min([t[0] for t in data])
max_x: int = max([t[0] for t in data])
min_y: int = min([t[1] for t in data])
max_y: int = max([t[1] for t in data])
min_z: int = min([t[2] for t in data])
max_z: int = max([t[2] for t in data])

def out_of_bounds(t):
    return not ((min_x - 2 < t[0] < max_x + 2) and (min_y - 2 < t[1] < max_y + 2) and (min_z - 2 < t[2] < max_z + 2))

def neighbours(t):
    deltas = [(1,0,0), (-1,0,0), (0,1,0), (0,-1, 0), (0,0,1), (0,0,-1)]
    return set([(t[0] + delta[0], t[1] + delta[1], t[2] + delta[2]) for delta in deltas])


"""
    Part One
"""
def exposed_faces(t):
    return 6 - len([n for n in neighbours(t) if n in data])

print(sum([exposed_faces(t) for t in data]))


"""
    Part Two
"""
free_air = set()
trapped_air = set()
all_points = set()

def trapped(t):
    
    if t in trapped_air:
        return True
    
    if t in free_air:
        return False
    
    if t in data:
        return False
    
    queue = deque([t])
    
    visited = set()
    
    while queue:
        
        node = queue.popleft()
        
        if node not in visited:
            visited.add(node)
            for n in neighbours(node):
                if n not in data:
                    queue.append(n)
                    if out_of_bounds(n):
                        free_air.add(t)
                        return False
    
    trapped_air.add(t)
    return True

for x in range(min_x - 1, max_x + 2):
    for y in range(min_y - 1, max_y + 2):
        for z in range(min_z - 1, max_z + 2):
            all_points.add((x, y, z))
            trapped((x, y, z))


def exposed_faces_p2(t):
    return 6 - len([n for n in neighbours(t) if n in data.union(trapped_air)])

print(sum([exposed_faces_p2(t) for t in data]))                 