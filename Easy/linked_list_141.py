from typing import Optional


class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
        self.pos = 0


class Solution:

    def __init__(self) -> None:
        self.head = None

    def push(self, data):
        new_node = ListNode(data)
        new_node.next = self.head
        new_node.pos = 0
        self.head = new_node

        return self.head

    def hasCycle(self, head: Optional[ListNode]) -> bool:
        hashset = set()
        current = head

        while current:
            if current in hashset:
                return True

            hashset.add(current)
            current = current.next

        return False

    def hasCycle2(self, head: Optional[ListNode]) -> bool:
        current = head

        while current:
            if current.pos == 1:
                return True

            current.pos = 1
            current = current.next

        return False

    def hasCycle3(self, head: Optional[ListNode]) -> bool:
        fast = head
        slow = head

        while slow and fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True

        return False


obj = Solution()
obj.push(1)
obj.push(2)
obj.push(3)
obj.push(4)
# obj.head.next.next.next.next = obj.head
print(obj.hasCycle(obj.head))
