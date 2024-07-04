from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        result = []

        def generate_permuation(start):
            if start == n - 1:
                result.append(nums[:])

            for i in range(start, n):
                nums[start], nums[i] = nums[i], nums[start]
                generate_permuation(start + 1)
                nums[start], nums[i] = nums[i], nums[start]

        generate_permuation(0)
        return result


obj = Solution()
nums = [1, 0]
print(obj.permute(nums))
