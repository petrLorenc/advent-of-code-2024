import copy
import networkx

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

mermaid_payload = "stateDiagram-v2\n"
all_nodes = list(sorted(list(values.keys()) + list(to_determine)))
# for node in all_nodes:
#     mermaid_graph += f'{node}["{node}"]\n'

for (name_a, operation, name_b), result in operations.items():
    mermaid_payload += f"""{name_a} --> {name_a}+{name_b}+{operation}
{name_b} --> {name_a}+{name_b}+{operation}
{name_a}+{name_b}+{operation} --> {result}
"""

for node in all_nodes:
    if node.startswith("x") or node.startswith("y"):
        mermaid_payload += f"[*] --> {node}\n"
    if node.startswith("z"):
        mermaid_payload += f"{node} --> [*]\n"

mermaid_graph = (
    """
<body>
    <div class="mermaid">
    """
    + mermaid_payload
    + """
    </div>
 
    <script src="https://cdn.jsdelivr.net/npm/mermaid/dist/mermaid.min.js">
    </script>
    <script>
        mermaid.initialize({ startOnLoad: true });
    </script>
</body>
"""
)

with open("mermaid.html", "w") as f:
    f.write(mermaid_graph)


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
