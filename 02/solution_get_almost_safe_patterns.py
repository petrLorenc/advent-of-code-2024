from typing import List, Tuple
from generic_tester import GenericSolution


# Constants for safety criteria
MIN_POSITIVE_DIFF = 1
MAX_POSITIVE_DIFF = 3
MIN_NEGATIVE_DIFF = -3
MAX_NEGATIVE_DIFF = -1


class Solution(GenericSolution):
    """
    Solution for Advent of Code Day 2: Red-Nosed Reports
    
    Calculate the number of almost safe patterns in the input data.
    A pattern is considered almost safe if it can be made safe by removing at most one number.
    
    Safety criteria:
    - A sequence is safe if all consecutive differences are either:
      * All positive and between 1-3 (inclusive), or
      * All negative and between -3 to -1 (inclusive)
    """

    def __init__(self) -> None:
        """Initialize counters for tracking patterns."""
        self.total_patterns: int = 0
        self.safe_patterns: int = 0

    def is_safe_sequence(self, sequence: List[int]) -> bool:
        """
        Check if a sequence is safe based on the following criteria:
        - All differences between consecutive elements are between 1 and 3 (inclusive), OR
        - All differences between consecutive elements are between -3 and -1 (inclusive)
        
        Args:
            sequence: List of integers to check
            
        Returns:
            True if the sequence is safe, False otherwise
        """
        if len(sequence) < 2:
            return True
            
        consecutive_differences = [x - y for x, y in zip(sequence, sequence[1:])]
        
        # Check if all differences are positive and within valid range
        if all(MIN_POSITIVE_DIFF <= diff <= MAX_POSITIVE_DIFF for diff in consecutive_differences):
            return True
            
        # Check if all differences are negative and within valid range
        if all(MIN_NEGATIVE_DIFF <= diff <= MAX_NEGATIVE_DIFF for diff in consecutive_differences):
            return True
            
        return False

    def generate_sequences_with_one_removed(self, sequence: List[int]) -> List[List[int]]:
        """
        Generate all possible sequences by removing exactly one element.
        
        Args:
            sequence: Original sequence to modify
            
        Returns:
            List of sequences, each with one element removed from the original
        """
        return [sequence[:idx] + sequence[idx + 1:] for idx in range(len(sequence))]

    def solution(self, input_data: str) -> Tuple[int, int]:
        """
        Process input data and count safe and almost-safe patterns.
        
        Args:
            input_data: Multi-line string where each line contains space-separated integers
            
        Returns:
            Tuple containing (total_patterns, safe_patterns)
        """
        for line in input_data.splitlines(keepends=False):
            self.total_patterns += 1
            sequence = [int(number) for number in line.strip().split()]
            
            if self.is_safe_sequence(sequence):
                self.safe_patterns += 1
            else:
                # Try removing one element to make it safe
                modified_sequences = self.generate_sequences_with_one_removed(sequence)
                for modified_sequence in modified_sequences:
                    if self.is_safe_sequence(modified_sequence):
                        self.safe_patterns += 1
                        break
                        
        return self.total_patterns, self.safe_patterns
