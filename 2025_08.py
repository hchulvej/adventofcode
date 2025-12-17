from collections import defaultdict

def read_data():
    with open("2025_08_test.txt") as f:
        return f.read().split("\n")

data = read_data()
points = defaultdict(tuple)

def parse_point(line):
    parts = line.split(",")
    return (int(parts[0]), int(parts[1]), int(parts[2]))

def read_points():
    for i in range(len(data)):
        points[i] = parse_point(data[i])
        

read_points()