with open("input.txt") as f:
    input_data = f.read().strip()

is_file = True
file_idx = 0
real_memory = []

for num in input_data:
    if is_file:
        real_memory.extend([file_idx] * int(num))
        file_idx += 1
        is_file = False
    else:
        real_memory.extend(["."] * int(num))
        is_file = True

# resort
idx_end = len(real_memory) - 1

print(real_memory)

while idx_end >= 0:
    print(idx_end)
    size_block = 0
    num = None
    while real_memory[idx_end] != "." or num is None:
        if num is None:
            num = real_memory[idx_end]
        elif real_memory[idx_end] != num:
            break
        idx_end -= 1
        size_block += 1
    num = None

    idx_start = 0
    possible_start = 0
    possible_max_size = 0
    while idx_start < idx_end:
        while real_memory[idx_start] != ".":
            idx_start += 1
        if idx_start > idx_end:
            break
        possible_max_size = 0
        possible_start = idx_start
        while real_memory[idx_start] == ".":
            possible_max_size += 1
            idx_start += 1
        if possible_max_size >= size_block:
            real_memory[possible_start:possible_start + size_block], real_memory[idx_end + 1: idx_end + size_block + 1] = real_memory[
                                                                                                                          idx_end + 1: idx_end + size_block + 1], real_memory[
                                                                                                                                                                  possible_start:possible_start + size_block]
            # print(real_memory)
            break

print(real_memory)

cnt = 0
for idx, num in enumerate(real_memory):
    cnt += idx * (int(num) if num != "." else 0)
print(cnt)
