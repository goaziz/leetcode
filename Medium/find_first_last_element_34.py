from typing import List


class Solution:
    def find_upper_bound(self, nums, left, right, target):

        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] <= target:
                left = mid + 1
            else:
                right = mid - 1

        return left - 1 if left > 0 and nums[left - 1] == target else -1

    def find_lower_bound(self, nums, left, right, target):

        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return left if left < len(nums) and nums[left] == target else -1

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]

        left = 0
        right = len(nums) - 1
        first_index = self.find_lower_bound(nums, left, right, target)
        last_index = self.find_upper_bound(nums, left, right, target)

        return [first_index, last_index]


obj = Solution()
nums = [5, 7, 7, 8, 8, 10]
target = 8
print(obj.searchRange(nums, target))
