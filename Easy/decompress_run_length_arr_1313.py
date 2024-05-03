from typing import List


class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        res = []
        i = 0
        j = len(nums)
        
        while i < j:
            res += [nums[i + 1]] * nums[i]
            i += 2
        
        return res


obj = Solution()
nums = [1, 2, 3, 4]
print(obj.decompressRLElist(nums))
