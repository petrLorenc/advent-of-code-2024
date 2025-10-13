from generic_tester import GenericSolution


class Solution(GenericSolution):
    """
    Calculate the number of safe patterns in the input data. A pattern is considered safe if the differences between consecutive numbers
    are all positive and less than or equal to 3, or all negative and greater than or equal to -3.
    """

    def __init__(self):
        self.all = 0
        self.safe = 0

    def solution(self, input_data: str):
        for line in input_data.splitlines(keepends=False):
            self.all += 1
            split_line = [int(x) for x in line.strip().split(" ")]
            first_num = split_line[0]
            last_num = split_line[1]

            if first_num == last_num or abs(last_num - first_num) > 3:
                continue
            increasing = first_num < last_num
            is_safe = True
            for char in split_line[2:]:
                if (
                    increasing
                    and last_num < int(char)
                    and abs(last_num - int(char)) <= 3
                ):
                    pass
                elif (
                    not increasing
                    and last_num > int(char)
                    and abs(last_num - int(char)) <= 3
                ):
                    pass
                else:
                    is_safe = False
                last_num = int(char)
            if is_safe:
                self.safe += 1
        return self.all, self.safe
