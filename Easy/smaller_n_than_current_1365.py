from typing import List


class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        res = []

        for i in range(len(nums)):
            count = 0
            for j in range(len(nums)):
                if nums[i] > nums[j]:
                    count += 1
            res.append(count)

        return res

    def smallerNumbersThanCurrent2(self, nums: List[int]) -> List[int]:
        sorted_arr = sorted(nums)
        hashmap = {}
        res = []
        for idx, val in enumerate(sorted_arr):
            if val not in hashmap:
                hashmap[val] = idx

        for i in range(len(nums)):
            res.append(hashmap[nums[i]])
        return res


obj = Solution()
nums = [6, 5, 4, 8]
print(obj.smallerNumbersThanCurrent2(nums))
