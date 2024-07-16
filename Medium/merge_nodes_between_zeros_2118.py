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
            while current.next is not None:
                current = current.next

            current.next = new_node

        return head

    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        new_head = None

        while current:
            current_sum = 0
            while current and current.val != 0:
                current_sum += current.val
                current = current.next

            if current_sum != 0:
                new_head = self.append(current_sum, new_head)

            if current:
                current = current.next

        return new_head

    def mergeNodes2(self, head: Optional[ListNode]) -> Optional[ListNode]:
        sentinel = ListNode(0)
        tail = sentinel
        current = head.next

        while current:
            current_sum = 0
            while current and current.val != 0:
                current_sum += current.val
                current = current.next

            if current_sum != 0:
                new_node = ListNode(current_sum)
                tail.next = new_node
                tail = new_node

            if current:
                current = current.next

        return sentinel.next

    def mergeNodes3(self, head: Optional[ListNode]) -> Optional[ListNode]:
        modify = head.next
        next_sum = modify

        while next_sum:
            current_sum = 0
            while next_sum.val != 0:
                current_sum += next_sum.val
                next_sum = next_sum.next

            modify.val = current_sum
            next_sum = next_sum.next
            modify.next = next_sum
            modify = modify.next

        return head.next

    def print_list(self, head):
        current = head

        while current:
            print(str(current.val), end=' --> ')
            current = current.next


obj = Solution()
head = None
head = obj.append(0, head)
head = obj.append(3, head)
head = obj.append(1, head)
head = obj.append(0, head)
head = obj.append(4, head)
head = obj.append(5, head)
head = obj.append(2, head)
head = obj.append(0, head)
obj.print_list(head)
new_head = obj.mergeNodes3(head)
print()
obj.print_list(new_head)
