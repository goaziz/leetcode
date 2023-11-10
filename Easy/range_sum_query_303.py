from typing import List


class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums

    def sumRange(self, left: int, right: int) -> int:
        return sum(self.nums[left:right + 1])


class NumArray2:

    def __init__(self, nums: List[int]):
        self.prefix_array = [nums[0]]
        for i in range(1, len(nums)):
            self.prefix_array.append(nums[i] + self.prefix_array[-1])
        print(self.prefix_array)

    def sumRange(self, left: int, right: int) -> int:
        if left == 0:
            return self.prefix_array[right]
        return self.prefix_array[right] - self.prefix_array[left - 1]


obj = NumArray2([-2, 0, 3, -5, 2, -1])
print(obj.sumRange(0, 2))
