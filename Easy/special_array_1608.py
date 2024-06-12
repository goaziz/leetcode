from typing import List


class Solution:
    def specialArray(self, nums: List[int]) -> int:

        for x in range(len(nums) + 1):
            count = 0
            for num in nums:
                if num >= x:
                    count += 1
            if x == count:
                return x
            count = 0

        return -1

    def specialArray2(self, nums: List[int]) -> int:
        nums.sort(reverse=True)

        for x in range(len(nums) + 1):
            s = sum(num >= x for num in nums)

            if x == s:
                return x

        return -1

    def specialArray3(self, nums: List[int]) -> int:
        N = len(nums)

        freq = [0] * (N + 1)
        for num in nums:
            freq[min(N, num)] += 1

        num_greater_than_or_equal = 0
        for i in range(N, 0, -1):
            num_greater_than_or_equal += freq[i]
            if i == num_greater_than_or_equal:
                return i

        return -1


obj = Solution()
nums = [5, 5, 5, 5, 5]
print(obj.specialArray2(nums))
