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

    def get_length(self, head: Optional[ListNode]) -> int:
        count = 0

        while head:
            head = head.next
            count += 1

        return count

    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Calculate the length of the list
        length = self.get_length(head)

        if length == 1 and n == 1:
            return None

        dummy = ListNode(0)
        dummy.next = head
        current = head
        previous = dummy

        while current:
            if length == n:
                previous.next = current.next
                break

            previous = current
            current = current.next
            length -= 1

        return dummy.next

    def removeNthFromEnd2(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        first = dummy
        second = dummy

        for i in range(n + 1):
            first = first.next

        while first:
            first = first.next
            second = second.next

        second.next = second.next.next
        return dummy.next

    def print_list(self, head):
        while head:
            print(head.val, end=' --> ')
            head = head.next


obj = Solution()
head = None
head = obj.append(1, head)
head = obj.append(2, head)
head = obj.append(3, head)
head = obj.append(4, head)
head = obj.append(5, head)
obj.print_list(head)
head = obj.removeNthFromEnd(head, 2)
print()
obj.print_list(head)
