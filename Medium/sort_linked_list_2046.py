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

    def sortLinkedList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        nums = []
        current = head

        while current.next:
            if current.next.val < 0:
                nums.append(current.next.val)
                current.next = current.next.next
            else:
                current = current.next

        dummy = ListNode(0)
        if nums:
            nums.sort()
            tail = dummy
            for num in nums:
                new_node = ListNode(num)
                tail.next = new_node
                tail = new_node

            curr = dummy
            while curr.next:
                curr = curr.next
            curr.next = head
        else:
            dummy.next = head

        return dummy.next

    def sortLinkedList2(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head

        while current.next:
            if current.next.val < 0:
                temp = current.next
                current.next = current.next.next
                temp.next = head
                head = temp
            else:
                current = current.next

        return head

    def print_list(self, head):
        current = head

        while current:
            print(current.val, end=' --> ')
            current = current.next


obj = Solution()
head = None
head = obj.append(0, head)
head = obj.append(2, head)
head = obj.append(-5, head)
head = obj.append(5, head)
head = obj.append(10, head)
head = obj.append(-10, head)
head = obj.sortLinkedList2(head)
obj.print_list(head)
