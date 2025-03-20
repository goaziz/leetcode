from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums = []
        i, j = 0, 0

        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                nums.append(nums1[i])
                i += 1
            else:
                nums.append(nums2[j])
                j += 1

        nums.extend(nums1[i:])
        nums.extend(nums2[j:])

        n = len(nums)
        idx = n // 2
        if n % 2 != 0:
            return nums[idx] / 1

        return (nums[idx - 1] + nums[idx]) / 2


obj = Solution()
nums1 = [1, 2]
nums2 = [3]
print(obj.findMedianSortedArrays(nums1, nums2))
