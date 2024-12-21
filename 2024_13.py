
import re

def read_input(input_file):
    with open(input_file) as f:
        lines = [line.strip() for line in f.readlines()]
    return lines

raw_input = read_input("2024_13_2.txt")

PRICE_A, PRICE_B = 3, 1

patterns = dict()
patterns["X+"] = re.compile(r'X\+\d+')
patterns["Y+"] = re.compile(r'Y\+\d+')
patterns["X="] = re.compile(r'X\=\d+')
patterns["Y="] = re.compile(r'Y\=\d+')

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
        
    

print(claw_machines)