from tester import TreeNode, Tester


class Solution:
    def spot_common_ancestors(self, root, p, q, layer, ancestors):
        root_p = root_q = False
        l_p = l_q = False
        r_p = r_q = False
        if root is not None:
            if root.val == p.val:
                root_p = True
            if root.val == q.val:
                root_q = True

            l_p, l_q = self.spot_common_ancestors(root.left, p, q, layer + 1, ancestors)
            r_p, r_q = self.spot_common_ancestors(root.right, p, q, layer + 1, ancestors)

        l_factor = (root_p or l_p or r_p)
        r_factor = (root_q or l_q or r_q)
        if l_factor and r_factor:
            ancestors.append((layer, root))

        return l_factor, r_factor

    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        ancestors = list()
        self.spot_common_ancestors(root, p, q, 0, ancestors)

        ancestors = sorted(ancestors, key=lambda x: x[0], reverse=True)

        if len(ancestors) <= 0:
            return None
        return ancestors[0][1]


if __name__ == '__main__':
    root = TreeNode(3)
    p = root.left = TreeNode(5)
    root.right = TreeNode(1)
    root.left.left = TreeNode(6)
    root.left.right = TreeNode(2)
    q = root.left.right.left = TreeNode(4)
    root.left.right.right = TreeNode(7)
    root.right.left = TreeNode(0)
    root.right.right = TreeNode(8)
    ret = Solution().lowestCommonAncestor(root, p, q)
    print(ret.val)

    Tester.print_tree(root)
