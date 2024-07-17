import math
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def __init__(self) -> None:
        self.head = None

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

    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head

        while current.next:
            curr_val = current.val
            next_val = current.next.val

            # find greatest common divisor
            gcd = self.find_gcd(curr_val, next_val)

            # insert gcd between pairs
            new_node = ListNode(gcd)
            new_node.next = current.next
            current.next = new_node

            current = current.next.next

        return head

    def insertGreatestCommonDivisors2(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head

        while current.next:
            curr_val = current.val
            next_val = current.next.val
            current.next, current = ListNode(
                math.gcd(curr_val, next_val), current.next), current.next

        return head

    def find_gcd(self, a: int, b: int) -> int:
        gcd = math.gcd(a, b)

        return gcd

    def print_list(self, head: Optional[ListNode]):
        current = head

        while current:
            print(str(current.val),  end=' --> ')
            current = current.next


obj = Solution()
head = None
head = obj.append(18, head)
head = obj.append(6, head)
head = obj.append(10, head)
head = obj.append(3, head)
head = obj.insertGreatestCommonDivisors2(head)
obj.print_list(head)
