from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        nums = []
        current = head

        while current.next:
            if current.next.val < 0:
                nums.append(current.next.val)
                current.next = current.next.next
            else:
                current = current.next

        dummy = ListNode(0)
        if nums:
            nums.sort()
            tail = dummy
            for num in nums:
                new_node = ListNode(num)
                tail.next = new_node
                tail = new_node

        return dummy.next
