from typing import List

from tester import Tester

cases = [
    ([10, 2], "102"),
    ([3, 30, 34, 5, 9], "3033459")
]


class MinNumberComponents:
    def __init__(self, val):
        self.val = val

    def __eq__(self, other):
        return self.val == self.val

    def __gt__(self, other):
        so = int(str(self.val) + str(other.val))
        os = int(str(other.val) + str(self.val))

        return so > os


class Solution:

    def minNumber(self, nums: List[int]) -> str:
        components = []
        for num in nums:
            components.append(MinNumberComponents(num))

        components = sorted(components)

        return "".join([str(component.val) for component in components])


if __name__ == '__main__':
    Tester(cases, Solution, Solution.minNumber).run()
