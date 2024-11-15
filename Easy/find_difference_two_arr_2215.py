from typing import List


class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        result = [[], []]
        nums1_set = set(nums1)
        nums2_set = set(nums2)

        for num in nums1_set:
            if num not in nums2_set:
                result[0].append(num)

        for num in nums2_set:
            if num not in nums1_set:
                result[1].append(num)

        return result


obj = Solution()
nums1 = [1, 2, 3, 3]
nums2 = [1, 1, 2, 2]
print(obj.findDifference(nums1, nums2))
