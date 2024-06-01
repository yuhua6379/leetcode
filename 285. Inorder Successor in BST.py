# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:

    def inorder_iter(self, root: TreeNode, result: list):
        result.append(root)
        if root.left is not None:
            self.inorder_iter(root.left, result)

        if root.right is not None:
            self.inorder_iter(root.right, result)

    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> Optional[TreeNode]:

        result = list()
        self.inorder_iter(root, result)

        result = sorted(result, key=lambda node: node.val)
        for idx, node in enumerate(result):
            if node == p:
                if len(result) == idx:
                    return None
                return result[idx + 1]

            

