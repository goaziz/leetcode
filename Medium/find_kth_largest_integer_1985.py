from typing import List


class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        nums = list(map(int, nums))
        nums.sort()

        return str(nums[-k])


obj = Solution()
nums = ["3", "6", "7", "10"]
k = 4
print(obj.kthLargestNumber(nums, k))
