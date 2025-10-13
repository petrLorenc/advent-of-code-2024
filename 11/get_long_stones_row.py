import copy

with open("input.txt") as f:
    input_data = f.read().strip()

initial_stones = [x.strip() for x in input_data.split(" ")]
cache = {}


def get_after_N_steps(stone: str, N: int, cache: dict):
    if str(stone) in cache and N in cache[str(stone)]:
        return cache[str(stone)][N]
    if N == 1:
        return 1
    paths = 0
    if (len(stone) % 2) == 0:
        res = get_after_N_steps(str(int(stone[: len(stone) // 2])), N - 1, cache)
        cache.setdefault(str(int(stone[: len(stone) // 2])), {}).setdefault(N - 1, res)
        paths += res

        res = get_after_N_steps(str(int(stone[len(stone) // 2 :])), N - 1, cache)
        cache.setdefault(str(int(stone[: len(stone) // 2])), {}).setdefault(N - 1, res)
        paths += res
    elif stone == "0":
        res = get_after_N_steps("1", N - 1, cache)
        cache.setdefault("1", {}).setdefault(N - 1, res)
        paths += res
    else:
        res = get_after_N_steps(str(int(stone) * 2024), N - 1, cache)
        cache.setdefault(str(int(stone) * 2024), {}).setdefault(N - 1, res)
        paths += res
    return paths


N = 76
# 3935565 31753 437818 7697 5 38 0 123
cnt = 0
for stone in initial_stones:
    print(x := get_after_N_steps(stone, N, cache))
    cnt += x
print(cnt)
