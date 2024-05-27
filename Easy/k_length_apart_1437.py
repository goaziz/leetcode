from typing import List


class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        count = k

        for i in nums:
            if i == 1:
                if count < k:
                    return False
                count = 0
            else:
                count += 1

        return True


obj = Solution()
nums = [1, 0, 0, 1, 0, 1]
k = 2
print(obj.kLengthApart(nums, k))
