import re

input = open("2023_15_test.in").read().split(",")

# Part 1
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


# Part 2
label_to_light_box = dict()
light_boxes_sizes = [0 for _ in range(256)]
focal_lengths = dict()
lens_order = dict()

for s in input:
    if s.find("=") > 0:
        label, focal_length = s.split("=")
        focal_length = int(focal_length)
        label_to_light_box[label] = hash(label)
        focal_lengths[label] = focal_length
        light_boxes_sizes[label_to_light_box[label]] += 1
        lens_order[label] = light_boxes_sizes[label_to_light_box[label]]
    else:
        label = s.split("-")[0]
        if label in label_to_light_box:
            light_boxes_sizes[label_to_light_box[label]] -= 1
            lens_order.pop(label)
            label_to_light_box.pop(label)
            focal_lengths.pop(label)    

print(lens_order)