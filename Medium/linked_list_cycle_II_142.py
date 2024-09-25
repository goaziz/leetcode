from typing import Optional


class ListNode:
    def __init__(self, x, next=None):
        self.val = x
        self.next = next


class Solution:

    def append(self, data: int, head: Optional[ListNode]) -> Optional[ListNode]:
        new_node = ListNode(data)
        if head is None:
            new_node.next = head
            head = new_node
        else:
            current = head
            while current.next:
                current = current.next
            current.next = new_node

        return head

    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast = head
        slow = head

        while slow and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                slow = head
                while slow != fast:
                    slow = slow.next
                    fast = fast.next
                return slow

        return None

    def detectCycle2(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        seen = set()

        while current:
            if current in seen:
                return current
            else:
                seen.add(current)
                current = current.next
        return None


obj = Solution()
head = None
head = obj.append(3, head)
head = obj.append(2, head)
head = obj.append(0, head)
head = obj.append(-4, head)
print(obj.detectCycle(head.next))
