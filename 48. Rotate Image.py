from typing import List

from tester import Tester

cases = [
    ([[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]],
     [[15, 13, 2, 5], [14, 3, 4, 1], [12, 6, 8, 9], [16, 7, 10, 11]]),

]


class Solution:

    def matrix_line_to_cache(self, matrix: List[List[int]], start_point: tuple[int, int], length, direction: int):
        if direction == 0:
            return [matrix[start_point[0]][start_point[1] + i] for i in range(length)]

        if direction == 1:
            return [matrix[start_point[0] + i][start_point[1]] for i in range(length)]

        if direction == 2:
            return [matrix[start_point[0]][start_point[1] - i] for i in range(length)]

        if direction == 3:
            return [matrix[start_point[0] - i][start_point[1]] for i in range(length)]

    def cache_to_matrix_line(self, matrix: List[List[int]], start_point: tuple[int, int], cache: list, direction: int):
        if direction == 0:
            for idx, value in enumerate(cache):
                matrix[start_point[0]][start_point[1] + idx] = value

        if direction == 1:
            for idx, value in enumerate(cache):
                matrix[start_point[0] + idx][start_point[1]] = value

        if direction == 2:
            for idx, value in enumerate(cache):
                matrix[start_point[0]][start_point[1] - idx] = value

        if direction == 3:
            for idx, value in enumerate(cache):
                matrix[start_point[0] - idx][start_point[1]] = value

    def rotate_inner(self, matrix: List[List[int]], top, left, right, bottom):
        if top >= bottom and left >= right:
            return
        length = right - left + 1

        cache0 = self.matrix_line_to_cache(matrix, (top, left), length, 0)
        cache1 = self.matrix_line_to_cache(matrix, (top, right), length, 1)
        cache2 = self.matrix_line_to_cache(matrix, (bottom, right), length, 2)
        cache3 = self.matrix_line_to_cache(matrix, (bottom, left), length, 3)

        self.cache_to_matrix_line(matrix, (top, left), cache3, 0)
        self.cache_to_matrix_line(matrix, (top, right), cache0, 1)
        self.cache_to_matrix_line(matrix, (bottom, right), cache1, 2)
        self.cache_to_matrix_line(matrix, (bottom, left), cache2, 3)

        self.rotate_inner(matrix, top + 1, left + 1, right - 1, bottom - 1)

    def rotate(self, matrix: List[List[int]]):
        """
        Do not return anything, modify matrix in-place instead.
        """

        top = 0
        left = 0
        right = len(matrix[0]) - 1
        bottom = len(matrix) - 1
        for line in matrix:
            print(line)

        self.rotate_inner(matrix, top, left, right, bottom)

        print("\n")
        for line in matrix:
            print(line)

        return matrix


if __name__ == '__main__':
    Tester(cases, Solution, Solution.rotate).run()
