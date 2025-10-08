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

def find_shortest_path_from_to(start_x, start_y, end_x, end_y):
    cost = [[0 for x in range(x_len)] for y in range(y_len)]
    cost[start_y][start_x] = 1
    queue = [(start_x, start_y)]
    while queue:
        x, y = queue.pop(0)
        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            new_x, new_y = x + dx, y + dy
            if 0 <= new_x < x_len and 0 <= new_y < y_len and board[new_y][new_x] != "#":
                if cost[new_y][new_x] >= cost[y][x] + 1 or cost[new_y][new_x] == 0:
                    cost[new_y][new_x] = cost[y][x] + 1
                    if (new_x, new_y) == (end_x, end_y):
                        return cost, cost[y][x] + 1
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
            if 0 <= new_x < x_len and 0 <= new_y < y_len and cost[new_y][new_x] < cost[start_y][start_x] and cost[new_y][new_x] != 0:
                path.append((new_y, new_x))
                start_y, start_x = new_y, new_x
                break
    return path[::-1]

print(path := get_path_from_cost(cost, (stop_y, stop_x), (start_y, start_x)))

def get_shortcuts(board, cost, paths, end_y, end_x):
    shorcuts_cost = []
    for idx, possible_path in enumerate(paths):
        start_y, start_x = possible_path
        for dx, dy in [(0, 2), (2, 0), (0, -2), (-2, 0)]:
            new_y, new_x = start_y + dy, start_x + dx
            if 0 <= new_x < x_len and 0 <= new_y < y_len and cost[new_y][new_x] != 0:
                if cost[new_y][new_x] > cost[start_y][start_x]:
                    shorcuts_cost.append(- cost[new_y][new_x] + cost[start_y][start_x] + 2 )
    return shorcuts_cost

print(saving := list(sorted(get_shortcuts(board, cost, path, stop_y, stop_x))))

saving = list(filter(lambda x: x <= -100, saving))
print(len(saving))