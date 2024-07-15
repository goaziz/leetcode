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

    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        current = head
        previous = None

        while current is not None and current.val == val:
            head = current.next
            current = head

        while current is not None:
            while current is not None and current.val != val:
                previous = current
                current = current.next

            if current is None:
                break

            previous.next = current.next
            current = previous.next

        return head

    def removeElements2(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        sentinel = ListNode(0)
        sentinel.next = head

        current = head
        previous = sentinel

        while current:
            if current.val == val:
                previous.next = current.next
            else:
                previous = current

            current = current.next

        return sentinel.next

    def print_list(self, head):
        current = head

        while current:
            print(str(current.val), end=' --> ')
            current = current.next


obj = Solution()
obj.push(2)
obj.push(1)
obj.push(2)
obj.push(3)
obj.push(4)
obj.push(3)
head = obj.removeElements2(obj.head, 3)
obj.print_list(head)
