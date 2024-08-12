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

    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        prev = dummy

        while head and head.next:
            temp = head.next
            head.next = temp.next
            prev.next = temp
            temp.next = head
            prev = head
            head = head.next
        
        return dummy.next

    def print_list(self, head):
        current = head

        while current:
            print(current.val, end=' --> ')
            current = current.next


obj = Solution()
head = None
head = obj.append(2, head)
head = obj.append(1, head)
head = obj.append(3, head)
head = obj.append(4, head)
obj.print_list(head)
head = obj.swapPairs(head)
print()
obj.print_list(head)
