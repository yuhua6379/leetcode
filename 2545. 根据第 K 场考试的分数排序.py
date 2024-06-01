from typing import List

from tester import Tester

cases = [
    ([[10, 6, 9, 1], [7, 5, 11, 2], [4, 8, 3, 15]], 2, [[7, 5, 11, 2], [10, 6, 9, 1], [4, 8, 3, 15]]),
    ([[3, 4], [5, 6]], 0, [[5, 6], [3, 4]])
]


class Solution:
    def sortTheStudents(self, score: List[List[int]], k: int) -> List[List[int]]:
        return sorted(score, key=lambda x: x[k], reverse=True)


if __name__ == '__main__':
    Tester(cases, Solution, Solution.sortTheStudents).run()
