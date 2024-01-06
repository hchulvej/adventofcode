import numpy as np

# Setup
input = []
with open("2023_14_1.in") as f:
    for line in f.readlines():
        input.append(list(line.replace("\n", "")))
    
grid = np.array(input)

# Helper functions

def swap(arr, c_1, c_2):
    temp = arr[*c_1]
    arr[*c_1] = arr[*c_2]
    arr[*c_2] = temp
    return arr

def slide_north(arr, coords):
    [r, c] = coords
    if r == 0 or (r > 0 and arr[r - 1, c] in ["O", "#"]):
        return arr
    else:
        arr = swap(arr, (r - 1, c), (r, c))
        return slide_north(arr, (r - 1, c))
    

def slide_all_north(arr):
    for r in range(1, arr.shape[0]):
        for c in [c for c in range(arr.shape[1]) if arr[r, c] == "O"]:
            arr = slide_north(arr, (r, c))
    return arr

def score(arr):
    total = 0
    for r in range(arr.shape[0]):
        for c in [c for c in range(arr.shape[1]) if arr[r, c] == "O"]:
            total += arr.shape[0] - r
    return total

# Part 1
north_grid = slide_all_north(grid)

print("Part 1:", score(north_grid))    


# Helper functions part 2

def rotate_grid(arr):
    return np.rot90(arr, 3)

def cycle(arr):
    # North
    arr = slide_all_north(arr)
    # East
    arr = rotate_grid(arr)
    arr = slide_all_north(arr)
    # South
    arr = rotate_grid(arr)
    arr = slide_all_north(arr)
    # West
    arr = rotate_grid(arr)
    arr = slide_all_north(arr)
    
    arr = rotate_grid(arr)
    return arr

c_grid = cycle(grid)
scores = dict()
for i in range(1000):
    s = score(c_grid)
    if not s in scores.keys():
        scores[s] = [i]
    else:    
        scores[s].append(i)
    c_grid = cycle(c_grid)

print(scores)
