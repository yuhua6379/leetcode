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

    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        count = 0
        cur = head
        last = None
        while cur is not None:
            last = cur
            cur = cur.next
            count += 1
        if last is not None:
            last.next = head

        cur = head
        k = k % count
        for _ in range(count - k - 1):
            cur = cur.next

        head = cur.next
        cur.next = None
        return head


if __name__ == '__main__':
    real_head = ListNode()
    cur = real_head
    for i in [0, 1, 2]:
        cur.next = ListNode(i)
        cur = cur.next
    s = Solution()
    ret = s.rotateRight(real_head.next, 4)
    # 0 012
    # 1 201
    # 2 120
    # 3 012
    # 4 201
    s.print_list(ret)

