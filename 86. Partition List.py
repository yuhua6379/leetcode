from typing import List, Optional
from tester import Tester, ListNode


class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        real_head = ListNode()
        real_head.next = head
        last = real_head
        cur = head

        spotted_node = None
        spotted_last_node = None
        while cur is not None:
            if cur.val >= x and spotted_node is None:
                spotted_node = cur
                spotted_last_node = last

            if spotted_node is not None and cur.val < x:
                spotted_last_node.next = cur
                temp = cur.next
                cur.next = spotted_node
                last.next = temp
                cur = last.next
                spotted_last_node = spotted_last_node.next
                Tester.print_node_list(real_head.next)
            else:
                last = cur
                cur = cur.next

        return real_head.next


if __name__ == '__main__':
    real_head = Tester.list_to_node_list([1, 4, 2, 3, 2, 5, 2])
    s = Solution()
    ret = s.partition(real_head.next, 3)
    Tester.print_node_list(ret)

