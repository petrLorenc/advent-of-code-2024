import copy

with open("input.txt", "r") as f:
    flatten_data = f.read()
    input_data: list[list] = [list(x.strip()) for x in flatten_data.split("\n")]
x_len = len(input_data[0])
y_len = len(input_data)

flatten_data = flatten_data.replace("\n", "")
cnt = 0
actual_x_idx = flatten_data.index("^") % x_len
actual_y_idx = flatten_data.index("^") // x_len

actual_direction = 0
directions = [
    (0, -1),  # up
    (1, 0),  # right
    (0, 1),  # down
    (-1, 0),
]  # left


def print_board(board):
    for line in board:
        print("".join(line))
    print("\n" * 2)


def is_in_loop(
    board,
    actual_y_idx,
    actual_x_idx,
    obstacle_x,
    obstacle_y,
    directions,
    actual_direction,
):
    board[obstacle_y][obstacle_x] = "-1"
    board[actual_y_idx][actual_x_idx] = "0"  # no need to have there ^
    # print_board(board)

    while True:
        actual_x_idx += directions[actual_direction][0]
        actual_y_idx += directions[actual_direction][1]

        if not (0 <= actual_x_idx < x_len and 0 <= actual_y_idx < y_len):
            break
        if str(actual_direction) == board[actual_y_idx][actual_x_idx]:  # in the loop
            return True

        if (
            board[actual_y_idx][actual_x_idx] != "#"
            and board[actual_y_idx][actual_x_idx] != "-1"
        ):
            board[actual_y_idx][actual_x_idx] = str(actual_direction)
        else:
            actual_x_idx -= directions[actual_direction][0]
            actual_y_idx -= directions[actual_direction][1]
            actual_direction = (actual_direction + 1) % 4
        # print_board(board)
    return False


cnt = 0
print(
    is_in_loop(
        copy.deepcopy(input_data),
        actual_y_idx,
        actual_x_idx,
        5,
        6,
        directions,
        actual_direction,
    )
)

for x in range(x_len):
    for y in range(y_len):
        print(x, y)
        if actual_y_idx == y and actual_x_idx == x:
            continue
        if is_in_loop(
            copy.deepcopy(input_data),
            actual_y_idx,
            actual_x_idx,
            x,
            y,
            directions,
            actual_direction,
        ):
            cnt += 1
            print("Loop found")
print(cnt)
