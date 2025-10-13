from functools import lru_cache

with open("input_2.txt") as f:
    input_data = f.readlines()

options = input_data[0]
designs = input_data[2:]

option_mapping = {}

for option in options.split(","):
    option = option.strip()
    option_mapping.setdefault(option[0], set()).add(option)

print(option_mapping)
designs = map(str.strip, designs)


# @lru_cache(maxsize=None)
def try_pattern(design: str):
    if design == "":
        return True
    response = False
    for pattern in option_mapping.get(design[0], []):
        if design.startswith(pattern):
            response = response or try_pattern(design[len(pattern) :])
        if response:
            return response
    return response


# print(sum([1 for design in designs if try_pattern(design, option_mapping)]))
cnt = 0
for design in designs:
    response = try_pattern(design)
    print(design, response)
    if response:
        cnt += 1
    print(cnt)
