from typing import List, Optional


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
            while current.next:
                current = current.next

            current.next = new_node

        return head

    def print_list(self, head):
        current = head

        while current:
            print(current.val, end=' --> ')
            current = current.next

    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        critical_points = []
        nums = []
        current = head

        while current:
            nums.append(current.val)
            current = current.next

        # iterate nums to select critical points
        for i in range(1, len(nums) - 1):
            if nums[i - 1] > nums[i] < nums[i + 1]:
                critical_points.append(i + 1)

            if nums[i - 1] < nums[i] > nums[i + 1]:
                critical_points.append(i + 1)

        if len(critical_points) < 2:
            return [-1, -1]

        max_distance = critical_points[-1] - critical_points[0]
        min_distance = float('inf')

        for i in range(1, len(critical_points)):
            min_distance = min(
                min_distance, critical_points[i] - critical_points[i - 1])

        return [min_distance, max_distance]

    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        critical_points = []
        previous = head
        current = head.next if head else None
        index = 0

        while current and current.next:
            next_node = current.next

            if previous.val > current.val < next_node.val:
                critical_points.append(current.val)

            if previous.val < current.val > next_node.val:
                critical_points.append(current.val)

            previous = current
            current = next_node
            index += 1

        if len(critical_points) < 2:
            return [-1, -1]

        max_distance = critical_points[-1] - critical_points[0]
        min_distance = float('inf')

        for i in range(1, len(critical_points)):
            min_distance = min(
                min_distance, critical_points[i] - critical_points[i - 1])

        return [min_distance, max_distance]


obj = Solution()
head = None
head = obj.append(2, head)
head = obj.append(2, head)
head = obj.append(2, head)
head = obj.append(2, head)
head = obj.append(2, head)
head = obj.append(2, head)
head = obj.append(2, head)
head = obj.append(2, head)
head = obj.append(2, head)
head = obj.append(2, head)
obj.print_list(head)
print()
print(obj.nodesBetweenCriticalPoints(head))
