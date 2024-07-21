from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def __init__(self) -> None:
        self.head = None

    def push(self, data):
        new_node = ListNode(data)
        new_node.next = self.head
        self.head = new_node

        return self.head

    def reverse(self, head):
        previous = None
        current = head

        while current:
            next_node = current.next
            current.next = previous
            previous = current
            current = next_node

        head = previous
        return head

    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        dummy = ListNode(0)
        tail = dummy
        stack = []

        while current:

            while stack and stack[-1].val < current.val:
                stack.pop()

            stack.append(current)
            current = current.next

        for node in stack:
            tail.next = node
            tail = node

        return dummy.next

    def removeNodes2(self, head: Optional[ListNode]) -> Optional[ListNode]:
        head = self.reverse(head)
        previous = None
        current = head
        max_n = 0

        while current:
            max_n = max(max_n, current.val)

            if max_n > current.val:
                previous.next = current.next
                deleted = current
                current = current.next
                deleted.next = None
            else:
                previous = current
                current = current.next

        return self.reverse(head)

    def print_list(self, head):
        current = head

        while current:
            print(str(current.val), end=' --> ')
            current = current.next


obj = Solution()
head = obj.push(1)
head = obj.push(1)
head = obj.push(2)
head = obj.push(1)
obj.print_list(head)
print()
head = obj.removeNodes2(head)
obj.print_list(head)
