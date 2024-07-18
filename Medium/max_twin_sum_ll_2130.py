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

    def pairSum(self, head: Optional[ListNode]) -> int:
        arr = []
        current = head

        while current:
            arr.append(current.val)
            current = current.next

        n = len(arr) - 1
        i = 0
        max_sum = 0

        while i < n:
            max_sum = max(max_sum, arr[i] + arr[n])
            i += 1
            n -= 1

        return max_sum


obj = Solution()
head = None
head = obj.append(1, head)
head = obj.append(100000, head)
print(obj.pairSum(head))
