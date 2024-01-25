from typing import List


class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        odds = [i for i in nums if i % 2 != 0]
        evens = [i for i in nums if i % 2 == 0]

        ans = []
        for odd, even in zip(odds, evens):
            ans.append(even)
            ans.append(odd)

        return ans

    def sortArrayByParityII2(self, nums: List[int]) -> List[int]:
        j = 1
        for i in range(0, len(nums), 2):
            if nums[i] % 2 == 0:
                while nums[i] % 2:
                    j += 2
                nums[i], nums[j] = nums[j], nums[i]

        return nums


obj = Solution()
nums = [3, 4]
print(obj.sortArrayByParityII2(nums))
