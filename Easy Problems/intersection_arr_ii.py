from collections import Counter

def intersect(nums1, nums2):
    s_1 = Counter(nums1)
    s_2 = Counter(nums2)

    return list((s_1 & s_2).elements())

nums = [1,2]
nums1 = [1, 1]

print(intersect(nums, nums1))
