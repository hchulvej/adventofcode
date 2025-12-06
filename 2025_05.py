def read_data():
    with open("2025_05.txt") as f:
        return f.read().split("\n")

data = read_data()

def read_intervals(data):
    intervals = []
    for l in range(data.index('')):
        start, end = data[l].split('-')
        intervals.append((int(start), int(end)))
    return sorted(intervals)

def read_ids(data):
    ids = []
    for l in range(data.index('') + 1, len(data)):
        ids.append(int(data[l]))
    return sorted(ids)

# Assume intervals are sorted
def merge_intervals_possible(interval_1, interval_2):
    low_1, high_1 = interval_1
    low_2, high_2 = interval_2
    return low_2 <= high_1

def merge_two_intervals(interval_1, interval_2):
    low_1, high_1 = interval_1
    low_2, high_2 = interval_2
    return (min(low_1, low_2), max(high_1, high_2))

def merge_all_intervals(intervals):
    merged = []
    current_interval = intervals[0]
    for next_interval in intervals[1:]:
        if merge_intervals_possible(current_interval, next_interval):
            current_interval = merge_two_intervals(current_interval, next_interval)
        else:
            merged.append(current_interval)
            current_interval = next_interval
    merged.append(current_interval)
    return merged    
        
## Part 1
intervals = read_intervals(data)
merged_intervals = merge_all_intervals(intervals)
ids = read_ids(data)

fresh_ids = 0
for id_ in ids:
    for interval in merged_intervals:
        if interval[0] <= id_ <= interval[1]:
            fresh_ids += 1
            break

print("Part 1: Number of fresh IDs = ", fresh_ids)

no_fresh_ids = 0
for interval in merged_intervals:
    no_fresh_ids += (interval[1] - interval[0] + 1)

print("Part 2: Number of fresh IDs = ", no_fresh_ids)