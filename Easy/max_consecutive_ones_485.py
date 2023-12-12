from typing import List


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        l = []
        count = 0

        for i in nums:
            if i == 1:
                count += 1
            else:
                l.append(count)
                count = 0

        if count != 0:
            l.append(count)

        return max(l)

    def findMaxConsecutiveOnes2(self, nums: List[int]) -> int:
        max_count = count = 0
        for num in nums:
            if num == 1:
                count += 1
            else:
                max_count = max(max_count, count)
                count = 0

        return max(max_count, count)


obj = Solution()
nums = [1, 0, 1, 1, 0, 1]
print(obj.findMaxConsecutiveOnes(nums))
