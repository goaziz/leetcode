from typing import List


class Solution:
    def binary_search(self, lo, hi, nums, target):
        while lo <= hi:
            mid = (lo + hi) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                hi = mid - 1
            else:
                lo = mid + 1
        return -1

    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)

        for i in range(n):
            complement = target - numbers[i]
            # search only after i
            j = self.binary_search(i + 1, n - 1, numbers, complement)

            if j != -1:
                return [i + 1, j + 1]  # convert to 1-based indexing

        return []

    def twoSum2(self, numbers: List[int], target: int) -> List[int]:
        i, j = 0, len(numbers) - 1

        while i < j:
            s = numbers[i] + numbers[j]

            if s > target:
                j -= 1
            elif s < target:
                i += 1
            else:
                break

        return [i + 1, j + 1]


obj = Solution()
numbers = [2, 4, 7, 11, 15, 16]
target = 20
print(obj.twoSum2(numbers, target))
