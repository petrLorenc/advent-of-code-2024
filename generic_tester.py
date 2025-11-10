"""
Assumes the two entry points in each file (solution_basic_XY and solution_advanced_XY).
It will also assumes input files in a format input_XY.txt

Flow is as follows:
1. Load the inputs from the file
2. Provide these inputs to basic_XY and advanced_XY
3. Log the metrics
"""

import argparse
import importlib
import glob
from abc import abstractmethod
import multiprocessing
import time


def _wrapper_function(solution, input_data, queue: multiprocessing.Queue):
    start_time = time.perf_counter()
    # main part - actual solution call
    result = solution.solution(input_data)
    
    end_time = time.perf_counter()
    elapsed_time = end_time - start_time
    queue.put((result, elapsed_time))


class GenericSolution:
    @abstractmethod
    def solution(self, input_data: str):
        raise NotImplementedError("Solution not implemented")


class GenericTester:
    def __init__(self, problem_root):
        self.problem_root = problem_root
        self.inputs: dict[str, str] = {}
        self.solutions: dict[str, GenericSolution] = {}
        self.load_inputs()
        self.load_solution()
        print(
            f"Loaded {len(self.inputs)} inputs and {len(self.solutions)} solutions.\n"
        )

    def load_inputs(self):
        for file in sorted(glob.glob(f"{self.problem_root}/input*.txt")):
            with open(file, "r") as f:
                self.inputs[file] = f.read()

    def load_solution(self):
        for file in glob.glob(f"{self.problem_root}/solution_*.py"):
            module_name = file.replace("/", ".").replace(".py", "")
            module = importlib.import_module(
                name=module_name, package=self.problem_root
            )
            class_obj = getattr(module, "Solution")
            # Not optimal but it dynamically imports do not load the same class to use issubclass
            if class_obj.__bases__[0].__name__ == "GenericSolution":
                self.solutions[module_name] = class_obj()

    def format_result(
        self,
        solution_class: GenericSolution,
        input_file: str,
        time_taken: float,
        result: str,
    ):
        output = f"Used {solution_class.__class__.__name__}"
        output += f" on {input_file}"
        output += f" in {time_taken:.8f}s"
        output += f" with result: {result}"
        output += "\n"
        output += f"Approach: {solution_class.__class__.__doc__}"
        output += "\n" + "*" * 20 + "\n"
        return output

    def solve_problem(self):
        for input_data in self.inputs.values():
            for solution_name, solution in self.solutions.items():
                print(f"Running {solution_name.split('.')[-1]}...")
                print(f"{input_data[:30]=}...")
                queue = multiprocessing.Queue()
                process = multiprocessing.Process(target=_wrapper_function, args=(solution, input_data, queue))
                process.start()
                process.join(timeout=30)  # 30 seconds timeout
                if process.is_alive():
                    process.terminate()
                    process.join()
                    print(f"Solution {solution.__class__.__name__} timed out.\n")
                    continue
                else:
                    result, elapsed_time = queue.get()

                print(
                    self.format_result(
                        solution, list(self.inputs.keys())[0], elapsed_time, result
                    )
                )


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run solutions for a given problem.")
    parser.add_argument(
        "problem_root", type=str, help="The root directory of the problem (e.g., '01')."
    )
    args = parser.parse_args()
    tester = GenericTester(problem_root=args.problem_root)
    tester.solve_problem()
