from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        freq = {}

        for num in nums:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1

        for key, val in freq:
            if val == 1:
                return key

    def singleNumber2(self, nums: List[int]) -> int:
        nums.sort()
        print(nums)
        for i in range(0, len(nums) - 1, 3):
            if nums[i] == nums[i + 1]:
                continue
            else:
                return nums[i]

        return nums[len(nums) - 1]

    def singleNumber3(self, nums: List[int]) -> int:
        return (3 * sum(set(nums)) - sum(nums)) // 2


obj = Solution()
nums = [0, 1, 0, 1, 0, 1, 99]
print(obj.singleNumber3(nums))
