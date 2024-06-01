from typing import List

from tester import Tester

cases = [
    ([3, 6, 7], [2, 4, 7, 9], 2),
    ([4, 6, 109, 111, 213, 215], [5, 110, 214], 1),
    ([0], [1000000000], 1000000000),
    ([6, 0, 4], [8, 7], 2),
    ([4, 7], [5, 9, 3], 3)
]

import bisect
import copy
MAX_INTEGER = 9999999999


def is_n_even(n):
    return n % 2 == 0


def get_grains_position_on_right(grains, hen_position):
    idx = bisect.bisect_left(grains, hen_position)
    if idx < 0 or idx >= len(grains):
        return None

    return idx


def get_grains_position_on_left(grains, hen_position):
    idx = get_grains_position_on_right(grains, hen_position)
    if idx is None:
        return None

    if grains[idx] == hen_position:
        return idx
    else:
        if idx - 1 < 0:
            return None
        else:
            return idx - 1


def forage_to_left_in_own_territory(index, hens, grains, distances):
    # 从当前位置，向左寻找谷物
    hen_position = hens[index]
    if index <= 0:
        # 如果这只鸡在最左边，就全是它的领地
        end = -1
    else:
        # 否则碰到另一只鸡就停止
        end = hens[index - 1]

    # 找一个比当前位置更左边或者就是当前位置的谷物
    idx = get_grains_position_on_left(grains, hen_position)
    if idx is None:
        return

    count = 0
    eat = 0
    last = hen_position
    for j in range(0, idx + 1):
        i = idx - j
        cur = grains[i]
        if cur <= end:
            # 如果提前发现了另一只鸡，就结束了，这就是这只鸡的领地
            return
        else:
            eat += 1
            count += abs(cur - last)
        last = cur
    if eat > 0:
        distances.append(count)


def forage_to_right_in_own_territory(index, hens, grains, distances):
    # 向右寻找吃的，包括本身，碰到下一只鸡就停
    hen_position = hens[index]
    if index >= len(hens) - 1:
        # 已经是最后一只鸡，就不会停了
        end = MAX_INTEGER
    else:
        # 否则下一只鸡就停
        end = hens[index + 1]

    # 找一个比自己位置右边或者就在自己位置的谷物
    idx = get_grains_position_on_right(grains, hen_position)
    if idx is None:
        return

    count = 0
    # 起点是鸡的位置
    last = hen_position
    eat = 0
    for i in range(idx, len(grains)):
        # 从找到的谷物往右走，直到没有饲料
        cur = grains[i]
        if cur >= end:
            # 如果提前发现了另一只鸡，就结束了，这就是这只鸡的领地
            break
        else:
            eat += 1
            count += (cur - last)
        last = cur
    if eat > 0:
        return distances.append(count)


class Solution:

    def minimumTime(self, hens: List[int], grains: List[int]) -> int:
        hens = sorted(hens)
        grains = sorted(grains)
        last = len(hens) - 1

        distances1 = []
        for i in range(1, len(hens)):
            forage_to_right_in_own_territory(i, hens, grains, distances1)

        forage_to_left_in_own_territory(0, hens, grains, distances1)
        # if is_n_even(len）)

        distances2 = []
        for i in range(0, len(hens) - 1):
            forage_to_left_in_own_territory(i, hens, grains, distances2)

        forage_to_right_in_own_territory(last, hens, grains, distances2)

        if len(distances1) > 0:
            solution1 = max(distances1)
        else:
            solution1 = MAX_INTEGER
        if len(distances2) > 0:
            solution2 = max(distances2)
        else:
            solution2 = MAX_INTEGER

        return min(solution1, solution2)


if __name__ == '__main__':
    Tester(cases, Solution, Solution.minimumTime).run()
