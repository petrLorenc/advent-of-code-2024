from collections import defaultdict

with open("input_2.txt") as f:
    input_data = f.read()

board = [list(x.strip()) for x in input_data.strip().split("\n")]
x_len = len(board[0])
y_len = len(board)


def print_board(board):
    for row in board:
        print("".join([f"{str(x):^6}" for x in row]))


def locate_item(ch):
    for x in range(x_len):
        for y in range(y_len):
            if board[y][x] == ch:
                return x, y


start_x, start_y = locate_item("S")
stop_x, stop_y = locate_item("E")

print_board(board)


def find_shortest_path_from_to(start_x, start_y, end_x, end_y, to_avoid="#"):
    cost = [[0 for x in range(x_len)] for y in range(y_len)]
    cost[start_y][start_x] = 1
    queue = [(start_x, start_y)]
    while queue:
        x, y = queue.pop(0)
        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            new_x, new_y = x + dx, y + dy
            if (new_x, new_y) == (end_x, end_y):
                cost[new_y][new_x] = cost[y][x] + 1
                return cost, cost[new_y][new_x]
            if (
                0 <= new_x < x_len
                and 0 <= new_y < y_len
                and board[new_y][new_x] != to_avoid
            ):
                if cost[new_y][new_x] >= cost[y][x] + 1 or cost[new_y][new_x] == 0:
                    cost[new_y][new_x] = cost[y][x] + 1
                    queue.insert(0, (new_x, new_y))
    return None, None


cost, steps = find_shortest_path_from_to(start_x, start_y, stop_x, stop_y)
print(steps)
print_board(cost)


def get_path_from_cost(cost, start, end):
    start_y, start_x = start
    end_y, end_x = end
    path = [(start_y, start_x)]
    while (start_x, start_y) != (end_x, end_y):
        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            new_y, new_x = start_y + dy, start_x + dx
            if (
                0 <= new_x < x_len
                and 0 <= new_y < y_len
                and cost[new_y][new_x] < cost[start_y][start_x]
                and cost[new_y][new_x] != 0
            ):
                path.append((new_y, new_x))
                start_y, start_x = new_y, new_x
                break
    return path[::-1]


print(path := get_path_from_cost(cost, (stop_y, stop_x), (start_y, start_x)))

to_save = 100


def get_shortcuts(board, cost, paths, end_y, end_x):
    shorcuts_cost = dict()
    shorcuts_cost_saving = dict()
    for idx, possible_path in enumerate(paths):
        start_y, start_x = possible_path
        for point in paths[idx:]:
            possible_y, possible_x = point
            # _, cost = find_shortest_path_from_to(start_x, start_y, possible_x, possible_y, to_avoid="*")
            c = abs(start_x - possible_x) + abs(start_y - possible_y)
            if c <= 20:
                new_cost = (
                    cost[start_y][start_x]
                    + (cost[end_y][end_x] - cost[possible_y][possible_x])
                    + c
                )
                shorcuts_cost.setdefault(c, []).append(
                    (
                        new_cost,
                        cost[end_y][end_x] - new_cost,
                        start_y,
                        start_x,
                        possible_y,
                        possible_x,
                    )
                )
                if (
                    cost[end_y][end_x] - new_cost >= to_save
                ):  # atleast 100 picoseconds saved
                    shorcuts_cost_saving[cost[end_y][end_x] - new_cost] = (
                        shorcuts_cost_saving.get(cost[end_y][end_x] - new_cost, 0) + 1
                    )
    return shorcuts_cost, shorcuts_cost_saving


d, short = get_shortcuts(board, cost, path, stop_y, stop_x)

for k, v in d.items():
    print(k, len(v))
print()
print()

s = 0
for k, v in sorted(short.items(), key=lambda x: x[0]):
    print(v, k)
    s += v

print(s)
