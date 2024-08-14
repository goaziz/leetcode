from collections import defaultdict
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

    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        freq = defaultdict(int)
        current = head

        while current:
            freq[current.val] += 1
            current = current.next

        dummy = ListNode(0)
        tail = dummy

        for key, val in freq.items():
            if val == 1:
                new_node = ListNode(key)
                tail.next = new_node
                tail = new_node

        return dummy.next

    def deleteDuplicates2(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        tail = dummy

        while head:
            if head.next and head.val == head.next.val:
                while head.next and head.val == head.next.val:
                    head = head.next

                tail.next = head.next
            else:
                tail = tail.next

            head = head.next

        return dummy.next

    def print_list(self, head):
        current = head

        while current:
            print(current.val, end=' --> ')
            current = current.next


obj = Solution()
head = None
head = obj.append(1, head)
head = obj.append(2, head)
head = obj.append(3, head)
head = obj.append(3, head)
head = obj.append(3, head)
head = obj.append(4, head)
head = obj.append(4, head)
head = obj.append(5, head)
obj.print_list(head)
head = obj.deleteDuplicates2(head)
print()
obj.print_list(head)
