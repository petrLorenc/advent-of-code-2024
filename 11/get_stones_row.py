import copy

with open("input.txt") as f:
    input_data = f.read().strip()

stones = [x.strip() for x in input_data.split(" ")]

print(stones)

for _ in range(25):
    new_stones = []
    for stone in stones:
        if (len(stone) % 2) == 0:
            new_stones.append(str(int(stone[: len(stone) // 2])))
            new_stones.append(str(int(stone[len(stone) // 2 :])))
        elif stone == "0":
            new_stones.append("1")
        else:
            new_stones.append(str(int(stone) * 2024))
    stones = copy.deepcopy(new_stones)
    print(stones)
print(len(stones))
