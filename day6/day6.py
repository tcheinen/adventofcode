from math import hypot
from collections import defaultdict

def calculate_size(data):
    output = defaultdict(int)
    for k, v in data.items():
        output[tuple(v[1])] += 1
    return output

def closest(data):
    data.sort()
    return (-1, (-1,-1)) if data[0][0] == data[1][0] else data[0]

def distance(a, b):
    return abs(b[0]-a[0]) + abs(b[1]-a[1])

def calculate_grid(data, size):
    grid = {}
    answer_2 = 0
    infinite_coords = set()
    for i in range(size+1):
        for j in range(size+1):
            grid[(i, j)] = closest(([(distance((i,j), x), x) for x in data]))
            total = sum([distance((i,j), x) for x in data])
            if(total < 10000):
                answer_2 += 1
            if(i == size or j == size or i == 0 or j == 0):
                infinite_coords.add((grid[(i, j)][1]))
    return grid, infinite_coords, answer_2

with open("input.txt") as f:
    points = set()
    for i in f.readlines():
        points.add(tuple([int(x) for x in i.rstrip().split(", ")]))
grid_400, infinite_coords, answer_2 = calculate_grid(points,400)
summed_grid = calculate_size(grid_400)
answer_1 = max([(k, v) for k, v in summed_grid.items() if k not in infinite_coords], key=lambda i: i[1])[1]
print("Answer 1: " + str(answer_1))
print("Answer 2: " + str(answer_2))