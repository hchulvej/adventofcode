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
    return not ((min_x - 1 < t[0] < max_x + 1) and (min_y - 1 < t[1] < max_y + 1) and (min_z - 1 < t[2] < max_z + 1))

def neighbours(t):
    deltas = [(1,0,0), (-1,0,0), (0,1,0), (0,-1, 0), (0,0,1), (0,0,-1)]
    return set([(t[0] + delta[0], t[1] + delta[1], t[2] + delta[2]) for delta in deltas if not out_of_bounds(((t[0] + delta[0], t[1] + delta[1], t[2] + delta[2])))])


"""
    Part One
"""
def exposed_faces(t):
    return 6 - len([n for n in neighbours(t) if n in data])

print(sum([exposed_faces(t) for t in data]))