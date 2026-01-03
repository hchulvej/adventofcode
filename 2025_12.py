
def read_data():
    shapes = []
    regions = []
    line_no = 0
    with open("2025_12_test.txt") as f:
        
        for line in f.read().split("\n"):
            if line_no < 30 and line_no % 5 != 0 and line_no % 5 != 4:
                shapes.append(line.strip())
            if line_no >= 30:
                region = dict()
                key = tuple(map(int, line.strip().split(":")[0].split("x")))
                val = tuple(map(int, line.strip().split(":")[1].strip().split(" ")))
                region[key] = val
                regions.append(region)
            line_no += 1
        
    return [shapes, regions]

data = read_data()

print(data[0])