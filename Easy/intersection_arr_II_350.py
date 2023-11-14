from typing import List


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        output = []

        for i in nums1:
            if nums2.count(i) > 0:
                output.append(i)
                nums2.remove(i)

        return output
    
    def intersect2(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # Not my solution but I like the approach.
        # Sort both the arrays first...
        sortedArr1 = sorted(nums1)
        sortedArr2 = sorted(nums2)
        # Use two pointers i and j for the two arrays and initialize both with zero.
        i = 0
        j = 0
        # Create a output list to store the output...
        output = []
        while i < len(sortedArr1) and j < len(sortedArr2):
            # If sortedArr1[i] is less than sortedArr2[j]...
            # Leave the smaller element and go to next(greater) element in nums1...
            if sortedArr1[i] < sortedArr2[j]:
                i += 1
            # If sortedArr1[i] is greater than sortedArr2[j]...
            # Go to next(greater) element in nums2 array...
            elif sortedArr2[j] < sortedArr1[i]:
                j += 1
            # If both the elements intersected...
            # Add this element to output & increment both i and j.
            else:
                output.append(sortedArr1[i])
                i += 1
                j += 1
        return output


obj = Solution()
nums1 = [1, 2, 2, 1]
nums2 = [2]
print(obj.intersect2(nums1, nums2))
