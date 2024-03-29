from math import inf
from typing import List


class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums = sorted(set(nums), reverse=True)

        if len(nums) < 3:
            return nums[0]
        return nums[2]

    def thirdMax2(self, nums: List[int]) -> int:
        nums.sort(reverse=True)

        count = 1
        prev_elem = nums[0]

        for index, value in enumerate(nums):
            if nums[index] != prev_elem:
                count += 1
                prev_elem = value

            if count == 3:
                return value

        return nums[0]

    def thirdMax3(self, nums: List[int]) -> int:
        # Three variables to store maxiumum three numbers till now.
        first_max = -inf
        second_max = -inf
        third_max = -inf

        for num in nums:
            # This number is already used once, thus we skip it.
            if first_max == num or second_max == num or third_max == num:
                continue

            # If current number is greater than first maximum,
            # It means that this is the greatest number and first maximum and second max
            # will become the next two greater numbers.
            if first_max <= num:
                third_max = second_max
                second_max = first_max
                first_max = num
            # When current number is greater than second maximum,
            # it means that this is the second greatest number.
            elif second_max <= num:
                third_max = second_max
                second_max = num
            # It is the third greatest number.
            elif third_max <= num:
                third_max = num

        # If third max was never updated, it means we don't have 3 distinct numbers.
        if third_max == -inf:
            return first_max

        return third_max


obj = Solution()
nums = [1, 2, 2, 5, 3, 5]
print(obj.thirdMax3(nums))
