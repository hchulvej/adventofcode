
def read_data():
    shapes = []
    regions = []
    line_no = 0
    with open("2025_12.txt") as f:
        
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

## Part 1 ##

def fit_boxes(region):
    shape = list(region.keys())[0]
    space_no_of_boxes = (shape[0] // 3) * (shape[1] // 3)
    needed_no_of_boxes = sum(list(region.values())[0])
    return space_no_of_boxes >= needed_no_of_boxes

no_of_regions = 0
for region in data[1]:
    if fit_boxes(region):
        no_of_regions += 1

print("Part 1:", no_of_regions)