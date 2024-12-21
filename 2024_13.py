
import re as regex
import sympy

def read_input(input_file):
    with open(input_file) as f:
        lines = [line.strip() for line in f.readlines()]
    return lines

raw_input = read_input("2024_13_1.txt")

PRICE_A, PRICE_B = 3, 1

patterns = dict()
patterns["X+"] = regex.compile(r'X\+\d+')
patterns["Y+"] = regex.compile(r'Y\+\d+')
patterns["X="] = regex.compile(r'X\=\d+')
patterns["Y="] = regex.compile(r'Y\=\d+')

claw_machines = []

for i in range(len(raw_input)):
    input = raw_input[i]
    if input.find("Button A") != -1:
        x = patterns["X+"].search(input).group(0).split("+")[1]
        y = patterns["Y+"].search(input).group(0).split("+")[1]
        claw_machine = {"A": (int(x), int(y))}
    if input.find("Button B") != -1:
        x = patterns["X+"].search(input).group(0).split("+")[1]
        y = patterns["Y+"].search(input).group(0).split("+")[1]
        claw_machine["B"] = (int(x), int(y))
    if input.find("Prize") != -1:
        x = patterns["X="].search(input).group(0).split("=")[1]
        y = patterns["Y="].search(input).group(0).split("=")[1]
        claw_machine["P"] = (int(x), int(y))
        claw_machines.append(claw_machine)
    if len(input) == 0:
        continue
        

def solve(claw_machine):
    coeff_matrix = sympy.Matrix([[claw_machine["A"][0], claw_machine["B"][0]], [claw_machine["A"][1], claw_machine["B"][1]]])
    const_matrix = sympy.Matrix([claw_machine["P"][0], claw_machine["P"][1]])
    if coeff_matrix.det() == 0:
        return "To be checked"
    else:
        a, b = coeff_matrix**(-1) * const_matrix
        return (a, b, a.is_integer and b.is_integer)   


# Part One

tokens = 0
for cm in claw_machines:
    s = solve(cm)
    if s[2]:
        tokens += s[0] * PRICE_A + s[1] * PRICE_B
print(tokens)


# Part Two

OFFSET = 10000000000000

for cm in claw_machines:
    cm["P"] = (cm["P"][0] + OFFSET, cm["P"][1] + OFFSET)

tokens = 0
for cm in claw_machines:
    s = solve(cm)
    if s[2]:
        tokens += s[0] * PRICE_A + s[1] * PRICE_B
print(tokens)