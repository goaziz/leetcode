from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = left + (right - left) // 2

            if nums[mid] == target:
                return True

            # Add a check for duplicates
            if nums[left] == nums[mid]:
                left += 1  # Skip the duplicate
                continue

            # Left half is sorted
            if nums[left] <= nums[mid]:
                if nums[left] <= target <= nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                # Right half is sorted
                if nums[mid] <= target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1

        return False


obj = Solution()
nums = [1, 0, 1, 1, 1]
target = 0
print(obj.search(nums, target))
