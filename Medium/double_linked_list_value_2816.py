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

    def reverse(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        previous = None
        while current:
            next_node = current.next
            current.next = previous
            previous = current
            current = next_node

        return previous

    def push(self, data: int, head: Optional[ListNode]) -> Optional[ListNode]:
        new_node = ListNode(data)
        new_node.next = head
        head = new_node

        return head

    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        stack = []

        while current:
            stack.append(current.val)
            current = current.next

        val = 0
        new_head = None
        while stack or val != 0:
            new_head = ListNode(0, new_head)
    
            if stack:
                val += stack.pop() * 2
            new_head.val = val % 10
            val //= 10

        return new_head

    def doubleIt2(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Reverse the linked list
        head = self.reverse(head)
        current = head
        # Set variable to track remainder and previous node
        previous = None
        carry = 0

        while current:
            # Double the current node
            doubled = current.val * 2
            # Derive the primary value from number
            value = (doubled + carry) % 10
            # Calculate carry after doubling the current node value
            carry = (doubled + carry) // 10
            # Update the current node value
            current.val = value
            previous = current
            current = current.next

        # If there's a carry after ending, add extra node
        if carry:
            previous.next = ListNode(carry)

        return self.reverse(head)

    def print_list(self, head):
        current = head
        while current:
            print(current.val, end=' --> ')
            current = current.next


obj = Solution()
head = None
head = obj.append(9, head)
head = obj.append(9, head)
head = obj.append(9, head)
# head = obj.reverse(head)
obj.print_list(head)
print()
head = obj.doubleIt(head)
obj.print_list(head)
