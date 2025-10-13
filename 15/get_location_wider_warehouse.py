from __future__ import annotations

from typing import Union

with open("input.txt") as f:
    input_data = f.read()

board, instructions = input_data.split("\n\n")

instructions = instructions.replace("\n", "")
board = [list(x) for x in board.split("\n")]
x_len = len(board[0])
y_len = len(board)

real_board: list[list[Union[MapObject]]] = [[] for y in range(y_len)]


def print_board(board):
    for row in board:
        print("".join([x.get_str() for x in row]))


def sum_coordinates(board):
    cnt = 0
    for x in range(x_len):
        for y in range(y_len):
            if board[y][x].get_str() == "O":
                cnt += 100 * y + x
    return cnt


class MapObject:
    def __init__(self, x, y, representation, parent=None):
        self.x = x
        self.y = y
        self.representation = representation  # it will be # for non-moving, . for empty and @ for actual robot
        self.parent = None

    def move(self, diff_x, diff_y, board, sibling=None) -> bool:
        if self.get_str() == "#":
            return False
        if self.can_move(diff_x, diff_y, board):
            # switch objects
            return True
        else:
            return False

    def get_str(self) -> str:
        return self.representation

    def can_move(self, diff_x, diff_y, board) -> tuple[bool, list[MapObject]]:
        if 0 <= self.x + diff_x < x_len and 0 <= self.y + diff_y < y_len:
            if board[self.y + diff_y][self.x + diff_x].get_str() == ".":
                if self.get_str() == "[":
                    if board[self.y][self.x + 1].can_move(diff_x, diff_y, board):
                        return True, [self, board[self.y][self.x + 1]]
                elif self.get_str() == "]":
                    if board[self.y][self.x - 1].can_move(diff_x, diff_y, board):
                        return True, [self, board[self.y][self.x - 1]]
                return True, [self]
        if board[self.y + diff_y][self.x + diff_x].can_move(diff_x, diff_y, board):
            return True, [self]
        return False, [None]


class WideMapObject:
    def __init__(self):
        self.l: MapObject = MapObject(len(real_board[y]), y, "[", self)
        self.r: MapObject = MapObject(len(real_board[y]), y, "]", self)

    def get_str(self) -> str:
        return self.l.get_str() + self.r.get_str()

    def move(self, diff_x, diff_y, board) -> bool:
        if diff_x == 0:
            return self.l.move(diff_x, diff_y, board, sibling=self.r) and self.r.move(
                diff_x, diff_y, board, sibling=self.l
            )
        elif diff_x == 1:
            return self.r.move(diff_x, diff_y, board, sibling=self.l)
        elif diff_x == -1:
            return self.l.move(diff_x, diff_y, board, sibling=self.r)
        return False


robot: MapObject = None
for x in range(x_len):
    for y in range(y_len):
        if board[y][x] == "#":
            real_board[y].append(MapObject(len(real_board[y]), y, "#"))
            real_board[y].append(MapObject(len(real_board[y]), y, "#"))
        elif board[y][x] == ".":
            real_board[y].append(MapObject(len(real_board[y]), y, "."))
            real_board[y].append(MapObject(len(real_board[y]), y, "."))
        elif board[y][x] == "@":
            robot = MapObject(len(real_board[y]), y, "@")
            real_board[y].append(robot)
            real_board[y].append(MapObject(len(real_board[y]), y, "."))
        elif board[y][x] == "O":
            wide_obj = WideMapObject()
            real_board[y].append(wide_obj)
            real_board[y].append(wide_obj)


print_board(real_board)
for instruction in instructions[:20]:
    print(instruction)
    if instruction == "<":
        robot.move(-1, 0, real_board, None)
    elif instruction == ">":
        robot.move(1, 0, real_board, None)
    elif instruction == "^":
        robot.move(0, -1, real_board, None)
    elif instruction == "v":
        robot.move(0, 1, real_board, None)
    print_board(real_board)

print(sum_coordinates(real_board))
