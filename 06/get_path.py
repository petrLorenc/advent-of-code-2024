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
directions = [(0, -1),  # up
              (1, 0),  # right
              (0, 1),  # down
              (-1, 0)]  # left

input_data[actual_y_idx][actual_x_idx] = "X"  # no need to have there ^


def print_board(board):
    for line in board:
        print("".join(line))
    print("\n"*2)



print_board(input_data)
while True:
    actual_x_idx += directions[actual_direction][0]
    actual_y_idx += directions[actual_direction][1]

    if not (0 <= actual_x_idx < x_len and 0 <= actual_y_idx < y_len):
        break

    if input_data[actual_y_idx][actual_x_idx] == "." or input_data[actual_y_idx][actual_x_idx] == "X":
        input_data[actual_y_idx][actual_x_idx] = "X"
    else:
        actual_x_idx -= directions[actual_direction][0]
        actual_y_idx -= directions[actual_direction][1]
        actual_direction = (actual_direction + 1) % 4
    print_board(input_data)

print("".join([x for y in input_data for x in y]).count("X"))