import copy
import functools
from typing import List

from tester import Tester

cases = [
    ([100, 4, 200, 1, 3, 2], 4),
    ([0, 3, 7, 2, 5, 8, 4, 6, 0, 1], 9)
]


class Solution:

    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)

        max_length = 0
        for n in num_set:
            if n - 1 not in num_set:
                i = 1
                while True:
                    if n + i not in num_set:
                        break
                    i += 1
                if i > max_length:
                    max_length = i

        return max_length


if __name__ == '__main__':
    Tester(cases, Solution, Solution.longestConsecutive).run()
