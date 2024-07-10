from collections import defaultdict
from typing import Optional


class ListNode:
    def __init__(self, val, next=None) -> None:
        self.val = val
        self.next = next


class Solution:
    def append(self, data, head: Optional[ListNode]):
        new_node = ListNode(data)

        if head is None:
            new_node.next = head
            head = new_node
        else:
            current = head
            while current.next != None:
                current = current.next
            current.next = new_node

        return head

    def frequenciesOfElements(self, head: Optional[ListNode]) -> Optional[ListNode]:
        freq = defaultdict(int)
        current = head

        while current is not None:
            freq[current.val] += 1
            current = current.next

        new_head = None
        for value in freq.values():
            new_head = self.append(value, new_head)

        return new_head

    def frequenciesOfElements2(self, head: Optional[ListNode]) -> Optional[ListNode]:
        freq = {}
        freq_head = None
        current = head

        while current is not None:
            if current.val in freq:
                freq_node = freq[current.val]
                freq_node.val += 1
            else:
                new_node = ListNode(1, freq_head)
                freq[current.val] = new_node
                freq_head = new_node

            current = current.next

        return freq_head

    def print_list(self, head: Optional[ListNode]):
        current = head

        while current is not None:
            print(str(current.val), end=' --> ')
            current = current.next


obj = Solution()
head = None
head = obj.append(1, head)
head = obj.append(2, head)
head = obj.append(3, head)
head = obj.append(2, head)
# head = obj.frequenciesOfElements(head)
head = obj.frequenciesOfElements2(head)
obj.print_list(head)
