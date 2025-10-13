with open("input.txt", "r") as f:
    input_data = f.readlines()

y_len = len(input_data)
x_len = len(input_data[0])

cnt = 0

for idx_line, line in enumerate(input_data):
    for idx_char, char in enumerate(line):
        if char != "A":
            continue
        if (
            idx_char + 1 >= x_len
            or idx_line + 1 >= y_len
            or idx_char - 1 < 0
            or idx_line - 1 < 0
        ):
            continue
        if (
            input_data[idx_line + 1][idx_char + 1] == "M"
            and input_data[idx_line - 1][idx_char - 1] == "S"
            and input_data[idx_line + 1][idx_char - 1] == "M"
            and input_data[idx_line - 1][idx_char + 1] == "S"
        ):
            cnt += 1
        if (
            input_data[idx_line + 1][idx_char + 1] == "S"
            and input_data[idx_line - 1][idx_char - 1] == "M"
            and input_data[idx_line + 1][idx_char - 1] == "S"
            and input_data[idx_line - 1][idx_char + 1] == "M"
        ):
            cnt += 1
        if (
            input_data[idx_line + 1][idx_char + 1] == "M"
            and input_data[idx_line - 1][idx_char - 1] == "S"
            and input_data[idx_line + 1][idx_char - 1] == "S"
            and input_data[idx_line - 1][idx_char + 1] == "M"
        ):
            cnt += 1
        if (
            input_data[idx_line + 1][idx_char + 1] == "S"
            and input_data[idx_line - 1][idx_char - 1] == "M"
            and input_data[idx_line + 1][idx_char - 1] == "M"
            and input_data[idx_line - 1][idx_char + 1] == "S"
        ):
            cnt += 1
print(cnt)
