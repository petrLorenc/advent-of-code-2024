from generic_tester import GenericSolution


class Solution(GenericSolution):
    """
    Calculate the number of almost safe patterns in the input data.
    A pattern is considered almost safe if it can be made safe by removing at most one number.
    """

    def __init__(self):
        self.all = 0
        self.safe = 0

    def check_if_correct(self, l):
        pairs = [x - y for x, y in zip(l, l[1:])]
        if all([0 < x <= 3 for x in pairs]):
            return True
        if all([-3 <= x < 0 for x in pairs]):
            return True
        return False

    def solution(self, input_data: str):
        for line in input_data.splitlines(keepends=False):
            self.all += 1
            split_line = [int(x) for x in line.strip().split(" ")]
            if self.check_if_correct(split_line):
                self.safe += 1
            else:
                for idx in range(len(split_line)):
                    if idx == 0:
                        new_split_line = split_line[1:]
                    elif idx == len(split_line) - 1:
                        new_split_line = split_line[:-1]
                    else:
                        new_split_line = split_line[0:idx] + split_line[idx + 1 :]
                    if self.check_if_correct(new_split_line):
                        self.safe += 1
                        break
        return self.all, self.safe
