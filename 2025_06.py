def read_data():
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

data = read_data()

## Part 1
def grand_total(data):
    total = 0
    for j in range(len(data)):
        if data[-1][j] == "+":
            total += sum(data[i][j] for i in range(len(data) - 1))
        else:  # "*"
            prod = 1
            for i in range(len(data) - 1):
                prod *= data[i][j]
            total += prod
    return total

print(grand_total(data))