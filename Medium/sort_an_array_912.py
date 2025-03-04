from typing import List


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        # Merge sort

        if len(nums) <= 1:
            return nums

        n = len(nums)
        mid = n // 2
        right = nums[mid:]
        left = nums[:mid]

        sorted_left = self.sortArray(left)
        sorted_right = self.sortArray(right)

        return self.merge(sorted_left, sorted_right)

    def merge(self, left, right):
        result = []
        i = j = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1

        result.extend(left[i:])
        result.extend(right[j:])

        return result

    def sortArray2(self, nums: List[int]) -> List[int]:
        # Counting sort

        min_n = min(nums)
        max_n = max(nums)
        counts = {}

        for num in nums:
            counts[num] = counts.get(num, 0) + 1

        idx = 0
        for i in range(min_n, max_n + 1):
            while counts.get(i, 0) > 0:
                nums[idx] = i
                idx += 1
                counts[i] -= 1

        return nums


obj = Solution()
nums = [5, 2, 3, 1]
print(obj.sortArray2(nums))
