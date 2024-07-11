from typing import Optional


class ListNode:
    def __init__(self, val, next=None) -> None:
        self.val = val
        self.next = next


class Solution:

    def push(self, val: int, head: Optional[ListNode]) -> Optional[ListNode]:
        new_node = ListNode(val)
        new_node.next = head
        head = new_node

        return head

    def deleteNodes(self, head: ListNode, m: int, n: int) -> ListNode:
        current = head
        previous = None
        i = 0

        while current is not None:
            if i == m:
                for _ in range(n):
                    if not current:
                        break
                    current = current.next
                previous.next = current
                i = 0
            else:
                i += 1
                previous = current
                current = current.next

        return head

    def print_list(self, head):
        current = head
        while current is not None:
            print(str(current.val), end=' --> ')
            current = current.next


obj = Solution()
m = 1
n = 3
head = None
for i in range(11, 0, -1):
    head = obj.push(i, head)
obj.print_list(head)
print()
head = obj.deleteNodes(head, m, n)
obj.print_list(head)
print()