with open("input_2.txt") as f:
    input_data = f.read()

board, instructions = input_data.split("\n\n")

instructions = instructions.replace("\n", "")
board = [list(x) for x in board.split("\n")]
x_len = len(board[0])
y_len = len(board)


def print_board(board):
    for row in board:
        print("".join([x.get_str() for x in row]))

def sum_coordinates(board):
    cnt = 0
    for x in range(x_len):
        for y in range(y_len):
            if board[y][x].get_str() == "O":
                cnt += (100 * y + x)
    return cnt

class MapObject:
    def __init__(self, x, y, representation):
        self.x = x
        self.y = y
        self.representation = representation  # it will be # for non-moving, . for empty and @ for actual robot

    def move(self, diff_x, diff_y, board) -> bool:
        if self.get_str() == "#":
            return False
        if self.can_move(diff_x, diff_y, board):
            # switch objects
            self.x += diff_x
            self.y += diff_y
            obj = board[self.y][self.x]
            board[self.y][self.x] = self
            board[self.y - diff_y][self.x - diff_x] = obj
            return True
        else:
            return False

    def get_str(self) -> str:
        return self.representation

    def can_move(self, diff_x, diff_y, board) -> bool:
        if 0 <= self.x + diff_x < x_len and 0 <= self.y + diff_y < y_len and board[self.y + diff_y][self.x + diff_x].get_str() == ".":
            return True
        if board[self.y + diff_y][self.x + diff_x].move(diff_x, diff_y, board):
            return True


robot: MapObject = None
for x in range(x_len):
    for y in range(y_len):
        board[y][x] = MapObject(x, y, board[y][x])
        if board[y][x].get_str() == "@":
            robot = board[y][x]

print_board(board)
for instruction in instructions:
    print(instruction)
    if instruction == "<":
        robot.move(-1, 0, board)
    elif instruction == ">":
        robot.move(1, 0, board)
    elif instruction == "^":
        robot.move(0, -1, board)
    elif instruction == "v":
        robot.move(0, 1, board)
    print_board(board)

print(sum_coordinates(board))