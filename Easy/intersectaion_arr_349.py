from typing import List


class Solution:

    def binary_search(self, target, arr):
        arr.sort()
        left = 0
        right = len(arr) - 1

        while left <= right:
            mid = left + (right - left) // 2

            if arr[mid] == target:
                return arr[mid]
            elif arr[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return None

    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        output = set()

        for i in nums1:
            val = self.binary_search(i, nums2)
            if val is not None:
                output.add(val)

        return list(output)


obj = Solution()
nums1 = [1, 2]
nums2 = [1, 1]
print(obj.intersection(nums1, nums2))
