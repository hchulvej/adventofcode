import re
from functools import cmp_to_key

def read_input(input_file):
    with open(input_file) as f:
        lines = [line for line in f.readlines()]
    return lines

raw_input = read_input("2024_03_1.txt")
combined = "".join(raw_input)

# Part One

pattern_mul = r"mul\((\d+),(\d+)\)"

total1 = 0
for a, b in re.findall(pattern_mul, combined):
    total1 += int(a) * int(b)
    

print(total1)

# part Two

pattern = r"mul\((\d+),(\d+)\)|(do\(\))|(don't\(\))"

def sum_line(line):
    enabled = True
    total = 0
    for a, b, do, dont in re.findall(pattern, line):
        if do or dont:
            enabled = bool(do)
        else:
            m = int(a) * int(b)
            total += m * (1 if enabled else 0)
    return total

print(sum_line(combined))