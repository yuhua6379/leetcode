class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def print_tree(root):
    lines, *_ = _display_aux(root)
    for line in lines:
        print(line)


def _display_aux(root):
    """Returns list of strings, width, height, and horizontal coordinate of the root."""
    # No child.
    if root.right is None and root.left is None:
        line = '%s' % root.val
        width = len(line)
        height = 1
        middle = width // 2
        return [line], width, height, middle

    # Only left child.
    if root.right is None:
        lines, n, p, x = _display_aux(root.left)
        s = '%s' % root.val
        u = len(s)
        first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
        second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
        shifted_lines = [line + u * ' ' for line in lines]
        return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

    # Only right child.
    if root.left is None:
        lines, n, p, x = _display_aux(root.right)
        s = '%s' % root.val
        u = len(s)
        first_line = s + x * '_' + (n - x) * ' '
        second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
        shifted_lines = [u * ' ' + line for line in lines]
        return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

    # Two children.
    left, n, p, x = _display_aux(root.left)
    right, m, q, y = _display_aux(root.right)
    s = '%s' % root.val
    u = len(s)
    first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '
    second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
    if p < q:
        left += [n * ' '] * (q - p)
    elif q < p:
        right += [m * ' '] * (p - q)
    zipped_lines = zip(left, right)
    lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_lines]
    return lines, n + m + u, max(p, q) + 2, n + u // 2


class Tester:

    def __init__(self, cases: list[tuple], solution, function):
        self.cases = cases
        self.solution = solution
        self.function = function

    def run(self):
        solution = self.solution()

        for case in self.cases:
            case = list(case)
            except_result = case.pop(-1)
            result = self.function(solution, *case)
            if result != except_result:
                raise RuntimeError(f"except {except_result} but get {result}")

    @staticmethod
    def print_node_list(head: ListNode):
        s = []
        while head is not None:
            s.append(str(head.val))
            head = head.next
        print(", ".join(s))

    @staticmethod
    def list_to_node_list(l: list) -> ListNode:
        real_head = ListNode()
        cur = real_head
        for i in l:
            cur.next = ListNode(i)
            cur = cur.next
        return real_head

    @staticmethod
    def print_matrix(matrix):
        for line in matrix:
            print(line)
        print("")

    @staticmethod
    def print_tree(root: TreeNode):
        print_tree(root)


if __name__ == '__main__':
    # Example usage:
    # Construct a binary tree as an example
    #       1
    #      / \
    #     2   3
    #    /   / \
    #   4   5   6
    root = TreeNode(3)
    root.left = TreeNode(5)
    root.right = TreeNode(1)
    root.left.left = TreeNode(6)
    root.left.right = TreeNode(2)
    root.left.right.left = TreeNode(4)
    root.left.right.right = TreeNode(7)
    root.right.left = TreeNode(0)
    root.right.right = TreeNode(8)

    # Print the tree
    Tester.print_tree(root)
