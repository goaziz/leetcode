from typing import List


class Solution:

    def compare(self, a, b):
        return str(a) + str(b) > str(b) + str(a)

    def largestNumber(self, nums: List[int]) -> str:

        n = len(nums)

        for i in range(n):
            for j in range(n - i - 1):
                if not self.compare(nums[j], nums[j + 1]):
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]

        result = ''.join(map(str, nums))

        return result if result[0] != '0' else '0'


obj = Solution()
nums = [3, 30, 34, 5, 9]
print(obj.largestNumber(nums))
