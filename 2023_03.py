input = []

with open('2023_03_test.txt', 'r') as f:
    for l in f.readlines():
        input.append(l.replace('\n', ''))


def get_input(r, c):
    return input[r][c]

print(get_input(4,1))