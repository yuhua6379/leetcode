from typing import Optional

from tester import TreeNode, Tester


class Solution:
    def __init__(self):
        self.layered_array = dict()

    def iter(self, root, layer):
        if root is None:
            if layer not in self.layered_array:
                self.layered_array[layer] = list()
            self.layered_array[layer].append(None)
        else:
            if layer not in self.layered_array:
                self.layered_array[layer] = list()

            self.layered_array[layer].append(root.val)
            self.iter(root.left, layer + 1)
            self.iter(root.right, layer + 1)

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:

        self.iter(root, 0)
        print(self.layered_array)
        for array in self.layered_array.values():
            if len(array) == 1:
                continue
            mid = int(len(array) / 2)
            print(array[:mid])
            print(array[mid:][::-1])
            if array[:mid] != array[mid:][::-1]:
                return False
        return True



if __name__ == '__main__':
    root = TreeNode(2)
    root.left = TreeNode(3)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.left.right.left = TreeNode(8)
    root.left.right.right = TreeNode(9)

    root.right.left = TreeNode(5)
    root.right.left.left = TreeNode(9)
    root.right.left.right = TreeNode(8)
    root.right.right = TreeNode(4)

    # root = TreeNode(1)
    # root.left = TreeNode(2)
    # root.right = TreeNode(2)
    # root.left.left = TreeNode(None)
    # root.left.right = TreeNode(3)
    #
    # root.right.left = TreeNode(None)
    # root.right.right = TreeNode(3)
    ret = Solution().isSymmetric(root)
    print(ret)

    Tester.print_tree(root)
