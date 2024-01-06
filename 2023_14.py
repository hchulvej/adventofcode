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


# Part 1
north_grid = slide_all_north(grid)
load_p1 = 0
for r in range(grid.shape[0]):
    for c in [c for c in range(grid.shape[1]) if grid[r, c] == "O"]:
        load_p1 += grid.shape[0] - r
print("Part 1:", load_p1)    


# Helper functions part 2
