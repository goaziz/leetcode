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

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        curr1 = l1
        curr2 = l2
        stack1 = []
        stack2 = []

        while curr1 or curr2:
            if curr1:
                stack1.append(curr1.val)
                curr1 = curr1.next

            if curr2:
                stack2.append(curr2.val)
                curr2 = curr2.next

        carry = 0
        new_head = None
        while stack1 or stack2 or carry != 0:
            val1 = 0
            val2 = 0

            if stack1:
                val1 = stack1.pop()

            if stack2:
                val2 = stack2.pop()
            s = (val1 + val2 + carry) % 10
            carry = (val1 + val2 + carry) // 10
            new_head = ListNode(s, new_head)

        return new_head

    def addTwoNumbers2(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        curr1 = l1
        curr2 = l2
        prev1 = None
        prev2 = None
        new_head = None
        while curr1 or curr2:
            val1 = 0
            val2 = 0
            
            if curr1:
                val1 = curr1.val
            
            if curr2:
                val2 = curr2.val
            
            s = val1 + val2
            new_head = ListNode(0, new_head)
            if s < 10:
                new_head.val = s
            
            

    def print_list(self, head):

        while head:
            print(head.val, end=' --> ')
            head = head.next


obj = Solution()
head1 = None
head2 = None
head1 = obj.append(7, head1)
head1 = obj.append(2, head1)
head1 = obj.append(4, head1)
head1 = obj.append(3, head1)
head2 = obj.append(5, head2)
head2 = obj.append(6, head2)
head2 = obj.append(4, head2)
obj.print_list(head1)
print()
obj.print_list(head2)
print()
head = obj.addTwoNumbers(head1, head2)
obj.print_list(head)
