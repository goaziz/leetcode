from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        return sum(range(len(nums) + 1)) - sum(nums)

    def missingNumber2(self, nums: List[int]) -> int:
        s = set(range(0, len(nums) + 1)).difference(set(nums))
        return list(s)[0]

    def missingNumber3(self, nums: List[int]) -> int:
        n = len(nums)
        total = n * (n + 1) // 2
        s = sum(nums)

        return total - s

    def missingNumber4(self, nums: List[int]) -> int:
        nums.sort()

        for i in range(len(nums)):
            if i != nums[i]:
                print(i)
                return i

        return nums[-1] + 1

    def missingNumber5(self, nums: List[int]) -> int:
        nums.sort()
        left, right = 0, len(nums) - 1
        while left <= right:
            middle = (left + right) // 2
            if nums[middle] == middle:
                left = middle + 1
            else:
                right = middle - 1
        return left


obj = Solution()
nums = [1, 0, 5, 3, 2]
print(obj.missingNumber5(nums))
