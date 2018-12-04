import re
from collections import defaultdict

dateRegex = re.compile("\[(.*?)\-(.*?)\-(.*?) (.*?):(.*?)\] (.*)")
def parse(line):
    data = dateRegex.search(line).groups()
    year = data[0]
    month = data[1]
    day = data[2]
    hour = data[3]
    minute = data[4]
    action = data[5]
    return (year, month, day, hour, minute, action)

with open("input.txt") as f:
    guards = defaultdict(list)
    time_sum = defaultdict(int)
    guard_cache = 0
    lines = sorted(f.readlines())
    counter = 0
    for line in lines:
        year, month, day, hour, minute, action = parse(line)
        if "falls" in action:
            counter = int(minute)
        elif "wakes" in action:
            time_sum[guard_cache] += (int(minute) - counter)
            guards[guard_cache].append(((int(minute), counter)))
            counter = 0
        else:
            guard_cache = action[7:action.find(" begins")]
    guard = max(time_sum.items(), key=lambda i: i[1])

    minutes = []
    for i in range(60):
        counter = 0
        for j in guards[guard[0]]:
            if j[1] <= i <= j[0]:
                counter += 1
        minutes.append((i, counter))
    minute = max(minutes, key=lambda i: i[1])
    print("Answer 1: " + str(int(guard[0]) * minute[0]))
    guard_times = []
    for g in guards:
        minutes = []
        for i in range(60):
            count = sum(1 for start, end in guards[g] if end <= i < start)
            guard_times.append((g, i, count))
id, minute, count = max(guard_times, key=lambda i: i[2])
print("Answer 2: " + str(int(id) * minute))