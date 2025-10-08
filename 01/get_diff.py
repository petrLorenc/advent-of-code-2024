"""
Two list of numbers (as columns) are given in the input file.
The task is to sum the differences between the

"""

with open("input.txt", "r") as f:
    input_data = f.readlines()
    first_column, second_column = [], []
    for in_ in input_data:
        first, second = in_.split("   ")
        first_column.append(int(first))
        second_column.append(int(second))
first_column = sorted(first_column)
second_column = sorted(second_column)

diff = 0
for first, second in zip(first_column, second_column):
    diff += abs(first - second)

print(diff)