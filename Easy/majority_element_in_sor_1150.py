from typing import List


class Solution:
    def isMajorityElement(self, nums: List[int], target: int) -> bool:
        n = len(nums)
        count = nums.count(target)

        if count > n // 2:
            return True
        else:
            return False

    def isMajorityElement2(self, nums: List[int], target: int) -> bool:
        def binary_search(nums, n, target):
            left = 0
            right = n - 1
            idx = n

            while left <= right:
                mid = (left + right) // 2

                if nums[mid] >= target:
                    right = mid - 1
                    idx = mid
                else:
                    left = mid + 1
            return idx

        n = len(nums)
        first_index = binary_search(nums, n, target)
        return first_index + n // 2 < n and nums[first_index + n // 2] == target


obj = Solution()
nums = [2, 4, 5, 5, 5, 5, 5, 6, 6]
target = 5
print(obj.isMajorityElement2(nums, target))
