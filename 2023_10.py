from collections import deque

input = open("2023_10_1.in").read().splitlines()

start_node = (102,118)
input[102] = input[102].replace("S", "7") # Read from input
# start_node = (1,1)
# input[1] = input[1].replace("S", "F") # Read from input
max_rows_index = len(input) - 1
max_cols_index = len(input[0]) - 1

def get(i, j):
    return input[i][j]

def valid(i, j):
    return i >= 0 and i <= max_rows_index and j >= 0 and j <= max_cols_index

def add_dirs(i, j, dirs):
    res = set()
    if valid(i, j):
        if "N" in dirs and valid(i - 1, j):
            res.add((i - 1, j))
        if "E" in dirs and valid(i, j + 1):
            res.add((i, j + 1))
        if "S" in dirs and valid(i + 1, j):
            res.add((i + 1, j))
        if "W" in dirs and valid(i, j - 1):
            res.add((i, j - 1))
    return res

# Adjacent nodes from (i, j)
def adj(i, j):
    res = set()
    if valid(i, j):
        pipe = get(i, j)
        # North-south pipe
        if pipe == "|":
            res.update(add_dirs(i, j, ["N", "S"]))
        # East-west pipe
        if pipe == "-":
            res.update(add_dirs(i, j, ["E", "W"]))
        # North-east
        if pipe == "L":
            res.update(add_dirs(i, j, ["N", "E"]))
        # North-west
        if pipe == "J":
            res.update(add_dirs(i, j, ["N", "W"]))
        # South-west
        if pipe == "7":
            res.update(add_dirs(i, j, ["S", "W"]))
        # South-east
        if pipe == "F":
            res.update(add_dirs(i, j, ["S", "E"]))
    return res

pipe_system = set()

def BFS():
    
    Q = deque()
    Q.appendleft(start_node)
    visited = set()
    
    dist_to = dict()
    dist_to[start_node] = 0
    
    while len(Q) > 0:
        next_e = Q.pop()
        if not next_e in visited:
            visited.add(next_e)
            adjs = adj(*next_e)
            Q.extendleft(adjs)
            for e in adjs:
                if e in dist_to:
                    dist_to[e] = min(dist_to[e], dist_to[next_e] + 1)
                else:
                    dist_to[e] = dist_to[next_e] + 1
    
    pipe_system.update(visited)
    print("Part 1: ", max(dist_to.values()))

BFS()

def ray_count(ray: str):
    if len(ray) == 0:
        return 0
    return ray.count("|") + ray.count("L7") + ray.count("FJ")

# Ray casting algorithm
inside = 0

for r in range(len(input)):
    for c in range(len(input[0])):
        if True: #get(r, c) == ".":
            ray = "".join([get(r, cc) for cc in range(c, len(input)) if (r,cc) in pipe_system if get(r,cc) != "-"])
            ray.replace("LJ","**")
            ray.replace("F7","**")
            if (ray.count("|") + ray.count("*")) % 2 == 1:
                inside += 1
            

print(inside)