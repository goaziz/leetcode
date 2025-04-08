from typing import List


class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        pos = sum(1 for num in nums if num > 0)
        neg = sum(1 for num in nums if num < 0)

        return max(pos, neg)

    def maximumCount2(self, nums: List[int]) -> int:
        def first_negative():
            left = 0
            right = len(nums)
            
            while left < right:
                mid = (right + left) // 2
                if nums[mid] < 0:
                    left = mid + 1
                else:
                    right = mid
            
            return left
        
        def first_positive():
            left = 0
            right = len(nums)
            
            while left < right:
                mid = (left + right) // 2
                if nums[mid] <= 0:
                    left = mid + 1
                else:
                    right = mid
            
            return left

        neg = first_negative()
        pos = len(nums) - first_positive()
        
        return max(neg, pos)
        

obj = Solution()
nums = [-2, -1, -1, 1, 2, 3]
print(obj.maximumCount2(nums))
