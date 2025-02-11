from typing import List


class Solution:
    def countElements(self, nums: List[int]) -> int:
        min_num = min(nums)
        max_num = max(nums)
        result = 0

        for num in nums:
            if min_num < num < max_num:
                result += 1
        return result


obj = Solution()
nums = [11, 7, 2, 15]
print(obj.countElements(nums))
