import re
from collections import deque
from functools import cache

"""
    Load and parse data
"""

with open('./2022_19_small.txt', "r", encoding="utf-8") as file:
    data = list()
    for line in file:
        data.append(tuple([int(x) for x in re.findall(r'\d+', line)]))

if False:
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
        
        if time == 0:
            continue
        
        max_geodes = max(max_geodes, d_geo)
    
        if tuple([time, d_ore, d_clay, d_obs, d_geo, r_ore, r_clay, r_obs, r_geo]) in seen_states:
            continue
        
        # Trimming the deposits
        # Void ressources that you can never spend
        if r_ore * time + d_ore > ms[0] * time:
            d_ore = ms[0] * time - r_ore * time
        if r_clay * time + d_clay > ms[1] * time:
            d_clay = ms[1] * time - r_clay * time
        if r_obs * time + d_obs > ms[2] * time:
            d_obs = ms[2] * time - r_obs * time
        
        seen_states.add(tuple([time, d_ore, d_clay, d_obs, d_geo, r_ore, r_clay, r_obs, r_geo]))
        #print(time, d_ore, d_clay, d_obs, d_geo, r_ore, r_clay, r_obs, r_geo)
        
        # Option 1: do not build robots
        queue.append(tuple([time - 1, d_ore + r_ore, d_clay + r_clay, d_obs + r_obs, d_geo + r_geo, r_ore, r_clay, r_obs, r_geo]))
        
        # If you can afford a geode robot, build it
        enough_robots = r_ore >= bp[5] and r_obs >= bp[6]
        if enough_robots:
            queue.append(tuple([time - 1, 0, 0, 0, d_geo + r_geo, 0, 0, 0, r_geo + 1]))
            print("Build geode robot")
        
        # Option 2: build an ore robot
        if bp[1] <= d_ore and r_ore < ms[0] and not enough_robots:
            queue.append(tuple([time - 1, d_ore + r_ore - bp[1], d_clay + r_clay, d_obs + r_obs, d_geo + r_geo, r_ore + 1, r_clay, r_obs, r_geo]))
            print("Build ore robot", r_ore, bp, ms)
        
        # Option 3: build a clay robot
        if bp[2] <= d_clay and r_clay < ms[1] and not enough_robots:
            queue.append(tuple([time - 1, d_ore + r_ore, d_clay + r_clay - bp[2], d_obs + r_obs, d_geo + r_geo, r_ore, r_clay + 1, r_obs, r_geo]))
            print("Build clay robot")
            
        # Option 4: build an obsidian robot
        if bp[3] <= d_ore and bp[4] <= d_clay and r_obs < ms[2] and not enough_robots:
            queue.append(tuple([time - 1, d_ore + r_ore - bp[3], d_clay + r_clay - bp[4], d_obs + r_obs, d_geo + r_geo, r_ore, r_clay, r_obs + 1, r_geo]))
            print("Build obsidian robot")
        
    return max_geodes

if False:
    quality_level = 0
    for t in data:
        quality_level += dfs(24,[0,0,0,0],[1,0,0,0],t) * t[0]   

    print(quality_level)


print(dfs(24,[0,0,0,0],[1,0,0,0],data[0]))