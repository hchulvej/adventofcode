import re
from dataclasses import dataclass
from functools import cache

"""
    Load and parse data
"""

with open('./2022_19.txt', "r", encoding="utf-8") as file:
    data = list()
    for line in file:
        data.append(tuple([int(x) for x in re.findall(r'\d+', line)]))

"""
    Part One
"""

def blueprint(t) -> dict:
    return {'no': t[0], 'ore_robot_price': [t[1], 0, 0], 'clay_robot_price': [t[2], 0, 0], 'obsidian_robot_price': [t[3], t[4], 0], 'geode_robot_price': [t[5], 0, t[6]]}

@dataclass(unsafe_hash=True)
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
        return ".".join([str(e) for e in [self.time_left, self.ore_robots, self.clay_robots, self.obsidian_robots, self.geode_robots, self.ore_deposit, self.clay_deposit, self.obsidian_deposit, self.geodes_opened]])

# Hint from hyper-neutrino
def max_spending(t: tuple) -> tuple:
    bp = blueprint(t)
    keys = ['ore_robot_price', 'clay_robot_price', 'obsidian_robot_price', 'geode_robot_price']
    res = []
    for i in range(3):
        res.append(max([bp[key][i] for key in keys]))
    return res

def move_on(state: State, bp: tuple) -> State:
    ms = max_spending(bp)
    old_state = state.get_state()
    old_state['time_left'] -= 1
    old_state['ore_deposit'] = min(old_state['ore_deposit'] + old_state['ore_robots'], ms[0] * old_state['time_left'])
    old_state['clay_deposit'] = min(old_state['clay_deposit'] + old_state['clay_robots'], ms[1] * old_state['time_left'])
    old_state['obsidian_deposit'] = min(old_state['obsidian_deposit'] + old_state['obsidian_robots'], ms[2] * old_state['time_left'])
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

def combined_move(state: State, type: str, bp: tuple) -> State:
    if type == 'wait':
        return move_on(state, bp)
    if type == 'ore':
        if afford_robot(state, 'ore', bp):
            state = buy_robot(state, 'ore', bp)
        return move_on(state, bp)
    if type == 'clay':
        if afford_robot(state, 'clay', bp):
            state = buy_robot(state, 'clay', bp)
        return move_on(state, bp)
    if type == 'obsidian':
        if afford_robot(state, 'obsidian', bp):
            state = buy_robot(state, 'obsidian', bp)
        return move_on(state, bp)
    if type == 'geode':
        if afford_robot(state, 'geode', bp):
            state = buy_robot(state, 'geode', bp)
        return move_on(state, bp)  



"""
    Part One: DFS
"""
@cache
def dfs(state: State, bp: tuple) -> int:
    
    if state.get_state()['time_left'] == 0:
        return state.get_state()['geodes_opened']
    
    key = state.get_signature()
    
    # Worst case maxval: do nothing
    maxval = state.get_state()['geodes_opened'] + state.get_state()['time_left'] * state.get_state()['geode_robots']
    
    types = ['wait', 'ore', 'clay', 'obsidian', 'geode']
    
    new_states = [combined_move(state, type, bp) for type in types]
    
    maxval = max(maxval, max([dfs(new_state, bp) for new_state in new_states])) 
    
    
    return maxval

quality_level = 0
for t in data:
    quality_level += dfs(State(24,1,0,0,0,0,0,0,0), t) * t[0]
print(quality_level)
