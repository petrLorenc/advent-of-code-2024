with open("input_2.txt") as f:
    input_data = f.readlines()

values = {}
operations = []
to_determine = set()

def apply_operation(value_a, operator, value_b):
    if operator == "AND":
        return value_a & value_b
    if operator == "OR":
        return value_a | value_b
    if operator == "XOR":
        return value_a ^ value_b


for line in input_data:
    if ":" in line:
        name, value = line.strip().split(": ")
        values[name] = int(value)
    if " -> " in line:
        pair, result = line.strip().split(" -> ")
        name_a, operation, name_b = pair.strip().split(" ")
        operations.append((name_a, operation, name_b, result))
        if name_a in values and name_b in values:
            values[result] = apply_operation(values[name_a], operation, values[name_b])
        else:
            to_determine.add(result)

print(values)
print(operations)
print(to_determine)

for _ in range(len(to_determine)):
    for name_a, operation, name_b, result in operations:
        if name_a in values and name_b in values and result in to_determine:
            values[result] = apply_operation(values[name_a], operation, values[name_b])
            to_determine.remove(result)

print()
print(sorted_values := list(sorted(values.items(), key=lambda x: x[0])))
print(operations)
print(to_determine)

bin_number = ""
for name, value in sorted_values:
    if name.startswith("z"):
        print(name)
        bin_number += str(value)
bin_number = bin_number[::-1]
print(bin_number)
print(int(bin_number, 2))