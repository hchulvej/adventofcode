input = open("2023_11_test.in").read().splitlines()

# Finding empty rows and columns
empty_rows = [r for r in range(len(input)) if input[r].count("#") == 0]
empty_cols = [c for c in range(len(input[0])) if not "#" in [input[r][c] for r in range(len(input))]]

# Scaling the input
scaled_input = []
for r in range(len(input)):
    new_r = ""
    for c in range(len(input[r])):
        new_r += input[r][c]
        if c in empty_cols:
            new_r += input[r][c]
    scaled_input.append(new_r)
    if r in empty_rows:
        scaled_input.append(new_r)

