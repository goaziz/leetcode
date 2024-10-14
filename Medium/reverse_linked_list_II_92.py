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
        while head:
            print(head.val, end=' --> ')
            head = head.next

    def reverse(self, nums, i, j):
        while i < j:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1

    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        node_vals = []
        current = head

        while current:
            node_vals.append(current.val)
            current = current.next

        self.reverse(node_vals, left - 1, right - 1)
        dummy = ListNode(-1)
        tail = dummy

        for val in node_vals:
            new_node = ListNode(val)
            tail.next = new_node
            tail = new_node

        return dummy.next

    def reverseBetween2(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head:
            return None

        curr, prev = head, None
        while left > 1:
            prev = curr
            curr = curr.next
            left, right = left - 1, right - 1

        tail, conn = curr, prev
        while right:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
            right -= 1

        if conn:
            conn.next = prev
        else:
            head = prev
        tail.next = curr
        return head

    def reverseBetween3(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(-1)
        dummy.next = head

        prev = dummy
        curr = dummy.next
        for _ in range(1, left):
            prev = prev.next
            curr = curr.next

        for _ in range(right - left):
            temp = curr.next
            curr.next = temp.next
            temp.next = prev.next
            prev.next = temp

        return dummy.next


obj = Solution()
head = None
head = obj.append(1, head)
head = obj.append(2, head)
head = obj.append(3, head)
head = obj.append(4, head)
head = obj.append(5, head)
obj.print_list(head)
print()
head = obj.reverseBetween(head, 2, 4)
obj.print_list(head)
