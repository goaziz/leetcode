from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        n = len(nums)
        count = 0
        for i in range(n - 1, -1, -1):
            if nums[i] == val:
                del nums[i]
                count += 1
        return n - count

    def removeElement2(self, nums: List[int], val: int) -> int:
        count = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[count] = nums[i]
                count += 1

        print(nums)
        return count


obj = Solution()
nums = [0, 1, 2, 2, 3, 0, 4, 2]
# nums = [1, 2, 1, 1, 2]
val = 2
print(obj.removeElement2(nums, val))
