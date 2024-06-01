import copy
import functools
from typing import List

from tester import Tester

cases = [
    ([[1, 3], [6, 9]], [2, 5], [[1, 5], [6, 9]]),
    ([[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], [4, 8], [[1, 2], [3, 10], [12, 16]]),
]


class Solution:
    def insert(self, intervals, newInterval):
        intervals.append(newInterval)
        intervals = sorted(intervals, key=lambda item: item[0])
        result = []
        cur = intervals[0]
        for interval in intervals[1:]:
            if cur[1] >= interval[0]:
                cur = [min(interval[0], cur[0]), max(interval[1], cur[1])]
            else:
                result.append(cur)
                cur = interval

        result.append(cur)
        return result



if __name__ == '__main__':
    Tester(cases, Solution, Solution.insert).run()
