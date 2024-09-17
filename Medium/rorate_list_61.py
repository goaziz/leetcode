from typing import List, Optional


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

    def print_list(self, head: Optional[ListNode]) -> str:
        while head:
            print(head.val, end=' --> ')
            head = head.next

    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        # Rotate list of integers to k places
        def rotate(nums: List[int], k: int) -> List[int]:
            n = len(nums)
            k = k % n
            nums[:] = nums[-k:] + nums[:-k]

            return nums

        if not head:
            return head

        nums = []
        current = head

        while current:
            nums.append(current.val)
            current = current.next

        nums = rotate(nums, k)
        dummy = ListNode()
        tail = dummy

        for num in nums:
            new_node = ListNode(num)
            tail.next = new_node
            tail = new_node

        return dummy.next

    def rotateRight2(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return None
        if not head.next:
            return head

        old_tail = head
        n = 1
        while old_tail.next:
            old_tail = old_tail.next
            n += 1
        old_tail.next = head

        new_tail = head
        for i in range(n - k % n - 1):
            new_tail = new_tail.next

        new_head = new_tail.next
        new_tail.next = None

        return new_head


obj = Solution()
head = None
head = obj.append(1, head)
head = obj.append(2, head)
head = obj.append(3, head)
head = obj.append(4, head)
head = obj.append(5, head)
obj.print_list(head)
head = obj.rotateRight2(head, 2)
print()
obj.print_list(head)
