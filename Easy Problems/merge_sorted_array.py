def merge(nums1, m, nums2, n):
    sp_1 = nums1[:m]
    sp_2 = nums2[:n]
    return sorted(sp_1 + sp_2)


nums1 = [1, 2, 3, 0, 0, 0]
nums2 = [2, 5, 6]
m = 3
n = 3

print(merge(nums1, m, nums2, n))
