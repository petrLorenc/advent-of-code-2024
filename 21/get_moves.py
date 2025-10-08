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
        "7": (0,0),
        "8": (0,1),
        "9": (0,2),
        "4": (1,0),
        "5": (1,1),
        "6": (1,2),
        "1": (2,0),
        "2": (2,1),
        "3": (2,2),
        "AVOID": (3,0),
        "0": (3,1),
        "A": (3,2)
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


def get_moves_for_robot_keypad(code):
    """
    +---+---+
    | ^ | A |
+---+---+---+
| < | v | > |
+---+---+---+
    """
    keypad_map = {
        "AVOID": (0, 0),
        "^": (0, 1),
        "A": (0, 2),
        "<": (1, 0),
        "v": (1, 1),
        ">": (1, 2)
    }
    position = "A"
    out = ""
    for c in code:
        y, x = keypad_map[c]
        init_y, init_x = keypad_map[position]
        up, down, left, right = "", "", "", ""

        for _ in range(x - init_x):
            right += ">"
        for _ in range(init_x - x):
            left += "<"
        for _ in range(y - init_y):
            down += "v"
        for _ in range(init_y - y):
            up += "^"

        avoid_y, avoid_x = keypad_map["AVOID"]
        if init_y == avoid_y and x == avoid_x:
            out += right + up + down + left + "A"
        elif y == avoid_y and init_x == avoid_x:
            out += right + up + down + left + "A"
        else:
            out += left + up + down + right + "A"
        position = c
    return out

outnum = 0

for input in inputs:
    print(input)
    first_code = get_moves_for_keypad(input)
    print(first_code)

    second_code = get_moves_for_robot_keypad(first_code)
    print(second_code)
    third_code = get_moves_for_robot_keypad(second_code)
    print(third_code)

    print(int(input[:-1]), len(third_code), int(input[:-1]) * len(third_code))
    outnum += int(input[:-1]) * len(third_code)

print()
print()
print(outnum)

# def reverse_get_moves_for_robot_keypad(code):
#     """
#     input is <v<A>>^AA<vA<A>>^AAvAA<^A>A<vA>^A<A>A<vA>^A<A>A<v<A>A>^AAvA<^A>A
#     output is based on
#     +---+---+
#     | ^ | A |
# +---+---+---+
# | < | v | > |
# +---+---+---+
#     """
#     keypad_map = {
#         "^": (0, 1),
#         "A": (0, 2),
#         "<": (1, 0),
#         "v": (1, 1),
#         ">": (1, 2)
#     }
#     output_position = "A"
#     out = ""
#     y, x = keypad_map[output_position]
#     for c in code:
#         if c == "A":
#             out += output_position
#
#         new_y, new_x = keypad_map[c]
#         if new_y > y:
#             out += "v"
#         elif new_y < y:
#             out += "^"
#         if new_x > x:
#             out += ">"
#         elif new_x < x:
#             out += "<"
#         out += "A"
#         y, x = new_y, new_x
#         output_position = c

"""
379A
^A ^^<<A >>A vvvA
<A>A <AAv<AA>>^A vAA^A v<AAA>^A
v<<A >>^A vA ^A || v<<A >>^A A v<A <A >>^AA vAA <^A >A  || v<A >^A A <A >A  || v<A <A >>^A A A vA <^A >A
<v<A >>^A vA ^A || <vA    <A A >>^A A vA <^A >A A vA ^A     <vA >^A A <A >A     <v<A >A >^A A A vA <^A >A
"""

"""
v<<A>>^AAv<A<A>>^AAvAA<^A>Av<A>^A<A>Av<A>^A<A>Av<A<A>>^AAvA<^A>A
<v<A>>^AA<vA<A>>^AAvAA<^A>A<vA>^A<A>A<vA>^A<A>A<v<A>A>^AAvA<^A>A
"""

"""
v<<A>>^Av<A<A>>^AAvAA<^A>Av<<A>>^AAvA^Av<A>^AA<A>Av<A<A>>^AAAvA<^A>A
<v<A>>^A<vA<A>>^AAvAA<^A>A<v<A>>^AAvA^A<vA>^AA<A>A<v<A>A>^AAAvA<^A>A
"""

"""
v<<A>>^AAAvA^Av<A<AA>>^AvAA<^A>Av<A<A>>^AAAvA<^A>Av<A>^A<A>A
<v<A>>^AAAvA^A<vA<AA>>^AvAA<^A>A<v<A>A>^AAAvA<^A>A<vA>^A<A>A
"""

"""
v<A<AA>>^AvAA<^A>Av<<A>>^AvA^Av<<A>>^AAvA<A>^A<A>Av<A<A>>^AAAvA<^A>A
<vA<AA>>^AvAA<^A>A<v<A>>^AvA^A<vA>^A<v<A>^A>AAvA^A<v<A>A>^AAAvA<^A>A
"""