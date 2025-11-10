from functools import lru_cache
from generic_tester import GenericSolution


class Solution(GenericSolution):
    __name__ = "SolutionWithLRUCache"
    def solution(self, input_data: str):
        """
        """

        input_lines = input_data.strip().split("\n")
        options = input_lines[0]
        designs = input_lines[2:]

        option_mapping = {}

        for option in options.split(","):
            option = option.strip()
            option_mapping.setdefault(option[0], set()).add(option)

        designs = map(str.strip, designs)

        @lru_cache(maxsize=None)
        def try_pattern(design: str) -> int:
            if design == "":
                return 1
            response = 0
            for pattern in option_mapping.get(design[0], []):
                if design.startswith(pattern):
                    response += try_pattern(design[len(pattern) :])
            return response

        valid_count = 0
        for design in designs:
            response = try_pattern(design)
            if response:
                valid_count += response
        return str(valid_count)