from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def append(self, data: int, head: Optional[ListNode]) -> Optional[ListNode]:
        new_head = ListNode(data)

        if head is None:
            new_head.next = head
            head = new_head
        else:
            current = head
            while current.next:
                current = current.next
            current.next = new_head

        return head

    def reverse(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head

        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node

        return prev

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        dummy = ListNode(0)
        current = dummy

        while l1 or l2 or carry != 0:
            val1 = 0
            val2 = 0

            if l1:
                val1 = l1.val
                l1 = l1.next

            if l2:
                val2 = l2.val
                l2 = l2.next

            s = (val1 + val2 + carry) % 10
            carry = (val1 + val2 + carry) // 10
            new_head = ListNode(s)
            current.next = new_head
            current = current.next

        return dummy.next

    def print_list(self, head):
        while head:
            print(head.val, end=' --> ')
            head = head.next


obj = Solution()
head1 = None
head2 = None
head1 = obj.append(2, head1)
head1 = obj.append(4, head1)
head1 = obj.append(3, head1)
head2 = obj.append(5, head2)
head2 = obj.append(6, head2)
head2 = obj.append(4, head2)
head = obj.addTwoNumbers(head1, head2)
obj.print_list(head)
