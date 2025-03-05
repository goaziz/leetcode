import itertools
from typing import List


class Solution:
    def sortEvenOdd(self, nums: List[int]) -> List[int]:
        odd = sorted(nums[::2])
        even = sorted(nums[1::2], reverse=True)

        result = []
        odd_idx, even_idx = 0, 0

        for i in range(len(nums)):
            if i % 2 == 0:
                result.append(odd[odd_idx])
                odd_idx += 1
            else:
                result.append(even[even_idx])
                even_idx += 1
        
        return result


obj = Solution()
nums = [4, 1, 2, 3]
print(obj.sortEvenOdd(nums))
