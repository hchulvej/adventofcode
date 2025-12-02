def read_data():
    with open("2025_02.txt") as f:
        return f.read().split(",")


data = read_data()


## Part 1
def check_validity(number, part=1):
    no_of_digits = len(str(number))
    if part == 1:
        if no_of_digits % 2 != 0:
            return True
        left_half = str(number)[: no_of_digits // 2]
        right_half = str(number)[no_of_digits // 2 :]
        return left_half != right_half
    else:
        max_length_of_reps = no_of_digits // 2
        for length in range(1, max_length_of_reps + 1):
            if no_of_digits % length == 0:
                pattern = str(number)[:length]
                repetitions = no_of_digits // length
                if pattern * repetitions == str(number):
                    return False
            
        return True

# We run throug data
sum_invalid_ids = 0
for line in data:
    if "-" in line:
        start, end = map(int, line.split("-"))
        invalid_numbers = [number for number in range(start, end + 1) if not check_validity(number, 1)]
        sum_invalid_ids += sum(invalid_numbers)

print("Part 1: Sum of invalid IDs:", sum_invalid_ids)


## Part 2
# We run throug data
sum_invalid_ids = 0
for line in data:
    if "-" in line:
        start, end = map(int, line.split("-"))
        invalid_numbers = [number for number in range(start, end + 1) if not check_validity(number, 2)]
        sum_invalid_ids += sum(invalid_numbers)

print("Part 2: Sum of invalid IDs:", sum_invalid_ids)