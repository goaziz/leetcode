from typing import List


class Solution:

    def binary_search(self, target, nums):
        right = len(nums) - 1
        left = 0

        while left <= right:
            mid = left + (right - left) // 2

            if nums[mid] == target:
                return True
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1

        return False

    def buildArray(self, target: List[int], n: int) -> List[str]:
        stack = []
        numbers = []

        for i in range(1, n + 1):
            stack.append('Push')
            numbers.append(i)

            if numbers == target:
                return stack

            if not self.binary_search(i, target):
                numbers.pop()
                stack.append('Pop')

        return stack

    def buildArray2(self, target: List[int], n: int) -> List[str]:
        stack = []
        i = 0

        for num in target:
            while i < num - 1:
                stack.append('Push')
                stack.append('Pop')
                i += 1

            stack.append('Push')
            i += 1

        return stack


obj = Solution()
target = [1, 2]
n = 4
print(obj.buildArray2(target, n))
