all_ = 0
unsafe = 0
safe = 0

with open("input.txt", "r") as f:
    for line in f.readlines():
        all_ += 1
        split_line = line.strip().split(" ")
        first_num = int(split_line[0])
        last_num = int(split_line[1])

        if first_num == last_num or abs(last_num - first_num) > 3:
            continue
        increasing = first_num < last_num
        is_safe = True
        for char in split_line[2:]:
            if increasing and last_num < int(char) and abs(last_num - int(char)) <= 3:
                pass
            elif not increasing and last_num > int(char) and abs(last_num - int(char)) <= 3:
                pass
            else:
                is_safe = False
            last_num = int(char)
        if is_safe:
            safe += 1
print(safe)


