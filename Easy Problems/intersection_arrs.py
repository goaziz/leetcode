class Solution:
    def intersection(self, nums1, nums2):
        s_1 = set(nums1)
        s_2 = set(nums2)

        return list(s_1.intersection(s_2))

obj = Solution()
nums1 = [4,9,5]
nums2 = [9,4,9,8,4]

print(obj.intersection(nums1, nums2))