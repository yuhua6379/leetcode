from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def print_list(self, head: ListNode):
        while head is not None:
            print(head.val)
            head = head.next
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        real_head = ListNode()
        real_head.next = head
        last = real_head
        cur = head

        while cur is not None:
            found = 0
            while cur.next is not None and cur.val == cur.next.val:
                cur = cur.next
                found += 1
            if found >= 1:
                last.next = cur.next
                cur = cur.next
            else:
                last = cur
                cur = cur.next

        self.print_list(real_head.next)

        return real_head.next


if __name__ == '__main__':
    real_head = ListNode()
    cur = real_head
    for i in [1, 2, 3, 3, 4, 4, 5]:
        cur.next = ListNode(i)
        cur = cur.next
    Solution().deleteDuplicates(real_head.next)
