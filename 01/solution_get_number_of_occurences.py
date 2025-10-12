from generic_tester import GenericSolution

class Solution(GenericSolution):
    """
    Count the number of occurrences where numbers in the first column match numbers in the second column.
    """
    def solution(self, input_data: str):
        input_data = input_data.splitlines()
        first_column = []
        mapping = {}
        for in_ in input_data:
            first, second = in_.split("   ")
            first_column.append(int(first))
            mapping.setdefault(int(second), []).append(second)

        occurrences = 0
        for first in first_column:
            occurrences += first * len(mapping.get(first, []))

        return occurrences
