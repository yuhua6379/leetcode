from enum import Enum
from typing import List

from tester import Tester

cases = [
    (8, [[0, 3], [0, 4], [1, 3], [2, 4], [2, 7], [3, 5], [3, 6], [3, 7], [4, 6]],
     [[], [], [], [0, 1], [0, 2], [0, 1, 3], [0, 1, 2, 3, 4], [0, 1, 2, 3]]),
    (5, [[0, 1], [0, 2], [0, 3], [0, 4], [1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]],
     [[], [0], [0, 1], [0, 1, 2], [0, 1, 2, 3]]),
]


def record_parent(parent_record: set, node, paths):
    if node in paths:
        for parent_node in paths[node]:
            if parent_node not in parent_record:
                parent_record.add(parent_node)
                record_parent(parent_record, parent_node, paths)


class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:

        paths = {}
        # 计算所有反向路径
        for edge in edges:
            if edge[1] not in paths:
                paths[edge[1]] = set()
            paths[edge[1]].add(edge[0])

        parent_records = []
        for i in range(n):
            parent_record = set()
            record_parent(parent_record, i, paths)
            parent_record = sorted(list(parent_record))
            parent_records.append(parent_record)

        return parent_records


if __name__ == '__main__':
    Tester(cases, Solution, Solution.getAncestors).run()
