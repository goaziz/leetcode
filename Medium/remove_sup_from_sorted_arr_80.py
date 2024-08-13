from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        count = 1
        prev = nums[0]
        idx = 1
        
        for i in range(1, len(nums)):
            if prev == nums[i]:
                count += 1
            else:
                count = 1
                prev = nums[i]
            
            if count >= 3:
                continue
            nums[idx] = prev
            idx += 1
        
        return idx

    def removeDuplicates2(self, nums: List[int]) -> int:
        idx, count = 1, 1
        
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                count += 1
            else:
                count = 1
            
            if count <= 2:
                nums[idx] = nums[i]
                idx += 1
        
        return idx

obj = Solution()
nums = [1, 1, 1, 2, 2, 3]
print(obj.removeDuplicates2(nums))
