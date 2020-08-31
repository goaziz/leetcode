class NumArray:

    def __init__(self, nums):
        self.nums = nums

    def sumRange(self, i: int, j: int) -> int:
        return sum(self.nums[i:j + 1])


nums = [-2, 0, 3, -5, 2, -1]
obj = NumArray(nums)
param = obj.sumRange(0, 5)
print(param)
