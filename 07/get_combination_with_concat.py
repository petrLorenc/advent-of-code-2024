import itertools

with open("input.txt") as f:
    input_data = f.readlines()

cnt = 0

for line in input_data:
    result, rest = line.strip().split(":")
    numbers = [int(x) for x in rest.strip().split(" ")]
    # print(result)
    # print(numbers)

    for subset in itertools.product(["*", "+", "||"], repeat=len(numbers) - 1):
        whole_expression = []
        actual_result = numbers[0]
        for operator, num2 in zip(subset, numbers[1:]):
            if operator == "+":
                actual_result += num2
            if operator == "*":
                actual_result *= num2
            if operator == "||":
                actual_result = int(str(actual_result) + str(num2))

        if actual_result == int(result):
            # print(results)
            cnt += actual_result
            break
print(cnt)