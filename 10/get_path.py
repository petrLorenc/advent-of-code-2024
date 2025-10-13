import copy

with open("input.txt") as f:
    input_data = f.read()

lines = [
    [int(x.strip()) if x.isdigit() else x for x in list(y)]
    for y in input_data.split("\n")
]
visited_board = [[0 for x in range(len(lines[0]))] for y in range(len(lines))]
x_len = len(lines[0])
y_len = len(lines)


def print_board(board):
    for line in board:
        print("".join([str(x) for x in line]))
    print("\n" * 2)


print_board(lines)


def try_path(board, visited_board, new_y, new_x, old_value):
    new_value = board[new_y][new_x]
    if new_value == -1:
        return 0

    if new_value != old_value + 1:
        return 0
    if visited_board[new_y][new_x] != 0:
        return 0
    if new_value == 9:
        return 1

    visited_board[new_y][new_x] = 1
    paths = 0
    if 0 <= new_x - 1 and visited_board[new_y][new_x - 1] == 0:
        paths += try_path(
            board, copy.deepcopy(visited_board), new_y, new_x - 1, new_value
        )
    if 0 <= new_y - 1 and visited_board[new_y - 1][new_x] == 0:
        paths += try_path(
            board, copy.deepcopy(visited_board), new_y - 1, new_x, new_value
        )
    if new_x + 1 < x_len and visited_board[new_y][new_x + 1] == 0:
        paths += try_path(
            board, copy.deepcopy(visited_board), new_y, new_x + 1, new_value
        )
    if new_y + 1 < y_len and visited_board[new_y + 1][new_x] == 0:
        paths += try_path(
            board, copy.deepcopy(visited_board), new_y + 1, new_x, new_value
        )
    return paths


cnt = 0

print(try_path(lines, copy.deepcopy(visited_board), 0, 2, -1))

for y in range(y_len):
    for x in range(x_len):
        if lines[y][x] == 0:
            print(new_cnt := try_path(lines, copy.deepcopy(visited_board), y, x, -1))
            cnt += new_cnt
print(cnt)
