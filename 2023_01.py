import re

input = []

d = {"one" : '1', "two" : '2', "three" : '3', "four" : '4', "five" : '5', "six" : '6', "seven" : '7', "eight" : '8', "nine" : '9'}

with open('2023_01_1.txt', 'r') as f:
    for l in f.readlines():
        input.append(l.replace('\n', ''))

def calibration_value(s, part):
    if part == 1:
        s = re.sub('[a-z]','',s)
        return int(s[-1]) + 10 * int(s[0])
    else:
        for k in d.keys():
            s = re.sub(k, k + d[k] + k, s)
        s = re.sub('[a-z]','',s)
        return int(s[-1]) + 10 * int(s[0])

total_sum = 0

for i in range(len(input)):
    total_sum = total_sum + calibration_value(input[i], 2)

print(total_sum)

   
