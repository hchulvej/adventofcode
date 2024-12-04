import re

def read_input(input_file):
    with open(input_file) as f:
        lines = [line for line in f.readlines()]
    return lines

raw_input = read_input("2024_03_1.txt")

# Part One

def multiply(s):
    return int(s.split("(")[1].split(",")[0]) * int(s.split(",")[1].split(")")[0])


pattern = r"mul\(\d+,\d+\)"

total = 0
for line in raw_input:
    total +=sum(list(map(multiply,re.findall(pattern, line))))

print(total)

# part Two

pattern_two= r"do(n't)?\(\)"

def do_line(line):
    pieces = []
    line = "do()" + line
    matches = list(re.finditer(pattern_two, line))
    for i in range(len(matches)):
        m1 = matches[i]
        if i < len(matches) - 1: m2 = matches[i + 1]
        if m1.group() == "do()":
            if i < len(matches) - 1:
                pieces.append(line[m1.end():m2.start()])
            else:
                pieces.append(line[m1.end():])
    return pieces      
            
        

total_2 = 0

for line in raw_input:
    for piece in do_line(line):
        total_2 += sum(list(map(multiply,re.findall(pattern, piece))))

print(total_2)