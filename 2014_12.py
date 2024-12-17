
def read_input(input_file):
    with open(input_file) as f:
        lines = [list(line.strip()) for line in f.readlines()]
    return lines

raw_input = read_input("2024_12_2.txt")

regions = dict()

def allowed(x, y):
    return 0 <= x < len(raw_input) and 0 <= y < len(raw_input[0])

current_region = 0
for row_no, row in enumerate(raw_input):
    for col_no, cell in enumerate(row):
        if (row_no, col_no) not in regions:
            regions[(row_no, col_no)] = current_region
            current_region += 1
        else:
            for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                if (row_no + dy, col_no + dx) in regions and allowed(row_no + dy, col_no + dx):
                    regions[(row_no, col_no)] = regions[(row_no + dy, col_no + dx)]
                    print((row_no, col_no), (row_no + dy, col_no + dx), regions[(row_no + dy, col_no + dx)])
                    
    

print(regions)