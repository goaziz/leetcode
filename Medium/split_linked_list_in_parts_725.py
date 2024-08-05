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

    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        nums = []
        current = head

        while current:
            nums.append(current.val)
            current = current.next

        n = len(nums)
        a, b = divmod(n, k)
        ans = []
        start = 0
        for i in range(k):
            # Calculate the end index
            end = start + a + (1 if i < b else 0)

            # Create new linked list by sub list
            dummy = ListNode(None)
            tail = dummy
            for num in nums[start:end]:
                new_node = ListNode(num)
                tail.next = new_node
                tail = new_node

            ans.append(dummy.next)
            # Update the start index for the next slice
            start = end

        return ans


obj = Solution()
head = None
head = obj.append(1, head)
head = obj.append(2, head)
head = obj.append(3, head)
# head = obj.append(4, head)
# head = obj.append(5, head)
# head = obj.append(6, head)
# head = obj.append(7, head)
# head = obj.append(8, head)
# head = obj.append(9, head)
# head = obj.append(10, head)
obj.splitListToParts(head, 5)
