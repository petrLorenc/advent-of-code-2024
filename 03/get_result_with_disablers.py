import re

result = 0
with open("input.txt") as f:
    input_data = f.read()
    do_indexes = list([x.start() for x in re.finditer("do\(\)", input_data)])
    # do_indexes = [1, 10, 100, 110]
    dont_indexes = list([x.start() for x in re.finditer("don't\(\)", input_data)])
    # dont_indexes = [20, 80, 105]
    operations = []

    actual_index = 0
    len_input = len(input_data)
    # len_input = 150
    max_idx = max(max(do_indexes), max(dont_indexes))
    do_idx = do_indexes.pop(0)
    dont_idx = dont_indexes.pop(0)
    last_used = 0

    enabled = True
    last_taken_do = True
    operation_find_index = re.compile(r"mul\(\d+,\d+\)")

    if do_idx < dont_idx:
        change_point = do_idx
    elif dont_idx < do_idx:
        change_point = dont_idx

    while actual_index < len(input_data):
        # print(do_idx, dont_idx, enabled)
        # print(actual_index, " ", min(do_idx, dont_idx), enabled)
        if enabled:
            operations.extend(
                operation_find_index.findall(
                    input_data[actual_index : min(do_idx, dont_idx)]
                )
            )
        actual_index = min(do_idx, dont_idx)

        if do_idx < dont_idx:
            if len(do_indexes) == 0:
                do_idx = len_input
            else:
                if not enabled:
                    pass
                else:
                    do_idx = do_indexes.pop(0)
            enabled = True
        elif dont_idx < do_idx:
            if len(dont_indexes) == 0:
                dont_idx = len_input
            else:
                if enabled:
                    pass
                else:
                    dont_idx = dont_indexes.pop(0)
            enabled = False
        else:
            break

    print(operations)
    for operation in operations:
        num_a, num_b = re.findall(r"\d+", operation)
        result += int(num_a) * int(num_b)
    print(result)
