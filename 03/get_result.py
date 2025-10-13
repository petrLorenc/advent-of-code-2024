import re

result = 0
with open("input.txt") as f:
    input_data = f.read()
    operations = re.findall(r"mul\(\d+,\d+\)", input_data)
    print(operations)
    for operation in operations:
        num_a, num_b = re.findall(r"\d+", operation)
        result += int(num_a) * int(num_b)
    print(result)
