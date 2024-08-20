from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
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

    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        curr = head
        greater_head = ListNode(0)
        less_head = ListNode(0)
        greater = greater_head
        less = less_head

        while curr:
            val = curr.val

            if x > val:
                less.next = curr
                less = less.next
            else:
                greater.next = curr
                greater = greater.next

            curr = curr.next

        less.next = greater_head.next
        greater.next = None

        return less_head.next

    def print_list(self, head):
        while head:
            print(head.val, end=' --> ')
            head = head.next


obj = Solution()
head = None
head = obj.append(1, head)
head = obj.append(4, head)
head = obj.append(3, head)
head = obj.append(2, head)
head = obj.append(5, head)
head = obj.append(2, head)
obj.print_list(head)
head = obj.partition(head, 3)
print()
obj.print_list(head)
