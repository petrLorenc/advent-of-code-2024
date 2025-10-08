with open("input.txt", "r") as f:
    input_data = f.readlines()
    first_column = []
    mapping = {}
    for in_ in input_data:
        first, second = in_.split("   ")
        first_column.append(int(first))
        mapping.setdefault(int(second), []).append(second)

occurrences = 0
for first in first_column:
    occurrences += first * len(mapping.get(first, []))

print(occurrences)