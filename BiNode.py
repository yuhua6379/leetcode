
class BiNode:

    def __init__(self, val):
        self.val = val
        self.last = None
        self.next = None

    @staticmethod
    def switch(head, node1, node2):
        next_ = node2.next
        last_ = node1.last
        if next_ is None:
            head.last = node1
        else:
            next_.last = node1

        last_.next = node2

        node1.last = node2
        node1.next = next_

        node2.last = last_
        node2.next = node1

    @staticmethod
    def insert(head, node):
        next_ = head.next
        head.next = node
        if head.last is None:
            head.last = node
        if next_ is not None:
            next_.last = node

        node.last = head
        node.next = next_

    @staticmethod
    def remove_last(head):
        new_tail = head.last.last
        head.last = new_tail
        new_tail.next = None


if __name__ == '__main__':
    head = BiNode(None)
    head.next = None
    head.last = None

    n1 = BiNode(1)
    n2 = BiNode(2)
    n3 = BiNode(3)
    BiNode.insert(head, n1)
    BiNode.insert(head, n2)
    BiNode.insert(head, n3)

    cur = head
    while cur:
        print(cur.val)
        cur = cur.next

    BiNode.switch(head, n3, n2)

    cur = head
    while cur:
        print(cur.val)
        cur = cur.next
