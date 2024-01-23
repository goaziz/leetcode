from typing import List


class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        even = [i for i in nums if i % 2 == 0]
        odd = [i for i in nums if i % 2 != 0]

        return even + odd

    def sortArrayByParity2(self, nums: List[int]) -> List[int]:
        count = 0
        for i in range(len(nums)):
            if nums[i] % 2 == 0:
                nums[i], nums[count] = nums[count], nums[i]
                count += 1

        return nums


obj = Solution()
nums = [3, 1, 2, 4]
print(obj.sortArrayByParity2(nums))
