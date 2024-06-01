from typing import List

from tester import Tester

cases = [
    # ([7, 4, 5, 3, 8], [[0, 2, 2], [4, 2, 4], [2, 13, 1000000000]], [True, False, True]),
    #
    # (
    # [5, 2, 6, 4, 1], [[3, 1, 2], [4, 10, 3], [3, 10, 100], [4, 100, 30], [1, 3, 1]], [False, True, True, False, False]),
    #
    # ([13, 45, 31, 29, 13, 20, 11, 33, 18, 13, 10, 39, 43, 36, 5, 38, 27, 38, 10, 33, 46, 17, 20, 28, 41, 29, 3, 35, 38,
    #   46, 32, 7, 37, 5, 27, 15, 46, 9, 11, 37, 47, 44, 48, 34, 37, 12, 3, 37, 29, 25, 7, 34, 45, 23, 17, 10, 46, 5, 37,
    #   34, 5, 45, 5], [[13, 4, 91]], [True]),

    ([16, 38, 8, 41, 30, 31, 14, 45, 3, 2, 24, 23, 38, 30, 31, 17, 35, 4, 9, 42, 28, 18, 37, 18, 14, 46, 11, 13, 19, 3,
      5, 39, 24, 48, 20, 29, 4, 19, 36, 11, 28, 49, 38, 16, 23, 24, 4, 22, 29, 35, 45, 38, 37, 40, 2, 37, 8, 41, 33, 8,
      40, 27, 13, 4, 33, 5, 8, 14, 19, 35, 31, 8, 8], [[43,1054,49]], [False])
]


class Solution:
    def canEat(self, candiesCount: List[int], queries: List[List[int]]) -> List[bool]:
        results = []
        for query in queries:
            favoriteTypei = query[0]
            favoriteDayi = query[1]
            dailyCapi = query[2]
            if dailyCapi == 0:
                # 不给吃肯定不行啊..
                results.append(False)
                continue

            # 最喜欢的前一天最高吃的数量
            max_eating_quantities = favoriteDayi * dailyCapi
            # 最喜欢的前一天最低吃的数量
            min_eating_quantities = query[1] - 1

            # 0-i类糖果总数
            unitil_i_totalCandiesCount = 0
            for i in range(favoriteTypei):
                unitil_i_totalCandiesCount += candiesCount[i]
            favoriteCount = candiesCount[favoriteTypei]

            # 吃第i类糖果，一天最少吃1个，就是n天最低吃n个，最多吃n*dailyCapi个

            if unitil_i_totalCandiesCount >= max_eating_quantities:
                # 吃不到，情况1：
                # 努力全吃，都吃不完0 ~ i-1的库存
                results.append(False)
            elif unitil_i_totalCandiesCount + favoriteCount < min_eating_quantities:
                # 吃不到，情况2：
                # 尽力不吃，都把库存+喜欢的糖果吃完了
                results.append(False)
            else:
                results.append(True)

        return results


if __name__ == '__main__':
    Tester(cases, Solution, Solution.canEat).run()
