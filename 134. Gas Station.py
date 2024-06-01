import copy
import functools
from typing import List

from tester import Tester

cases = [
    # ([1, 2, 3, 4, 5], [3, 4, 5, 1, 2], 3),
    # ([2, 3, 4], [3, 4, 3], -1),
    ([4], [5], -1)
]


class Solution:

    def play_through(self, gas: List[int], index) -> bool:
        gas_tank = 0
        for _ in range(len(gas)):
            gas_tank += gas[index]
            if gas_tank < 0:
                return False, index
            index += 1
            index %= len(gas)

        return True, index

    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        for i, item in enumerate(cost):
            gas[i] -= item

        i = 0
        while True:
            if gas[i] < 0:
                i += 1
                if i >=len(gas):
                    return -1
                continue
            available, last_index = self.play_through(gas, i)
            if available:
                return i
            if last_index < i:
                return -1

            i = last_index

        return -1


if __name__ == '__main__':
    Tester(cases, Solution, Solution.canCompleteCircuit).run()
