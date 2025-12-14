def read_data_p1():
    with open("2025_06.txt") as f:
        return_data = []
        for item in f.read().split("\n"):
            all_items = item.split(" ")
            items = []
            for i in range(len(all_items)):
                if all_items[i] != "":
                    if all_items[i] in ["*", "+"]:
                        items.append(all_items[i])
                    else:
                        items.append(int(all_items[i]))
            return_data.append(items)
        return return_data

data = read_data_p1()

## Part 1
def grand_total(data):
    total = 0
    for col in range(len(data[0])):
        if data[-1][col] == "+":
            total += sum(data[i][col] for i in range(len(data) - 1))
        if data[-1][col] == "*":
            prod = 1
            for i in range(len(data) - 1):
                prod *= data[i][col]
            total += prod
    return total

print("Part 1: The grand total is", grand_total(data))

## Part 2
def read_data_p2():
    with open("2025_06.txt") as f:
        return f.read().split("\n")

data2 = read_data_p2()

sign_placements = []

for i in range(len(data2[4])):
    if data2[4][i] in ["+", "*"]:
        sign_placements.append(i)
        
number_placements = []

for j in range(len(sign_placements) - 1):
    number_placements.append((data2[4][sign_placements[j]], sign_placements[j], sign_placements[j + 1] - 2))

number_placements.append((data2[4][sign_placements[-1]], sign_placements[-1], len(data2[0]) - 1))
    
def get_values(no_placement):
    values = []
    for c in range(no_placement[1], no_placement[2] + 1):
        col = []
        for r in range(4):
            if data2[r][c] == " ":
                col.append("")
            else:
                col.append(data2[r][c])
        values.append(int("".join(col)))
        
    return values


## Part 2
def grand_total2():
    total = 0
    for no_placement in number_placements:
        values = get_values(no_placement)
        if no_placement[0] == "+":
            total += sum(values)
        if no_placement[0] == "*":
            prod = 1
            for val in values:
                prod *= val
            total += prod
    return total

print("Part 2: The grand total is", grand_total2())
