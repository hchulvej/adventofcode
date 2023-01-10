import re
from collections import deque
from functools import cache

"""
    Load and parse data
"""

with open('./2022_19.txt', "r", encoding="utf-8") as file:
    data = list()
    for line in file:
        data.append(tuple([int(x) for x in re.findall(r'\d+', line)]))

if True:
    for t in data:
        print(t)

"""
    Part One
    
    data: [1, 4, 2, 3, 14, 2, 7]
    - blueprint number 0
    - ore cost of ore robot 1
    - ore cost of clay robot 2
    - ore cost of obsidian robot 3
    - clay cost of obsidian robot 4
    - ore cost of geode robot 5
    - obsidian cost of geode robot 6
    
"""
# You can at most build one robot per minute,
# so there is a cap on possible spending
# This also means that there is no need to build more
# robots of each type than the max spending, since
# each robot mines 1 ressource per minute
def max_spending(t: list[int]) -> list[int]:
    res = list([0, 0, 0]) # ore, clay, obsidian
    res[0] = max(t[1], t[2], t[3], t[5])
    res[1] = t[4]
    res[2] = t[6]
    return res




def dfs(time_left: int, deposit: list[int], robots: list[int], bp: tuple[int]) -> int:
    
    # 0: ore, 1: clay, 2: obsidian
    ms = max_spending(bp)
    
    # Optimizations:
    # 1: never have more robots than given in max spending
    # 2: if you can produce a geode robot, do so every round
    # 3: avoid creation of excess ressources
    
    # deposit: 0 ore, 1 clay, 2 obsidian, 3 geodes
    # robots: 0 ore, 1 clay, 2 obsidian, 3 geode
    
    queue = deque([tuple([time_left, *deposit, *robots])])
    
    seen_states = set()
    
    max_geodes = 0
    
    while queue:
        
        state = queue.popleft()
        time, d_ore, d_clay, d_obs, d_geo, r_ore, r_clay, r_obs, r_geo = state
        
        max_geodes = max(max_geodes, d_geo)
    
    
    

if False:
    quality_level = 0
    for t in data:
        quality_level += dfs(24,[0,0,0,0],[1,0,0,0],t) * t[0]   

    print(quality_level)


print(dfs(32,[0,0,0,0],[1,0,0,0],data[0]))