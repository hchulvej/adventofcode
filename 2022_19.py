import re
from dataclasses import dataclass

"""
    Load and parse data
"""

with open('./2022_19_small.txt', "r", encoding="utf-8") as file:
    data = list()
    for line in file:
        data.append(tuple([int(x) for x in re.findall(r'\d+', line)]))

"""
    Part One
"""

def blueprint(t) -> dict:
    return {'no': t[0], 'ore_robot_price': [t[1], 0, 0], 'clay_robot_price': [t[2], 0, 0], 'obsidian_robot_price': [t[3], t[4], 0], 'geode_robot_price': [t[5], 0, t[6]]}

@dataclass
class State:
    time_left: int
    ore_robots: int
    clay_robots: int
    obsidian_robots: int
    geode_robots: int
    ore_deposit: int
    clay_deposit: int
    obsidian_deposit: int
    geodes_opened: int
    
    def get_state(self):
        return dict(zip(['time_left', 'ore_robots', 'clay_robots', 'obsidian_robots', 'geode_robots', 'ore_deposit', 'clay_deposit', 'obsidian_deposit', 'geodes_opened'], [self.time_left, self.ore_robots, self.clay_robots, self.obsidian_robots, self.geode_robots, self.ore_deposit, self.clay_deposit, self.obsidian_deposit, self.geodes_opened]))

    def get_signature(self):
        return [self.time_left, self.ore_robots, self.clay_robots, self.obsidian_robots, self.geode_robots, self.ore_deposit, self.clay_deposit, self.obsidian_deposit, self.geodes_opened].join(".")

def move_on(state: State) -> State:
    old_state = state.get_state()
    old_state['time_left'] -= 1
    old_state['ore_deposit'] += old_state['ore_robots']
    old_state['clay_deposit'] += old_state['clay_robots']
    old_state['obsidian_deposit'] += old_state['obsidian_robots']
    old_state['geodes_opened'] += old_state['geode_robots']
    return State(*old_state.values())
    
def afford_robot(state: State, type: str, bp: tuple) -> bool:
    current_state = state.get_state()
    if type == 'ore':
        return all([current_state['ore_deposit'] >= blueprint(bp)['ore_robot_price'][0], current_state['clay_deposit'] >= blueprint(bp)['ore_robot_price'][1], current_state['obsidian_deposit'] >= blueprint(bp)['ore_robot_price'][2]])
    if type == 'clay':
        return all([current_state['ore_deposit'] >= blueprint(bp)['clay_robot_price'][0], current_state['clay_deposit'] >= blueprint(bp)['clay_robot_price'][1], current_state['obsidian_deposit'] >= blueprint(bp)['clay_robot_price'][2]])
    if type == 'obsidian':
        return all([current_state['ore_deposit'] >= blueprint(bp)['obsidian_robot_price'][0], current_state['clay_deposit'] >= blueprint(bp)['obsidian_robot_price'][1], current_state['obsidian_deposit'] >= blueprint(bp)['obsidian_robot_price'][2]])
    if type == 'geode':
        return all([current_state['ore_deposit'] >= blueprint(bp)['geode_robot_price'][0], current_state['clay_deposit'] >= blueprint(bp)['geode_robot_price'][1], current_state['obsidian_deposit'] >= blueprint(bp)['geode_robot_price'][2]])           

def buy_robot(state: State, type: str, bp: tuple) -> State:
    old_state = state.get_state()
    if type == 'ore':
        old_state['ore_robots'] += 1
        old_state['ore_deposit'] -= blueprint(bp)['ore_robot_price'][0] + 1 #because of move_on
        old_state['clay_deposit'] -= blueprint(bp)['ore_robot_price'][1]
        old_state['obsidian_deposit'] -= blueprint(bp)['ore_robot_price'][2]
        return State(*old_state.values())
    if type == 'clay':
        old_state['clay_robots'] += 1
        old_state['ore_deposit'] -= blueprint(bp)['clay_robot_price'][0]
        old_state['clay_deposit'] -= blueprint(bp)['clay_robot_price'][1] + 1 #because of move_on
        old_state['obsidian_deposit'] -= blueprint(bp)['clay_robot_price'][2]
        return State(*old_state.values())
    if type == 'obsidian':
        old_state['obsidian_robots'] += 1
        old_state['ore_deposit'] -= blueprint(bp)['obsidian_robot_price'][0]
        old_state['clay_deposit'] -= blueprint(bp)['obsidian_robot_price'][1]
        old_state['obsidian_deposit'] -= blueprint(bp)['obsidian_robot_price'][2] + 1 #because of move_on
        return State(*old_state.values())
    if type == 'geode':
        old_state['geode_robots'] += 1
        old_state['ore_deposit'] -= blueprint(bp)['geode_robot_price'][0]
        old_state['clay_deposit'] -= blueprint(bp)['geode_robot_price'][1]
        old_state['obsidian_deposit'] -= blueprint(bp)['geode_robot_price'][2]
        old_state['geodes_opened'] -= 1 #because of move_on
        return State(*old_state.values())

max_opened_geodes = 0

# DFS

cache = dict()
for bp in data:
    cache[bp] = dict()

def dfs(bp: tuple, state: State) -> int:
    
    if state.get_signature() in cache[bp]:
        return cache[bp][state.get_signature()]
    
    visited = set()
    
    stack = [state]
    
    while len(stack) > 0:
        
        starting_state = stack.pop()
        
        if starting_state.get_state()['time_left'] == 0:
            cache[bp][starting_state.get_signature()] = state.get_state()['geodes_opened']
            
        
        if starting_state.get_signature() not in visited:
            
            visited.add(starting_state.get_signature())
            
            if afford_robot(starting_state, 'ore', bp):
                b_ore = buy_robot(starting_state, 'ore', bp)
                b_ore = move_on(b_ore)
                stack.append(b_ore)
                