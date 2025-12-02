def read_data():
    with open("2025_02.txt") as f:
        return f.read().split(",")


data = read_data()


# Part 1
def check_validity(number):
    no_of_digits = len(str(number))
    if no_of_digits % 2 != 0:
        return True
    left_half = str(number)[: no_of_digits // 2]
    right_half = str(number)[no_of_digits // 2 :]
    return left_half != right_half

# We run throug data
sum_invalid_ids = 0
for line in data:
    if "-" in line:
        start, end = map(int, line.split("-"))
        invalid_numbers = [number for number in range(start, end + 1) if not check_validity(number)]
        sum_invalid_ids += sum(invalid_numbers)

print("Sum of invalid IDs:", sum_invalid_ids)