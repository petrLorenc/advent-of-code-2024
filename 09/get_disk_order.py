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
idx_start = 0
idx_end = len(real_memory) - 1

print(real_memory)

while idx_start < idx_end:
    while real_memory[idx_start] != ".":
        idx_start += 1
    while real_memory[idx_end] == ".":
        idx_end -= 1
    if idx_start < idx_end:
        real_memory[idx_start], real_memory[idx_end] = (
            real_memory[idx_end],
            real_memory[idx_start],
        )

print(real_memory)

cnt = 0
for idx, num in enumerate(real_memory[: real_memory.index(".")]):
    cnt += idx * int(num)
print(cnt)
