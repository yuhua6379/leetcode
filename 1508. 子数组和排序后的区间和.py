from typing import List

from tester import Tester

cases = [
    ([1, 2, 3, 4], 4, 1, 5, 13),
    ([1, 2, 3, 4], 4, 3, 4, 6),
    ([1, 2, 3, 4], 4, 1, 10, 50),

]


class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        lst = []
        for i in range(len(nums)):
            for j in range(i + 1, len(nums) + 1):
                lst.append(sum(nums[i: j]))

        lst = sorted(lst)

        return sum(lst[left-1: right]) % (10**9 + 7)


if __name__ == '__main__':
    Tester(cases, Solution, Solution.rangeSum).run()
