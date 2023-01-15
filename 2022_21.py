"""
    Load and parse data
    
    'root: pppw + sjmn', 'dbpl: 5'
"""
with open('./2022_21.txt', "r", encoding="utf-8") as file:
    data = list()
    for line in file:
        data.append(line.strip())

monkeys = dict()

for line in data:
    s = line.split(" ")
    monkeys[s[0][0:4]] = dict()
    if len(s) == 2:
        monkeys[s[0][0:4]]['type'] = 'shouter'
        monkeys[s[0][0:4]]['value'] = int(s[1])
    else:
        monkeys[s[0][0:4]]['type'] = 'calculator'
        monkeys[s[0][0:4]]['value'] = None
        monkeys[s[0][0:4]]['helper_monkeys'] = tuple([s[1], s[3]])
        monkeys[s[0][0:4]]['operation'] = s[2]
        
"""
    Part One
"""

waiting_monkeys = list()
ready_monkeys = list()

# Initializing
for monkey_name, monkey_business in monkeys.items():
    if monkey_business['type'] == 'shouter':
        ready_monkeys.append(monkey_name)
    else:
        waiting_monkeys.append(monkey_name)

if False:
    while 'root' not in ready_monkeys:
        
        wm = [m for m in waiting_monkeys]
        
        for monkey_name in wm:
            monkey_business = monkeys[monkey_name]
            if monkey_business['helper_monkeys'][0] in ready_monkeys and monkey_business['helper_monkeys'][1] in ready_monkeys:
                val1 = monkeys[monkey_business['helper_monkeys'][0]]['value']
                val2 = monkeys[monkey_business['helper_monkeys'][1]]['value']
                if monkey_business['operation'] == '+':
                    monkey_business['value'] = val1 + val2
                    ready_monkeys.append(monkey_name)
                    waiting_monkeys.remove(monkey_name)
                if monkey_business['operation'] == '-':
                    monkey_business['value'] = val1 - val2
                    ready_monkeys.append(monkey_name)
                    waiting_monkeys.remove(monkey_name)
                if monkey_business['operation'] == '*':
                    monkey_business['value'] = val1 * val2
                    ready_monkeys.append(monkey_name)
                    waiting_monkeys.remove(monkey_name)
                if monkey_business['operation'] == '/':
                    monkey_business['value'] = val1 // val2
                    ready_monkeys.append(monkey_name)
                    waiting_monkeys.remove(monkey_name)
            else:
                continue

    for monkey_name, monkey_business in monkeys.items():
        if monkey_name == 'root':
            print(monkey_business['value'])
        else:
            continue