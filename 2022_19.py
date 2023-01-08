import re
from dataclasses import dataclass, field

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

def do_nothing(state: State) -> State:
    old_state = state.get_state()
    old_state['time_left'] -= 1
    old_state['ore_deposit'] += old_state['ore_robots']
    old_state['clay_deposit'] += old_state['clay_robots']
    old_state['obsidian_deposit'] += old_state['obsidian_robots']
    old_state['geodes_opened'] += old_state['geode_robots']
    return State(*old_state.values())
    
#def afford_robot(state: State, type: str) -> State:   
    

# Example
s = State(24, 1, 0, 0, 0, 0, 0, 0, 0)
print(s)
ns = do_nothing(s)
print(ns)