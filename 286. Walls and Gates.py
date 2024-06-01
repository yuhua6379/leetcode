from enum import Enum
from typing import List

from tester import Tester

cases = [
    ([
         [2147483647, -1, 0, 2147483647],
         [2147483647, 2147483647, 2147483647, -1],
         [2147483647, -1, 2147483647, -1],
      [0, -1, 2147483647, 2147483647]], [[3, -1, 0, 1], [2, 2, 1, -1], [1, -1, 2, -1], [0, -1, 3, 4]]),
    ([[-1]], [[-1]])
]


class TypeOfRoom(Enum):
    Gate = 0
    Wall = 1
    Space = 2


class Solution:

    def which(self, num: int):
        if num == 0:
            return TypeOfRoom.Gate

        elif num == -1:
            return TypeOfRoom.Wall

        else:
            return TypeOfRoom.Space

    def locate_gates(self, rooms: list[list[int]]) -> list[tuple[int, int]]:
        gates = []
        for i in range(len(rooms)):
            for j in range(len(rooms[i])):
                if self.which(rooms[i][j]) is TypeOfRoom.Gate:
                    gates.append((i, j))
        return gates

    def up(self, i: int, j: int, rooms: list[list[int]]):
        if i == 0:
            return None, None
        i -= 1
        if self.which(rooms[i][j]) in (TypeOfRoom.Wall, TypeOfRoom.Gate):
            return None, None

        return i, j

    def down(self, i: int, j: int, rooms: list[list[int]]):
        if i == len(rooms) - 1:
            return None, None
        i += 1
        if self.which(rooms[i][j]) in (TypeOfRoom.Wall, TypeOfRoom.Gate):
            return None, None

        return i, j

    def left(self, i: int, j: int, rooms: list[list[int]]):
        if j == 0:
            return None, None
        j -= 1
        if self.which(rooms[i][j]) in (TypeOfRoom.Wall, TypeOfRoom.Gate):
            return None, None

        return i, j

    def right(self, i: int, j: int, rooms: list[list[int]]):
        if j == len(rooms[i]) - 1:
            return None, None
        j += 1
        if self.which(rooms[i][j]) in (TypeOfRoom.Wall, TypeOfRoom.Gate):
            return None, None

        return i, j

    def dfs(self, i: int, j: int, rooms: list[list[int]], steps: int, visited: set):
        # print(i, j, rooms[i][j], steps)
        # if steps > len(rooms) * len(rooms[i]):
        #     return
        if (i, j) in visited:
            return
        visited.add((i, j))

        if rooms[i][j] > steps:
            rooms[i][j] = steps

        ni, nj = self.up(i, j, rooms)
        if ni is not None:
            self.dfs(ni, nj, rooms, steps + 1, visited)

        ni, nj = self.left(i, j, rooms)
        if ni is not None:
            self.dfs(ni, nj, rooms, steps + 1, visited)

        ni, nj = self.down(i, j, rooms)
        if ni is not None:
            self.dfs(ni, nj, rooms, steps + 1, visited)

        ni, nj = self.right(i, j, rooms)
        if ni is not None:
            self.dfs(ni, nj, rooms, steps + 1, visited)

    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        for i, j in self.locate_gates(rooms):
            self.dfs(i, j, rooms, 0, set())
        return rooms


if __name__ == '__main__':
    Tester(cases, Solution, Solution.wallsAndGates).run()
