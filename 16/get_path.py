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
cost = [[0 for x in range(x_len)] for y in range(y_len)]


def find_shortest_path_from_to(start_x, start_y, end_x, end_y):
    cost[start_y][start_x] = 0
    queue = [(start_x, start_y, (1, 0))]
    while queue:
        x, y, direction = queue.pop(0)
        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            new_x, new_y = x + dx, y + dy
            if 0 <= new_x < x_len and 0 <= new_y < y_len and board[new_y][new_x] != "#":
                if (dx, dy) == direction:
                    if cost[new_y][new_x] >= cost[y][x] + 1 or cost[new_y][new_x] == 0:
                        cost[new_y][new_x] = cost[y][x] + 1
                        queue.insert(0, (new_x, new_y, (dx, dy)))
                else:
                    if (
                        cost[new_y][new_x] >= cost[y][x] + 1001
                        or cost[new_y][new_x] == 0
                    ):
                        cost[new_y][new_x] = cost[y][x] + 1001
                        queue.insert(0, (new_x, new_y, (dx, dy)))
        # print_board(cost)


print(find_shortest_path_from_to(start_x, start_y, stop_x, stop_y))
print_board(cost)
