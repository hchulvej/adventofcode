import re
from functools import cmp_to_key

def read_input(input_file):
    with open(input_file) as f:
        lines = [line for line in f.readlines()]
    return lines

raw_input = read_input("2024_03_1.txt")

# Part One

def multiply(s):
    return int(s.split("(")[1].split(",")[0]) * int(s.split(",")[1].split(")")[0])


pattern_mul = r"mul\(\d+,\d+\)"

total1 = 0
for line in raw_input:
    total1 +=sum(list(map(multiply,re.findall(pattern_mul, line))))

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

print(sum([sum_line(line) for line in raw_input]))