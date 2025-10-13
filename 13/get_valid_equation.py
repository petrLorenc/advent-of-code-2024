"""
This is the input
Button A: X+94, Y+34
Button B: X+22, Y+67
Prize: X=8400, Y=5400

Parse the input and get the valid combination of X and Y for the prize.
"""

with open("input.txt") as f:
    input_data = f.read()

examples = []
for example in input_data.split("\n\n"):
    x1 = 0
    y1 = 0
    x2 = 0
    y2 = 0
    rx = 0
    ry = 0
    for line in example.split("\n"):
        if "Button A" in line:
            x1 = int(line.split("X+")[1].split(",")[0])
            y1 = int(line.split("Y+")[1])
        elif "Button B" in line:
            x2 = int(line.split("X+")[1].split(",")[0])
            y2 = int(line.split("Y+")[1])
        elif "Prize: " in line:
            rx = int(line.split("X=")[1].split(",")[0])
            ry = int(line.split("Y=")[1])
    examples.append((x1, y1, x2, y2, rx, ry))

print(examples)

cnt = 0
for x1, y1, x2, y2, rx, ry in examples:
    y = (x1 * ry - rx * y1) / (-y1 * x2 + x1 * y2)
    if y % 1 == 0:
        print(y)
        x = (rx - x2 * y) / x1
        if x % 1 == 0:
            print(x)
            cnt += 1 * y + 3 * x
print(cnt)
