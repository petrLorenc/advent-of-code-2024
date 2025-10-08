import copy

with open("input.txt") as f:
    input_data = f.read()

input_data = [list(x) for x in input_data.split("\n")]
y_len = len(input_data)
x_len = len(input_data[0])

visited_map = [[0 for x in range(x_len)] for y in range(y_len)]
visited_now = [[0 for x in range(x_len)] for y in range(y_len)]
def get_size_area(input_data, y, x, visited, visited_now):
    area = 1
    fence = visited[y][x]
    visited_now[y][x] = 1
    initial_letter = input_data[y][x]
    if 0 <= y - 1 and input_data[y-1][x] == initial_letter and visited_now[y-1][x] == 0:
        new_area, new_fence = get_size_area(input_data, y - 1, x, visited, visited_now)
        area += new_area
        fence += new_fence
    if y + 1 < y_len and input_data[y+1][x] == initial_letter and visited_now[y+1][x] == 0:
        new_area, new_fence = get_size_area(input_data, y + 1, x, visited, visited_now)
        area += new_area
        fence += new_fence
    if 0 <= x - 1 and input_data[y][x-1] == initial_letter and visited_now[y][x-1] == 0:
        new_area, new_fence = get_size_area(input_data, y, x - 1, visited, visited_now)
        area += new_area
        fence += new_fence
    if x + 1 < x_len and input_data[y][x+1] == initial_letter and visited_now[y][x+1] == 0:
        new_area, new_fence = get_size_area(input_data, y, x + 1, visited, visited_now)
        area += new_area
        fence += new_fence

    return area, fence


for y in range(y_len):
    for x in range(x_len):
        initial_letter = input_data[y][x]
        same = 4
        if 0 <= y - 1 and input_data[y - 1][x] == initial_letter:
            same -= 1
        if y + 1 < y_len and input_data[y + 1][x] == initial_letter:
            same -= 1
        if 0 <= x - 1 and input_data[y][x - 1] == initial_letter:
            same -= 1
        if x + 1 < x_len and input_data[y][x + 1] == initial_letter:
            same -= 1
        visited_map[y][x] = same

cnt = 0
for y in range(y_len):
    for x in range(x_len):
        if visited_now[y][x] == 0:
            new_area, new_fence = get_size_area(input_data, y, x, visited_map, visited_now)
            cnt += new_area * new_fence
print(cnt)
