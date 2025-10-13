x_len = 101
y_len = 103

# x_len = 11
# y_len = 7

with open("input_2.txt") as f:
    data = f.readlines()

robots = []


class Robot:
    def __init__(self, position: tuple, velocity: tuple, limits: tuple):
        self.position = position
        self.velocity = velocity
        self.limits = limits

    def make_move(self):
        self.position = (
            (self.position[0] + self.velocity[0]) % self.limits[0],
            (self.position[1] + self.velocity[1]) % self.limits[1],
        )


for robot in data:
    position, velocity = robot.strip().split(" ")
    position_x, position_y = position.replace("p=", "").strip().split(",")
    velocity_x, velocity_y = velocity.replace("v=", "").strip().split(",")
    robots.append(
        Robot(
            (int(position_x), int(position_y)),
            (int(velocity_x), int(velocity_y)),
            (x_len, y_len),
        )
    )


def print_robots_on_board():
    board = [[0 for _ in range(x_len)] for _ in range(y_len)]
    for robot in robots:
        board[robot.position[1]][robot.position[0]] += 1
    for row in board:
        print("".join([str(x) if x != 0 else "." for x in row]))


print_robots_on_board()
for _ in range(100):
    for robot in robots:
        robot.make_move()
    print_robots_on_board()
    print("")

# sum quadrants
board = [[0 for _ in range(x_len)] for _ in range(y_len)]
for robot in robots:
    board[robot.position[1]][robot.position[0]] += 1

cnt_1 = 0
for x in range(x_len // 2):
    for y in range(y_len // 2):
        cnt_1 += board[y][x]
print(cnt_1)
cnt_2 = 0
for x in range(x_len // 2 + 1, x_len):
    for y in range(y_len // 2 + 1, y_len):
        cnt_2 += board[y][x]
print(cnt_2)
cnt_3 = 0
for x in range(x_len // 2 + 1, x_len):
    for y in range(y_len // 2):
        cnt_3 += board[y][x]
print(cnt_3)
cnt_4 = 0
for x in range(x_len // 2):
    for y in range(y_len // 2 + 1, y_len):
        cnt_4 += board[y][x]
print(cnt_4)
print(cnt_1 * cnt_2 * cnt_3 * cnt_4)
