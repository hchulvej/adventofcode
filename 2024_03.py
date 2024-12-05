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


pattern = r"mul\(\d+,\d+\)"

total = 0
for line in raw_input:
    total +=sum(list(map(multiply,re.findall(pattern, line))))

print(total)

# part Two

pattern_do = r"do\(\)"
pattern_dont = r"don't\(\)"

def extract_and_sort_line(line):
    mul_matches = list(re.finditer(pattern, line))
    do_matches = list(re.finditer(pattern_do, line))
    dont_matches = list(re.finditer(pattern_dont, line))
    return sorted(mul_matches + do_matches + dont_matches, key=cmp_to_key(lambda m1, m2: m1.start() - m2.start()))         
            
def enable_items(sorted_list):
    multiplication_list = []
    enabled = True
    for item in sorted_list:
        if item.group() == "do()":
            enabled = True
        elif item.group() == "don't()":
            enabled = False
        else:
            if enabled:
                multiplication_list.append(int(item.group().split("(")[1].split(",")[0]) * int(item.group().split(",")[1].split(")")[0]))
    return multiplication_list
           

total_2 = 0
for line in raw_input:
    total_2 += sum(enable_items(extract_and_sort_line(line)))

print(total_2)

def extract_and_process_line(line):
    # Combine all patterns into one regex
    combined_pattern = f"{pattern}|{pattern_do}|{pattern_dont}"
    
    # Find all matches in the order they appear
    matches = re.finditer(combined_pattern, line)
    
    # Process instructions
    enabled = True
    results = []
    print(f"Processing line: {line.strip()}")
    for match in matches:
        instruction = match.group()
        print(f"Match found: {instruction}")
        if instruction == "do()":
            enabled = True
            print("Enabled mul instructions.")
        elif instruction == "don't()":
            enabled = False
            print("Disabled mul instructions.")
        else:
            if enabled:
                x, y = int(match.group().split(",")[1].split(")")[0])
                product = x * y
                results.append(product)
                print(f"Multiplying: {x} * {y} = {product}")
            else:
                print(f"Ignoring mul instruction: {instruction}")
    return results

extract_and_process_line(raw_input[0])