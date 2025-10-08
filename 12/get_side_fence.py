import copy

with open("input.txt") as f:
    input_data = f.read()

input_data = [list(x) for x in input_data.split("\n")]
y_len = len(input_data)
x_len = len(input_data[0])

# [UP, DOWN, LEFT, RIGHT]
visited_map = [[[0,0,0,0] for x in range(x_len)] for y in range(y_len)]

"""
AAAA
BBCD
BBCC
EEEC
"""

# collect changes
for y in range(y_len):
    for x in range(x_len):
        letter = input_data[y][x]
        next_letter = input_data[y][x + 1] if x + 1 < x_len else "1"
        if letter != next_letter:
            visited_map[y][x][3] = 1
    for x in range(x_len - 1, -1, -1):
        letter = input_data[y][x]
        next_letter = input_data[y][x - 1] if x - 1 >= 0 else "1"
        if letter != next_letter:
            visited_map[y][x][2] = 1
for x in range(x_len):
    for y in range(y_len):
        letter = input_data[y][x]
        next_letter = input_data[y - 1][x] if y - 1 >= 0 else "1"
        if letter != next_letter:
            visited_map[y][x][0] = 1
    for y in range(y_len - 1, -1, -1):
        letter = input_data[y][x]
        next_letter = input_data[y + 1][x] if y + 1 < y_len else "1"
        if letter != next_letter:
            visited_map[y][x][1] = 1

# [UP, DOWN, LEFT, RIGHT]
print(visited_map)

# [UP, DOWN, LEFT, RIGHT]
for y in range(y_len):
    for x in range(x_len):
        letter = input_data[y][x]
        next_letter = input_data[y][x + 1] if x + 1 < x_len else "1"
        if next_letter != letter:
            pass
        elif letter == next_letter:
            if visited_map[y][x + 1][0] == 1:
                visited_map[y][x][0] = 0
            if visited_map[y][x + 1][1] == 1:
                visited_map[y][x][1] = 0

for x in range(x_len):
    for y in range(y_len):
        letter = input_data[y][x]
        next_letter = input_data[y + 1][x] if y + 1 < y_len else "1"
        if next_letter != letter:
            pass
        elif letter == next_letter:
            if visited_map[y + 1][x][2] == 1:
                visited_map[y][x][2] = 0
            if visited_map[y + 1][x][3] == 1:
                visited_map[y][x][3] = 0

def get_fence_area(input_data, y, x, visited, visited_now):
    area = 1
    fence = sum(visited[y][x])
    visited_now[y][x] = 1
    initial_letter = input_data[y][x]
    if 0 <= y - 1 and input_data[y-1][x] == initial_letter and visited_now[y-1][x] == 0:
        new_area, new_fence = get_fence_area(input_data, y - 1, x, visited, visited_now)
        area += new_area
        fence += new_fence
    if y + 1 < y_len and input_data[y+1][x] == initial_letter and visited_now[y+1][x] == 0:
        new_area, new_fence = get_fence_area(input_data, y + 1, x, visited, visited_now)
        area += new_area
        fence += new_fence
    if 0 <= x - 1 and input_data[y][x-1] == initial_letter and visited_now[y][x-1] == 0:
        new_area, new_fence = get_fence_area(input_data, y, x - 1, visited, visited_now)
        area += new_area
        fence += new_fence
    if x + 1 < x_len and input_data[y][x+1] == initial_letter and visited_now[y][x+1] == 0:
        new_area, new_fence = get_fence_area(input_data, y, x + 1, visited, visited_now)
        area += new_area
        fence += new_fence

    return area, fence

visited_now = [[0 for x in range(x_len)] for y in range(y_len)]
cnt = 0
for y in range(y_len):
    for x in range(x_len):
        if visited_now[y][x] == 0:
            new_area, new_fence = get_fence_area(input_data, y, x, visited_map, visited_now)
            cnt += new_area * new_fence

print(visited_map)
print(cnt)