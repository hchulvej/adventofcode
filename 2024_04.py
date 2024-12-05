import re

def read_input(input_file):
    with open(input_file) as f:
        lines = [line.strip() for line in f.readlines()]
    return lines

raw_input = read_input("2024_04_1.txt")

# Part One

pattern = r"(XMAS)"

def count_xmas(s):
    return len(re.findall(pattern, s))

NO_ROWS = len(raw_input)
NO_COLS = len(raw_input[0])

rows_right = raw_input
rows_left = [row[::-1] for row in rows_right]
cols_up = ["".join([row[i] for row in raw_input]) for i in range(NO_COLS)]
cols_down = [col[::-1] for col in cols_up]
diag_down_left = ["".join([raw_input[i][j] for i in range(NO_ROWS) for j in range(NO_COLS) if i + j == k]) for k in range((NO_ROWS + NO_COLS) - 1)]
diag_up_right = [diag[::-1] for diag in diag_down_left]
diag_down_right = ["".join([raw_input[i][j] for i in range(NO_COLS) for j in range(NO_ROWS) if i - j == k]) for k in range(1-(NO_COLS), NO_ROWS)]
diag_up_left = [diag[::-1] for diag in diag_down_right]

all_the_rows = [*rows_right, *rows_left, *cols_up, *cols_down, *diag_down_left, *diag_up_right, *diag_down_right, *diag_up_left]


xmas_counter_1 = 0   
for s in all_the_rows:
    xmas_counter_1 += count_xmas(s)

print(xmas_counter_1)


# Part Two

def three_by_threes():
    res = []
    for i in range(NO_ROWS - 2):
        for j in range(NO_COLS - 2):
            res.append(raw_input[i][j:j+3] + raw_input[i+1][j:j+3] + raw_input[i+2][j:j+3])
    return res

def is_xmas(three_by_three):
    res = three_by_three[4] == "A"
    res *= (three_by_three[0] == "M" and three_by_three[8] == "S") or (three_by_three[0] == "S" and three_by_three[8] == "M")
    res *= (three_by_three[2] == "M" and three_by_three[6] == "S") or (three_by_three[2] == "S" and three_by_three[6] == "M")
    return 1 if res else 0

xmas_counter_2 = 0

for three_by_three in three_by_threes():
    xmas_counter_2 += is_xmas(three_by_three)

print(xmas_counter_2)