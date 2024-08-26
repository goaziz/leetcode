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
        head1 = self.reverse(l1)
        head2 = self.reverse(l2)

        carry = 0
        new_head = None
        while head1 or head2 or carry != 0:
            val1 = 0
            val2 = 0

            if head1:
                val1 = head1.val
                head1 = head1.next

            if head2:
                val2 = head2.val
                head2 = head2.next

            s = (val1 + val2 + carry) % 10
            carry = (val1 + val2 + carry) // 10
            new_head = ListNode(s, new_head)

        return new_head

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
