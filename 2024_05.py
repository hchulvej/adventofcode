
def read_input(input_file):
    with open(input_file) as f:
        lines = [line.strip() for line in f.readlines()]
    return lines

raw_input = read_input("2024_05_2.txt")

ordering = [tuple(map(int,s.split("|"))) for s in raw_input if s.count("|") == 1]
updates = [tuple(map(int,s.split(","))) for s in raw_input if s.count(",") > 0]

print(ordering)
print(updates)

print(raw_input)