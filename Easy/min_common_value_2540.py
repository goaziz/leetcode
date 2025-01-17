from typing import List


class Solution:

    def binary_search(self, target, nums):
        hi = len(nums)
        lo = 0

        while lo < hi:
            mid = (hi + lo) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                hi = mid - 1
            else:
                lo = mid + 1

        return -1

    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        result = []

        for num in nums1:
            pos = self.binary_search(num, nums2)
            if pos != -1:
                result.append(num)

        return min(result) if result else -1

    def getCommon2(self, nums1: List[int], nums2: List[int]) -> int:
        i = j = 0
        
        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                i += 1
            elif nums1[i] > nums2[j]:
                j += 1
            else:
                return nums1[i]
        
        return -1


obj = Solution()
nums1 = [1, 2, 3]
nums2 = [2, 4]
print(obj.getCommon2(nums1, nums2))
