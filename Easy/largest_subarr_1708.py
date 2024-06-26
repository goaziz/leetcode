from typing import List


class Solution:
    def largestSubarray(self, nums: List[int], k: int) -> List[int]:
        sub_array = nums[:k]

        for i in range(1, len(nums) - k + 1):
            sub_arr = nums[i: i + k]
            if sub_arr > sub_array:
                sub_array = sub_arr

        return sub_array

    def largestSubarray(self, nums: List[int], k: int) -> List[int]:
        max_num = nums[0]
        idx = 0

        for i in range(1, len(nums) - k + 1):
            if nums[i] > max_num:
                max_num = nums[i]
                idx = i
                
        return nums[idx: idx + k]


obj = Solution()
nums = [1, 4, 5, 2, 3]
k = 4
print(obj.largestSubarray(nums, k))
