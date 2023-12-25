from math import lcm

input = open("2023_08_1.in").read().splitlines()

instructions =list(input[0])
nodes = dict()

for ln in input[2:]:
    temp_1 = ln.split("=")
    temp_2 = temp_1[1].replace("(", "").replace(")", "").split(", ")
    nodes[temp_1[0].strip()] = (temp_2[0].strip(), temp_2[1].strip())

# Part 1
def steps(node, part=1):
    no_steps = 0
    curr = node
    if part == 1:
        while curr != "ZZZ":
            instruction = instructions[no_steps % len(instructions)]
            if instruction == "L":
                curr = nodes[curr][0]
            else:
                curr = nodes[curr][1]
            no_steps += 1
    else:
        while curr[-1] != "Z":
            instruction = instructions[no_steps % len(instructions)]
            if instruction == "L":
                curr = nodes[curr][0]
            else:
                curr = nodes[curr][1]
            no_steps += 1
    return no_steps

print("Part 1: Number of steps required is", steps("AAA"))


# Part 2
starting_nodes = [n for n in nodes if n[-1] == "A"]
path_lengths = [steps(n, 2) for n in starting_nodes]

print("Part 2: Number of steps required is", lcm(*path_lengths))