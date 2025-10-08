with open("input_2.txt") as f:
    input_data = f.read()

key_or_lock = input_data.split("\n\n")

keys = []
locks = []


def get_columns(lines):
    columns = []
    for idx_column in range(len(lines[0])):
        c = "".join([line[idx_column] for line in split_lines])
        columns.append(c.count("#") - 1)
    return columns


for k_or_l in key_or_lock:
    split_lines = k_or_l.split("\n")
    if split_lines[0].startswith("....."):
        keys.append(get_columns(split_lines))
    if split_lines[0].startswith("#####"):
        locks.append(get_columns(split_lines))
print(keys)
print(locks)

matching = 0

for key in keys:
    for lock in locks:
        if all(k + l <= 5 for k, l in zip(key, lock)):
            matching += 1
print(matching)
