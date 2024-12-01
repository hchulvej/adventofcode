
# Part One

def parse_line(line):
    vals = line.strip().split()
    return [int(v) for v in vals]

def read_input(input_file):
    with open(input_file) as f:
        lines = [parse_line(line) for line in f.readlines()]
    return lines
        
parsed_input = read_input("2024_01_1.txt")

left_side = [v[0] for v in parsed_input]
left_side.sort()
right_side = [v[1] for v in parsed_input]
right_side.sort()

print(sum(abs(right_side[i] - left_side[i]) for i in range(len(left_side))))



# Part Two

counter = {v : right_side.count(v) for v in left_side}
print(sum([v * counter[v] for v in counter]))