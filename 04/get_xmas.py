with open("input.txt", "r") as f:
    input_data = f.readlines()

y_len = len(input_data)
x_len = len(input_data[0])

cnt = 0

for idx_line, line in enumerate(input_data):
    for idx_char, char in enumerate(line):
        if char != "X":
            continue
        # test horizontal right
        if idx_char + 3 < x_len:
            if line[idx_char + 1] == "M" and line[idx_char + 2] == "A" and line[idx_char + 3] == "S":
                print("Found MAS")
                cnt += 1
        # test horizontal left
        if idx_char - 3 >= 0:
            if line[idx_char - 1] == "M" and line[idx_char - 2] == "A" and line[idx_char - 3] == "S":
                print("Found SAM")
                cnt += 1
        # test vertical up
        if idx_line + 3 < y_len:
            if input_data[idx_line + 1][idx_char] == "M" and input_data[idx_line + 2][idx_char] == "A" and input_data[idx_line + 3][idx_char] == "S":
                print("Found MAS")
                cnt += 1
        # test vertical down
        if idx_line - 3 >= 0:
            if input_data[idx_line - 1][idx_char] == "M" and input_data[idx_line - 2][idx_char] == "A" and input_data[idx_line - 3][idx_char] == "S":
                print("Found SAM")
                cnt += 1
        # test diagonal up right
        if idx_line + 3 < y_len and idx_char + 3 < x_len:
            if input_data[idx_line + 1][idx_char + 1] == "M" and input_data[idx_line + 2][idx_char + 2] == "A" and input_data[idx_line + 3][idx_char + 3] == "S":
                print("Found MAS")
                cnt += 1
        # test diagonal up left
        if idx_line + 3 < y_len and idx_char - 3 >= 0:
            if input_data[idx_line + 1][idx_char - 1] == "M" and input_data[idx_line + 2][idx_char - 2] == "A" and input_data[idx_line + 3][idx_char - 3] == "S":
                print("Found MAS")
                cnt += 1
        # test diagonal down right
        if idx_line - 3 >= 0 and idx_char + 3 < x_len:
            if input_data[idx_line - 1][idx_char + 1] == "M" and input_data[idx_line - 2][idx_char + 2] == "A" and input_data[idx_line - 3][idx_char + 3] == "S":
                print("Found MAS")
                cnt += 1
        # test diagonal down left
        if idx_line - 3 >= 0 and idx_char - 3 >= 0:
            if input_data[idx_line - 1][idx_char - 1] == "M" and input_data[idx_line - 2][idx_char - 2] == "A" and input_data[idx_line - 3][idx_char - 3] == "S":
                print("Found MAS")
                cnt += 1
print(cnt)