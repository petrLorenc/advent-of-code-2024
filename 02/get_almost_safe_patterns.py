all_ = 0
unsafe = 0
safe = 0


def check_if_correct(l):
    pairs = [x - y for x, y in zip(l, l[1:])]
    if all([0 < x <= 3 for x in pairs]):
        return True
    if all([-3 <= x < 0 for x in pairs]):
        return True
    return False


with open("input.txt", "r") as f:
    for line in f.readlines():
        all_ += 1
        split_line = [int(x) for x in line.strip().split(" ")]
        if check_if_correct(split_line):
            safe += 1
        else:
            for idx in range(len(split_line)):
                if idx == 0:
                    new_split_line = split_line[1:]
                elif idx == len(split_line) - 1:
                    new_split_line = split_line[:-1]
                else:
                    new_split_line = split_line[0:idx] + split_line[idx + 1:]
                if check_if_correct(new_split_line):
                    safe += 1
                    break
print(safe)

