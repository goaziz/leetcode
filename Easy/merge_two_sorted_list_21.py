from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def append(self, data, head: Optional[ListNode]) -> Optional[ListNode]:
        new_node = ListNode(data)

        if head is None:
            return new_node
        else:
            current = head
            while current.next is not None:
                current = current.next

            current.next = new_node

        return head

    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        arr = []
        curr1 = list1
        curr2 = list2

        while curr1 is not None:
            arr.append(curr1.val)
            curr1 = curr1.next

        while curr2 is not None:
            arr.append(curr2.val)
            curr2 = curr2.next

        arr.sort()
        new_head = None

        for num in arr:
            new_head = self.append(num, new_head)

        return new_head

    def mergeTwoLists2(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        prehead = ListNode(-1)
        prev = prehead

        while list1 and list2:
            if list1.val <= list2.val:
                prev.next = list1
                list1 = list1.next
            else:
                prev.next = list2
                list2 = list2.next
            prev = prev.next

        prev = list1 or list2
        return prehead.next

    def print_list(self, head):
        current = head

        while current is not None:
            print(str(current.val), end=' --> ')
            current = current.next


obj = Solution()
head1 = None
head1 = obj.append(1, head1)
head1 = obj.append(2, head1)
head1 = obj.append(3, head1)
obj.print_list(head1)
print()
head2 = None
head2 = obj.append(1, head2)
head2 = obj.append(3, head2)
head2 = obj.append(4, head2)
obj.print_list(head2)
print()
head = obj.mergeTwoLists2(head1, head2)
obj.print_list(head)
