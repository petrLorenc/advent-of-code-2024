import itertools

with open("input.txt") as f:
    input_data = f.readlines()

cnt = 0

for line in input_data:
    result, rest = line.strip().split(":")
    numbers = rest.strip().split(" ")
    # print(result)
    # print(numbers)

    for subset in itertools.product(["*", "+"], repeat=len(numbers) - 1):
        whole_expression = []
        actual_result = 0
        whole_expression.insert(0, "(")
        whole_expression.append(numbers[0])
        for operator, num2 in zip(subset, numbers[1:]):
            whole_expression.insert(0, "(")
            whole_expression.append(operator)
            whole_expression.append(num2)
            whole_expression.append(")")
        whole_expression.append(")")
        whole_expression = "".join(whole_expression)
        results = int(eval(whole_expression))

        if results == int(result):
            # print(results)
            cnt += results
            break
print(cnt)
