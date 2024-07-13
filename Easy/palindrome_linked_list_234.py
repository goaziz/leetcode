from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def append(self, head: Optional[ListNode], data: int) -> Optional[ListNode]:
        new_node = ListNode(data)

        if head is None:
            return new_node
        else:
            current = head
            while current.next is not None:
                current = current.next
            current.next = new_node

        return head

    def print_list(self, head: Optional[ListNode]) -> str:
        current = head

        while current is not None:
            print(str(current.val), end=' --> ')
            current = current.next

    def reverse(self, head: Optional[ListNode]) -> ListNode:
        current = head
        previous = None

        while current is not None:
            next_node = current.next
            current.next = previous
            previous = current
            current = next_node

        return previous

    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        fast = head
        slow = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        first_half = head
        second_head = self.reverse(slow)

        while second_head:
            if second_head.val != first_half.val:
                return False

            first_half = first_half.next
            second_head = second_head.next

        return True


obj = Solution()
head = None
head = obj.append(head, 1)
head = obj.append(head, 2)
head = obj.append(head, 3)
head = obj.append(head, 4)
obj.print_list(head)
print()
print(obj.isPalindrome(head))
