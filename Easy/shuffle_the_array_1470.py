from typing import List


class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        arr1 = nums[:n]
        arr2 = nums[n:]
        arr = []

        for i, j in zip(arr1, arr2):
            arr.append(i)
            arr.append(j)

        return arr

    def shuffle2(self, nums: List[int], n: int) -> List[int]:
        arr = [0] * (2 * n)

        for i in range(n):
            arr[2 * i] = nums[i]
            arr[2 * i + 1] = nums[n + i]

        return arr


obj = Solution()
nums = [2, 5, 1, 3, 4, 7]
n = 3
print(obj.shuffle2(nums, n))
