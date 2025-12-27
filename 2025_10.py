
def read_light_diagram(ldiagram):
    res = []
    for indicator in ldiagram[1:-1]:
        res.append(indicator)
    return res

def read_wiring_schematics(schematics):
    res = []
    for light in schematics:
        cs = light[1:-1].split(",")
        res.append(list(map(int, cs)))
    return res

def read_joltage_requirement(jrequirement):
    req = jrequirement[1:-1]
    return sorted(list(map(int, req.split(","))))

def change_light(current_state):
    if current_state == ".":
        return "#"
    else:
        return "."  

def turn_lights_on(light_diagram, button_schematic):
    for pos in button_schematic:
        light_diagram[pos] = change_light(light_diagram[pos])
    return light_diagram

def required_wiring_schematics(light_diagram):
    return sorted([i for i in range(len(light_diagram)) if light_diagram[i] == "#"])

def add_schemes(wschem1, wschem2):
    res = list(wschem1)
    for w in wschem2:
        if w in res:
            res.remove(w)
        else:
            res.append(w)
    return sorted(res)

def read_data():
    with open("2025_10_test.txt") as f:
        res = []
        for l in f.read().split("\n"):
            if l.strip():
                ls = l.split(" ")
                machine = []
                machine.append(read_light_diagram(ls[0]))
                temp = []
                for n in ls[1:-1]:
                    temp.append(n)
                machine.append(read_wiring_schematics(temp))
                machine.append(read_joltage_requirement(ls[-1]))
                res.append(machine)
        return res

data = read_data()

def scheme_additions(data_line):
    light_diagram = data_line[0]
    starting_diagram = ["." for _ in light_diagram]
    wiring_schematics = data_line[1]
    
    req_wiring = required_wiring_schematics(light_diagram)
    button_presses = dict()
    button_presses[1] = wiring_schematics
    
    problem_solved = False
    no_of_presses = 1
    while not problem_solved:
        for scheme in button_presses[no_of_presses]:
            new_light_diagram = turn_lights_on(starting_diagram.copy(), scheme)
            new_req_wiring = required_wiring_schematics(new_light_diagram)
            if new_req_wiring == req_wiring:
                problem_solved = True
                return no_of_presses, scheme
            button_presses[no_of_presses + 1] = [add_schemes(scheme, s) for s in wiring_schematics for scheme in button_presses[no_of_presses]]
        no_of_presses += 1


for i in range(len(data)):
    print("Machine", i + 1, "requires", scheme_additions(data[i])[0], "button presses.")

#print("Part 1:", sum([scheme_additions(data[i])[0] for i in range(len(data))]))