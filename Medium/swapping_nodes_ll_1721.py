
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

    def print_list(self, head):
        current = head

        while current:
            print(current.val, end=' --> ')
            current = current.next

    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        nums = []
        current = head

        # collect list values to array
        while current:
            nums.append(current.val)
            current = current.next

        # swap elements by given k-th
        nums[k - 1], nums[-k] = nums[-k], nums[k - 1]

        dummy = ListNode(0)
        tail = dummy

        # re-create linked list after swapping
        for num in nums:
            neW_node = ListNode(num)
            tail.next = neW_node
            tail = neW_node

        return dummy.next

    def swapNodes2(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        length = 0
        front_node = None
        end_node = None
        current = head

        # find length of list and set the front node
        while current:
            length += 1
            if length == k:
                front_node = current
            current = current.next

        end_node = head
        # find and set end node at (length - k)th node
        for i in range(1, length - k + 1):
            end_node = end_node.next

        # swap front and end nodes
        temp = front_node.val
        front_node.val = end_node.val
        end_node.val = temp

        return head

    def swapNodes3(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        length = 0
        front_node = None
        end_node = None
        current = head

        while current:
            length += 1

            # end_node is k nodes behind current node
            # so when front node reaches k-th position
            # then end_node starts to iterate to get last k-th position
            if end_node:
                end_node = end_node.next

            if length == k:
                front_node = current
                end_node = head

            current = current.next

        temp = front_node.val
        front_node.val = end_node.val
        end_node.val = temp

        return head


obj = Solution()
head = None
head = obj.append(7, head)
head = obj.append(9, head)
head = obj.append(6, head)
head = obj.append(6, head)
head = obj.append(7, head)
head = obj.append(8, head)
head = obj.append(3, head)
head = obj.append(0, head)
head = obj.append(9, head)
head = obj.append(5, head)
obj.print_list(head)
print()
head = obj.swapNodes2(head, 5)
obj.print_list(head)
