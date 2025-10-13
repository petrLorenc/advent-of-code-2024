import copy
import networkx

graph = networkx.DiGraph()

with open("input_2.txt") as f:
    input_data = f.readlines()

values = {}
operations = {}
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
        operations[(name_a, operation, name_b)] = result
        to_determine.add(result)

print(values)
print(operations)
print(to_determine)


def get_output_mapping(values, operations, to_determine):
    values = copy.deepcopy(values)
    operations = copy.deepcopy(operations)
    to_determine = copy.deepcopy(to_determine)

    for _ in range(len(to_determine)):
        for (name_a, operation, name_b), result in operations.items():
            if name_a in values and name_b in values and result in to_determine:
                values[result] = apply_operation(
                    values[name_a], operation, values[name_b]
                )
                to_determine.remove(result)
        if not to_determine:
            break

    return values


def test_if_addition_work(values):
    sorted_values = list(sorted(values.items(), key=lambda x: x[0]))

    bin_number_z = ""
    bin_number_x = ""
    bin_number_y = ""
    for name, value in sorted_values:
        if name.startswith("z"):
            bin_number_z += str(value)
        if name.startswith("x"):
            bin_number_x += str(value)
        if name.startswith("y"):
            bin_number_y += str(value)
    return int(bin_number_z[::-1], 2) == int(bin_number_x[::-1], 2) + int(
        bin_number_y[::-1], 2
    )


new_values = get_output_mapping(values, operations, to_determine)
print(test_if_addition_work(new_values))


def get_result_key(ta, tb, top):
    for (a, op, b), dest in operations.items():
        if ((a, b) == (ta, tb) or (a, b) == (tb, ta)) and op == top:
            return dest
    return None


all_nodes = list(sorted(list(values.keys()) + list(to_determine)))

swapped = []
overall_carry = None
max_z_numbers = sum(1 for x in all_nodes if x.startswith("z"))
for i in range(max_z_numbers - 1):
    output_sum = get_result_key(f"x{i:02d}", f"y{i:02d}", "XOR")
    hidden_carry = get_result_key(f"x{i:02d}", f"y{i:02d}", "AND")
    carry, carry_1, carry_2 = 0, 0, 0
    sum_1, sum_2 = output_sum, output_sum

    if overall_carry is not None:
        carry_2 = get_result_key(carry, sum_1, "AND")
        if carry_2 is None:
            carry_1, sum_1 = sum_1, carry_1
            swapped.extend([sum_1, carry_1])
            carry_2 = get_result_key(carry, sum_1, "AND")

        sum_2 = get_result_key(carry, sum_1, "XOR")
        if sum_1 is not None and sum_1.startswith("z"):
            sum_1, sum_2 = sum_2, sum_1
            swapped.extend([sum_1, sum_2])

        if carry_1 is not None and carry_1.startswith("z"):
            carry_1, sum_2 = sum_2, carry_1
            swapped.extend([carry_1, sum_2])

        if carry_2 is not None and carry_2.startswith("z"):
            carry_2, sum_2 = sum_2, carry_2
            swapped.extend([carry_2, sum_2])

        new_carry = get_result_key(carry_2, carry_1, "OR")
    else:
        new_carry = None

    if (
        new_carry is not None
        and new_carry.startswith("z")
        and new_carry != f"z{max_z_numbers - 1:02d}"
    ):
        new_carry, sum_2 = sum_2, new_carry
        swapped.extend([new_carry, sum_2])

    if carry is not None:
        carry = new_carry
    else:
        carry = carry_1
print(swapped)
print(",".join(sorted(swapped)))

# swap values in operations
