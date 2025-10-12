"""
Two list of numbers (as columns) are given in the input file.
The task is to sum the differences between the

"""

from generic_tester import GenericSolution


class Solution(GenericSolution):
    """
    Calculate the sum of absolute differences between two columns of numbers.
    """

    def solution(self, input_data: str):
        first_column, second_column = [], []
        for in_ in input_data.splitlines():
            first, second = in_.split("   ")
            first_column.append(int(first))
            second_column.append(int(second))
        first_column = sorted(first_column)
        second_column = sorted(second_column)

        diff = 0
        for first, second in zip(first_column, second_column):
            diff += abs(first - second)

        return diff
