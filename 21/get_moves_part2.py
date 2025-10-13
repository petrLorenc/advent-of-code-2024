from functools import cache

with open("input_2.txt") as f:
    inputs = f.readlines()

inputs = list(map(str.strip, inputs))


def get_moves_for_keypad(code):
    """
    +---+---+---+
    | 7 | 8 | 9 |
    +---+---+---+
    | 4 | 5 | 6 |
    +---+---+---+
    | 1 | 2 | 3 |
    +---+---+---+
        | 0 | A |
        +---+---+
    """
    keypad_map = {
        "7": (0, 0),
        "8": (0, 1),
        "9": (0, 2),
        "4": (1, 0),
        "5": (1, 1),
        "6": (1, 2),
        "1": (2, 0),
        "2": (2, 1),
        "3": (2, 2),
        "AVOID": (3, 0),
        "0": (3, 1),
        "A": (3, 2),
    }
    position = "A"
    out = ""
    for c in code:
        y, x = keypad_map[c]
        init_y, init_x = keypad_map[position]
        up, down, left, right = "", "", "", ""

        for _ in list(range(init_y - y)):
            up += "^"
        for _ in range(y - init_y):
            down += "v"
        for _ in range(x - init_x):
            right += ">"
        for _ in list(range(init_x - x)):
            left += "<"

        avoid_y, avoid_x = keypad_map["AVOID"]
        if init_y == avoid_y and x == avoid_x:
            out += right + up + down + left + "A"
        elif y == avoid_y and init_x == avoid_x:
            out += right + up + down + left + "A"
        else:
            out += left + up + down + right + "A"

        position = c
    return out


robot_keypad_map = {"^": (0, 1), "A": (0, 2), "<": (1, 0), "v": (1, 1), ">": (1, 2)}


@cache
def get_moves_for_robot_keypad(init_c, final_c):
    """
        +---+---+
        | ^ | A |
    +---+---+---+
    | < | v | > |
    +---+---+---+
    """
    end_y, end_x = robot_keypad_map[final_c]
    start_y, start_x = robot_keypad_map[init_c]

    right = ">" * (end_x - start_x)
    left = "<" * (start_x - end_x)
    down = "v" * (end_y - start_y)
    up = "^" * (start_y - end_y)

    if start_y == 0 and end_x == 0:
        o = right + up + down + left + "A"
    elif end_y == 0 and start_x == 0:
        o = right + up + down + left + "A"
    else:
        o = left + up + down + right + "A"
    return o


outnum = 0


@cache
def get_moves_for_level(p, c, level) -> int:
    out = get_moves_for_robot_keypad(p, c)
    if level == 1:
        return len(out)
    else:
        return get_moves_for_level("A", out[0], level - 1) + sum(
            (get_moves_for_level(p, c, level - 1) for p, c in zip(out[0:], out[1:]))
        )


for input in inputs:
    print(input)
    first_code = get_moves_for_keypad(input)
    print(first_code)
    LEVEL = 25
    code = get_moves_for_level("A", first_code[0], LEVEL) + sum(
        get_moves_for_level(p, c, LEVEL) for p, c in zip(first_code[0:], first_code[1:])
    )
    # print(third_code)

    print(int(input[:-1]), code, int(input[:-1]) * code)
    outnum += int(input[:-1]) * code

print()
print()
print(outnum)
