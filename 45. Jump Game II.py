import copy
import functools
from typing import List

from tester import Tester

cases = [
    # ([2,3,1,1,4], 2),
    # ([2,3,0,1,4], 2),
    # ([0], 0),
    # ([2,1], 1),
    ([1,2,3], 2)
]


class Solution:
    def _jump(self, nums: List[int], time: int, foot_print, idx) -> int:
        if idx >= len(nums) - 1:
            return time
        if nums[idx] >= len(nums):
            return time + 1
        if nums[idx] == 0:
            return 100000000000000

        ret = []
        for i in range(0, nums[idx]):
            i = i + 1
            if idx + i not in foot_print:
                v = self._jump(nums, time, foot_print, idx + i)
            else:
                v = foot_print[idx + i]
            foot_print[idx + i] = v
            ret.append(v)

        return min(ret) + 1

    def jump(self, nums: List[int]) -> int:
        foot_print = dict()
        return self._jump(nums, 0, foot_print, 0)



if __name__ == '__main__':
    Tester(cases, Solution, Solution.jump).run()
