from time import sleep

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
        self.position = ((self.position[0] + self.velocity[0]) % self.limits[0],
                         (self.position[1] + self.velocity[1]) % self.limits[1])


for robot in data:
    position, velocity = robot.strip().split(" ")
    position_x, position_y = position.replace("p=","").strip().split(",")
    velocity_x, velocity_y = velocity.replace("v=","").strip().split(",")
    robots.append(Robot((int(position_x), int(position_y)), (int(velocity_x), int(velocity_y)), (x_len, y_len)))


import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

clear_screen()

def print_robots_on_board(output=False):
    is_tree = False
    board = [[0 for _ in range(x_len)] for _ in range(y_len)]
    for robot in robots:
        board[robot.position[1]][robot.position[0]] += 1
    output = []
    for row in board:
        output.append("".join([str(x) if x != 0 else "." for x in row]) + "\n")
    for start in range(10, x_len - 10):
        for end in range(start + 10, x_len - 10):
            if end - start > 10:
                if all([x != 0 for x in board[50][start:end]]):
                    is_tree = True

    return output, is_tree



print_robots_on_board()
with open("output.txt", "w") as f:
    for _ in range(10000):
        print(_)
        for robot in robots:
            robot.make_move()
        possible_tree, is_tree = print_robots_on_board()
        if _ > 7000:
            f.write(str(_) + "\n")
            f.writelines(possible_tree)
        if is_tree:
            print(possible_tree)
            print("found")
            break
