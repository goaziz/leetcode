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

    def print_list(self, head):
        while head:
            print(head.val, end=' --> ')
            head = head.next


    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        stack = []
        ans = []
        current = head
        index = 0

        while current:
            val = current.val
            ans.append(0)
            
            while stack and val > stack[-1][1]:
                idx = stack.pop()[0]
                ans[idx] = val

            stack.append([index, val])
            index += 1
            current = current.next

        return ans

    def nextLargerNodes2(self, head: Optional[ListNode]) -> List[int]:
        values = []

        while head:
            values.append(head.val)
            head = head.next

        ans = [0] * len(values)
        stack = []
        for i, value in enumerate(values):
            while stack and values[stack[-1]] < value:
                idx = stack.pop()
                ans[idx] = value
            stack.append(i)

        return ans


obj = Solution()
head = None
head = obj.append(2, head)
head = obj.append(1, head)
head = obj.append(5, head)
obj.print_list(head)
print()
print(obj.nextLargerNodes(head))
