class Solution:
    def twoSum(self, nums, target):

        differenceMap = dict()

        for i, j in enumerate(nums):
            difference = target - j
            if difference in differenceMap:
                return [differenceMap[difference], i]
            else:
                differenceMap[j] = i

objects = Solution()
nums = [2, 7, 11, 15]
target = 9

print(objects.twoSum(nums, target))
