from typing import List


class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        count = 0

        for i in nums:
            if len(str(i)) % 2 == 0:
                count += 1

        return count

    def findNumbers2(self, nums: List[int]) -> int:
        count = 0

        for num in nums:
            if (num >= 10 and num <= 99) or (num >= 1000 and num <= 9999) or num == 100000:
                count += 1

        return count


obj = Solution()
nums = [12, 345, 2, 6, 7896]
print(obj.findNumbers(nums))
