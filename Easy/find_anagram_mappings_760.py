from typing import List


class Solution:
    def anagramMappings(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = []
        for num in nums1:
            idx = nums2.index(num)
            ans.append(idx)

        return ans

    def anagramMappings2(self, nums1: List[int], nums2: List[int]) -> List[int]:
        hashmap = {}

        for num in range(len(nums2)):
            hashmap[nums2[num]] = num

        ans = []
        for num in range(len(nums1)):
            idx = hashmap.get(nums1[num])
            ans.append(idx)

        return ans


obj = Solution()
nums1 = [12, 28, 46, 32, 50]
nums2 = [50, 12, 32, 46, 28]
print(obj.anagramMappings2(nums1, nums2))
