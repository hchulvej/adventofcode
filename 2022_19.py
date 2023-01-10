import re
from collections import deque

"""
    Load and parse data
"""

with open('./2022_19.txt', "r", encoding="utf-8") as file:
    data = list()
    for line in file:
        data.append(tuple([int(x) for x in re.findall(r'\d+', line)]))

"""
    Part One
    
    data: (1, 4, 2, 3, 14, 2, 7)
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
def max_spending(t: tuple) -> list[int]:
    res = list([0, 0, 0]) # ore, clay, obsidian
    res[0] = max(t[1], t[2], t[3], t[5])
    res[1] = t[4]
    res[2] = t[6]
    return res



def dfs(time_left_i: int, deposit_i: tuple[int], robots_i: tuple[int], bp_i: tuple[int]) -> int:
    # deposit: 0 ore, 1 clay, 2 obsidian, 3 geodes
    # robots: 0 ore, 1 clay, 2 obsidian, 3 geode
    
    visited = set((time_left_i,deposit_i,robots_i,bp_i))
    
    queue = deque([(time_left_i,deposit_i,robots_i,bp_i)])
    
    # 0: ore, 1: clay, 2: obsidian
    ms = max_spending(bp_i)
    
    # Optimizations:
    # 1: never have more robots than given in max spending
    # 2: if you can produce a geode robot, do so every round
    # 3: avoid creation of excess ressources
    
    max_geodes = 0
    
    while queue:
        
        t = queue.popleft()
        #print(t)
        time_left = t[0]
        deposit = t[1]
        robots = t[2]
        bp = t[3] 
        
        if (time_left, deposit, robots, bp) in visited:
            continue
        
        visited.add((time_left, deposit, robots, bp))
        
        max_geodes = max(max_geodes, deposit[3])
        
        if time_left == 0:
            continue
        
        # Optimization 1
        # buy ore robot if possible and desirable
        if deposit[0] >= bp[1] and robots[0] < ms[0]:
            new_deposit = (deposit[0] + robots[0] - bp[1], deposit[1] + robots[1], deposit[2] + robots[2], deposit[3] + robots[3])
            new_robots = (robots[0] + 1, robots[1], robots[2], robots[3])
            queue.append((time_left - 1, new_deposit, new_robots, bp))
            #print(t)
        
        # buy clay robot if possible and desirable
        if deposit[0] >= bp[2] and robots[1] < ms[1]:
            new_deposit = (deposit[0] + robots[0] - bp[2], deposit[1] + robots[1], deposit[2] + robots[2], deposit[3] + robots[3])
            new_robots = (robots[0], robots[1] + 1, robots[2], robots[3])
            queue.append((time_left - 1, new_deposit, new_robots, bp))
            #print(t)
        
        # buy obisian robot if possible and desirable
        if deposit[0] >= bp[3] and deposit[1] >= bp[4] and robots[2] < ms[2]:
            new_deposit = (deposit[0] + robots[0] - bp[3], deposit[1] + robots[1] - bp[4], deposit[2] + robots[2], deposit[3] + robots[3])
            new_robots = (robots[0], robots[1], robots[2] + 1, robots[3])
            queue.append((time_left - 1, new_deposit, new_robots, bp))
            #print(t)
        
        # buy geode robot if possible
        if deposit[0] >= bp[5] and deposit[2] >= bp[6]:
            new_deposit = (deposit[0] + robots[0] - bp[5], deposit[1] + robots[1], deposit[2] + robots[2] - bp[6], deposit[3] + robots[3])
            new_robots = (robots[0], robots[1], robots[2], robots[3] + 1)
            queue.append((time_left - 1, new_deposit, new_robots, bp))
            
        # do not build anything
        # Optimization 2
        # if there are bp[5] ore robots and bp[6] obsidian robots, a geode robot can be built every round
        if robots[0] + deposit[0] < bp[5] or robots[2] + deposit[2] < bp[6]:
            new_deposit = (deposit[0] + robots[0], deposit[1] + robots[1], deposit[2] + robots[2], deposit[3] + robots[3])
            queue.append((time_left - 1, new_deposit, robots, bp))
        
    return max_geodes    

if True:
    quality_level = 0
    for t in data:
        quality_level += dfs(24,(0,0,0,0),(1,0,0,0),t) * t[0]   

    print(quality_level)


#print(dfs(32,(0,0,0,0),(1,0,0,0),data[0]))