class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverse(self, head):
        prev = None
        current = head

        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        head = prev

    def plusOne(self, head: ListNode) -> ListNode:
        self.reverse(head)
        carry = 1
        current = head

        while current:
            new_val = current.val + carry
            carry = new_val // 10
            current.val = new_val % 10

            if carry == 0:
                break
            if not current.next and carry > 0:
                carry = 0
            current = current.next

        self.reverse(head)
        return head
