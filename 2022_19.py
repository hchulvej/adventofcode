import re
from collections import deque
import math

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
def max_spending(t: tuple[int]) -> list[int]:
    res = list([0, 0, 0]) # ore, clay, obsidian
    res[0] = max(t[1], t[2], t[3], t[5])
    res[1] = t[4]
    res[2] = t[6]
    return res




def solve(time_left: int, deposit: list[int], robots: list[int], bp: tuple[int]) -> int:
    
    
    # 0: ore, 1: clay, 2: obsidian
    max_ore, max_clay, max_obs = max_spending(bp)
    ore_cost_r_ore, ore_cost_r_clay, ore_cost_r_obs, clay_cost_r_obs, ore_cost_r_geo, obs_cost_r_geo = bp[1:]
    
    
    # Optimizations:
    # 1: never have more robots than given in max spending
    # 2: if you can produce a geode robot, do so every round
    # 3: avoid creation of excess ressources
    
    # deposit: 0 ore, 1 clay, 2 obsidian, 3 geodes
    # robots: 0 ore, 1 clay, 2 obsidian, 3 geode
    
    staring_state = (time_left, *deposit, *robots)
    print(staring_state)
    print(max_ore, max_clay, max_obs)
    queue = deque([staring_state])
    
    seen_states = set()
    
    max_geodes = 0
    
    while queue:
        
        state = queue.popleft()
        time, d_ore, d_clay, d_obs, d_geo, r_ore, r_clay, r_obs, r_geo = state
        
        if d_geo > max_geodes:
            max_geodes = d_geo
        
        if time == 0:
            continue
        
         
        # Trimming the inventory
        # Void robots that you don't need
        r_ore = min(r_ore, max_ore)
        r_clay = min(r_clay, max_clay)
        r_obs = min(r_obs, max_obs)
        # Void ressources that you can never spend
        if max_ore * time - r_ore * (time - 1) <= d_ore:
            d_ore = max_ore * time - r_ore * (time - 1)
        if max_clay * time - r_clay * (time - 1) <= d_clay:
            d_clay = max_clay * time - r_clay * (time - 1)
        if max_obs * time - r_obs * (time - 1) <= d_obs:
            d_obs =max_obs * time - r_obs * (time - 1)
        
        
        
        if (time, d_ore, d_clay, d_obs, d_geo, r_ore, r_clay, r_obs, r_geo) in seen_states:
            continue
        
        seen_states.add((time, d_ore, d_clay, d_obs, d_geo, r_ore, r_clay, r_obs, r_geo))
        
        #if len(seen_states) % 100000 == 0:
        #    print(f"({time}, {d_ore}, {d_clay}, {d_obs}, {d_geo}, {r_ore}, {r_clay}, {r_obs}, {r_geo})")
        
        
        assert d_ore >=0 and d_clay >= 0 and d_obs >= 0 and d_geo >= 0, f"({time}, {d_ore}, {d_clay}, {d_obs}, {d_geo}, {r_ore}, {r_clay}, {r_obs}, {r_geo})"
        
                   
        # Option 1: do not build robots
        queue.append((time - 1, d_ore + r_ore, d_clay + r_clay, d_clay + r_clay, d_geo + r_geo, r_ore, r_clay, r_obs, r_geo))
        
        # Option 2: build an ore robot
        if ore_cost_r_ore <= d_ore:
            queue.append((time - 1, d_ore + r_ore - ore_cost_r_ore, d_clay + r_clay, d_obs + r_obs, d_geo + r_geo, r_ore + 1, r_clay, r_obs, r_geo))
            #print("Build ore robot", d_ore, r_ore, bp, ms)
        
        # Option 3: build a clay robot
        if ore_cost_r_clay <= d_ore:
            queue.append((time - 1, d_ore + r_ore - ore_cost_r_clay, d_clay + r_clay, d_obs + r_obs, d_geo + r_geo, r_ore, r_clay + 1, r_obs, r_geo))
            #print("Build clay robot")
            
        # Option 4: build an obsidian robot
        if ore_cost_r_obs <= d_ore and clay_cost_r_obs <= d_clay:
            queue.append((time - 1, d_ore + r_ore - ore_cost_r_obs, d_clay + r_clay - clay_cost_r_obs, d_obs + r_obs, d_geo + r_geo, r_ore, r_clay, r_obs + 1, r_geo))
            #print("Build obsidian robot")
        
        if ore_cost_r_geo <= d_ore and obs_cost_r_geo <= d_obs:
            queue.append((time - 1, d_ore + r_ore - ore_cost_r_geo, d_clay + r_clay, d_obs + r_obs - obs_cost_r_geo, d_geo + r_geo, r_ore, r_clay, r_obs, r_geo + 1))
    
    
            
    return max_geodes

def solvejp(Co, Cc, Co1, Co2, Cg1, Cg2, T):
    best = 0
    # state is (ore, clay, obsidian, geodes, r1, r2, r3, r4, time)
    S = (0, 0, 0, 0, 1, 0, 0, 0, T)
    Q = deque([S])
    SEEN = set()
    while Q:
        state = Q.popleft()
        #print(state)
        o,c,ob,g,r1,r2,r3,r4,t = state

        best = max(best, g)
        if t==0:
            continue

        Core = max([Co, Cc, Co1, Cg1])
        if r1>=Core:
            r1 = Core
        if r2>=Co2:
            r2 = Co2
        if r3>=Cg2:
            r3 = Cg2
        if o >= t*Core-r1*(t-1):
            o = t*Core-r1*(t-1)
        if c>=t*Co2-r2*(t-1):
            c = t*Co2 - r2*(t-1)
        if ob>=t*Cg2-r3*(t-1):
            ob = t*Cg2-r3*(t-1)

        state = (o,c,ob,g,r1,r2,r3,r4,t)

        if state in SEEN:
            continue
        SEEN.add(state)

        if len(SEEN) % 1000000 == 0:
            print(t,best,len(SEEN))
        assert o>=0 and c>=0 and ob>=0 and g>=0, state
        Q.append((o+r1,c+r2,ob+r3,g+r4,r1,r2,r3,r4,t-1))
        if o>=Co: # buy ore
            Q.append((o-Co+r1, c+r2, ob+r3, g+r4, r1+1,r2,r3,r4,t-1))
        if o>=Cc:
            Q.append((o-Cc+r1, c+r2, ob+r3, g+r4, r1,r2+1,r3,r4,t-1))
        if o>=Co1 and c>=Co2:
            Q.append((o-Co1+r1, c-Co2+r2, ob+r3, g+r4, r1,r2,r3+1,r4,t-1))
        if o>=Cg1 and ob>=Cg2:
            Q.append((o-Cg1+r1, c+r2, ob-Cg2+r3, g+r4, r1,r2,r3,r4+1,t-1))
    return best

if False:
    quality_level = 0
    for t in data:
        quality_level += dfs(24,[0,0,0,0],[1,0,0,0],t) * t[0]   

    print(quality_level)


print(solve(24,[0,0,0,0],[1,0,0,0],data[0]))
print(solvejp(*data[0][1:], 24))