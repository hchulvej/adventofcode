input = open("2023_15_1.in").read().split(",")

# Determine the ASCII code for the current character of the string.
# Increase the current value by the ASCII code you just determined.
# Set the current value to itself multiplied by 17.
# Set the current value to the remainder of dividing itself by 256.
def hash(s, factor=17):
    curr = 0
    for c in list(s):
        curr = ((curr + ord(c)) * factor) % 256
    return curr

print("Part 1:", sum([hash(s) for s in input]))    
