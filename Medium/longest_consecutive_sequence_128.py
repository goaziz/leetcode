from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest_sequence = 0
        nums = set(nums)

        for num in nums:
            if num - 1 not in nums:
                current_num = num
                count = 1

                while current_num + 1 in nums:
                    current_num += 1
                    count += 1
                longest_sequence = max(longest_sequence, count)

        return longest_sequence


obj = Solution()
nums = [100, 4, 200, 1, 3, 2]
print(obj.longestConsecutive(nums))
