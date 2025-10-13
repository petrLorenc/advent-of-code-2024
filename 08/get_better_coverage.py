with open("input.txt") as f:
    input_data = f.read().strip()
lines = [[x.strip() for x in list(y)] for y in input_data.split("\n")]

x_len = len(lines[0])
y_len = len(lines)

points_mapping = {}
cnt = 0
antennas = 0


def print_board(board):
    for line in board:
        print("".join(line))
    print("\n" * 2)


for x in range(x_len):
    for y in range(y_len):
        if lines[y][x] != ".":
            points_mapping.setdefault(lines[y][x], []).append((x, y))
            antennas += 1

print(points_mapping)
print_board(lines)

for point, coordinates in points_mapping.items():
    for idx in range(len(coordinates)):
        for n_idx in range(len(coordinates)):
            x1, y1 = coordinates[idx]
            x2, y2 = coordinates[n_idx]

            diff_x1_x2 = x2 - x1
            diff_y1_y2 = y2 - y1

            for i in range(1, max(x_len, y_len)):
                new_x1 = x1 + i * diff_x1_x2
                new_y1 = y1 + i * diff_y1_y2

                if 0 <= new_x1 < x_len and 0 <= new_y1 < y_len:
                    if lines[new_y1][new_x1] == "." or lines[new_y1][new_x1] == "#":
                        lines[new_y1][new_x1] = "#"
                        cnt += 1

            for i in range(1, max(x_len, y_len)):
                new_x2 = x1 - i * diff_x1_x2
                new_y2 = y1 - i * diff_y1_y2

                if 0 <= new_x2 < x_len and 0 <= new_y2 < y_len:
                    if lines[new_y2][new_x2] == "." or lines[new_y2][new_x2] == "#":
                        lines[new_y2][new_x2] = "#"
                        cnt += 1

print_board(lines)
print("".join([x for y in lines for x in y]).count("#") + antennas)
print(cnt)
