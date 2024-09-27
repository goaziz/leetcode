from typing import List


class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        num_sets = set(nums)
        
        while original in num_sets:
            original *= 2
        
        return original
