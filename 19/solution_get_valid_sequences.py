from generic_tester import GenericSolution


class Solution(GenericSolution):
    def solution(self, input_data: str):
        """
        This solution uses a recursive approach to check if each design can be formed
        using the given set of valid option patterns. It builds a mapping of starting
        characters to their corresponding patterns for efficient lookup.
        """

        input_lines = input_data.strip().split("\n")
        options = input_lines[0]
        designs = input_lines[2:]

        option_mapping = {}

        for option in options.split(","):
            option = option.strip()
            option_mapping.setdefault(option[0], set()).add(option)

        designs = map(str.strip, designs)

        def try_pattern(design: str) -> bool:
            if design == "":
                return True
            response = False
            for pattern in option_mapping.get(design[0], []):
                if design.startswith(pattern):
                    response = response or try_pattern(design[len(pattern) :])
                if response:
                    return response
            return response

        valid_count = sum(1 for design in designs if try_pattern(design))
        return str(valid_count)