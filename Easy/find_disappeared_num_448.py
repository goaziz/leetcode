from collections import Counter
from typing import List


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        set_of_numbers = set(nums)
        current_range = list(range(1, n + 1))
        return list(set(current_range).difference(set_of_numbers))

    def findDisappearedNumbers2(self, nums: List[int]) -> List[int]:
        n = len(nums) + 1
        c = Counter(nums)
        output = []

        for i in range(1, n):
            if i not in c:
                output.append(i)

        return output

    def findDisappearedNumbers3(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        pretty solution, not mine
        """

        # Iterate over each of the elements in the original array
        for i in range(len(nums)):

            # Treat the value as the new index
            new_index = abs(nums[i]) - 1

            # Check the magnitude of value at this new index
            # If the magnitude is positive, make it negative
            # thus indicating that the number nums[i] has
            # appeared or has been visited.
            if nums[new_index] > 0:
                nums[new_index] *= -1

        # Response array that would contain the missing numbers
        result = []
        print(nums)
        # Iterate over the numbers from 1 to N and add all those
        # that have positive magnitude in the array
        for i in range(1, len(nums) + 1):
            if nums[i - 1] > 0:
                result.append(i)

        return result


obj = Solution()
nums = [4, 3, 2, 7, 8, 2, 3, 1]
print(obj.findDisappearedNumbers3(nums))
