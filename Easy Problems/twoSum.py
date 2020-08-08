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
nums = [1, 2, 3, 1]
target = 3

print(objects.twoSum(nums, target))
