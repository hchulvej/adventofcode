import re

def read_input(input_file):
    with open(input_file) as f:
        lines = [line.strip() for line in f.readlines()]
    return lines

raw_input = read_input("2024_04_1.txt")

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